import os
from pathlib import Path
from typing import Any

import gradio as gr
from dotenv import load_dotenv
from openai import OpenAI

from prompts import MODE_DESCRIPTIONS, PROMPT_TEMPLATES

MODEL_NAME = "gpt-4.1-mini"

# Load environment variables from a local .env file if it exists.
load_dotenv(dotenv_path=Path(__file__).parent / ".env")

SYSTEM_PROMPT = (
    "You are Advanced Python Tutor Bot, an expert and patient teacher for beginners. "
    "Help with Python fundamentals, debugging, quizzes, and code quality. "
    "When relevant, include beginner-friendly data structures and algorithms guidance "
    "(lists, dicts, sets, stacks, queues, recursion, sorting, searching, Big-O at a simple level)."
)


def _history_to_messages(history: list[Any]) -> list[dict[str, str]]:
    """Convert Gradio chat history into OpenAI message objects.

    Supports both older history formats (list of [user, assistant]) and
    newer message formats (list of dicts).
    """
    messages: list[dict[str, str]] = []

    for item in history:
        if isinstance(item, dict):
            role = item.get("role")
            content = item.get("content", "")
            if role in {"user", "assistant"} and content:
                messages.append({"role": role, "content": str(content)})
            continue

        if isinstance(item, (list, tuple)) and len(item) == 2:
            user_text, assistant_text = item
            if user_text:
                messages.append({"role": "user", "content": str(user_text)})
            if assistant_text:
                messages.append({"role": "assistant", "content": str(assistant_text)})

    return messages


def build_messages(mode: str, user_input: str, history: list[Any]) -> list[dict[str, str]]:
    """Build OpenAI messages using mode template + ongoing chat history."""
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    messages.extend(_history_to_messages(history))

    mode_instruction = PROMPT_TEMPLATES[mode].format(user_input=user_input)
    messages.append({"role": "user", "content": mode_instruction})
    return messages


def get_tutor_response(user_input: str, history: list[Any], mode: str) -> str:
    """Generate a response from OpenAI for the selected tutoring mode."""
    if not user_input or not user_input.strip():
        return "Please enter some text or code so I can help you."

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return (
            "Missing OPENAI_API_KEY. Add it to a `.env` file in this folder like: "
            "OPENAI_API_KEY=your_key_here"
        )

    try:
        client = OpenAI(api_key=api_key)
        messages = build_messages(mode, user_input.strip(), history or [])
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            temperature=0.4,
        )
        return response.choices[0].message.content or "I could not generate a response. Please try again."
    except Exception as error:
        return f"Something went wrong while contacting the AI service: {error}"


def build_app() -> gr.Blocks:
    theme = gr.themes.Soft(primary_hue="blue", secondary_hue="slate", neutral_hue="slate")

    with gr.Blocks(title="Advanced Python Tutor Bot", theme=theme) as app:
        gr.Markdown(
            """
        # 🧠 Advanced Python Tutor Bot
        A professional learning assistant for beginners: explanations, debugging, quizzes, and code improvements.
        """
        )

        with gr.Row():
            with gr.Column(scale=2):
                mode = gr.Dropdown(
                    choices=["Explain Concept", "Debug Code", "Quiz Me", "Improve Code"],
                    value="Explain Concept",
                    label="Tutor Mode",
                    info="Pick how you want the tutor to help in this chat.",
                )
            with gr.Column(scale=3):
                mode_note = gr.Markdown(MODE_DESCRIPTIONS["Explain Concept"])

        mode.change(lambda m: MODE_DESCRIPTIONS[m], inputs=mode, outputs=mode_note)

        gr.ChatInterface(
            fn=get_tutor_response,
            additional_inputs=[mode],
        )


    return app


if __name__ == "__main__":
    build_app().launch()
