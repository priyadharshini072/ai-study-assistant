from dotenv import load_dotenv
import os
from huggingface_hub import InferenceClient

load_dotenv()

token = os.getenv("HF_TOKEN")
client = InferenceClient(token=token)

model = "Qwen/Qwen3.8-2.4T-A95B"

messages = [
    {
        "role": "system",
        "content": "You are an AI Study Assistant. Explain topics clearly and simply for a college student."
    }
]

print("=" * 50)
print("             STUDYMATE AI")
print("        Your Personal AI Study Assistant")
print("=" * 50)

while True:
    print("\n===== STUDYMATE AI MENU =====")
    print("1. Ask a question")
    print("2. Exit")
    print("3. Generate Quiz")
    print("4. Summarize Topic")
    print("5. Generate Exam Answer")
    print("6. Generate Flashcards")

    choice = input("Enter your choice: ")

    if choice == "2":
        print("StudyMate AI stopped. Goodbye!")
        break

    elif choice == "1":
        question = input("Enter your question: ")

        messages.append({
            "role": "user",
            "content": question
        })

        response = client.chat_completion(
            messages=messages,
            model=model
        )

        answer = response.choices[0].message.content

        print("\n===== AI ANSWER =====")
        print(answer)

        messages.append({
            "role": "assistant",
            "content": answer
        })

    elif choice == "3":
        topic = input("Enter the topic for the quiz: ")

        quiz_prompt = (
            "Create 5 multiple-choice questions about "
            + topic
            + ". Give 4 options for each question and clearly show the correct answer."
        )

        response = client.chat_completion(
            messages=[
                {
                    "role": "user",
                    "content": quiz_prompt
                }
            ],
            model=model
        )

        answer = response.choices[0].message.content

        print("\n===== QUIZ =====")
        print(answer)

    elif choice == "4":
        topic = input("Enter the topic to summarize: ")

        summary_prompt = (
            "Give a simple and clear study summary of "
            + topic
            + ". Include the important points a college student should remember."
        )

        response = client.chat_completion(
            messages=[
                {
                    "role": "user",
                    "content": summary_prompt
                }
            ],
            model=model
        )

        answer = response.choices[0].message.content

        print("\n===== SUMMARY =====")
        print(answer)

    elif choice == "5":
        topic = input("Enter the exam question or topic: ")

        exam_prompt = (
            "Write a well-structured college exam answer for: "
            + topic
            + ". Include an introduction, important points, examples if useful, and a conclusion. "
            "Use simple language and clear headings."
        )

        response = client.chat_completion(
            messages=[
                {
                    "role": "user",
                    "content": exam_prompt
                }
            ],
            model=model
        )

        answer = response.choices[0].message.content

        print("\n===== EXAM ANSWER =====")
        print(answer)

    elif choice == "6":
        topic = input("Enter the topic for flashcards: ")

        flashcard_prompt = (
            "Create 5 simple study flashcards about "
            + topic
            + ". For each flashcard, give a Question and Answer. "
            "Keep the answers short and easy to remember."
        )

        response = client.chat_completion(
            messages=[
                {
                    "role": "user",
                    "content": flashcard_prompt
                }
            ],
            model=model
        )

        answer = response.choices[0].message.content

        print("\n===== FLASHCARDS =====")
        print(answer)

    else:
        print("Invalid choice. Please enter 1, 2, 3, 4, 5, or 6.")
