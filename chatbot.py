import os
from google import genai

# Set API key
os.environ["GEMINI_API_KEY"] = "YOUR_API_KEY_HERE"

# Create client
client = genai.Client()

history = []

print("Chatbot started (type 'quit' to exit)")

while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        break

    try:
        # Add user message to history
        history.append({
            "role": "user",
            "parts": [user_input]
        })

        # Send entire conversation
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=history
        )

        ai_reply = response.text

        print("AI:", ai_reply)

        # Save AI response in history
        history.append({
            "role": "model",
            "parts": [ai_reply]
        })

    except Exception as e:
        print("Error:", e)