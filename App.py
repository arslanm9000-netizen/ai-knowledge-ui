import streamlit as st

st.set_page_config(page_title="AI Knowledge Assistant", layout="wide")

st.title("🤖 AI Knowledge Assistant")

st.info("A small AI-based internal knowledge assistant that lets Bee's Knees employees ask questions and retrieve grounded answers from SOPs, onboarding guides, policy documents, and resolved-ticket examples.")

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