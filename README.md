#  MoodBot — The Chatbot I Wish I Could Be

I take life too seriously. I worry. I overthink.

So I built the opposite of myself.

MoodBot is a silly, carefree AI chatbot that sees life full of opportunities. 
It lifts your mood instantly — with bad dad jokes, wild energy, and a reminder 
that life isn't as heavy as we make it.

## What It Does
- Detects your mood (sad, angry, crazy) and responds accordingly
- Remembers the full conversation — it knows what you said earlier
- Saves every chat session to a timestamped file
- Gives you a warm, funny goodbye when you leave

## Tech Stack
- Python
- Google Gemini API (gemini-2.5-flash)
- Stateful chat sessions
- python-dotenv for secure API key management

## How to Run
1. Clone the repo
2. Create a virtual environment and install dependencies:
   pip install google-genai python-dotenv
3. Create a .env file with your Gemini API key:
   GEMINI_API_KEY=your_key_here
4. Run:
   python mood_bot.py

## Why I Built This
Because sometimes you need a friend who doesn't take life seriously.
And sometimes that friend is a Python script.
