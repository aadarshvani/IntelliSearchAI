# main.py
"""IntelliSearch AI - AI-Powered Research Assistant"""

import streamlit as st
from langchain.callbacks import StreamlitCallbackHandler

from config import PAGE_CONFIG
from session_manager import init_session, add_message, start_new_conversation, clear_api_key, get_messages
from ui_components import render_sidebar, render_header, render_chat_stats, display_messages, show_api_required
from tools import initialize_search_tools
from agent import create_intelligent_agent, build_context_prompt

def main():
    """Main application"""
    # Setup page
    st.set_page_config(**PAGE_CONFIG)
    
    # Initialize session
    init_session()
    
    # Render sidebar
    api_key, model, new_chat_btn, clear_key_btn = render_sidebar()
    
    # Handle button actions
    if new_chat_btn:
        start_new_conversation()
        st.rerun()
    
    if clear_key_btn:
        clear_api_key()
        st.rerun()
    
    # Render header
    render_header()
    
    # Check API key
    if not api_key:
        show_api_required()
    
    # Get messages
    messages = get_messages()
    
    # Display chat stats
    render_chat_stats(messages)
    
    # Display chat history
    display_messages(messages)
    
    # Handle user input
    if user_input := st.chat_input("Ask me anything..."):
        # Add user message
        add_message('user', user_input)
        
        # Display user message
        with st.chat_message('user'):
            st.write(user_input)
        
        # Get AI response
        try:
            # Initialize tools and agent
            tools = initialize_search_tools()
            agent = create_intelligent_agent(api_key, model, tools)
            
            # Generate response
            with st.chat_message('assistant'):
                callback = StreamlitCallbackHandler(
                    st.container(),
                    expand_new_thoughts=False,
                    collapse_completed_thoughts=True
                )
                
                # Build context-aware prompt
                context_prompt = build_context_prompt(messages, user_input)
                
                # Get response
                with st.spinner('🔍 Researching your question...'):
                    response = agent.run(context_prompt, callbacks=[callback])
                
                # Display and save response
                st.write(response)
                add_message('assistant', response)
                
        except Exception as e:
            error_message = f"❌ Error: {str(e)}"
            st.error(error_message)
            add_message('assistant', error_message)

if __name__ == "__main__":
    main()