# Study AI Bot

Hey there! I built this study assistant to help students actually learn stuff instead of just getting quick answers. It's powered by Hack Club AI and runs on Flask.

**Heads up:** The bot might take a moment to think before responding - just be patient with it!

## What It Does

This thing is pretty cool - it basically acts like a really patient tutor:

- **Actually talks with you:** Remembers what you've been discussing so conversations flow naturally
- **Handles your PDFs:** Drop in a document and it'll use that info to help answer your questions
- **Math that doesn't suck:** All those fancy equations render properly with LaTeX support
- **Teaching approach:** Won't just give you answers - guides you to figure things out yourself
- **Looks decent:** Clean interface that works on your phone too
- **Remembers your chat:** Keeps track of your conversation while you're using it

## Screenshots

The bot walks you through problems step by step. It'll ask you questions that make you think, show math equations that actually look right, and remember what you talked about earlier. If you upload a PDF, it uses that content to give better answers.

## Getting It Running

### What You Need

- Python 3.7 or newer
- The usual pip stuff

### Setting It Up

**Grab the code:**

```bash
git clone https://github.com/AathilFelix/study-ai-bot.git
cd study-ai-bot
```

**Set up a virtual environment (trust me, you want this):**

```bash
python -m venv .venv
source .venv/bin/activate  # Windows folks: .venv\Scripts\activate
```

**Install the stuff it needs:**

```bash
pip install -r requirements.txt
```

**Fire it up:**

```bash
python app.py
```

**Check it out:**
Go to http://127.0.0.1:5000 in your browser

## How to Use This Thing

### Just Chatting

Type your question, hit "Ask", and it'll walk you through the solution. No shortcuts - it actually helps you understand.

### Uploading PDFs

Hit "Choose File", pick a PDF, and now the bot can reference that document when answering questions. Pretty handy for homework help.

### Math Stuff

It handles LaTeX math notation like:

- Regular inline: `$$x = 5$$`
- Big display equations: `$$E = mc^2$$`
- Standard notation: `$x^2 + y^2 = z^2$`

### Starting Over

There's a reset button when you want to clear everything and start fresh.

## The Technical Bits

### How It Works

- **Backend:** Flask because it's simple and works
- **AI:** Hack Club's Qwen 3-32B model (no API keys needed!)
- **PDF stuff:** PyPDF2 pulls text out of documents
- **Math rendering:** MathJax makes equations look professional
- **Frontend:** Bootstrap 5 for the UI
- **Text processing:** Full markdown support

### What's Under the Hood

- `app.py` - Main Flask app with all the routes
- `hackclub_ai.py` - Talks to the AI and handles prompts
- `templates/index.html` - The web interface
- `uploads/` - Where uploaded PDFs live

### How It Remembers Stuff

Uses Flask sessions to keep track of your conversation and any PDFs you've uploaded. When you have a document uploaded, it automatically includes relevant chunks in the AI's context.

## Configuration

### Environment Stuff

Since it uses Hack Club AI, you don't need to mess with API keys or anything.

### Making It Your Own

- Change the teaching style by editing prompts in `hackclub_ai.py`
- Adjust how much PDF content gets included in `get_rag_context()`
- Customize the look in `templates/index.html`

## Development

### File Layout

```
study-ai-bot/
├── app.py                 # Main Flask app
├── hackclub_ai.py         # AI interface
├── requirements.txt       # What Python needs
├── setup.sh              # Setup script
├── templates/
│   └── index.html        # The web page
├── uploads/              # PDF storage
└── README.md            # You're reading it
```

### Adding New Features

- **New pages:** Add routes in `app.py`
- **Change AI behavior:** Edit the prompts in `hackclub_ai.py`
- **Frontend changes:** Update `templates/index.html`
- **New dependencies:** Add them to `requirements.txt`

## What It Needs to Run

Main packages:

- `flask` - The web framework
- `markdown` - Text processing
- `PyPDF2` - PDF text extraction
- `werkzeug` - Security utilities
- `markupsafe` - Safe string handling

## Contributing

Want to help make this better?

1. Fork it
2. Make a branch for your feature
3. Do your thing
4. Test it thoroughly
5. Send a pull request

## License

It's open source - use it, modify it, learn from it. That's what it's for.

## Need Help?

Run into issues?

- Open a GitHub issue
- Check the troubleshooting section below

## When Things Go Wrong

### Common Problems

**Bot's not responding**

- Make sure Flask is actually running
- Check your internet connection
- Give it a few seconds - sometimes it's just thinking

**PDF upload failing**

- Make sure the PDF isn't password protected
- Big files take longer to process
- Try a smaller PDF first

**Math not showing up right**

- Check if MathJax loaded (look in browser dev tools)
- Use proper LaTeX: `$$inline$$` or `$$display$$`

**Conversation getting weird**

- Clear your browser cookies
- Hit the reset button
- Refresh the page

## What's Next

Ideas I'm thinking about:

- Support for Word docs and PowerPoint slides
- Better PDF processing with vector embeddings
- User accounts so conversations persist
- Export chat transcripts
- Mobile app version
- More advanced math solving
- Integration with Canvas/Blackboard

---

Built this because I got tired of students just wanting quick answers instead of actually learning. Hope it helps!
