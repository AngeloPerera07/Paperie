# Paperie

AI-powered document summarizer for PDF and TXT files. Upload a document, get instant GPT-powered summaries, and ask questions about its contents.

## Features

- Upload PDF or TXT files
- AI-generated document summaries using GPT
- Chat with your document to ask specific questions
- Simple desktop interface

## Getting Started

### Prerequisites

- Python 3.9+
- An [OpenAI API key](https://platform.openai.com/api-keys)

### Installation

```bash
pip install pypdf openai
```

### Configuration

Create an environment variable with your OpenAI API key:

```bash
export OPENAI_API_KEY="your-api-key-here"
```

On Windows (PowerShell), set it persistently (then open a **new** terminal):

```powershell
setx OPENAI_API_KEY "your-api-key-here"
```

### Running

```bash
python app.py
```

## License

MIT