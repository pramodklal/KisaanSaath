from setuptools import find_packages, setup

setup(
    name="KisaanSaathiBOT",
    version="0.0.1",
    author="Pramod",
    author_email="pramodklal@gmail.com",
    packages=find_packages(),
    install_requires=['google-cloud-aiplatform','streamlit','google-generativeai','python-dotenv','langchain','PyPDF2','chromadb','faiss-cpu','langchain_google_genai']
)