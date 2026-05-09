# Python Tutor Bot

Python Tutor Bot is a small educational AI app for beginner Python learners.

It can help with:
- Explaining Python concepts
- Debugging Python code
- Giving short quizzes
- Improving code quality

## Tech Stack
- Python
- Gradio
- OpenAI Python SDK

## Project Files
- `app.py` → Gradio app and OpenAI call logic
- `prompts.py` → reusable prompt templates for all tutor modes
- `requirements.txt` → dependencies

## Setup

1. **Clone or open this project**
2. **Create and activate a virtual environment** (recommended)

```bash
python -m venv .venv
source .venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set your OpenAI API key as an environment variable**

```bash
export OPENAI_API_KEY="your_api_key_here"
```

5. **Run the app**

```bash
python app.py
```

6. Open the local Gradio URL shown in your terminal.

## How to Use

1. Select a mode from the dropdown:
   - Explain Concept
   - Debug Code
   - Quiz Me
   - Improve Code
2. Enter your Python question, concept, or code.
3. Click **Get Help**.

## Notes for Beginners
- If your input box is empty, the app will ask you to enter text/code.
- If `OPENAI_API_KEY` is missing, the app will show a clear setup message.
- Keep prompts specific for better answers.
