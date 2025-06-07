# session_manager.py
"""Session management for IntelliSearch AI"""

import streamlit as st
from config import WELCOME_MSG

def init_session():
    """Initialize session state"""
    if 'messages' not in st.session_state:
        st.session_state.messages = [WELCOME_MSG.copy()]
    if 'api_key' not in st.session_state:
        st.session_state.api_key = ''

def add_message(role: str, content: str):
    """Add message to chat history"""
    st.session_state.messages.append({
        'role': role,
        'content': content
    })

def start_new_conversation():
    """Start fresh conversation (keep API key)"""
    st.session_state.messages = [WELCOME_MSG.copy()]

def clear_api_key():
    """Remove API key from session"""
    st.session_state.api_key = ''

def get_messages():
    """Get current messages"""
    return st.session_state.messages