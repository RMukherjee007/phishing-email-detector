import streamlit as st
from core.classifier import EmailClassifier

st.set_page_config(page_title="AI Phishing Detector", page_icon="🛡️")

@st.cache_resource
def initialize_model():
    # Placeholder: In production, load a larger dataset or a saved .pkl
    clf = EmailClassifier()
    demo_texts = [
        "Are we still on for the project meeting at 3 PM?",
        "URGENT: Your account access is restricted. Verify here: http://bit.ly/fake-auth",
        "Please find the attached invoice for last month's services.",
        "Your subscription has expired. Update billing now: http://netflix-secure.com"
    ]
    labels = [0, 1, 0, 1]
    clf.train(demo_texts, labels)
    return clf

classifier = initialize_model()

st.title("🛡️ Phishing Email Detector")
st.markdown("Analyze email content for suspicious patterns, URLs, and urgent language.")

email_input = st.text_area("Paste Email Text:", placeholder="Example: Your account is suspended...", height=200)

if st.button("Analyze Content", type="primary"):
    if email_input.strip():
        result = classifier.predict(email_input)
        
        if result.label == 1:
            st.error(f"Analysis: {result.label_name}")
            st.warning(f"Confidence Score: {result.confidence:.2%}")
            st.info("Flagged for: Suspicious URL patterns or urgent call-to-action language.")
        else:
            st.success(f"Analysis: {result.label_name}")
            st.write(f"Confidence Score: {result.confidence:.2%}")
    else:
        st.info("Please enter email text to begin analysis.")
