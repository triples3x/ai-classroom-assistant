# app.py — AI Classroom Assistant (Roza Shaimurat)
import streamlit as st
from openai import OpenAI
import os

# --- Page Setup ---
st.set_page_config(page_title="AI Classroom Assistant", page_icon="🤖")
st.title("🤖 AI Classroom Assistant – AP CSP Edition")
st.caption("AI-generated • Teacher-reviewed • Ethical & Educational")

# --- API Key Setup ---
API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    st.warning("⚠️ Please set your OpenAI API key in a .env file.")
client = OpenAI(api_key=API_KEY)

# --- Sidebar ---
st.sidebar.header("Settings")
ethics_mode = st.sidebar.checkbox("Enable Ethics Mode", value=True)
model = st.sidebar.selectbox("Model", ["gpt-4o-mini", "gpt-4o"], index=0)

# --- Helper Function ---
def generate(prompt):
    try:
        response = client.responses.create(
            model=model,
            input=prompt,
            temperature=0.7
        )
        output = response.output_text
    except Exception as e:
        output = f"⚠️ Error: {e}"
    if ethics_mode:
        output += "\n\n—\n**Ethics note:** Verify AI suggestions and adapt them for your students."
    return output

# --- Tabs ---
tab1, tab2 = st.tabs(["🧠 Lesson Planner", "💬 Student Help Bot"])

with tab1:
    st.subheader("Lesson Planner")
    topic = st.selectbox("Choose an AP CSP topic:", [
        "Variables and Data Types",
        "Conditionals and Booleans",
        "Loops and Iteration",
        "Lists and Data Structures",
        "Events and Interactivity",
        "Algorithms and Abstraction",
        "Data and Privacy",
        "AI Ethics and Impacts"
    ])
    duration = st.slider("Lesson Duration (minutes):", 30, 120, 60)
    if st.button("Generate Lesson Plan"):
        prompt = f"Create a {duration}-minute AP CSP lesson on {topic}. Include: objectives, vocabulary, a mini activity, 3 quiz questions, and an exit ticket."
        st.write(generate(prompt))

with tab2:
    st.subheader("Student Help Bot")
    question = st.text_area("Enter a student's question or concept they struggle with:")
    if st.button("Explain Concept"):
        prompt = f"Explain this concept clearly for a high school CS student: {question}. Include an example and a self-check question."
        st.write(generate(prompt))
