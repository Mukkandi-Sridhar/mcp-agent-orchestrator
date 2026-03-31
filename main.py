"""
MCP Multi-Server Agent - Main Entry Point
-----------------------------------------

This script connects all components and runs the command-line AI assistant.
"""

import asyncio
from config import logger
from mcp_client import get_mcp_tools
from agent_factory import create_mcp_agent


async def main():
    """
    Main function providing the CLI interface for the MCP agent.
    """

    logger.info("Initializing MCP Agent Orchestrator...")

    # 1. Retrieve tools from MCP servers
    try:
        tools = await get_mcp_tools()
    except Exception as e:
        logger.error(f"Agent initialization failed. Could not load tools: {e}")
        return

    # 2. Build the ReAct Agent using the retrieved tools
    agent = create_mcp_agent(tools)

    # 3. Setup conversation session configuration
    config = {
        "configurable": {
            "thread_id": "conversation_session"
        }
    }

    print("\n" + "="*50)
    print("Agent ready. Type 'exit' to quit.")
    print("="*50 + "\n")

    # 4. Initial introduction
    try:
        response = await agent.ainvoke(
            {
                "messages": [
                    {
                        "role": "system",
                        "content": "You are a helpful AI assistant that can use tools."
                    },
                    {
                        "role": "user",
                        "content": "Introduce yourself and explain what tools you have available from the connected servers."
                    }
                ]
            },
            config=config
        )
        print(f"Assistant: {response['messages'][-1].content}\n")
    except Exception as e:
        logger.warning(f"Initial introduction failed: {e}")

    # 5. CLI loop
    while True:

        print("Choices:")
        print("1. Ask a question")
        print("2. Exit")

        choice = input("\nEnter choice (1-2): ").strip()

        if choice == "1":
            query = input("\nYour question: ").strip()
            if not query:
                continue

            print("\nThinking...")
            try:
                response = await agent.ainvoke(
                    {"messages": query},
                    config=config
                )

                print("\nAssistant Response:\n" + "-"*20)
                print(response["messages"][-1].content)
                print("-"*20 + "\n")
            except Exception as e:
                logger.error(f"Error during agent invocation: {e}")

        elif choice == "2" or choice.lower() == "exit":
            print("\nExiting program.\n")
            break

        else:
            print("Invalid option. Please enter 1 or 2.")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
