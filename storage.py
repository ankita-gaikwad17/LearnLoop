import csv
from pathlib import Path

DATA_FILE = Path(__file__).parent / "learning_data.csv"

def load_topics():
    if not DATA_FILE.exists():
        return []

    with open(DATA_FILE, "r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))

def save_topic(subject, topic, score):
    file_exists = DATA_FILE.exists()

    with open(DATA_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["subject", "topic", "score"]
        )

        if not file_exists or DATA_FILE.stat().st_size == 0:
            writer.writeheader()

        writer.writerow({
            "subject": subject,
            "topic": topic,
            "score": score
        })