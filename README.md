# 📝 Paragraph Assistant

A simple web-based paragraph generator using **FastAPI** for backend.

## 🚀 Features

- Accepts a topic from the user
- Sends it to a FastAPI backend
- Generates a paragraph using AI (or any logic you define)
- Displays the output on the same page

## 📁 Project Structure

├── fast_api.py # FastAPI backend code
├── requirements.txt # Python dependencies
├── .env # Environment variables
└── README.md # This file


## 📦 Installation

```bash
git clone https://github.com/yourusername/paragraph-assistant.git
cd paragraph-assistant
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
pip install -r requirements.txt

## Create a .env file and add your API key or other config:
API_KEY=your_api_key_here

▶️ Run the Project
uvicorn fast_api:app --reload

