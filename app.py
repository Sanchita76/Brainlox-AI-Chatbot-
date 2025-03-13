from flask import Flask, request, jsonify , send_file , render_template
from extract_data import extract_courses
from process_data import generate_embeddings, load_vectorstore
from query_engine import search_query
from generate_pdf import generate_pdf

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("chat.html")  # Chatbot UI

# Route to extract course data
@app.route('/extract', methods=['GET'])
def extract():
    try:
        courses = extract_courses()
        return jsonify({"message": "Courses extracted successfully!", "data": courses})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to process and store embeddings
@app.route('/process', methods=['POST'])
def process():
    try:
        generate_embeddings()
        return jsonify({"message": "Embeddings generated and stored in FAISS!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to handle user queries
@app.route('/query', methods=['GET'])
def query():
    user_query = request.args.get("question", "")
    if not user_query:
        return jsonify({"error": "Query parameter is missing."}), 400
    
    try:
        response = search_query(user_query)
        return jsonify({"query": user_query, "results": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

#pdf generation   
@app.route('/generate_pdf', methods=['GET'])
def generate_pdf_report():
    user_query = request.args.get("question", "")
    if not user_query:
        return jsonify({"error": "Query parameter is missing."}), 400
    try:
        pdf_path = generate_pdf(user_query)
        return send_file(pdf_path, as_attachment=True, download_name="Brainlox_Report.pdf", mimetype="application/pdf")
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_query = data.get("question", "")

    if not user_query:
        return jsonify({"error": "Query parameter is missing."}), 400

    try:
        response = search_query(user_query)
        return jsonify({"query": user_query, "response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
