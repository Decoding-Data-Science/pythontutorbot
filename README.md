# Advanced Python Tutor Bot

Advanced Python Tutor Bot is a small educational AI app for beginner Python learners.

It helps with:
- Explaining Python concepts
- Debugging Python code
- Running interactive quizzes
- Improving code quality
- Beginner-friendly data structures and algorithms (DSA) guidance

## Tech Stack
- Python
- Gradio
- OpenAI Python SDK
- python-dotenv

## Features
- Professional Gradio layout with theme and clear mode descriptions
- Chat interface with persistent in-session chat history
- Four tutor modes:
  - Explain Concept
  - Debug Code
  - Quiz Me
  - Improve Code
- Reusable prompt templates
- Input validation and API key error handling

## Project Files
- `app.py` → Gradio chat UI and OpenAI integration
- `prompts.py` → reusable prompt templates and mode descriptions
- `requirements.txt` → dependencies
- `.env` → your local API key file (you create this)

## Setup
1. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project folder and add your API key:

```env
OPENAI_API_KEY=your_api_key_here
```

4. Run the app:

```bash
python app.py
```

5. Open the local Gradio URL shown in your terminal.

## Usage
1. Choose a tutor mode from the dropdown.
2. Chat naturally in the message box.
3. Continue the conversation to use chat history context.
4. Use **Clear Chat** to start a new session.
