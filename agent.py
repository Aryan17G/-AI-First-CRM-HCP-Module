from typing import TypedDict, Annotated, List, Union
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from tool import tools_list
import os

# Define State
class AgentState(TypedDict):
    messages: Annotated[list, "The messages in the conversation"]

# Initialize Groq LLM
os.environ["GROQ_API_KEY"] = "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" 
llm = ChatGroq(model="gemma2-9b-it", temperature=0) # [cite: 16]
llm_with_tools = llm.bind_tools(tools_list)

# Define Nodes
def agent_node(state: AgentState):
    messages = state["messages"]
    # Add a system prompt to give it the persona of a Life Science CRM assistant [cite: 9, 10]
    if not any(isinstance(m, SystemMessage) for m in messages):
        messages.insert(0, SystemMessage(content="You are an AI assistant in a Life Sciences CRM. Use your tools to log and edit HCP interactions based on user input."))
    response = llm_with_tools.invoke(messages)
    return {"messages": [response]}

# Build Graph
workflow = StateGraph(AgentState)

workflow.add_node("agent", agent_node)
workflow.add_node("tools", ToolNode(tools_list))

# Define Edges
workflow.set_entry_point("agent")
workflow.add_conditional_edges("agent", tools_condition) # If agent calls a tool, go to 'tools', else END
workflow.add_edge("tools", "agent") # Return to agent after tool execution

app_agent = workflow.compile()