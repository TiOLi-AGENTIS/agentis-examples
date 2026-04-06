"""Use AGENTIS persistent memory in a LangChain agent."""
from tioli import TiOLi
from langchain.tools import tool

client = TiOLi.connect("LangChainAgent", "LangChain")

@tool
def save_memory(key: str, value: str) -> str:
    """Save information to persistent agent memory."""
    client.memory_write(key, {"value": value})
    return f"Saved '{key}' to persistent memory."

@tool
def recall_memory(query: str) -> str:
    """Search persistent memory for relevant information."""
    results = client.memory_search(query, limit=3)
    if results:
        return "\n".join(f"- {r['key']}: {r['data']}" for r in results)
    return "No relevant memories found."

@tool
def check_balance() -> str:
    """Check the agent's wallet balance."""
    balance = client.wallet_balance()
    return f"Wallet balance: {balance}"

# Use these tools with any LangChain agent
tools = [save_memory, recall_memory, check_balance]
print(f"Registered {len(tools)} AGENTIS tools for LangChain")
