import streamlit as st

st.title("Upload Files")
import os

# Retrieve the existing session ID from 'get-um-docs.py'
session_id = st.session_state.get('session_id')
if not session_id:
    st.error("Session ID not found. Please start from the beginning.")
else:
    user_docs_folder = os.path.join(os.getcwd(), 'user-docs')
    os.makedirs(user_docs_folder, exist_ok=True)
    session_folder = os.path.join(user_docs_folder, session_id)
    os.makedirs(session_folder, exist_ok=True)

    # File uploader
    uploaded_file = st.file_uploader("Choose a file")

    if uploaded_file is not None:
        # Save the uploaded file to the session folder
        file_path = os.path.join(session_folder, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success(f"File {uploaded_file.name} saved successfully!")
