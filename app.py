import streamlit as st
from core.classifier import EmailClassifier, ResultInterpreter

st.set_page_config(page_title="Phishing Email Detector")

if "example_loaded" not in st.session_state:
    st.session_state.example_loaded = False

st.title("Phishing Email Detection")

classifier = EmailClassifier()
classifier.train(
    ["hello meeting tomorrow", "urgent verify account http://fake.com"],
    [0, 1],
)
interpreter = ResultInterpreter(classifier)

email = st.text_area(
    "Email text",
    value="URGENT: verify your account http://fake.com"
    if st.session_state.example_loaded
    else "",
)

if st.button("Load Example"):
    st.session_state.example_loaded = True
    st.rerun()

if st.button("Analyze"):
    result, details = interpreter.predict_with_details(email)
    st.write(result.label_name, f"{result.confidence:.2%}")
    st.write(details)
