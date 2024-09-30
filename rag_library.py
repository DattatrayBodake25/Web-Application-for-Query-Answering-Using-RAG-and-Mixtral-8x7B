# rag_library.py
from transformers import pipeline

# Replace 'YOUR_HUGGING_FACE_API_KEY' with your actual API key
HUGGING_FACE_API_KEY = 'my_key'

# Specify the local path to the RAG model folder
RAG_MODEL_PATH = r"D:\AI Assignment\OmniValueSolutions\backend\facebookrag-sequence-nq"

def rag_answer_query(user_query, mixtral_output):
    # Initialize RAG pipeline with the local path
    rag_pipeline = pipeline("text-generation", model=RAG_MODEL_PATH, device=0)

    # Generate an answer using RAG, combining Mixtral output
    rag_output = rag_pipeline({
        'query': user_query,
        'context': mixtral_output['context'],
        'answer': mixtral_output['answer']
    })

    return rag_output[0]['generated_text']
