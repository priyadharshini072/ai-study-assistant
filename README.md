# StudyMate AI

StudyMate AI is an LLM-based AI Study Assistant designed to help college students learn and prepare for exams.

## Features

- Ask questions and get AI-generated answers
- Generate multiple-choice quizzes
- Summarize study topics
- Generate structured exam answers
- Generate study flashcards
- Maintain conversation history

## Technologies Used

- Python
- Hugging Face Inference API
- Hugging Face LLM
- python-dotenv
- VS Code

## LLM Model

The project uses:

Qwen/Qwen3.8-2.4T-A95B

The model receives the student's request and generates an AI-based response.

## How It Works

1. The student selects an option from the menu.
2. The application receives the student's input.
3. The input is sent to the LLM through Hugging Face.
4. The LLM generates a response.
5. The response is displayed in the terminal.

## Project Features

### 1. Ask a Question

Students can ask any study-related question and receive an AI-generated explanation.

### 2. Generate Quiz

The application generates five multiple-choice questions with four options and answers.

### 3. Summarize Topic

The application creates a simple summary containing important points.

### 4. Generate Exam Answer

The application creates a structured answer with an introduction, important points, examples, and conclusion.

### 5. Generate Flashcards

The application generates question-and-answer flashcards for revision.

## Project Structure

AI_Study_Assistant/
│
├── app.py
├── README.md
├── .env
└── venv/

## Security

The Hugging Face API token is stored in the `.env` file and should not be uploaded to GitHub.

## Future Improvements

- Add a graphical user interface
- Add PDF/document question answering
- Add voice input
- Add user login
- Add study progress tracking
- Deploy the application online

## Author

Priyadharshini