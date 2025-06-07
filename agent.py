# agent.py
"""AI agent for IntelliSearch AI"""

from langchain_groq import ChatGroq
from langchain.agents import initialize_agent, AgentType
from config import AGENT_CONFIG

def create_intelligent_agent(api_key: str, model: str, tools):
    """Create the AI research agent"""
    try:
        # Initialize LLM
        llm = ChatGroq(
            api_key=api_key,
            model=model,
            streaming=True,
            temperature=AGENT_CONFIG['temperature']
        )
        
        # Create agent
        agent = initialize_agent(
            tools=tools,
            llm=llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True,
            handle_parsing_errors=True,
            max_iterations=AGENT_CONFIG['max_iterations']
        )
        
        return agent
        
    except Exception as e:
        raise Exception(f"Failed to create agent: {str(e)}")

def build_context_prompt(messages, current_question):
    """Build context-aware prompt for better responses"""
    if len(messages) <= 1:
        return current_question
    
    # Get recent conversation context
    recent_messages = messages[-(AGENT_CONFIG['context_messages']):-1]
    
    context = "Previous conversation context:\n"
    for msg in recent_messages:
        role = "User" if msg['role'] == 'user' else "Assistant"
        context += f"{role}: {msg['content'][:100]}...\n"
    
    return f"{context}\nCurrent question: {current_question}"