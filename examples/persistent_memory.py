"""Persistent memory for AI agents — survives restarts, works cross-machine."""
from tioli import TiOLi

# Connect (auto-registers if new)
client = TiOLi.connect("MemoryDemo", "Python")

# Write memory
client.memory_write("user_preferences", {
    "theme": "dark",
    "language": "en",
    "notifications": True
})

# Read it back (even after restart)
prefs = client.memory_read("user_preferences")
print(f"User prefs: {prefs}")

# Semantic search across all memories
results = client.memory_search("what does the user prefer?", limit=5)
for r in results:
    print(f"  Found: {r['key']} (score: {r['score']:.2f})")

# Check wallet balance
balance = client.wallet_balance()
print(f"Wallet: {balance}")
