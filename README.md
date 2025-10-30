# 💬 Customer Sentiment Analysis App

A simple, interactive **AI-powered sentiment analysis app** built with **Python**, **Hugging Face Transformers**, and **Streamlit**.  
This app analyzes customer feedback from surveys and classifies each response as **Positive** or **Negative**, while also providing visual insights.

---

## 🚀 Features

✅ Upload a CSV file with a column named **"Response"**  
✅ Performs **sentiment analysis** using deep learning (DistilBERT)  
✅ Generates a **bar chart** of sentiment distribution  
✅ Displays a **word cloud** of common terms  
✅ Allows you to **download results** with sentiments added  
✅ Runs completely free on **Streamlit Cloud**

---

## 🧠 Tech Stack

| Tool | Purpose |
|------|----------|
| **Python** | Programming language |
| **Transformers (Hugging Face)** | Deep learning NLP model |
| **Torch** | Backend for running the model |
| **Pandas** | Data processing |
| **Matplotlib / Seaborn** | Data visualization |
| **WordCloud** | Visualizing top words |
| **Streamlit** | Interactive web interface |

---

## 📦 Installation (Run Locally)

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/sentiment-analysis-app.git
   cd sentiment-analysis-app

2. Create a virtual environment
   python3 -m venv venv
   source venv/bin/activate

3. Install dependencies
   pip install -r requirements.txt

4. Run the app
   streamlit run app.py

5. Open your browser → http://localhost:8501

🌐 Online Demo
Try it here:
🔗 https://dharmatejav-lab-sentiment-analysis-app.streamlit.app
