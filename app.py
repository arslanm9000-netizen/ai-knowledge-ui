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
        "answer": "To reset your password, go to the company portal → click 'Forgot Password' → follow the email instructions.",
        "sources": ["SOP: Password Reset Guide", "Ticket #4521"],
        "confidence": "92%"
    },
    "vpn": {
        "answer": "If VPN is not working, check your internet connection, restart the VPN client, and re-enter your credentials.",
        "sources": ["SOP: VPN Troubleshooting", "Ticket #3321"],
        "confidence": "88%"
    },
    "email": {
        "answer": "Set up your company email using Outlook with your credentials and sync settings.",
        "sources": ["SOP: Email Setup Guide"],
        "confidence": "90%"
    },
    "device": {
        "answer": "To set up your device, install required software and join the company domain.",
        "sources": ["SOP: Device Setup"],
        "confidence": "85%"
    },
    "policy": {
        "answer": "Follow the acceptable use policy: no unauthorized software and maintain secure access.",
        "sources": ["Policy Document"],
        "confidence": "95%"
    },
    "onboarding": {
        "answer": "During onboarding, set up your account, configure email and VPN, and review company policies.",
        "sources": ["Onboarding Guide"],
        "confidence": "91%"
    },
    "login": {
        "answer": "If you cannot log in, try resetting your password or contact IT support.",
        "sources": ["Ticket #5678"],
        "confidence": "89%"
    }
}

# Search logic
if search_clicked:
    if user_input:
        st.header("📊 Results")

        user_text = user_input.lower()

        if "password" in user_text:
            result = knowledge_base["password"]
        elif "vpn" in user_text:
            result = knowledge_base["vpn"]
        elif "email" in user_text:
            result = knowledge_base["email"]
        elif "device" in user_text:
            result = knowledge_base["device"]
        elif "policy" in user_text or "policies" in user_text or "rule" in user_text:
            result = knowledge_base["policy"]
        elif "onboarding" in user_text or "new employee" in user_text or "get started" in user_text:
            result = knowledge_base["onboarding"]
        elif "login" in user_text or "log in" in user_text or "can't log" in user_text:
            result = knowledge_base["login"]
        else:
            result = {
                "answer": "No matching result found.",
                "sources": [],
                "confidence": "50%"
            }

        answer = result["answer"]
        sources = result["sources"]
        confidence = result["confidence"]

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
