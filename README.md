# Chrome_Extension #

This is an AI-powered Chrome extension that allows users to ask natural language questions about the currently open web page and receive AI generated answers in real time. The system captures the active tab url, sends it to a FastApi backend where the page content is processed using a RAG pipeline built with LangChain, OpenAI and FAISS.

# AI Workflow #

1. User opens any webpage in Chrome.
2. User opens the extension and enters a question.
3. Extension captures the current tab URL.
4. URL + question is sent to the FastAPI backend.
5. Backend loads the webpage content using WebBaseLoader.
6. Content is split into smaller chunks.
7. Chunks are converted to vector embeddings.
8. Embeddings are stored in FAISS.
9. Relevant chunks are retrieved using similarity search.
10.Retrieved context is sent to the LLM to generate the answer.

# Output #

<img width="1289" height="622" alt="image" src="https://github.com/user-attachments/assets/979983e8-8102-4055-8a75-868ecac40bb7" />
