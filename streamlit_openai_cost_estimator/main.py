import tempfile

import pandas as pd
import streamlit as st
import tiktoken
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter

from streamlit_openai_cost_estimator.streamlit_components.sidebar import sidebar

# Get the encoding for tokenization
encoding = tiktoken.get_encoding("cl100k_base")

# Set the page configuration for Streamlit app
st.set_page_config(page_title="OpenAI Cost Estimator💲", page_icon="💲", layout="wide")

# Display the header
st.header("💲OpenAI Cost Estimator")

# Display the sidebar
sidebar()

# Input file upload for the PDF
input_file = st.file_uploader("Upload your PDF here", type=["pdf"])

# Initialize the text splitter
text_splitter = CharacterTextSplitter(
    separator=st.session_state["separator"],
    chunk_size=st.session_state["chunk_size"],
    chunk_overlap=st.session_state["chunk_overlap"],
    length_function=len,
)

if input_file:
    # Calculate the token length and price
    with st.spinner(text="Calculating token length & price"):
        # Save the uploaded PDF as a temporary file
        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as temp_file:
            temp_file.write(input_file.read())
            temp_file_path = temp_file.name

        # Load the PDF using the PyPDFLoader
        loader = PyPDFLoader(temp_file_path)
        pages = loader.load_and_split(text_splitter)

        # Calculate the total number of tokens in the PDF
        num_token = 0
        page_number = []
        page_num_char = []
        pages_num_token = []
        for page in pages:
            page_number.append(page.metadata["page"])
            page_num_char.append(len(page.page_content))
            page_num_token = len(encoding.encode(page.page_content))
            pages_num_token.append(page_num_token)
            num_token += page_num_token
        price = round(num_token / 1000 * st.session_state["price_1k_token"], 6)

    # Create a new DataFrame to display the results
    df = pd.DataFrame(
        {"num_chunks": [len(pages)], "num_token": [num_token], "price": [price]}
    )
    df_pages = pd.DataFrame(
        {
            "page_number": page_number,
            "number_of_characters": page_num_char,
            "number_of_token": pages_num_token,
        }
    )

    # Display the results
    st.success(f"Your results are ready!")
    st.dataframe(
        df.style.format({"price": "{:.6f}"}), use_container_width=True, hide_index=True
    )
    st.dataframe(df_pages, use_container_width=True, hide_index=True)
