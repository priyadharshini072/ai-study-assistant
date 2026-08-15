import streamlit as st
import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

token = os.getenv("HF_TOKEN")

client = InferenceClient(token=token)

model = "Qwen/Qwen3.8-2.4T-A95B"

st.set_page_config(
    page_title="StudyMate AI",
    page_icon="📚"
)

st.title("📚 StudyMate AI")
st.write("Your Personal AI Study Assistant")

option = st.selectbox(
    "Choose a feature",
    [
        "Ask a Question",
        "Generate Quiz",
        "Summarize Topic",
        "Generate Exam Answer",
        "Generate Flashcards"
    ]
)

topic = st.text_input("Enter your topic or question")

if st.button("Generate"):

    if not topic:
        st.warning("Please enter a topic or question.")

    else:
        if option == "Ask a Question":
            prompt = topic

        elif option == "Generate Quiz":
            prompt = (
                "Create 5 multiple-choice questions about "
                + topic
                + ". Give 4 options for each question and clearly show the correct answer."
            )

        elif option == "Summarize Topic":
            prompt = (
                "Give a simple and clear study summary of "
                + topic
                + ". Include the important points a college student should remember."
            )

        elif option == "Generate Exam Answer":
            prompt = (
                "Write a well-structured college exam answer for: "
                + topic
                + ". Include an introduction, important points, examples if useful, "
                "and a conclusion. Use simple language and clear headings."
            )

        else:
            prompt = (
                "Create 5 simple study flashcards about "
                + topic
                + ". For each flashcard, give a Question and Answer. "
                "Keep the answers short and easy to remember."
            )

        with st.spinner("StudyMate AI is thinking..."):

            response = client.chat_completion(
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are an AI Study Assistant. "
                            "Explain topics clearly and simply for a college student."
                        )
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                model=model
            )

            answer = response.choices[0].message.content

        st.subheader("AI Response")
        st.write(answer)