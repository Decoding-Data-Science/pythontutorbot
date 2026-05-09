PROMPT_TEMPLATES = {
    "Explain Concept": (
        "Explain this Python concept for a beginner using simple words, a short example, "
        "and a quick summary at the end:\n\n{user_input}"
    ),
    "Debug Code": (
        "Help debug this Python code. Identify likely errors, explain why they happen, and "
        "show a corrected version. End with a short prevention checklist:\n\n{user_input}"
    ),
    "Quiz Me": (
        "Run a short interactive Python quiz for a beginner based on this topic. "
        "Ask one question at a time, wait for the learner's answer, then give feedback and continue:\n\n{user_input}"
    ),
    "Improve Code": (
        "Improve this Python code for readability, style, and beginner-friendly best practices. "
        "Explain each improvement clearly and show before/after snippets when possible:\n\n{user_input}"
    ),
}

MODE_DESCRIPTIONS = {
    "Explain Concept": "**Explain Concept**: Learn a topic with plain-English explanations and examples.",
    "Debug Code": "**Debug Code**: Find errors, understand causes, and get corrected code.",
    "Quiz Me": "**Quiz Me**: Practice with a guided one-question-at-a-time mini quiz.",
    "Improve Code": "**Improve Code**: Refactor code for readability, structure, and best practices.",
}
