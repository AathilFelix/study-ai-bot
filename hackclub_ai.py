from openai import OpenAI
import re

client = OpenAI(
    base_url="https://ai.hackclub.com/",
    api_key="none-thanks-to-hackclub"
)

def build_meta_prompt(teaching=True):
    """Return the system meta prompt describing the study-bot behavior.

    teaching=True -> hinting/guided responses (default). teaching=False -> full worked solutions.
    """
    if teaching:
        meta = (
            "You are a helpful study bot. "
            "When answering student questions, guide them to learn and understand concepts, "
            "rather than giving direct answers. "
            "Encourage critical thinking and provide hints or explanations. "
            "Use LaTeX formatting for math expressions: \\( \\) for inline math and \\[ \\] for display math."
        )
    else:
        meta = (
            "You are a helpful study bot. "
            "Provide a clear, step-by-step worked solution that shows intermediate calculations and the final answer. "
            "Be concise and show the arithmetic for each step. "
            "Use LaTeX formatting for math expressions: \\( \\) for inline math and \\[ \\] for display math."
        )
    return meta

def ask_hackclub(messages, model="qwen/qwen3-32b", teaching=True):
    """Send messages to Hack Club AI and clean the response.

    messages may be either a string (single user message) or a list of message dicts
    with keys 'role' and 'content' to represent a conversation history.
    teaching=True -> guided/hinting responses. teaching=False -> full worked solution.
    """
    meta = build_meta_prompt(teaching=teaching)

    # Normalize messages into a list of dicts
    if isinstance(messages, str):
        body_messages = [{"role": "user", "content": messages}]
    else:
        # assume it's a list of message dicts already
        body_messages = list(messages)

    # Prepend system meta
    payload_messages = [{"role": "system", "content": meta}] + body_messages

    response = client.chat.completions.create(
        model=model,
        messages=payload_messages
    )

    raw_response = response.choices[0].message.content
    cleaned_response = re.sub(r'<think>.*?</think>', '', raw_response, flags=re.DOTALL)

    return cleaned_response.strip()
