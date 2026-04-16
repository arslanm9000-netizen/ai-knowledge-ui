import streamlit as st

st.set_page_config(page_title="AI Knowledge Assistant", layout="wide")

st.title("🤖 AI Knowledge Assistant")

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

# Knowledge base (UPDATED with outdated flag)
knowledge_base = {
    "password": {
        "answer": "To reset your password, go to the company portal → click 'Forgot Password' → follow the email instructions.",
        "sources": ["SOP: Password Reset Guide"],
        "confidence": "92%",
        "outdated": False
    },
    "vpn": {
        "answer": "Restart VPN client, check internet, and re-enter credentials.",
        "sources": ["SOP: VPN Troubleshooting"],
        "confidence": "88%",
        "outdated": False
    },
    "onboarding": {
        "answer": "Set up your account, configure email and VPN, and review company policies.",
        "sources": ["Onboarding Guide"],
        "confidence": "91%",
        "outdated": False
    },
    "login": {
        "answer": "Reset your password or contact IT support.",
        "sources": ["Ticket #5678"],
        "confidence": "89%",
        "outdated": False
    },
    "policy": {
        "answer": "Company policies define acceptable system usage and security rules.",
        "sources": ["Policy Document v1.2"],
        "confidence": "95%",
        "outdated": True   # 🔥 THIS IS THE RED FLAG CASE
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
        elif "onboarding" in user_text or "new employee" in user_text or "get started" in user_text:
            result = knowledge_base["onboarding"]
        elif "login" in user_text or "log in" in user_text:
            result = knowledge_base["login"]
        elif "policy" in user_text or "policies" in user_text or "rules" in user_text:
            result = knowledge_base["policy"]
        else:
            result = {
                "answer": "No matching result found.",
                "sources": [],
                "confidence": "50%",
                "outdated": False
            }

        answer = result["answer"]
        sources = result["sources"]
        confidence = result["confidence"]
        outdated = result["outdated"]

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

        # 🔥 OUTDATED FLAG DISPLAY
        if outdated:
            st.error("⚠️ Warning: This document may be outdated.")

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
