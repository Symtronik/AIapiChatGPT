import os
import openai
import dotenv

dotenv.load_dotenv()

API_KEY = os.getenv("SECRET_KEY_CHATGPT")

openai.api_key = API_KEY

message_history = []

def chat(inp, role="user"):
    message_history.append({"role":role, "content":inp})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message_history,
    )
    reply_content = completion.choices[0].message.content
    print(reply_content)
    message_history.append(({"role": "assistant", "content": reply_content}))
    return reply_content

while True:
    user_input = input("Text: ")
    print("Your text", user_input)
    print()
    chat(user_input)
    print()

