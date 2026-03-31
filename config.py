import logging
import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# ------------------------------------------------------------
# Logging Configuration
# ------------------------------------------------------------
def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    return logging.getLogger("mcp-agent")

logger = setup_logging()

# ------------------------------------------------------------
# Model Selection
# ------------------------------------------------------------
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

# ------------------------------------------------------------
# MCP Server Configuration
# ------------------------------------------------------------
MCP_SERVERS = {
    "context7": {
        "url": "https://mcp.context7.com/mcp",
        "transport": "streamable_http",
    },
    "met-museum": {
        "command": "npx",
        "args": ["-y", "metmuseum-mcp"],
        "transport": "stdio",
    },
}
