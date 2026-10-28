import streamlit as st
from storage import load_topics, save_topic

st.set_page_config(
    page_title="LearnLoop",
    page_icon="📚",
    layout="centered"
)

st.title("LearnLoop")
st.write("Track your learning and plan your revision.")

# Load saved topics from the CSV file
if "topics" not in st.session_state:
    st.session_state.topics = load_topics()

st.header("Add a Topic")

subject = st.text_input("Subject", placeholder="e.g. Physics")
topic = st.text_input("Topic", placeholder="e.g. Electrostatics")
score = st.number_input(
    "Quiz score (%)",
    min_value=0,
    max_value=100,
    value=50
)

if st.button("Save Topic"):
    if subject.strip() and topic.strip():
        new_topic = {
            "subject": subject.strip(),
            "topic": topic.strip(),
            "score": int(score)
        }

        save_topic(
            new_topic["subject"],
            new_topic["topic"],
            new_topic["score"]
        )

        st.session_state.topics.append(new_topic)
        st.success("Topic saved successfully!")
    else:
        st.warning("Please enter both subject and topic.")

st.header("Your Learning Progress")

if st.session_state.topics:
    for item in st.session_state.topics:
        st.subheader(item["topic"])
        st.write(f"Subject: {item['subject']}")
        st.write(f"Quiz score: {item['score']}%")

        if int(item["score"]) < 60:
            st.warning("Revision recommended")
        else:
            st.success("Good progress — keep practising!")

        st.divider()
else:
    st.info("No topics saved yet. Add your first topic above.")