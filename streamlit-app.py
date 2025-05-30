import streamlit as st
import pandas as pd
from mlProject.pipeline.prediction import PredictionPipeline

# Set page configuration
st.set_page_config(
    page_title="Plan Abandonment Risk Predictor",
    page_icon="💸",
    layout="centered"
)

# --- Background Image Styling ---
st.markdown(
    """
    <style>
    /* Background image styling */
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1605902711622-cfb43c4437d1");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
    }

    /* Text box styling */
    .title {
        background-color: rgba(255, 255, 255, 0.8);
        padding: 1.5rem;
        border-radius: 10px;
        margin-top: 2rem;
        text-align: center;
    }

    .input-container {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 2rem;
        border-radius: 15px;
        margin-top: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Page Title ---
st.markdown('<div class="title"><h1>📊 Plan Abandonment Risk Predictor</h1><p>Estimate the likelihood of clients abandoning their financial plans</p></div>', unsafe_allow_html=True)

# --- Input Section ---
with st.container():
    st.markdown('<div class="input-container">', unsafe_allow_html=True)

    gender_id = st.selectbox("Gender", options=[0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
    risk_apetite = st.slider("Risk Appetite", 0.0, 1.0, 0.5)
    fraud_score = st.slider("Fraud Score", 0.0, 1.0, 0.1)
    monthly_expense = st.number_input("Monthly Expense (USD)", min_value=0.0)
    account_type = st.selectbox("Account Type", options=["Savings", "Current"])
    total_transactions = st.number_input("Total Transactions", min_value=0)
    total_transaction_amount = st.number_input("Total Transaction Amount", min_value=0.0)
    total_withdrawn_amount = st.number_input("Total Withdrawn Amount", min_value=0.0)

    # Predict Button
    if st.button("🔍 Predict Risk"):
        input_df = pd.DataFrame([{
            "gender_id": gender_id,
            "risk_apetite": risk_apetite,
            "fraud_score": fraud_score,
            "monthly_expense": monthly_expense,
            "type": account_type,
            "total_transactions": total_transactions,
            "total_transaction_amount": total_transaction_amount,
            "total_withdrawn_amount": total_withdrawn_amount
        }])

        try:
            obj = PredictionPipeline()
            predicted_prob = obj.predict(input_df)[0]
            score_percent = round(predicted_prob * 100, 2)

            st.markdown("---")
            if predicted_prob > 0.5:
                st.error(f"**Risk Score: {score_percent}%**\n\n⚠️ **High Risk of Plan Abandonment**")
            else:
                st.success(f"**Risk Score: {score_percent}%**\n\n✅ **Low Risk of Plan Abandonment**")

        except Exception as e:
            st.error("❌ An error occurred during prediction.")
            st.exception(e)

    st.markdown('</div>', unsafe_allow_html=True)
