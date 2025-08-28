# Study AI Bot

An intelligent study assistant that helps students learn through guided questioning and step-by-step explanations. Built with Flask and powered by Hack Club AI.

# **PLEASE WAIT FOR FEW MOMENTS FOR THE BOT TO RESPOND THANKS!**

## Features

- **Conversational Learning**: Multi-turn conversations that remember context
- **PDF Document Support**: Upload PDFs for context-aware answers using RAG (Retrieval-Augmented Generation)
- **Math Expression Rendering**: Full LaTeX support with MathJax for mathematical notation
- **Teaching-Focused**: Guides students to understand concepts rather than giving direct answers
- **Clean Bootstrap UI**: Modern, responsive chat interface
- **Session Memory**: Maintains conversation history during your session

## Screenshots

The bot provides step-by-step guidance for solving problems:

- Asks leading questions to help students think through problems
- Renders mathematical expressions beautifully
- Maintains conversation context across multiple questions
- Uses uploaded PDF content to provide relevant context

## Installation

### Prerequisites

- Python 3.7+
- pip package manager

### Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/AathilFelix/study-ai-bot.git
   cd study-ai-bot
   ```

2. **Create and activate virtual environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**

   ```bash
   python app.py
   ```

5. **Open in browser**
   Navigate to `http://127.0.0.1:5000`

## Usage

### Basic Chat

1. Type your question in the text area
2. Click "Ask" to get a response
3. The bot will guide you through the solution step-by-step

### PDF Upload

1. Click "Choose File" and select a PDF document
2. The bot will use the PDF content as context for your questions
3. Ask questions related to the uploaded material

### Math Support

The bot supports LaTeX mathematical notation:

- Inline math: `\(x = 5\)`
- Display math: `\[E = mc^2\]`
- Standard notation: `$x^2 + y^2 = z^2$`

### Reset Conversation

- Use the reset button to clear conversation history and start fresh

## Technical Details

### Architecture

- **Backend**: Flask web framework
- **AI Model**: Hack Club AI (Qwen 3-32B)
- **PDF Processing**: PyPDF2 for text extraction
- **Math Rendering**: MathJax for LaTeX expressions
- **UI Framework**: Bootstrap 5 for responsive design
- **Markdown**: Full markdown support with extensions

### Key Components

- `app.py` - Main Flask application with routes and session management
- `hackclub_ai.py` - AI model interface and prompt engineering
- `templates/index.html` - Frontend chat interface
- `uploads/` - Directory for uploaded PDF files

### Session Management

- Conversation history stored in Flask sessions
- PDF content cached per session
- RAG context automatically included when available

## Configuration

### Environment Variables

The bot uses Hack Club AI which requires no API key setup.

### Customization

- Modify prompts in `hackclub_ai.py` to change teaching style
- Adjust RAG context length in `get_rag_context()` function
- Customize UI styling in `templates/index.html`

## Development

### File Structure

```
study-ai-bot/
├── app.py                 # Main Flask application
├── hackclub_ai.py         # AI model interface
├── requirements.txt       # Python dependencies
├── setup.sh              # Setup script
├── templates/
│   └── index.html        # Frontend template
├── uploads/              # PDF upload directory
└── README.md            # This file
```

### Adding Features

1. **New Routes**: Add to `app.py`
2. **AI Behavior**: Modify prompts in `hackclub_ai.py`
3. **Frontend**: Update `templates/index.html`
4. **Dependencies**: Add to `requirements.txt`

## Dependencies

Core packages:

- `flask` - Web framework
- `markdown` - Text processing
- `PyPDF2` - PDF text extraction
- `werkzeug` - Utilities and security
- `markupsafe` - Safe string handling

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source. Feel free to use and modify for educational purposes.

## Support

For issues and questions:

- Open an issue on GitHub
- Check the troubleshooting section below

## Troubleshooting

### Common Issues

**Bot not responding**

- Check if Flask server is running
- Verify internet connection for AI model access
- Please wait for a few moments

**PDF upload not working**

- Ensure PDF is not password protected
- Check file size (large PDFs may take time to process)

**Math not rendering**

- Ensure MathJax is loading (check browser console)
- Use proper LaTeX syntax: `\(inline\)` or `\[display\]`

**Session issues**

- Clear browser cookies and refresh
- Use the reset button to clear conversation

## Future Enhancements

- [ ] Multiple file format support (Word, PowerPoint)
- [ ] Advanced RAG with vector embeddings
- [ ] User accounts and persistent history
- [ ] Export conversation transcripts
- [ ] Mobile app version
- [ ] Advanced math solving capabilities
- [ ] Integration with learning management systems

---

Built with ❤️ for students who want to learn better, not just get answers.
