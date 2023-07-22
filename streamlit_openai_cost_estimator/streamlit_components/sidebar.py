import streamlit as st


def sidebar():
    with st.sidebar:
        st.markdown(
            "## Welcome to the OpenAI Cost Estimator Tool! 💲\n"
            "Estimate the cost of generating embeddings for your documents and optimize your project budget.\n"
        )
        st.session_state["MODEL_TYP"] = "gpt-3.5-turbo"

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
