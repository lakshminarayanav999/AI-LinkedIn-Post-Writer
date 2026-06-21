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
