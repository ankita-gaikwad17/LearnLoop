import streamlit as st
from storage import load_topics, save_topic

st.set_page_config(
    page_title="LearnLoop",
    page_icon="📚",
    layout="centered"
)

st.title("📚 LearnLoop")
st.write("Track your learning and plan your revision.")

# Load saved topics from CSV
if "topics" not in st.session_state:
    st.session_state.topics = load_topics()

st.header("Add a Topic")

with st.form("topic_form"):
    subject = st.text_input(
        "Subject",
        placeholder="e.g. Physics"
    )

    topic = st.text_input(
        "Topic",
        placeholder="e.g. Electrostatics"
    )

    score = st.number_input(
        "Quiz score (%)",
        min_value=0,
        max_value=100,
        value=50,
        step=1
    )

    submitted = st.form_submit_button("Save Topic")

if submitted:
    if subject.strip() and topic.strip():
        save_topic(subject.strip(), topic.strip(), int(score))

        # Reload all records from CSV
        st.session_state.topics = load_topics()

        st.success("Topic saved successfully!")
    else:
        st.warning("Please enter both subject and topic.")

st.divider()
st.header("Your Learning Progress")

topics = st.session_state.topics

if topics:
    total_topics = len(topics)
    average_score = sum(
        int(item["score"]) for item in topics
    ) / total_topics

    col1, col2 = st.columns(2)

    col1.metric("Topics Tracked", total_topics)
    col2.metric("Average Score", f"{average_score:.1f}%")

    for index, item in enumerate(topics, start=1):
        with st.container(border=True):
            st.subheader(item["topic"].title())
            st.write(f"**Subject:** {item['subject'].title()}")

            current_score = int(item["score"])
            st.write(f"**Quiz score:** {current_score}%")
            st.progress(current_score)

            if current_score < 60:
                st.warning("Revision recommended")
            else:
                st.success("Good progress — keep practising!")

else:
    st.info("No topics saved yet. Add your first topic above.")