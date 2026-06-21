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

from transformers import pipeline
import datetime

def get_user_input():
    print("\n========== AI LinkedIn Post Writer ==========\n")

    project_name = input("Enter Project Name: ").strip()
    project_description = input("Enter Project Description: ").strip()
    tech_used = input("Enter Technologies Used (comma separated): ").strip()

    return project_name, project_description, tech_used


def generate_linkedin_post(writer, project_name, project_description, tech_used):

    prompt = f"""
Write a professional LinkedIn post for a student project.

Project Name: {project_name}

Project Description:
{project_description}

Technologies Used:
{tech_used}

Requirements:
1. Start with an engaging opening.
2. Explain the project briefly.
3. Mention technologies used.
4. Include learning experience.
5. End with a positive statement.
6. Add relevant hashtags.
7. Keep the post concise and professional.
"""

    result = writer(
        prompt,
        max_length=200,
        do_sample=True,
        temperature=0.8
    )

    return result[0]["generated_text"]


def save_post(post):
    filename = f"linkedin_post_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(post)

    return filename


def main():

    print("Loading AI model...")
    print("Please wait for a few seconds...\n")

    try:
        writer = pipeline(
            "text2text-generation",
            model="google/flan-t5-base"
        )

        print("Model loaded successfully!\n")

    except Exception as e:
        print("Error loading model:")
        print(e)
        return

    while True:

        project_name, project_description, tech_used = get_user_input()

        if not project_name or not project_description or not tech_used:
            print("\nAll fields are required!\n")
            continue

        print("\nGenerating LinkedIn post...\n")

        try:
            post = generate_linkedin_post(
                writer,
                project_name,
                project_description,
                tech_used
            )

            print("=" * 60)
            print("GENERATED LINKEDIN POST")
            print("=" * 60)
            print(post)
            print("=" * 60)

            filename = save_post(post)

            print(f"\nPost saved successfully as: {filename}")

        except Exception as e:
            print("Error generating post:")
            print(e)

        choice = input("\nGenerate another post? (y/n): ").lower()

        if choice != 'y':
            print("\nThank you for using AI LinkedIn Post Writer!")
            break


if __name__ == "__main__":
    main()
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
