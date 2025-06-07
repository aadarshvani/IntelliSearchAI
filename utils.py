# utils.py
"""Utility functions for IntelliSearch AI"""

import json
import datetime
from typing import List, Dict

def export_chat_to_json(messages: List[Dict]) -> str:
    """Export chat history as downloadable JSON"""
    export_data = {
        'exported_at': datetime.datetime.now().isoformat(),
        'app': 'IntelliSearch AI',
        'conversation': messages
    }
    return json.dumps(export_data, indent=2)

def get_chat_stats(messages: List[Dict]) -> Dict:
    """Get basic conversation statistics"""
    user_msgs = len([m for m in messages if m['role'] == 'user'])
    ai_msgs = len([m for m in messages if m['role'] == 'assistant'])
    
    return {
        'total_messages': len(messages),
        'user_messages': user_msgs,
        'ai_messages': ai_msgs
    }

def create_filename() -> str:
    """Create timestamped filename"""
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"intellisearch_chat_{timestamp}.json"

def validate_groq_key(api_key: str) -> bool:
    """Basic GROQ API key validation"""
    return bool(api_key and len(api_key) > 20 and api_key.startswith('gsk_'))