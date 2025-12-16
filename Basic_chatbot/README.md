# 🤖 Basic GenAI Chatbot (Streamlit + Azure OpenAI)

A simple, product-style conversational chatbot built using **Streamlit** and **Azure OpenAI**.  
This project demonstrates **LLM integration, chat memory, and configurable model behavior** using environment variables.

---

## ✨ Features

- Chat-style web UI
- Conversation memory (context-aware replies)
- Azure OpenAI integration 
- Configurable temperature & token limits
- Secure configuration using `.env`

---

## 🛠 Tech Stack

- **Python**
- **Streamlit**
- **Azure OpenAI**
- **python-dotenv**

---

## 📦 Installation Steps

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/lala-tendu/learning_by_building_GenAI.git
cd learning_by_building_GenAI
```
### 2️⃣ Create a Virtual Environment
```bash
python -m venv myenv
```
### 3️⃣ Activate the Virtual Environment
```bash
myenv\Scripts\activate
```
### 4️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 5️⃣ Configure Environment Variables
- Create a .env file in the project root and add:
```bash
OPENAI_API_KEY=
OPENAI_API_ENDPOINT=
OPENAI_API_VERSION=2024-02-15-preview

TEMPERATURE=0.7
MAX_TOKENS=300
```
- ⚠️ Do not commit .env to GitHub.
### 6️⃣ Run the Application
```bash
streamlit run app.py
```
- The application will open automatically in your browser.

