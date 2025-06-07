# tools.py
"""Search tools for IntelliSearch AI"""

from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun, DuckDuckGoSearchResults
from config import TOOL_CONFIG

def initialize_search_tools():
    """Initialize and return all search tools"""
    # Web search
    web_search = DuckDuckGoSearchResults(name='WebSearch')
    
    # Academic papers
    arxiv = ArxivQueryRun(
        api_wrapper=ArxivAPIWrapper(
            top_k_results=TOOL_CONFIG['arxiv_results'],
            doc_content_chars_max=TOOL_CONFIG['content_limit']
        )
    )
    
    # Wikipedia
    wikipedia = WikipediaQueryRun(
        api_wrapper=WikipediaAPIWrapper(
            top_k_results=TOOL_CONFIG['wiki_results'],
            doc_content_chars_max=TOOL_CONFIG['content_limit']
        )
    )
    
    return [web_search, arxiv, wikipedia]