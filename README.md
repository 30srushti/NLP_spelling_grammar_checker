
AI-powered NLP tool that automatically detects and corrects grammar and spelling mistakes in text using transformer-based models. It improves sentence structure, clarity, and writing quality in real time.

# 📝 NLP Grammar & Spell Checker (Transformer-Based)

This project is a web-based **Grammar and Spell Correction Tool** built using **Flask** and a powerful **Transformer model (T5)** for grammatical error correction.

It takes user input, processes it using a deep learning model, and returns a corrected version of the text with improved grammar and spell accuracy.

---

## 🚀 Features

- ✔ Corrects **grammar mistakes** using a T5 Transformer model  
- ✔ Fixes **spelling errors automatically**  
- ✔ Clean and responsive UI  
- ✔ Real-time text correction on button click  
- ✔ Easy to run locally  
- ✔ Works offline after model download

---

## 🤖 NLP Model Used

This project uses:

**`vennify/t5-base-grammar-correction`**  
(A fine-tuned T5 model for grammar correction)

- Built using HuggingFace Transformers  
- Beam search decoding for higher correction accuracy  
- Handles long sentences (up to 512 tokens)

---

## 🛠 Technologies Used

- **Python 3**
- **Flask (Backend & Routing)**
- **HuggingFace Transformers**
- **PyTorch**
- **HTML, CSS** (Frontend UI)
- **Bootstrap** (Styling)

---

## 📂 Project Structure

NLP_spelling_grammar_checker/
│── app.py # Flask application
│── templates/
│ └── index.html # User interface
│── venv/ # Virtual environment (ignored in Git)
│── .gitignore
│── README.md


##Install Dependencies
pip install flask transformers torch sentencepiece

 Run the Flask App
python app.py

 Open in Browser
http://127.0.0.1:5000/

##Output

<img width="1916" height="1060" alt="Screenshot 2025-11-25 105715" src="https://github.com/user-attachments/assets/06275a79-cb8a-401c-a948-478b1516436a" />



