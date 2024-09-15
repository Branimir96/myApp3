import os
import sqlite3
from openai import OpenAI
from datetime import datetime

# Initialize the OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def chat_with_gpt(messages):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {str(e)}"

def init_db():
    conn = sqlite3.connect('chatgpt_responses.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS responses
                 (timestamp TEXT, user_input TEXT, response TEXT)''')
    conn.commit()
    return conn

def save_response(conn, user_input, response):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c = conn.cursor()
    c.execute("INSERT INTO responses VALUES (?, ?, ?)", (timestamp, user_input, response))
    conn.commit()

def main():
    print("Welcome to ChatGPT! Type 'quit' to exit.")
    messages = [{"role": "system", "content": "You are a helpful assistant."}]
    conn = init_db()

    try:
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'quit':
                break

            messages.append({"role": "user", "content": user_input})
            response = chat_with_gpt(messages)
            print(f"ChatGPT: {response}")
            save_response(conn, user_input, response)
            messages.append({"role": "assistant", "content": response})
    finally:
        conn.close()

if __name__ == "__main__":
    main()