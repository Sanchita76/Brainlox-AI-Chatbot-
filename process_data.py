import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from extract_data import extract_courses

EMBEDDINGS_PATH = "faiss_store"

def generate_embeddings():
    print("🔍 Extracting courses from Brainlox...")

    courses = extract_courses()
    if not courses:
        print("⚠️ No courses found! Check `extract_data.py`.")
        return

    print(f"✅ Successfully extracted {len(courses)} courses.")

    # ✅ Ensure markdown-friendly storage for FAISS
    texts = [f"### {course['title']}\n\n{course['description']}" for course in courses]

    # ✅ Use RecursiveCharacterTextSplitter for better structure
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=2000, chunk_overlap=100, separators=["\n\n", "\n", " "]
    )

    split_texts = text_splitter.create_documents(texts)

    if not split_texts:
        print("⚠️ No split texts generated. Check data formatting.")
        return

    print("🛠️ Generating embeddings with Markdown-friendly formatting...")
    embeddings = OpenAIEmbeddings()
    faiss_index = FAISS.from_documents(split_texts, embeddings)

    os.makedirs(EMBEDDINGS_PATH, exist_ok=True)
    faiss_index.save_local(EMBEDDINGS_PATH)

    print("🎉 FAISS index created and stored in faiss_store/.")

def load_vectorstore():
    if not os.path.exists(EMBEDDINGS_PATH):
        raise Exception("⚠️ FAISS index not found. Run `python process_data.py` first.")
    return FAISS.load_local(EMBEDDINGS_PATH, OpenAIEmbeddings(), allow_dangerous_deserialization=True)

if __name__ == "__main__":
    generate_embeddings()
