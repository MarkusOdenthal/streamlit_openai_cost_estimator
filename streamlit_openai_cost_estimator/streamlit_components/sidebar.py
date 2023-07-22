import streamlit as st
from langchain.text_splitter import (
    CharacterTextSplitter,
    RecursiveCharacterTextSplitter,
)


def sidebar():
    with st.sidebar:
        st.markdown(
            "## Welcome to the OpenAI Cost Estimator Tool! 💲\n"
            "Estimate the cost of generating embeddings for your documents and optimize your project budget.\n"
        )
        st.markdown("## Settings")
        option = st.selectbox(
            "Choose your Text Splitter",
            ("Split by character", "Recursively split by character"),
        )
        if option == "Split by character":
            st.write(
                r'This is the simplest method. This splits based on characters (by default "\n") and measure '
                r"chunk length by number of characters."
            )
        if option == "Recursively split by character":
            st.write(
                r'Recommended text splitter for generic content. It prioritizes keeping paragraphs, sentences, and words together to maintain semantic coherence. Default split characters: "\n\n", "\n", " ", "".'
            )
        st.markdown("---")
        chunk_size = st.slider("Refine the Chunksize?", 1, 4000, 4000)
        chunk_overlap = st.slider("Refine the Overlap Size?", 0, 1000, 800)
        separator = st.text_input("How should the text seperated?", value=r"\n")

        if option == "Split by character":
            # Initialize the text splitter
            st.session_state["text_splitter"] = CharacterTextSplitter(
                separator=separator,
                chunk_size=chunk_size,
                chunk_overlap=chunk_overlap,
                length_function=len,
            )
        if option == "Recursively split by character":
            st.session_state["text_splitter"] = RecursiveCharacterTextSplitter(
                chunk_size=chunk_size,
                chunk_overlap=chunk_overlap,
                length_function=len,
            )
        # Numeric input for the price of Ada v2 Embedding per 1K tokens
        current_pricing = 0.0001
        st.session_state["price_1k_token"] = st.number_input(
            f"Ada v2 Embedding ${current_pricing} / 1K tokens",
            min_value=0.0,
            max_value=1.0,
            value=0.0001,
            step=current_pricing,
            format="%f",
        )

        st.markdown("---")
        st.markdown("# About")
        st.markdown(
            "🚀The OpenAI Cost Estimator is a powerful tool designed to help individuals, businesses, and organizations "
            "estimate the cost of generating embeddings for their documents. It serves as an essential resource for "
            "OpenAI users, enabling them to calculate the cost of splitting documents into embeddings and storing them "
            "into a vector database.\n"
        )
        st.markdown(
            "To achieve optimal document processing efficiency and cost-effectiveness, the OpenAI Cost Estimator "
            "seamlessly integrates the Langchain library, specifically utilizing the CharacterTextSplitter module. By "
            "harnessing the capabilities of Langchain's CharacterTextSplitter, users gain the flexibility to experiment "
            "with various settings, such as chunk_size and chunk_overlap. This empowers users to tailor their text data "
            "processing approach to perfection, ensuring that they make the most out of their investment while generating "
            "high-quality embeddings. 🔨\n"
        )
        st.markdown("---")
        st.markdown(
            "Made by [MarkusOdenthal](https://www.linkedin.com/in/markus-odenthal/)"
        )
        st.markdown("---")
