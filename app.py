import os

import gradio as gr
from openai import OpenAI

from prompts import PROMPT_TEMPLATES

MODEL_NAME = "gpt-4.1-mini"


def build_messages(mode: str, user_input: str):
    """Build a beginner-friendly system and user message for the selected mode."""
    template = PROMPT_TEMPLATES[mode]
    return [
        {"role": "system", "content": "You are Python Tutor Bot, a friendly Python teaching assistant for beginners."},
        {"role": "user", "content": template.format(user_input=user_input)},
    ]


def get_tutor_response(mode: str, user_input: str) -> str:
    """Generate a response from OpenAI for the selected tutoring mode."""
    if not user_input or not user_input.strip():
        return "Please enter some text or code so I can help you."

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return "Missing OPENAI_API_KEY. Please set your environment variable and try again."

    try:
        client = OpenAI(api_key=api_key)
        messages = build_messages(mode, user_input.strip())

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            temperature=0.4,
        )
        return response.choices[0].message.content or "I could not generate a response. Please try again."
    except Exception as error:
        return f"Something went wrong while contacting the AI service: {error}"


def build_app():
    with gr.Blocks(title="Python Tutor Bot") as app:
        gr.Markdown("# 🐍 Python Tutor Bot")
        gr.Markdown("Learn Python with explanations, debugging help, quizzes, and code improvement tips.")

        mode = gr.Dropdown(
            choices=["Explain Concept", "Debug Code", "Quiz Me", "Improve Code"],
            value="Explain Concept",
            label="Choose a learning mode",
        )

        user_input = gr.Textbox(
            label="Enter your question or code",
            lines=10,
            placeholder="Example: Why do I get an IndexError in this loop?",
        )

        output = gr.Textbox(label="Tutor response", lines=12)

        with gr.Row():
            submit_btn = gr.Button("Get Help")
            clear_btn = gr.Button("Clear")

        submit_btn.click(fn=get_tutor_response, inputs=[mode, user_input], outputs=output)
        clear_btn.click(lambda: ("", ""), inputs=None, outputs=[user_input, output])

    return app


if __name__ == "__main__":
    build_app().launch()
