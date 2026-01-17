import streamlit as st
import threading
import os
import asyncio
import sys

# --- 1. THE "ULTIMATE" GLOBAL LOCK ---
# We check if our custom 'bot_lock' exists in the system modules.
# This prevents the bot from starting twice, even if the page is refreshed.
if "bot_lock" not in sys.modules:
    sys.modules["bot_lock"] = True
    FIRST_RUN = True
else:
    FIRST_RUN = False

# --- 2. STREAMLIT UI ---
st.set_page_config(page_title="Bot Server", page_icon="🚀")
st.title("Service Status: Online ✅")
st.write("The bot is running in the background.")

# BRIDGE: Injects Streamlit Secrets into the environment
for key, value in st.secrets.items():
    os.environ[key] = str(value)

# --- 3. YOUR CODE ---
RAW_CODE = """
#!/usr/bin/env python3

import os
import sys

def check_requirements():
    try:
        import discord
        import aiohttp
        print("✅ All requirements are installed!")
        return True
    except ImportError as e:
        print(f"❌ Missing requirement: {e}")
        print("📦 Installing requirements...")
        os.system("pip install -r requirements.txt")
        return False

def check_token():
    """Check if bot token is set"""
    token = os.environ.get('DISCORD_BOT_TOKEN', '')
    if token and token != 'YOUR_BOT_TOKEN_HERE':
        print("✅ Bot token found in environment variables!")
        return True
    
    # Check in the bot file
    try:
        with open('apollo_bot.py', 'r') as f:
            content = f.read()
            if 'YOUR_BOT_TOKEN_HERE' in content:
                print("⚠️  Bot token not set! Please edit apollo_bot.py and add your token.")
                print("   Line to edit: token = 'YOUR_BOT_TOKEN_HERE'")
                return False
            else:
                print("✅ Bot token found in configuration!")
                return True
    except:
        print("❌ Could not read apollo_bot.py")
        return False

def main():
    print("=" * 50)
    print("🌟 Apollo Bot - Quick Start Check")
    print("=" * 50)
    print()
    
    # Check requirements
    print("📦 Checking requirements...")
    check_requirements()
    print()
    
    # Check token
    print("🔑 Checking bot token...")
    if not check_token():
        print()
        print("📝 To get your bot token:")
        print("   1. Go to https://discord.com/developers/applications")
        print("   2. Create a new application")
        print("   3. Go to 'Bot' section")
        print("   4. Click 'Add Bot'")
        print("   5. Copy the token")
        sys.exit(1)
    print()
    
    print("🚀 Starting Apollo Bot...")
    print()
    print("📌 Commands to try once bot is online:")
    print("   • a.fact - Get a useless fact")
    print("   • a.dog - See a cute dog")
    print("   • a.joke - Laugh at a joke")
    print("   • a.help - See all commands")
    print()
    print("=" * 50)
    
    # Import and run the bot
    import apollo_bot
    apollo_bot.bot.run(apollo_bot.token)

if __name__ == "__main__":
    main()
"""

# --- 4. STARTUP ENGINE ---
def run_bot():
    # Setup new loop for this specific background thread
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    # Passing 'globals()' ensures functions can see each other
    exec(RAW_CODE, globals())

if FIRST_RUN:
    thread = threading.Thread(target=run_bot, daemon=True)
    thread.start()
    st.success("🚀 Bot launched for the first time!")
else:
    st.info("ℹ️ Bot is already running in the background.")

# Show a small clock so the user knows the page is "alive"
st.divider()
st.caption(f"Last page refresh: {time.strftime('%H:%M:%S')}")
