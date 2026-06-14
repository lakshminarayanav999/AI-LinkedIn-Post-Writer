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
* Google FLAN-T5 Base Model

---

## 📦 Installation

### 1. Clone the Repository

```bash
https://github.com/lakshminarayanav999/AI-LinkedIn-Post-Writer.git
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
Project Name: AI-LinkedIn-Post-writer
Project Description: A Python-based  AI application that uses FLAN-T5 to generate professional LinkedIn posts from user-provided project details, demonstrating practical LLM integration and prompt engineering.
Technologies Used: Python, NLP, hugging face transformers
```

Example Output:

```text
🚀 Excited to share my latest project: AI LinkedIn Post Writer!

This application uses Generative AI to help users create professional LinkedIn posts by simply providing project details such as the project name, description, and technologies used.

Built with Python, Hugging Face Transformers, PyTorch, and Google's FLAN-T5 model, this project gave me hands-on experience with LLM integration, prompt engineering, and AI-powered text generation.

Looking forward to exploring more real-world applications of Generative AI and Natural Language Processing.

#AI #GenerativeAI #Python #MachineLearning #LLM #NLP #OpenSource
```

---

## 💻 Sample Code

```python
from transformers import pipeline

writer = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"
)

project_name = input("Enter Project Name: ")
project_description = input("Enter Project Description: ")
technologies = input("Enter Technologies Used: ")

prompt = f"""
Write a professional LinkedIn post for a student developer.

Project Name: {project_name}
Project Description: {project_description}
Technologies Used: {technologies}

The post should:
- Be professional and engaging
- Mention key learnings
- Highlight technologies used
- End with relevant hashtags
- Be suitable for posting on LinkedIn
"""

result = writer(prompt, max_length=200)

print("\nGenerated LinkedIn Post:\n")
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
