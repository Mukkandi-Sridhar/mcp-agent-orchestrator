from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import InMemorySaver
from config import OPENAI_MODEL

def create_mcp_agent(tools):
    """
    Initializes the ChatOpenAI model and builds the LangGraph ReAct agent.
    """
    
    # Initialize the model with the configured OPENAI_MODEL name
    model = ChatOpenAI(
        model=OPENAI_MODEL
    )
    
    # Conversation memory (storing conversation state)
    checkpointer = InMemorySaver()
    
    # Create the ReAct agent using the provided tools and memory
    agent = create_react_agent(
        model=model,
        tools=tools,
        checkpointer=checkpointer
    )
    
    return agent
