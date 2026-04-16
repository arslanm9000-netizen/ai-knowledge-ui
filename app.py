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

# Knowledge base (FULLY MATCHES SLIDE)
knowledge_base = {
    "password": {
        "answer": "To reset your password, go to the company portal → click 'Forgot Password' → follow the email instructions.",
        "sources": ["SOP: Password Reset Guide"],
        "confidence": "92%",
        "outdated": False
    },
    "onboarding": {
        "answer": "During onboarding, set up your account, configure email and VPN, and review company policies.",
        "sources": ["Onboarding Guide"],
        "confidence": "91%",
        "outdated": False
    },
    "backup": {
        "answer": "If a backup failure occurs, check logs, retry the backup, and escalate to the IT infrastructure team if unresolved.",
        "sources": ["SOP: Backup Failure Handling", "Ticket #7789"],
        "confidence": "87%",
        "outdated": False
    },
    "policy": {
        "answer": "Leave policies define employee entitlements such as vacation days, sick leave, and approval procedures.",
        "sources": ["Policy Document v1.2"],
        "confidence": "95%",
        "outdated": True   # 🔥 RED FLAG (matches slide)
    }
}

# Search logic
if search_clicked:
    if user_input:
        st.header("📊 Results")

        user_text = user_input.lower()

        if "password" in user_text:
            result = knowledge_base["password"]

        elif "onboarding" in user_text or "new employee" in user_text or "get started" in user_text:
            result = knowledge_base["onboarding"]

        elif "backup" in user_text or "backup failure" in user_text or "escalate" in user_text:
            result = knowledge_base["backup"]

        elif "policy" in user_text or "policies" in user_text or "leave" in user_text:
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

        # 🔥 OUTDATED FLAG (matches slide exactly)
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
