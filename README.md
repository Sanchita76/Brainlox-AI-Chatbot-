# Brainlox AI Chatbot 🤖📄 : Debales AI Internship Assignment
<div align="center">Smart AI chatbot and PDF generator for course insights & quick learning!</div>
  <br>
  <p align="center">
    <img src="ss/abcd(1).jpg" alt="Brainlox AI Chatbot" width="170" height="80">
  </p>

 ## 📝 Overview
The Brainlox AI Chatbot is an **AI-powered conversational assistant** designed to help users explore courses on Brainlox efficiently. It extracts course details, curriculum, and pricing from the official Brainlox website and provides instant responses to user queries.

Additionally, the system includes a **PDF generation feature**, allowing users to generate and **download a summary report of course details** for offline use.

This chatbot uses **LangChain, FAISS, and Flask RESTful API** to provide a fast, interactive, and intelligent user experience.

## Try it Out 

**[Visit Site]()**

## ✨ Key Features
✅ AI-Powered Chatbot – Understands user queries and retrieves accurate course information.<br>
✅ Real-Time Course Extraction – Fetches course details, curriculum, and pricing from Brainlox.<br>
✅ Fast Search Using FAISS – Embeds course data and searches efficiently.<br>
✅ Generate & Download PDFs – Summarizes course details into a structured PDF file.<br>
✅ User-Friendly UI – Simple and intuitive interface to interact with the chatbot & download PDFs.<br>
✅ Two-Page System – Separate pages for Chatbot (chat.html) and PDF Generator (index.html).<br>

## 🛠️ Technologies Used
- Programming Language: Python 🐍<br>
- **Web Framework**: Flask 🌐<br>
- **AI & NLP**: LangChain, OpenAI Embeddings 🤖<br>
- **Vector Search Engine**: FAISS ⚡<br>
- Frontend: HTML, CSS, JavaScript 🎨<br>
- PDF Generation: FPDF 📄<br>
- **Web Scraping**: BeautifulSoup 🌍<br>

## 🎨 Design Idea<br>
<img src="https://github.com/user-attachments/assets/428fb33c-9f52-4a86-be1b-9d5a24518140" width="300">

The project follows a modular and scalable design:<br>

- Course Extraction Module (extract_data.py) – Scrapes and structures course data.<br>
- Vector Storage & Search (process_data.py) – Converts text into embeddings and stores in FAISS for fast retrieval.<br>
- Flask RESTful API (app.py) – Manages chatbot interactions and PDF generation.<br>
- Frontend Interface – Provides user-friendly navigation between chatbot (chat.html) and PDF generator (index.html).<br>

## ⚙️ Setup Instructions
1️⃣ **Clone the Repository**<br>
```
git clone https://github.com/your-github-username/Brainlox-Chatbot.git<br>
cd Brainlox-Chatbot<br>
```

2️⃣ **Install Dependencies**<br>
```
pip install -r requirements.txt <br>
```

3️⃣ **Set Up OpenAI API Key** <br>
```
Create a .env file in the project directory and add:<br>
OPENAI_API_KEY="your-api-key-here"<br>
```

4️⃣ **Generate FAISS Embeddings**<br>
```
python process_data.py 
```
(This will fetch Brainlox courses, create embeddings, and store them in FAISS.)<br>

5️⃣ **Run the Flask Server**<br>
```
python app.py
```
(This starts the chatbot & PDF generator at http://127.0.0.1:5000/)<br>

## Demo 
**Running Flask**<br>
<img src="https://github.com/user-attachments/assets/7fcd9d48-0d30-4e1a-a8cf-b34f6ee50977" width="500"><br>

**Course Details Extraction**<br>
<img src="https://github.com/user-attachments/assets/536a2911-979b-4ae6-bae0-57b5c329168d" width="500"><br>
<img src="https://github.com/user-attachments/assets/3ae9a5c2-82ff-46da-aef8-898a235a0673" width="500"><br>

## 🛠️ Use Cases
💡 Students & Learners – Quickly find the right courses without manually browsing.<br>
💡 **Educators & Institutions** – Automate course recommendations and summaries.<br>
💡 **Corporate Training** – Provide employees with a smart way to find relevant courses.<br>
💡 Researchers & Analysts – Retrieve structured data on online learning trends.<br>

## 🚀 Future Scope & Improvements<br>
🔹 Enhance Chatbot Intelligence – Integrate GPT-based conversational AI.<br>
🔹 Course Recommendations – Suggest similar courses based on interests.<br>
🔹 User Authentication – Allow personalized course tracking.<br>
🔹 Real-Time Data Updates – Automatically refresh the course database.<br>
🔹 Multi-Language Support – Expand chatbot capabilities for non-English users.<br>

## 📜 Conclusion
The Brainlox AI Chatbot & PDF Generator offers a smart, interactive, and efficient way to explore online courses. With AI-powered search, real-time data extraction, and instant PDF generation, this tool enhances learning experiences while saving time. 🚀

## 👨‍💻 Author & Contributions
Developed by [Mehuli Biswas] 🛠️ | GitHub: [https://github.com/Sanchita76]

🔥 If you find this useful, give it a ⭐ on GitHub! 😊

