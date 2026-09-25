import streamlit as st
import sympy as sp

# -----------------------------
# PAGE CONFIGURATION
# -----------------------------
st.set_page_config(
    page_title="DON CALCULATOR",
    page_icon="🕴️",
    layout="centered"
)

# -----------------------------
# MAFIA STYLE CSS
# -----------------------------
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700&family=Roboto+Mono:wght@400;500;700&display=swap');

.stApp {
    background:
        radial-gradient(circle at top, #252525 0%, #101010 40%, #050505 100%);
    color: #eeeeee;
}

h1, h2, h3 {
    font-family: 'Cinzel', serif;
    color: #d4af37;
    text-align: center;
}

.main-title {
    font-family: 'Cinzel', serif;
    color: #d4af37;
    text-align: center;
    font-size: 42px;
    font-weight: 700;
    letter-spacing: 4px;
}

.subtitle {
    text-align: center;
    color: #888888;
    font-family: 'Roboto Mono', monospace;
    margin-bottom: 30px;
}

.result-box {
    background: linear-gradient(135deg, #181818, #252525);
    border: 1px solid #d4af37;
    border-radius: 12px;
    padding: 25px;
    margin-top: 20px;
    text-align: center;
}

.result-text {
    color: #d4af37;
    font-size: 30px;
    font-family: 'Roboto Mono', monospace;
    font-weight: bold;
}

.stButton > button {
    background: linear-gradient(145deg, #292929, #111111);
    color: #d4af37;
    border: 1px solid #d4af37;
    border-radius: 8px;
    font-family: 'Cinzel', serif;
    font-weight: bold;
    transition: 0.2s;
}

.stButton > button:hover {
    background: #d4af37;
    color: #000000;
    border-color: #ffffff;
}

div[data-baseweb="select"] > div {
    background-color: #151515;
    color: #ffffff;
    border: 1px solid #444444;
}

input {
    background-color: #151515 !important;
    color: white !important;
}

hr {
    border-color: #333333;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------
# HEADER
# -----------------------------

st.markdown(
    '<div class="main-title">🕴️ DON CALCULATOR</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">THE MATH FAMILY • NO MISTAKES ALLOWED</div>',
    unsafe_allow_html=True
)


# -----------------------------
# MODE SELECTION
# -----------------------------

mode = st.radio(
    "Choose your operation",
    ["🧮 Mafia Calculator", "📐 Derivative Solver"],
    horizontal=True
)


# =========================================================
# BASIC CALCULATOR
# =========================================================

if mode == "🧮 Mafia Calculator":

    st.subheader("🕴️ Make Your Move")

    col1, col2 = st.columns(2)

    with col1:
        num1 = st.number_input(
            "First Number",
            value=0.0
        )

    with col2:
        num2 = st.number_input(
            "Second Number",
            value=0.0
        )

    operation = st.selectbox(
        "Choose Operation",
        [
            "➕ Addition",
            "➖ Subtraction",
            "✖️ Multiplication",
            "➗ Division"
        ]
    )

    calculate = st.button(
        "💰 CALCULATE",
        use_container_width=True
    )

    if calculate:

        if operation == "➕ Addition":
            result = num1 + num2

        elif operation == "➖ Subtraction":
            result = num1 - num2

        elif operation == "✖️ Multiplication":
            result = num1 * num2

        elif operation == "➗ Division":

            if num2 == 0:
                st.error("🚫 The Don doesn't divide by zero.")
                result = None
            else:
                result = num1 / num2

        if result is not None:

            st.markdown(
                f"""
                <div class="result-box">
                    <div>THE DON'S ANSWER</div>
                    <div class="result-text">{result}</div>
                </div>
                """,
                unsafe_allow_html=True
            )


# =========================================================
# DERIVATIVE SOLVER
# =========================================================

else:

    st.subheader("📐 The Don's Calculus Department")

    st.write(
        "Enter a mathematical expression in terms of **x**."
    )

    expression = st.text_input(
        "Enter your function",
        placeholder="Example: x^3 + 2*x^2 - 5*x"
    )

    variable = st.text_input(
        "Variable",
        value="x"
    )

    solve = st.button(
        "🔫 SOLVE DERIVATIVE",
        use_container_width=True
    )

    if solve:

        if expression.strip() == "":
            st.warning("Enter a function first.")

        else:

            try:

                x = sp.Symbol(variable)

                # Convert ^ to ** for Python/SymPy
                expression = expression.replace("^", "**")

                function = sp.sympify(
                    expression,
                    locals={variable: x}
                )

                derivative = sp.diff(
                    function,
                    x
                )

                st.markdown(
                    f"""
                    <div class="result-box">
                        <div>ORIGINAL FUNCTION</div>
                        <div class="result-text">
                            {sp.latex(function)}
                        </div>

                        <br>

                        <div>THE DON'S DERIVATIVE</div>
                        <div class="result-text">
                            {sp.latex(derivative)}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.success(
                    f"Derivative: {derivative}"
                )

            except Exception:
                st.error(
                    "🚫 The Don couldn't understand that expression. "
                    "Check your mathematical syntax."
                )


# -----------------------------
# FOOTER
# -----------------------------

st.divider()

st.caption(
    "🕴️ DON CALCULATOR • Powered by Python + Streamlit + SymPy"
)
