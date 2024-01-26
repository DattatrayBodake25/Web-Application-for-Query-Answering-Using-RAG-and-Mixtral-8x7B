# mixtral_library.py
from transformers import pipeline

# hugging face API key
HUGGING_FACE_API_KEY = 'my_api_key'

# Specify the local path to the Mixtral model folder
MIXTRAL_MODEL_PATH = r"D:\AI Assignment\OmniValueSolutions\backend\TheBlokeMixtral-8x7B-v0.1-GGUF"

def mixtral_8x7b_parse_document(document_content):
    # Initialize Mixtral 8x7B pipeline with the local path
    mixtral_pipeline = pipeline("text-generation", model=MIXTRAL_MODEL_PATH, device=0)

    # Use Mixtral 8x7B to answer questions about the document
    mixtral_output = mixtral_pipeline({
        'question': 'What is in the document?',
        'context': document_content
    })

    return mixtral_output
