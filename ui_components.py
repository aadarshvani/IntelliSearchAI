# ui_components.py
"""UI components for IntelliSearch AI"""

import streamlit as st
from config import AVAILABLE_MODELS, DEFAULT_MODEL, APP_NAME, APP_TAGLINE
from utils import validate_groq_key, get_chat_stats, export_chat_to_json, create_filename

def render_sidebar():
    """Render sidebar with controls"""
    st.sidebar.title('⚙️ Controls')
    
    # API Key (persistent)
    if 'api_key' not in st.session_state:
        st.session_state.api_key = ''
    
    api_key = st.sidebar.text_input(
        '🔑 GROQ API Key:',
        value=st.session_state.api_key,
        type='password',
        help='Your key stays saved during the session'
    )
    
    if api_key != st.session_state.api_key:
        st.session_state.api_key = api_key
    
    # Validation indicator
    if st.session_state.api_key:
        if validate_groq_key(st.session_state.api_key):
            st.sidebar.success('✅ Valid API Key')
        else:
            st.sidebar.warning('⚠️ Check API Key Format')
    
    # Model selection
    model = st.sidebar.selectbox(
        '🤖 AI Model:',
        AVAILABLE_MODELS,
        index=0,
        format_func=lambda x: x.replace('-', ' ').title()
    )
    
    st.sidebar.markdown('---')
    
    # Action buttons
    col1, col2 = st.sidebar.columns(2)
    with col1:
        new_chat = st.button('🆕 New Chat', use_container_width=True)
    with col2:
        clear_key = st.button('🗑️ Clear Key', use_container_width=True)
    
    return st.session_state.api_key, model, new_chat, clear_key

def render_header():
    """Render main header"""
    st.title(f'{APP_NAME}')
    st.markdown(f'*{APP_TAGLINE}*')
    st.markdown('---')

def render_chat_stats(messages):
    """Render conversation statistics"""
    if len(messages) > 1:  # More than welcome message
        stats = get_chat_stats(messages)
        st.sidebar.markdown('📊 **Chat Stats**')
        st.sidebar.write(f"Messages: {stats['total_messages']}")
        st.sidebar.write(f"Your questions: {stats['user_messages']}")
        
        # Export button
        if st.sidebar.button('💾 Export Chat'):
            chat_json = export_chat_to_json(messages)
            st.sidebar.download_button(
                '📥 Download JSON',
                chat_json,
                create_filename(),
                'application/json'
            )

def display_messages(messages):
    """Display chat messages"""
    for message in messages:
        with st.chat_message(message['role']):
            st.write(message['content'])

def show_api_required():
    """Show API key requirement"""
    st.warning('🔑 Please enter your GROQ API key in the sidebar to start chatting')
    st.info('💡 Get your free API key from [GROQ Console](https://console.groq.com/keys)')
    
    with st.expander('ℹ️ About IntelliSearch AI'):
        st.write("""
        **IntelliSearch AI** is an intelligent research assistant that can:
        
        - 🌐 Search the web for current information
        - 📚 Find academic papers from arXiv
        - 📖 Access Wikipedia knowledge
        - 🧠 Provide context-aware responses
        - 💾 Export conversation history
        
        Built with Langchain, GROQ, and Streamlit.
        """)
    
    st.stop()