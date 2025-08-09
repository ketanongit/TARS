# TARS Chatbot (v1)

A Python-based chatbot that uses the Mistral 7B model via llama-cpp-python for conversational AI with persistent memory and streaming responses.

## Features

- Interactive command-line chat interface with real-time streaming
- Persistent conversation memory stored in `memory.txt`
- Uses Mistral 7B Instruct model for responses
- Colorized terminal output with live response streaming
- Sarcastic and helpful AI personality (inspired by TARS from Interstellar)
- System prompt priming for consistent personality
- Temperature-controlled responses for natural conversation

## Prerequisites

- Python 3.7+
- Mistral 7B model file (GGUF format)
- Sufficient RAM (4-8GB recommended for 7B models)

## Setup

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

This will install:

- `llama-cpp-python` - Python bindings for llama.cpp (no separate compilation needed!)
- `colorama` - Cross-platform colored terminal text

### 2. Download Model

Download the Mistral 7B Instruct model in GGUF format and update the `MODEL_PATH` in `tars.py`:

```python
MODEL_PATH = r"path/to/your/mistral-7b-instruct-v0.2.Q5_K_M.gguf"
```

Popular sources for GGUF models:

- Hugging Face (search for "GGUF" models)
- TheBloke's quantized models

### 3. Configure Model Path

Edit `tars.py` and update the model path to match your setup:

```python
MODEL_PATH = r"E:\mistral-7b-instruct-v0.2.Q5_K_M.gguf"  # Your model path
```

## Usage

Run the chatbot:

```bash
python tars.py
```

The bot will:

1. Load the model into memory (this may take a moment)
2. Prime the TARS personality
3. Start the interactive chat

**Chat Commands:**

- Type your messages and press Enter to chat
- Type `exit` or `quit` to end the conversation
- Responses stream in real-time as TARS "thinks"
- Conversation history is automatically saved to `memory.txt`

## File Structure

```
├── tars.py           # Main chatbot script
├── requirements.txt  # Python dependencies
├── memory.txt        # Conversation history (auto-generated)
├── README.md         # This file
└── .gitignore        # Git ignore rules
```

## Configuration

The chatbot uses these key parameters in `tars.py`:

```python
n_ctx=2048          # Context window size
max_tokens=256      # Max response length
temperature=0.7     # Response creativity (0.0-1.0)
```

## Dependencies

- `llama-cpp-python` - Direct Python interface to llama.cpp (no CLI needed)
- `colorama` - Cross-platform colored terminal text

## Notes

- The chatbot maintains conversation context across sessions
- Memory file grows with each conversation - consider clearing it periodically
- Model responses depend on the quality and size of the GGUF model used
- Streaming responses provide real-time feedback
- System prompt ensures consistent TARS personality

## Troubleshooting

- **Model not found**: Verify the `MODEL_PATH` points to a valid GGUF file
- **Out of memory**: Try a smaller quantized model (Q4_K_M instead of Q5_K_M)
- **Slow loading**: Model loading is normal - larger models take longer
- **Slow responses**: Consider GPU acceleration by installing `llama-cpp-python` with CUDA support
- **Installation issues**: Try `pip install llama-cpp-python --force-reinstall --no-cache-dir`

  