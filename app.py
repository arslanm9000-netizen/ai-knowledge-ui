import streamlit as st

# Page setup
st.set_page_config(page_title="AI Knowledge Assistant", layout="wide")

# Title
st.title("🤖 AI Knowledge Assistant")

# Description
st.info("AI-powered assistant to quickly find answers from company knowledge like SOPs, tickets, and policies.")

st.write("---")

# Sidebar
st.sidebar.title("📂 Filter Knowledge Type")
category = st.sidebar.selectbox(
    "Choose category",
    ["All", "SOPs", "Tickets", "Policies", "Training"]
)

# Input
st.header("🔍 Ask a Question")
user_input = st.text_input("Type your question here:")
search_clicked = st.button("Search")

st.write("---")

# Knowledge base
knowledge_base = {
    "password": {
        "answer": "Use the password reset SOP: go to portal → click 'Forgot Password' → follow email instructions.",
        "sources": ["SOP: Password Reset Guide", "Ticket #4521"],
        "confidence": "92%"
    },
    "vpn": {
        "answer": "Check internet, restart VPN client, and re-enter credentials. Follow VPN troubleshooting SOP.",
        "sources": ["SOP: VPN Troubleshooting", "Ticket #3321"],
        "confidence": "88%"
    },
    "email": {
        "answer": "Set up email using Outlook with your company credentials and sync settings.",
        "sources": ["SOP: Email Setup Guide"],
        "confidence": "90%"
    },
    "device": {
        "answer": "Set up your device by installing required software and joining the company domain.",
        "sources": ["SOP: Device Setup"],
        "confidence": "85%"
    },
    "policy": {
        "answer": "Follow the Acceptable Use Policy: no unauthorized software and maintain secure access.",
        "sources": ["Policy Document"],
        "confidence": "95%"
    },
    "onboarding": {
        "answer": "During onboarding, set up your account, configure email, VPN, and review company policies.",
        "sources": ["Onboarding Guide"],
        "confidence": "91%"
    },
    "login": {
        "answer": "If you cannot log in, reset your password or contact IT support.",
        "sources": ["Ticket #5678"],
        "confidence": "89%"
    }
}

# Search logic (ONLY runs when button clicked)
if search_clicked:
    if user_input:
        st.header("📊 Results")

        answer = "No matching result found."
        sources = []
        confidence = "50%"

        for key in knowledge_base:
            if key in user_input.lower():
                answer = knowledge_base[key]["answer"]
                sources = knowledge_base[key]["sources"]
                confidence = knowledge_base[key]["confidence"]
                break

        col1, col2 = st.columns([3, 1])

        with col1:
            st.subheader("Top Answer")
            st.write(answer)

        with col2:
            st.subheader("Confidence")
            st.metric(label="Score", value=confidence)

        st.write("---")

        st.subheader("📄 Sources Used")
        if sources:
            for s in sources:
                st.write(f"- {s}")
        else:
            st.write("No sources available.")

        st.success("Answer retrieved successfully!")

    else:
        st.warning("Please enter a question.")

# Button styling
st.markdown("""
<style>
.stButton>button {
    background-color: #4CAF50;
    color: white;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)
