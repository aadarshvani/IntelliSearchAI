# IntelliSearch AI 🧠

An intelligent AI research assistant built with Langchain, GROQ, and Streamlit. Search the web, academic papers, and Wikipedia with context-aware conversations.

## ✨ Features

- 🌐 **Multi-Source Search**: Web, arXiv papers, Wikipedia
- 🧠 **Context Awareness**: Remembers conversation history  
- 💾 **Export Conversations**: Download chat as JSON
- 🔄 **Session Management**: New chat & API key controls
- 📊 **Chat Statistics**: Track conversation metrics
- 🎯 **Smart Models**: Choose from multiple GROQ models

## 🚀 Quick Start

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the app**:
   ```bash
   streamlit run main.py
   ```

3. **Get GROQ API Key**:
   - Visit [GROQ Console](https://console.groq.com/keys)
   - Create free account & generate key
   - Enter key in sidebar

## 📁 Project Structure

```
intellisearch-ai/
├── main.py              # Main application
├── config.py            # Configuration settings
├── agent.py             # AI agent logic
├── tools.py             # Search tools
├── ui_components.py     # UI elements
├── session_manager.py   # Session handling
├── utils.py             # Helper functions
├── requirements.txt     # Dependencies
└── README.md           # Documentation
```

## 🛠️ Architecture

**Clean, modular design** showcasing:
- Separation of concerns
- Configuration management  
- State management patterns
- Error handling
- User experience design

## 💼 Job-Ready Features

This project demonstrates:
- **Python Best Practices**: Clean, readable code
- **Streamlit Mastery**: Advanced UI components
- **API Integration**: GROQ LLM integration
- **State Management**: Session persistence
- **Modular Architecture**: Scalable code structure
- **User Experience**: Intuitive interface design

## 🎯 Usage Examples

**Research Questions:**
- "What are the latest developments in quantum computing?"
- "Explain machine learning algorithms with examples"
- "Current trends in renewable energy technology"

**Academic Research:**
- "Find recent papers on artificial intelligence ethics"
- "What's new in climate change research?"

## 🔧 Customization

**Add New Models** (config.py):
```python
AVAILABLE_MODELS = [
    'mixtral-8x7b-32768',
    'llama3-8b-8192', 
    'Gemma2-9b-it'
    # ... existing models
]
```

**Adjust Search Results** (config.py):
```python
TOOL_CONFIG = {
    'arxiv_results': 3,      # More papers
    'content_limit': 800     # Longer summaries
}
```

## 🚀 Deployment Ready

- Environment variables support
- Configuration externalization
- Error handling & validation
- User feedback systems
- Export/import functionality

## 🤝 Contributing

Built with modern development practices. Perfect for:
- Portfolio projects
- Job interviews  
- Learning Langchain
- Streamlit applications
---

**Built by Aadarsh Vani** | [LinkedIn](https://www.linkedin.com/in/aadarsh-vani-a60a641a0/) | [GitHub](https://github.com/aadarshvani)