import os
import openai

# Make sure you set your API key before running:
# export OPENAI_API_KEY="your_api_key"  (Linux/Mac)
# setx OPENAI_API_KEY "your_api_key"    (Windows)

openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_ai():
    print("🤖 AI Assistant (type 'exit' to quit)")
    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit", "bye"]:
            print("AI: Goodbye! 👋")
            break

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # or "gpt-4" if available
                messages=[{"role": "user", "content": user_input}]
            )
            print("AI:", response["choices"][0]["message"]["content"])
        except Exception as e:
            print("⚠️ Error:", e)

if __name__ == "__main__":
    chat_with_ai()
