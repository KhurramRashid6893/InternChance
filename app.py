from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd 
import google.generativeai as genai
import os

app = Flask(__name__)

# --- Configuration ---
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
gemini_model = genai.GenerativeModel("gemini-3-flash-preview")

# Load the ML model
try:
    with open('model.pkl', 'rb') as f:
        ml_model = pickle.load(f)
except FileNotFoundError:
    ml_model = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        df_input = pd.DataFrame([{
            'cgpa': float(data['cgpa']),
            'dsa': int(data['dsa']),
            'projects': int(data['projects']),
            'hackathons': int(data['hackathons']),
            'certs': int(data['certs'])
        }])
        
        prediction = ml_model.predict(df_input)[0]
        probability = ml_model.predict_proba(df_input)[0][1]
        
        return jsonify({
            'shortlisted': int(prediction),
            'probability': round(probability * 100, 2)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.json
        # Construct a detailed prompt using the user's data
        prompt = (
            f"Act as a strict but encouraging Career Coach. Analyze this student's profile based on the following data: "
            f"CGPA: {data['cgpa']}, DSA Problems Solved: {data['dsa']}, Projects: {data['projects']}, "
            f"Hackathons: {data['hackathons']}, Certifications: {data['certs']}. \n\n"
            f"1. Explain each part: Where do they lag? How much improvement is needed in each specific area to reach a top-tier level? \n"
            f"2. Provide exactly 5 actionable 'Best Suggestions' to improve their profile immediately.\n"
            f"3. End with one powerful, unique motivational quote.\n"
            f"Format the output using HTML tags (<h3>, <ul>, <li>, <strong>) for easy rendering."
        )
        response = gemini_model.generate_content(prompt)
        return jsonify({"analysis": response.text})
    except Exception as e:
        return jsonify({"analysis": "Could not generate analysis at this time."}), 500

@app.route('/chat', methods=['POST'])
def chat():
    user_msg = request.json.get("message")
    try:
        prompt = f"System: You are an AI Career Coach. User asks: {user_msg}. Keep answers short and professional."
        response = gemini_model.generate_content(prompt)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"response": "Error processing request."})

if __name__ == "__main__":
    app.run(port= 5000, host = "0.0.0.0")
