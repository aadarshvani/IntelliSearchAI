# config.py
"""Configuration for IntelliSearch AI"""

# App Info
APP_NAME = "IntelliSearch AI"
APP_TAGLINE = "AI-Powered Research Assistant"
APP_ICON = "🧠"

# Models
AVAILABLE_MODELS = [
    'Gemma2-9b-it',
    'llama-3.3-70b-versatile',
]
DEFAULT_MODEL = 'Gemma2-9b-it'

# Tool Settings
TOOL_CONFIG = {
    'arxiv_results': 1,
    'wiki_results': 1,
    'content_limit': 1000
}

# Agent Settings
AGENT_CONFIG = {
    'temperature': 0.7,
    'max_iterations': 5,
    'context_messages': 10
}

# UI Settings
PAGE_CONFIG = {
    'page_title': APP_NAME,
    'page_icon': APP_ICON,
    'layout': "wide"
}

# Messages
WELCOME_MSG = {
    'role': 'assistant',
    'content': f'👋 Welcome to **{APP_NAME}**! I can search the web, academic papers, and Wikipedia to help answer your questions. What would you like to know?'
}