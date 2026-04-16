import streamlit as st

st.set_page_config(page_title="AI Knowledge Assistant", layout="wide")

st.title("🤖 AI Knowledge Assistant")

st.info("“AI-powered assistant to quickly find answers from company knowledge like SOPs, tickets, and policies.")

st.write("---")

st.sidebar.title("📂 Filter Knowledge Type")
category = st.sidebar.selectbox(
    "Choose category",
    ["All", "SOPs", "Tickets", "Policies", "Training"]
)

st.header("🔍 Ask a Question")
user_input = st.text_input("Type your question here:")

search_clicked = st.button("Search")

st.write("---")

if search_clicked:
    if user_input:
        st.header("📊 Results")

        col1, col2 = st.columns([3, 1])

        with col1:
            st.subheader("Top Answer")
            st.write("Example answer from knowledge base.")

        with col2:
            st.subheader("Confidence")
            st.metric(label="Score", value="87%")

        st.write("---")

        st.subheader("📄 Sources Used")
        st.write("- SOP: Example Guide")
        st.write("- Ticket #1234")

        st.success("Answer retrieved successfully!")

    else:
        st.warning("Please enter a question.")




st.markdown("""
<style>
.stButton>button {
    background-color: #4CAF50;
    color: white;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)



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
    }
}









if "password" in user_input.lower():
    answer = "Use the password reset SOP."
else:
    answer = "No matching result found."

st.write(answer)








answer = "No matching result found."
sources = []
confidence = "50%"

for key in knowledge_base:
    if key in user_input.lower():
        answer = knowledge_base[key]["answer"]
        sources = knowledge_base[key]["sources"]
        confidence = knowledge_base[key]["confidence"]
        break








st.write(answer)

st.subheader("📄 Sources Used")
for s in sources:
    st.write(f"- {s}")

st.metric("Confidence", confidence)
