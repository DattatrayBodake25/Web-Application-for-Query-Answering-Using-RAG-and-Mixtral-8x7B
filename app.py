import os
from flask import Flask, render_template, request, jsonify
from mixtral_library import mixtral_8x7b_parse_document
from rag_library import rag_answer_query
import openai
import fitz
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Set your OpenAI API key
openai.api_key = 'my_open_ai_key'

# Function to load content from a PDF file
def load_document_content(pdf_path):
    doc = fitz.open(pdf_path)
    content = ""
    for page_num in range(doc.page_count):
        page = doc[page_num]
        content += page.get_text()
    doc.close()
    return content

# Load PDF document content here
pdf_path = r"D:\AI Assignment\OmniValueSolutions\scrum_master_en.pdf"
document_content = load_document_content(pdf_path)

# Define the rephrase_with_chatgpt function before using it
def rephrase_with_chatgpt(text):
    try:
        # Call the OpenAI ChatGPT API to rephrase the text
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Given the explanation: '{text}', please use the Feynman Technique to explain in a simple, intuitive way.",
            max_tokens=150,
            n=1,  # Number of completions
            stop=None,
        )

        return response.choices[0].text.strip()

    except Exception as e:
        # Handle API request errors
        return f"Error during ChatGPT rephrasing: {str(e)}"

@app.route('/')
def index():
    return render_template('query.html', document_title='Scrum Master')

@app.route('/answer', methods=['POST'])
def answer_query():
    try:
        data = request.get_json()

        if 'query' not in data:
            raise ValueError('Invalid request. "query" parameter missing.')

        user_query = data['query']

        print("Received query:", user_query)

        # Part 1: Document Parsing with Mixtral 8x7B
        mixtral_output = mixtral_8x7b_parse_document(document_content)
        print("Mixtral Output:", mixtral_output)

        # Part 2: Query Answering with RAG
        rag_output = rag_answer_query(user_query, mixtral_output)
        print("RAG Output:", rag_output)

        # Part 4: ChatGPT Implementation
        chatgpt_output = rephrase_with_chatgpt(rag_output)
        print("ChatGPT Output:", chatgpt_output)

        return jsonify({'answer': chatgpt_output})

    except ValueError as ve:
        error_message = f'ValueError: {str(ve)}'
        print(error_message)
        return jsonify({'error': error_message}), 400

    except Exception as e:
        error_message = f'Internal Server Error: {str(e)}'
        print(error_message)
        return jsonify({'error': error_message}), 500

if __name__ == '__main__':
    app.run(debug=True)