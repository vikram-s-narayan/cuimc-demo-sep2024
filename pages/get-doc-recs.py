import streamlit as st

st.title("Get Document Recommendations")

import os

user_docs_directory = os.path.join('user-docs', st.session_state.session_id)
all_documents_content = ""

for filename in os.listdir(user_docs_directory):
    file_path = os.path.join(user_docs_directory, filename)
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            all_documents_content += file.read() + "\n\n ---------------- \n\n"

import openai
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")

# Set the OpenAI API key
openai.api_key = openai_api_key

MODEL = "gpt-4o-2024-08-06"
# Function to get GPT-4 response
def get_gpt4o_response(prompt, context):
    response = openai.chat.completions.create(
        model=MODEL,
        temperature=0,
                messages=[
            {
                "role": "system",
                "content": prompt
            },
                        {
                "role": "user",
                "content": f"CONTEXT: {context}"
            }
            ]
    )
    return response.choices[0].message.content



# Define the prompt
prompt = (
    "You are a helpful insurance pre-authorization assistant at a hospital reviewing documents for completeness and accuracy before they are sent to the payer. "
    "Review the context provided (which includes the UM guidelines and documents being submitted) and give a list of missing documents and requirements."
)

# Get the response from GPT-4
gpt4_response = get_gpt4o_response(prompt, all_documents_content)

# Display the response in the Streamlit app
st.subheader("GPT-4 Review")
st.write(gpt4_response)
