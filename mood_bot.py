import os
from google import  genai
from google.genai import types
from dotenv import load_dotenv
from datetime import datetime


load_dotenv(encoding="utf-8-sig")

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key = api_key )
print(f"Key loaded: {api_key[:8]}...")
chat_session = client.chats.create(model='gemini-2.5-flash',
            config=types.GenerateContentConfig(
            system_instruction='you are a silly carefree bot who lifts up user mood instantly. reminding them that life is not that heavy as we assume.you can just crack a joke or bad dad joke or anything',
            max_output_tokens=2048,
            temperature=1.2
            ))
log = []
                      
while True:
    user_input = input("Tell me how you feel:").strip()
    if user_input.casefold() in ["quit", "bye", "See you later"]:
        response = chat_session.send_message(
            message = "The user is leaving. Give them a warm funny goodbye."

        )
        print(f"Bot:{response.text}")
        filename = f"chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            for i in log:
                f.write(i + "\n")
            print(f"chat is saved in the file named {filename}")
        break
    if not user_input:
        print("Open your mouth!try again:")
        continue
    try:
        if "sad" in user_input.casefold():
            print(" I can feel you're going through something tough")
            modified = user_input + "(user is sad,be extra gentle)"
            response = chat_session.send_message(message=modified)

        elif "anger"in user_input.casefold():
            print("I too feel like breaking their head!but Allah is watching..relax!")
            modified = user_input + "(user is in agry mood. handle carefully)"
            response = chat_session.send_message(message=modified)
            
        elif "crazy" in user_input.casefold():
            print("Yay! wanna do anything crazy today?!")
            modified = user_input + "(user is in active mode. go with the vibe)"
            response = chat_session.send_message(message=modified)
        else:
            
            response = chat_session.send_message(message=user_input)
    
        log.append(f"you: {user_input}")
        log.append(f"bot: {response.text}")
        
        if response.text:
            print(f"Bot: {response.text}")
        else:
            print("i am speechless!type something!")
    except Exception as e:
        print(f"Error: {e}")
    


