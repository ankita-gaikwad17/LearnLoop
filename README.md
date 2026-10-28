# LearnLoop — Student Learning Progress Tracker

LearnLoop is a student learning progress tracker built with Python and Streamlit. It helps students record subjects, topics, and quiz scores, monitor learning progress, and identify topics that need revision.

# Features

- Record subjects and topics
- Save quiz scores
- Track learning progress
- Get revision recommendations based on scores
- Store learning records in a CSV file

# Technologies Used

- Python
- Streamlit
- CSV

# Run Locally

Install the dependencies:

pip install -r requirements.txt

Run the application:

streamlit run app.py

# Project Structure

- "app.py" — Main application and user interface
- "storage.py" — Saves learning records
- "learning_data.csv" — Stores saved topics and scores
- "requirements.txt" — Lists dependencies

# Limitations

The current application stores topics during the session and uses simple score-based rules to recommend revision. It does not yet provide AI-generated study recommendations.

# Goal

To help students organize their learning and make revision easier.
