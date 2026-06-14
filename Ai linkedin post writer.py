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
