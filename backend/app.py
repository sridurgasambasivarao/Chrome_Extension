from fastapi import FastAPI
from pydantic import BaseModel
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI()

# Allow Chrome extension requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["chrome-extension://bdepgoofmegacnpndheopanmcgipcjcb"],
    allow_methods=["*"],
    allow_headers=["*"],
)

model = ChatOpenAI(model = "gpt-4.1-mini")
embeddings = OpenAIEmbeddings()

prompt = PromptTemplate(
    template="""
    Answer the following question:
    {question}

    Based only on this webpage content:
    {text}
    """,
    input_variables=["question", "text"]
)

parser = StrOutputParser()

chain = prompt | model | parser


class QueryRequest(BaseModel):
    url: str
    question: str



@app.post("/ask")
def ask_question(request: QueryRequest):
    loader = WebBaseLoader(request.url)
    docs = loader.load()

    #handle token overflow risk
    splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=200)

    chunks = splitter.split_documents(docs)

    vectorstore = FAISS.from_documents(
        chunks,
        embeddings
    )

    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

    relevant_docs = retriever.invoke(request.question)

    context = "\n\n".join([doc.page_content for doc in relevant_docs])

    result = chain.invoke({
        "question": request.question,
        "text": context
    })

    return {"answer": result}