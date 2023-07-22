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

# Slider to adjust the chunk size for text splitting
chunk_size = st.slider("Refine the Chunksize?", 1, 4000, 4000)

# Slider to adjust the overlap size for text splitting
chunk_overlap = st.slider("Refine the Overlap Size?", 0, 1000, 800)

# Numeric input for the price of Ada v2 Embedding per 1K tokens
price_1k_token = st.number_input(
    "Ada v2 Embedding $X / 1K tokens",
    min_value=0.0,
    max_value=1.0,
    value=0.0001,
    step=0.0001,
    format="%f",
)

# Initialize the text splitter
text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap,
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
        for page in pages:
            num_token += len(encoding.encode(page.page_content))
        price = round(num_token / 1000 * price_1k_token, 6)

    # Create a new DataFrame to display the results
    data = {"num_chunks": [len(pages)], "num_token": [num_token], "price": [price]}
    df = pd.DataFrame(data)

    # Display the results
    st.success(f"Your results are ready!")
    st.dataframe(
        df.style.format({"price": "{:.6f}"}), use_container_width=True, hide_index=True
    )
