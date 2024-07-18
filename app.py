import streamlit as st
from lyzr_automata.ai_models.openai import OpenAIModel
from lyzr_automata import Agent, Task
from lyzr_automata.pipelines.linear_sync_pipeline import LinearSyncPipeline
from PIL import Image
from lyzr_automata.tasks.task_literals import InputType, OutputType
import os

# Set the OpenAI API key
os.environ["OPENAI_API_KEY"] = st.secrets["apikey"]

st.markdown(
    """
    <style>
    .app-header { visibility: hidden; }
    .css-18e3th9 { padding-top: 0; padding-bottom: 0; }
    .css-1d391kg { padding-top: 1rem; padding-right: 1rem; padding-bottom: 1rem; padding-left: 1rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

image = Image.open("./logo/lyzr-logo.png")
st.image(image, width=150)

# App title and introduction
st.title("Cybersecurity Assistant")
st.markdown("Welcome to Cybersecurity Assistant, your personalized cybersecurity advisor. Simply input your online activities and your device specification, and receive tailored tips to keep your digital life secure and protected.")
st.markdown("            1) Mention your online activities (websites visited, download habits, device and network usage etc). ")
st.markdown("            2) Mention your device specifications.")
input = st.text_input(" Please enter the above details:",placeholder=f"""Type here""")

open_ai_text_completion_model = OpenAIModel(
    api_key=st.secrets["apikey"],
    parameters={
        "model": "gpt-4-turbo-preview",
        "temperature": 0.2,
        "max_tokens": 1500,
    },
)


def generation(input):
    generator_agent = Agent(
        role="Expert CYBERSECURITY CONSULTANT",
        prompt_persona=f"Your task is to DEVELOP Personalized Security Tips and CREATE a Custom Security Checklist tailored to an individual's online activities and device specifications.")
    prompt = f"""
You are an Expert CYBERSECURITY CONSULTANT. Your task is to DEVELOP Personalized Security Tips and CREATE a Custom Security Checklist tailored to an individual's online activities and device specifications.

Follow this step-by-step approach:

1. IDENTIFY detailed information about the user’s ONLINE ACTIVITIES, such as browsing habits, frequently visited websites, and common online transactions.

2. NEXT , ANALYZE the provided data on the USER'S DEVICE DETAILS including operating system, antivirus software in use, and any existing security measures.

3. ANALYZE the provided details to IDENTIFY potential vulnerabilities and areas of risk associated with the user's digital behavior and device setup.

4. FORMULATE personalized security tips that ADDRESS the specific risks identified, ensuring you EMPHASIZE the importance of each tip in maintaining online safety.

5. COMPILE a comprehensive SECURITY CHECKLIST that includes regular updates, strong password creation, two-factor authentication, secure Wi-Fi usage, backup protocols, and phishing scam awareness.

You MUST ensure these instructions are clear, concise, and actionable.


 """

    generator_agent_task = Task(
        name="Generation",
        model=open_ai_text_completion_model,
        agent=generator_agent,
        instructions=prompt,
        default_input=input,
        output_type=OutputType.TEXT,
        input_type=InputType.TEXT,
    ).execute()

    return generator_agent_task 
   
if st.button("Assist!"):
    solution = generation(input)
    st.markdown(solution)

with st.expander("ℹ️ - About this App"):
    st.markdown("""
    This app uses Lyzr Automata Agent . For any inquiries or issues, please contact Lyzr.

    """)
    st.link_button("Lyzr", url='https://www.lyzr.ai/', use_container_width=True)
    st.link_button("Book a Demo", url='https://www.lyzr.ai/book-demo/', use_container_width=True)
    st.link_button("Discord", url='https://discord.gg/nm7zSyEFA2', use_container_width=True)
    st.link_button("Slack",
                   url='https://join.slack.com/t/genaiforenterprise/shared_invite/zt-2a7fr38f7-_QDOY1W1WSlSiYNAEncLGw',
                   use_container_width=True)