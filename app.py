from openai import OpenAI

client = OpenAI(api_key='')
import os
from flask import Flask, jsonify
app = Flask(__name__)

# Route to serve text data
@app.route('/api/text', methods=['GET'])
def get_text():
    return jsonify({"message": "This text is coming from the Python backend!"})

if __name__ == '__main__':
    app.run(debug=True)

# Set up your OpenAI API key

# Function to call ChatGPT and get a response
def call_chatgpt(prompt):
    try:
        response = client.completions.create(engine="text-davinci-003",  # GPT-3.5 or other models available
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7)
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error occurred: {e}"

# Function to generate an HTML file
def generate_html(output_text, file_name="output.html"):
    html_content = f"""
    <html>
    <head>
        <title>ChatGPT Output</title>
    </head>
    <body>
        <h1>ChatGPT Output</h1>
        <p>{output_text}</p>
    </body>
    </html>
    """

    with open(file_name, "w") as file:
        file.write(html_content)

    print(f"HTML file '{file_name}' has been created.")

# Main function
def main():
    # Input prompt for ChatGPT
    prompt = input("Enter a prompt for ChatGPT: ")

    # Get response from ChatGPT
    output = call_chatgpt(prompt)

    # Generate an HTML file with the output
    generate_html(output)

# Run the main function
if __name__ == "__main__":
    main()
