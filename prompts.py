PROMPT_TEMPLATES = {
    "Explain Concept": (
        "Explain this Python concept for a beginner using simple words, a short example, "
        "and a quick summary at the end:\n\n{user_input}"
    ),
    "Debug Code": (
        "Help debug this Python code. Identify likely errors, explain why they happen, and "
        "show a corrected version:\n\n{user_input}"
    ),
    "Quiz Me": (
        "Create a short Python quiz for a beginner based on this topic. Include 3 questions, "
        "wait for answers, then provide feedback when asked:\n\n{user_input}"
    ),
    "Improve Code": (
        "Improve this Python code for readability, style, and beginner-friendly best practices. "
        "Explain each improvement clearly:\n\n{user_input}"
    ),
}
