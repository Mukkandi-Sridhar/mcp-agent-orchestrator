from langchain_mcp_adapters.client import MultiServerMCPClient
from config import MCP_SERVERS, logger

async def get_mcp_tools():
    """
    Connects to the configured MCP servers and retrieves their tools.
    """
    client = MultiServerMCPClient(MCP_SERVERS)
    
    logger.info("Connecting to MCP servers and retrieving tools...")

    try:
        # Retrieve tools from the MCP servers
        tools = await client.get_tools()
        logger.info(f"Successfully loaded {len(tools)} MCP tools")
        return tools
    except Exception as e:
        logger.error(f"Failed to connect to MCP servers: {e}")
        raise e
