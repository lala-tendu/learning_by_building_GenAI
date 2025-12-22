# 🚀 AI Image Generator (FLUX.2-Pro + Streamlit)

A clean and simple **Text-to-Image Generator** built using **Streamlit**, powered by the **FLUX.2-pro** model through Azure/OpenAI API.

---

## 🌟 Features

- 🎨 Generate images from custom text prompts  
- ⚡ Uses **flux2-pro** model for high-quality outputs  
- 📥 Download generated images instantly  
- 🔐 Secure API key handling with `.env`   

---

## 📦 Tech Stack

- Streamlit  
- Azure/OpenAI Image API  
- FLUX.2-pro model  
- Python (requests, Pillow, python-dotenv)


---

## 🔧 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/lala-tendu/learning_by_building_GenAI/new/main/Image_generator.git
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Create a .env file
```bash
AZURE_API_KEY=your_api_key_here
AZURE_API_URI="your_URI_here"
```
### 4. ▶️ Run the App
```bash
streamlit run app.py
```
---

🧠 How It Works

1. User enters a text prompt
2. Backend sends a POST request to Azure
3. API returns Base64 image
4. Base64 → PNG decoded
5. Streamlit displays the image + download option

---

🤝 Contributing

Contributions, issues, and feature requests are welcome.

---

⭐ Show Your Support

If you liked this project, please star ⭐ the repository!
---
