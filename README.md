# AI LinkedIn Post Writer

## 🚀 Overview

AI LinkedIn Post Writer is a simple Python application that generates professional LinkedIn posts from basic project details. Users provide information such as the project name, description, and technologies used, and an AI language model automatically creates a ready-to-post LinkedIn update.

This project demonstrates a beginner-friendly **LLM (Large Language Model) integration** using Hugging Face Transformers and Google's FLAN-T5 model.

---

## 🎯 Project Objective

Many students and interns struggle to write LinkedIn posts about their projects, even when sharing their achievements is important for networking and career growth.

This tool solves that problem by generating concise, engaging, and professional LinkedIn posts with minimal user input.

---

## ✨ Features

* Generate LinkedIn posts using AI
* Simple command-line interface
* No API key required
* Uses an open-source Hugging Face model
* Beginner-friendly implementation of LLM integration
* Customizable prompts for different project types

---

## 🛠️ Technologies Used

* Python
* Hugging Face Transformers
* PyTorch
* Google FLAN-T5 Base Model

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-linkedin-post-writer.git
cd ai-linkedin-post-writer
```

### 2. Install Dependencies

```bash
pip install transformers torch
```

---

## ▶️ Usage

Run the application:

```bash
python main.py
```

Example Input:

```text
Project Name: CBC FAQ Bot
Project Description: Answers community questions automatically
Technologies Used: Python, NLP
```

Example Output:

```text
Excited to share my latest project, CBC FAQ Bot! 🚀

Built using Python and NLP, this project helps answer community questions efficiently and improves access to information.

Working on this project helped me strengthen my problem-solving and AI development skills. Looking forward to building more impactful solutions!

#Python #AI #MachineLearning #Project
```

---

## 💻 Sample Code

```python
from transformers import pipeline

writer = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"
)

prompt = """
Write a short, friendly LinkedIn post about a project called
CBC FAQ Bot that answers community questions using Python.
"""

result = writer(prompt, max_length=120)

print(result[0]["generated_text"])
```

---

## 🧠 How It Works

1. User enters project details.
2. The application creates a prompt from the input.
3. FLAN-T5 processes the prompt.
4. The model generates a LinkedIn-ready post.
5. The generated text is displayed to the user.

This workflow represents a basic but practical example of LLM integration.

---

## 📁 Project Structure

```text
ai-linkedin-post-writer/
│
├── main.py
├── requirements.txt
├── README.md
└── app/                 # Optional Streamlit UI
```

---

## 🔮 Future Enhancements

* Streamlit web interface
* Multiple post styles (professional, casual, technical)
* Hashtag generation
* Post length selection
* Support for additional LLMs
* Copy-to-clipboard functionality

---

## 🎓 Learning Outcomes

Through this project, you will learn:

* Fundamentals of LLM integration
* Prompt engineering basics
* Using Hugging Face Transformers
* Working with text generation models
* Building practical AI-powered applications

---

## 👨‍💻 Author

lakshminarayana velugubanti
