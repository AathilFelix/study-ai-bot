from flask import Flask, render_template, request, session
from hackclub_ai import ask_hackclub
import os
import PyPDF2
import markdown
from werkzeug.utils import secure_filename
import re

app = Flask(__name__)
app.secret_key = 'studybot_secret_key'
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def extract_pdf_text(pdf_path):
    text = ""
    try:
        with open(pdf_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception:
        text = ""
    return text

def get_rag_context(query, pdf_text):
    if pdf_text:
        return pdf_text[:1000]
    return ""

def process_math_expressions(text):
    """
    Process and protect math expressions from markdown interference
    """
    # Protect inline math expressions \( ... \)
    text = re.sub(r'\\\((.*?)\\\)', r'<span class="math-inline">\\(\1\\)</span>', text, flags=re.DOTALL)
    
    # Protect display math expressions \[ ... \]
    text = re.sub(r'\\\[(.*?)\\\]', r'<div class="math-block">\\[\1\\]</div>', text, flags=re.DOTALL)
    
    # Also handle $ ... $ for inline math (common alternative)
    text = re.sub(r'(?<!\$)\$(?!\$)([^$]+?)\$(?!\$)', r'<span class="math-inline">$\1$</span>', text)
    
    # Handle $$ ... $$ for display math
    text = re.sub(r'\$\$(.*?)\$\$', r'<div class="math-block">$$\1$$</div>', text, flags=re.DOTALL)
    
    return text

@app.route("/", methods=["GET", "POST"])
def index():
    answer = None
    pdf_uploaded = False
    if request.method == "POST":
        if 'pdf' in request.files:
            pdf_file = request.files['pdf']
            if pdf_file and pdf_file.filename.lower().endswith('.pdf'):
                filename = secure_filename(pdf_file.filename)
                pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                pdf_file.save(pdf_path)
                pdf_text = extract_pdf_text(pdf_path)
                session['pdf_text'] = pdf_text
                pdf_uploaded = True
                
        question = request.form.get("chat", "")
        pdf_text = session.get('pdf_text', "")

        if question.strip():
            # build conversation history
            history = session.get('history', [])

            # If there is RAG context, send it as a system message
            context = get_rag_context(question, pdf_text)
            if context:
                if not any(m.get('role') == 'system' and 'Relevant study material' in m.get('content', '') for m in history):
                    history.insert(0, {"role": "system", "content": f"Relevant study material:\n{context}"})

            # append user message
            history.append({"role": "user", "content": question})

            # call the model with the full history
            raw_answer = ask_hackclub(history)
            # append assistant reply to history
            history.append({"role": "assistant", "content": raw_answer})
            session['history'] = history
            
            # Process math expressions BEFORE markdown
            processed_answer = process_math_expressions(raw_answer)
            
            # Convert markdown to HTML with math-friendly settings
            answer = markdown.markdown(
                processed_answer, 
                extensions=['extra', 'nl2br'],
                extension_configs={
                    'extra': {},
                    'nl2br': {}
                }
            )
            
    return render_template('index.html', answer=answer, pdf_uploaded=pdf_uploaded)

if __name__ == "__main__":
    app.run(debug=True)
