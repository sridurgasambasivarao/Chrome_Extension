# Chrome_Extension #

This is an AI-powered Chrome extension that allows users to ask natural language questions about the currently open web page and receive AI generated answers in real time. The system captures the active tab url, sends it to a FastApi backend where the page content is processed using a RAG pipeline built with LangChain, OpenAI and FAISS.