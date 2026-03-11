from langchain_core.tools import tool
from model import SessionLocal, HCPInteraction
from pydantic import BaseModel, Field
from typing import Optional

# Tool 1: Log Interaction (Required)
@tool
def log_interaction(hcp_name: str, topics_discussed: str, date: Optional[str] = None) -> str:
    """Use this tool to log a new interaction with a Healthcare Professional (HCP). 
    It captures interaction data potentially using the LLM for entity extraction."""
    db = SessionLocal()
    new_interaction = HCPInteraction(
        hcp_name=hcp_name, 
        topics_discussed=topics_discussed,
        date=date
    )
    db.add(new_interaction)
    db.commit()
    return f"Successfully logged interaction with {hcp_name}."

# Tool 2: Edit Interaction (Required)
@tool
def edit_interaction(hcp_name: str, new_topics: str) -> str:
    """Use this tool to modify or edit existing logged data for an HCP interaction."""
    db = SessionLocal()
    interaction = db.query(HCPInteraction).filter(HCPInteraction.hcp_name == hcp_name).first()
    if interaction:
        interaction.topics_discussed = new_topics
        db.commit()
        return f"Updated interaction details for {hcp_name}."
    return f"Could not find an existing interaction for {hcp_name}."

# Tool 3: Search HCP Directory
@tool
def search_hcp(hcp_name: str) -> str:
    """Search the database to see if an HCP exists in the system."""
    return f"Found {hcp_name} in the cardiology department." # Mocked response

# Tool 4: Sentiment Analyzer
@tool
def analyze_sentiment(interaction_text: str) -> str:
    """Analyze the interaction text to infer if the HCP sentiment is Positive, Neutral, or Negative."""
    # In a real scenario, this could trigger a smaller LLM chain. For now, it's a tool node.
    if "great" in interaction_text.lower() or "impressed" in interaction_text.lower():
        return "Positive"
    return "Neutral"

# Tool 5: Follow-up Generator
@tool
def generate_follow_ups(topics: str) -> str:
    """Generate suggested follow-up actions based on the topics discussed."""
    return "Schedule follow-up meeting in 2 weeks; Send brochure."

# Combine them into a list for the LangGraph node
tools_list = [log_interaction, edit_interaction, search_hcp, analyze_sentiment, generate_follow_ups]