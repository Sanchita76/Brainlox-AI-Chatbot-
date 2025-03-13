from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from process_data import load_vectorstore

def search_query(user_query):
    vectorstore = load_vectorstore()

    llm = ChatOpenAI(model="gpt-4", temperature=0.2)

    prompt_template = PromptTemplate(
        template="You are an AI assistant helping users find technical courses from Brainlox. "
            "Use ONLY the following course data to answer:\n{context}\n\n"
            "User Query: {question}\n\n"
            "Answer STRICTLY based on the given course data. Do NOT provide general internet knowledge or mention external platforms.",
        input_variables=["context", "question"]
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
        chain_type_kwargs={"prompt": prompt_template}
    )

    response = qa_chain.run(user_query)
    return response
