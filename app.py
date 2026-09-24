import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Mafia Calculator",
    page_icon="🖤",
    layout="centered"
)

# Dark Mafia CSS
st.markdown("""
<style>

.stApp {
    background: #080808;
    color: #f2f2f2;
}

/* Main title */
.mafia-title {
    text-align: center;
    color: #c9a227;
    font-family: Georgia, serif;
    font-size: 42px;
    font-weight: bold;
    letter-spacing: 4px;
    margin-bottom: 5px;
}

.mafia-subtitle {
    text-align: center;
    color: #888888;
    font-family: Georgia, serif;
    font-size: 15px;
    letter-spacing: 2px;
    margin-bottom: 30px;
}

/* Calculator box */
.calculator {
    background: #111111;
    border: 1px solid #4a0d0d;
    border-radius: 18px;
    padding: 30px;
    box-shadow: 0 0 25px rgba(120, 0, 0, 0.25);
}

/* Labels */
label {
    color: #c9a227 !important;
    font-weight: bold !important;
}

/* Number inputs */
div[data-baseweb="input"] {
    background-color: #181818;
    border: 1px solid #3d3d3d;
    border-radius: 10px;
}

div[data-baseweb="input"] input {
    color: white !important;
    background-color: #181818 !important;
}

/* Select box */
div[data-baseweb="select"] > div {
    background-color: #181818;
    border: 1px solid #3d3d3d;
    color: white;
    border-radius: 10px;
}

/* Calculate button */
.stButton > button {
    width: 100%;
    background: #5c0b0b;
    color: #f1d27a;
    border: 1px solid #c9a227;
    border-radius: 10px;
    height: 50px;
    font-size: 17px;
    font-weight: bold;
    letter-spacing: 2px;
    transition: 0.3s;
}

.stButton > button:hover {
    background: #8b1111;
    color: white;
    border-color: #f0c94a;
}

/* Result */
.result-box {
    margin-top: 25px;
    padding: 18px;
    text-align: center;
    background: #160909;
    border: 1px solid #8b1111;
    border-radius: 10px;
    color: #c9a227;
    font-family: Georgia, serif;
    font-size: 24px;
    font-weight: bold;
}

.footer {
    text-align: center;
    color: #555555;
    margin-top: 25px;
    font-size: 12px;
    letter-spacing: 2px;
}

</style>
""", unsafe_allow_html=True)


# Title
st.markdown(
    '<div class="mafia-title">♠ MAFIA CALCULATOR ♠</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="mafia-subtitle">CALCULATE WITH STYLE</div>',
    unsafe_allow_html=True
)

# Calculator container
st.markdown('<div class="calculator">', unsafe_allow_html=True)

# Number inputs
number1 = st.number_input(
    "FIRST NUMBER",
    value=0.0
)

number2 = st.number_input(
    "SECOND NUMBER",
    value=0.0
)

# Operation
operation = st.selectbox(
    "CHOOSE OPERATION",
    [
        "Addition",
        "Subtraction",
        "Multiplication",
        "Division"
    ]
)

# Calculate
if st.button("CALCULATE"):

    if operation == "Addition":
        result = number1 + number2

    elif operation == "Subtraction":
        result = number1 - number2

    elif operation == "Multiplication":
        result = number1 * number2

    elif operation == "Division":

        if number2 == 0:
            st.error("You cannot divide by zero.")
            result = None
        else:
            result = number1 / number2

    if result is not None:
        st.markdown(
            f'<div class="result-box">RESULT: {result}</div>',
            unsafe_allow_html=True
        )

st.markdown('</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="footer">♠ CLASS • POWER • PRECISION ♠</div>',
    unsafe_allow_html=True
)
