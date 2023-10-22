import os
import openai
import dotenv

dotenv.load_dotenv()

API_KEY = os.getenv("SECRET_KEY_CHATGPT")

openai.api_key = API_KEY

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role":"user", "content": "What is the circumference of the moon in km?"}]
)


reply_content = completion.choices[0].message.content
print(reply_content)
# response = completion['choices'][0]['message']['content']

message_history = []
user_input = input(">: ")

print("User's input was", user_input)

message_history.append(({"role": "assistant", "content": user_input}))

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=message_history,
)

reply_content = completion.choices[0].message.content
print(reply_content)

user_input = input(">:")
print("User's input was", user_input)
print()
message_history.append(({"role": "user", "content": user_input}))
completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=message_history,
)
reply_content = completion.choices[0].message.content
print(reply_content)
