<<<<<<< HEAD
import streamlit as st
import pandas as pd
import joblib

# =====================================================
# CONFIG
# =====================================================

st.set_page_config(
    page_title="Network Anomaly Detection",
    layout="wide"
)

# =====================================================
# LOAD MODEL
# =====================================================

MODEL_PATH = "randomForestClassifier.pkl"

model = joblib.load(MODEL_PATH)

# =====================================================
# TITLE
# =====================================================

st.title("Network Anomaly Detection Dashboard")

st.markdown(
    """
    Prediksi apakah traffic network termasuk:
    - **Normal**
    - **Anomaly / Intrusion**
    """
)

# =====================================================
# INPUT LAYOUT
# =====================================================

col1, col2 = st.columns(2)

with col1:

    network_packet_size = st.number_input(
        "Network Packet Size",
        min_value=0,
        value=500
    )

    protocol_type = st.selectbox(
        "Protocol Type",
        ["TCP", "UDP", "ICMP"]
    )

    login_attempts = st.number_input(
        "Login Attempts",
        min_value=0,
        value=1
    )

    session_duration = st.number_input(
        "Session Duration",
        min_value=0.0,
        value=300.0
    )

    encryption_used = st.selectbox(
        "Encryption Used",
        ["AES", "DES", "None"]
    )

with col2:

    ip_reputation_score = st.slider(
        "IP Reputation Score",
        min_value=0.0,
        max_value=1.0,
        value=0.5
    )

    failed_logins = st.number_input(
        "Failed Logins",
        min_value=0,
        value=0
    )

    browser_type = st.selectbox(
        "Browser Type",
        ["Chrome", "Firefox", "Edge", "Safari", "Unknown"]
    )

    unusual_time_access = st.selectbox(
        "Unusual Time Access",
        [0, 1]
    )

# =====================================================
# PREDICT BUTTON
# =====================================================

if st.button("Predict"):

    input_df = pd.DataFrame([{
        "network_packet_size": network_packet_size,
        "protocol_type": protocol_type,
        "login_attempts": login_attempts,
        "session_duration": session_duration,
        "encryption_used": encryption_used,
        "ip_reputation_score": ip_reputation_score,
        "failed_logins": failed_logins,
        "browser_type": browser_type,
        "unusual_time_access": unusual_time_access
    }])

    prediction = model.predict(input_df)[0]

    probability = model.predict_proba(input_df)[0]

    normal_prob = probability[0]
    anomaly_prob = probability[1]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("Anomaly / Intrusion Detected")
    else:
        st.success("Normal Network Activity")

    st.write("Confidence Score")

    st.progress(float(max(normal_prob, anomaly_prob)))

    st.write(
        {
            "Normal Probability": round(normal_prob, 4),
            "Anomaly Probability": round(anomaly_prob, 4)
        }
    )

# =====================================================
# BATCH PREDICTION
# =====================================================

st.markdown("---")
st.subheader("Batch Prediction (CSV Upload)")

uploaded_file = st.file_uploader(
    "Upload CSV",
    type=["csv"]
)

if uploaded_file:

    batch_df = pd.read_csv(uploaded_file)

    batch_predictions = model.predict(batch_df)

    batch_df["prediction"] = batch_predictions

    batch_df["prediction_label"] = batch_df["prediction"].map({
        0: "Normal",
        1: "Anomaly"
    })

    st.dataframe(
        batch_df,
        use_container_width=True
    )

    csv = batch_df.to_csv(index=False)

    st.download_button(
        "Download Prediction Result",
        csv,
        "network_predictions.csv",
        "text/csv"
=======
import streamlit as st
import pandas as pd
import joblib

# =====================================================
# CONFIG
# =====================================================

st.set_page_config(
    page_title="Network Anomaly Detection",
    layout="wide"
)

# =====================================================
# LOAD MODEL
# =====================================================

MODEL_PATH = "randomForestClassifier.pkl"

model = joblib.load(MODEL_PATH)

# =====================================================
# TITLE
# =====================================================

st.title("Network Anomaly Detection Dashboard")

st.markdown(
    """
    Prediksi apakah traffic network termasuk:
    - **Normal**
    - **Anomaly / Intrusion**
    """
)

# =====================================================
# INPUT LAYOUT
# =====================================================

col1, col2 = st.columns(2)

with col1:

    network_packet_size = st.number_input(
        "Network Packet Size",
        min_value=0,
        value=500
    )

    protocol_type = st.selectbox(
        "Protocol Type",
        ["TCP", "UDP", "ICMP"]
    )

    login_attempts = st.number_input(
        "Login Attempts",
        min_value=0,
        value=1
    )

    session_duration = st.number_input(
        "Session Duration",
        min_value=0.0,
        value=300.0
    )

    encryption_used = st.selectbox(
        "Encryption Used",
        ["AES", "DES", "None"]
    )

with col2:

    ip_reputation_score = st.slider(
        "IP Reputation Score",
        min_value=0.0,
        max_value=1.0,
        value=0.5
    )

    failed_logins = st.number_input(
        "Failed Logins",
        min_value=0,
        value=0
    )

    browser_type = st.selectbox(
        "Browser Type",
        ["Chrome", "Firefox", "Edge", "Safari", "Unknown"]
    )

    unusual_time_access = st.selectbox(
        "Unusual Time Access",
        [0, 1]
    )

# =====================================================
# PREDICT BUTTON
# =====================================================

if st.button("Predict"):

    input_df = pd.DataFrame([{
        "network_packet_size": network_packet_size,
        "protocol_type": protocol_type,
        "login_attempts": login_attempts,
        "session_duration": session_duration,
        "encryption_used": encryption_used,
        "ip_reputation_score": ip_reputation_score,
        "failed_logins": failed_logins,
        "browser_type": browser_type,
        "unusual_time_access": unusual_time_access
    }])

    prediction = model.predict(input_df)[0]

    probability = model.predict_proba(input_df)[0]

    normal_prob = probability[0]
    anomaly_prob = probability[1]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("Anomaly / Intrusion Detected")
    else:
        st.success("Normal Network Activity")

    st.write("Confidence Score")

    st.progress(float(max(normal_prob, anomaly_prob)))

    st.write(
        {
            "Normal Probability": round(normal_prob, 4),
            "Anomaly Probability": round(anomaly_prob, 4)
        }
    )

# =====================================================
# BATCH PREDICTION
# =====================================================

st.markdown("---")
st.subheader("Batch Prediction (CSV Upload)")

uploaded_file = st.file_uploader(
    "Upload CSV",
    type=["csv"]
)

if uploaded_file:

    batch_df = pd.read_csv(uploaded_file)

    batch_predictions = model.predict(batch_df)

    batch_df["prediction"] = batch_predictions

    batch_df["prediction_label"] = batch_df["prediction"].map({
        0: "Normal",
        1: "Anomaly"
    })

    st.dataframe(
        batch_df,
        use_container_width=True
    )

    csv = batch_df.to_csv(index=False)

    st.download_button(
        "Download Prediction Result",
        csv,
        "network_predictions.csv",
        "text/csv"
>>>>>>> 1cd948768f3a51ffc16d4e12c644ee23431ca93e
    )