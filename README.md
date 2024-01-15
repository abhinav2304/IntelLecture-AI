

---

# AI-Powered Lecture Interaction System

## Overview
This project offers a dynamic way to enhance student engagement during lectures. It includes a web portal for students to submit questions in real-time, and an AI-powered script to summarize these questions using GPT technology. 

## Key Features
- **Question Submission Portal**: A web-based platform where students can submit their questions during the lecture.
- **Real-Time AI Summarization**: A Python script (`summarize.py`) that uses GPT to summarize the submitted questions.
- **Local Server Setup**: Simple setup with PHP to run the submission portal.

## Installation and Setup
1. **Clone the repository**: `git clone [repository URL]`.
2. **Navigate to the project directory**: `cd [project-directory]`.
3. **Start the Local Server**: Run `php -S localhost:8000` to initiate the local web server.
4. **Access the Portal**: Open a web browser and visit `http://localhost:8000` to access the submission portal.
    Note: you'd want GPT API to make it work and have to insert in summarize.py file.
## Usage
- **Submitting Questions**: Students can visit the portal during the lecture to submit their questions.
- **Running the Summarization Script**: After collecting questions, run the `summarize.py` script to generate a summary using the GPT API.

## License
This project is licensed under [specify the license] - see the `LICENSE` file for details.

---

