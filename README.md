```markdown 
  🚀InternChance Pro - AI Career Architect   ( https://internchance.onrender.com)   

  InternChance Pro   is an intelligent career dashboard designed to help students evaluate their internship readiness and receive personalized, AI-driven coaching.

By combining Machine Learning (Random Forest) for probability prediction and Generative AI (Google Gemini) for qualitative analysis, this tool acts as a 24/7 personal career coach.

---

   ✨ Features  

     1. AI Probability Predictor
- Uses a trained Machine Learning model   (Random Forest) to analyze student stats.
-   Inputs: CGPA, DSA Problems Solved, Projects, Hackathons, Certifications.
-   Output:   A percentage probability of being shortlisted for top-tier internships.

    🧠 2. Deep Profile Analysis (Gemini Powered)
- Goes beyond simple numbers to explain   "Why?"  
- Generates a custom HTML report highlighting strengths and weaknesses.
- Provides a   Personalized Roadmap   to fill skill gaps.

    🎓 3. Smart Learning Hub
-   Dynamic Topic Suggestions:   The AI extracts specific technical topics you need to learn.
-   One-Click Learning:   Click on suggested tags (e.g., "Learn Docker") to instantly find curated YouTube tutorials.
-   Custom Search:   A built-in search bar to find video resources for any other topic without leaving the dashboard.

    💬 4. AI Career Assistant (Chatbot)
- A conversational interface to ask specific questions about interviews, resume tips, or industry trends.
- Powered by Google's   Gemini-Pro   model.

    📱 5. Modern & Responsive UI
-   Mobile-First Design:   Fully responsive sidebar and grid layout that works on phones, tablets, and desktops.
-   Glassmorphism UI:   Clean, modern aesthetics with interactive cards and smooth animations.
-   Daily Motivation:   Embedded YouTube Shorts section for daily inspiration.

---

   🛠️ Tech Stack

-   Backend:   Python, Flask
-   ML Engine:   Scikit-learn (Random Forest Classifier), Pandas
-   AI Integration:   Google Generative AI (Gemini)
-   Frontend:   HTML5, CSS3 (Custom responsive design), JavaScript (Vanilla)
-   Icons & Fonts:   FontAwesome, Google Fonts (Poppins)

---

   ⚙️ Installation & Setup

    1. Clone the Repository
```bash
git clone [https://github.com/yourusername/internchance.git](https://github.com/yourusername/internchance.git)
cd internchance

```

    2. Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
  Windows
venv\Scripts\activate
  Mac/Linux
source venv/bin/activate

```

    3. Install Dependencies

Create a `requirements.txt` file (if not present) with the following and install it:

```txt
flask
pandas
scikit-learn
google-generativeai

```

Run installation:

```bash
pip install -r requirements.txt

```

    4. Set Up API Key

Open `app.py` and replace the placeholder API key with your actual   Google Gemini API Key  :

```python
genai.configure(api_key="YOUR_ACTUAL_API_KEY_HERE")

```

 (Note: It is best practice to use environment variables for API keys in production) 

    5. Train the Model (First Run Only)

Before running the app, ensure the ML model is trained and saved.

```bash
python train_model.py

```

This will generate `model.pkl` in your directory.

    6. Run the Application

```bash
python app.py

```

Visit `http://127.0.0.1:5000` in your browser.

---

   📂 Project Structure

```
InternChance/
│
├── app.py                   Main Flask application & routes
├── train_model.py           Script to train and save the ML model
├── model.pkl                Serialized Machine Learning model
│
├── data/
│   └── internship_data.csv   Dataset for training
│
├── static/
│   ├── style.css            Main stylesheet (Responsive & Modern)
│   └── script.js            Frontend logic (API calls, UI updates)
│
├── templates/
│   ├── base.html            Base HTML layout with headers/scripts
│   └── index.html           Main dashboard template
│
└── README.md                Project documentation

```

   📸 Usage Guide

1.   Dashboard:   Enter your academic and technical stats in the "Profile Stats" card.
2.   Analyze:   Click "Analyze Probability" to see your score.
3.   Get Coaching:   If you want deeper insights, click   "Get AI Coaching"  .
4.   Learn:   Use the generated   Topic Buttons   to watch tutorials or ask the   Chatbot   for specific advice.

---

   🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to fork the repository and submit a pull request.

   📄 License

This project is open-source and available under the [MIT License](https://www.google.com/search?q=LICENSE).

```

```
