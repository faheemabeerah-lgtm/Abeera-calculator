import streamlit as st
import sympy as sp

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="DON CALCULATOR",
    page_icon="💙",
    layout="centered"
)

# =========================================================
# LIGHT BLUE + HEART BUTTON CSS
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');

/* ---------- MAIN PAGE ---------- */

.stApp {
    background:
        linear-gradient(135deg, #dff6ff 0%, #bde9ff 50%, #a7ddff 100%);
    color: #17324d;
    font-family: 'Poppins', sans-serif;
}


/* ---------- TITLE ---------- */

.main-title {
    text-align: center;
    color: #1976a8;
    font-size: 38px;
    font-weight: 700;
    letter-spacing: 2px;
    margin-top: 10px;
}

.subtitle {
    text-align: center;
    color: #4c7892;
    font-size: 14px;
    margin-bottom: 25px;
}


/* ---------- CALCULATOR CONTAINER ---------- */

.calculator-box {
    background: rgba(255, 255, 255, 0.72);
    border-radius: 30px;
    padding: 25px;
    box-shadow:
        0 15px 35px rgba(49, 125, 160, 0.20),
        inset 0 1px 2px rgba(255,255,255,0.8);
    border: 1px solid rgba(255,255,255,0.8);
}


/* ---------- DISPLAY ---------- */

.display-box {
    background: #eefaff;
    border-radius: 22px;
    padding: 20px;
    min-height: 90px;
    margin-bottom: 20px;
    text-align: right;
    border: 2px solid #b6e5f7;
    box-shadow: inset 0 3px 8px rgba(55,140,180,0.10);
}

.display-label {
    color: #78a4b8;
    font-size: 13px;
}

.display-result {
    color: #12577b;
    font-size: 34px;
    font-weight: 700;
    word-wrap: break-word;
}


/* ---------- HEART BUTTONS ---------- */

.stButton > button {
    position: relative;
    height: 58px;
    width: 58px;
    margin: auto;

    background: #ffffff;
    color: #1976a8;

    border: none;

    /* Heart shape */
    border-radius: 0;

    transform: rotate(-45deg);

    box-shadow:
        4px 6px 12px rgba(45, 120, 155, 0.20);

    transition: all 0.2s ease;
}


/* Create heart using pseudo-elements */

.stButton > button::before,
.stButton > button::after {
    content: "";
    position: absolute;
    width: 58px;
    height: 58px;
    background: #ffffff;
    border-radius: 50%;
    z-index: -1;
}

.stButton > button::before {
    top: -29px;
    left: 0;
}

.stButton > button::after {
    top: 0;
    left: 29px;
}


/* Button text */

.stButton > button p {
    transform: rotate(45deg);
    font-size: 16px;
    font-weight: 700;
}


/* Hover */

.stButton > button:hover {
    background: #d9f4ff;
    color: #0d638e;

    transform:
        rotate(-45deg)
        scale(1.08);

    border: none;
}


/* ---------- SPECIAL BUTTON ---------- */

.special-button > button {
    background: #74c9ef !important;
    color: white !important;
}


/* ---------- OPERATION SELECTOR ---------- */

div[data-baseweb="select"] > div {
    background-color: #f5fcff !important;
    border: 2px solid #b6e5f7 !important;
    border-radius: 15px !important;
}


/* ---------- INPUTS ---------- */

input {
    background-color: #f5fcff !important;
    color: #174f6b !important;
    border-radius: 15px !important;
}


/* ---------- RESULT ---------- */

.result-box {
    background: rgba(255,255,255,0.8);
    border-radius: 22px;
    padding: 20px;
    margin-top: 20px;
    text-align: center;
    border: 2px solid #b6e5f7;
}

.result-title {
    color: #6794a9;
    font-size: 14px;
}

.result-text {
    color: #12648b;
    font-size: 30px;
    font-weight: 700;
}


/* ---------- DERIVATIVE BOX ---------- */

.derivative-box {
    background: linear-gradient(
        135deg,
        #ffffff,
        #e5f8ff
    );

    border-radius: 25px;
    padding: 25px;
    margin-top: 20px;

    border: 2px solid #a9ddf4;

    box-shadow:
        0 10px 25px rgba(46, 129, 165, 0.15);
}


/* ---------- HEADINGS ---------- */

h1, h2, h3 {
    color: #17688f !important;
}


/* ---------- DIVIDER ---------- */

hr {
    border-color: #a9dcef !important;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">💙 DON CALCULATOR 💙</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">A LITTLE CALCULATOR WITH A LOT OF HEART ♡</div>',
    unsafe_allow_html=True
)


# =========================================================
# MODE SELECTION
# =========================================================

mode = st.radio(
    "Choose calculator mode",
    ["🧮 Calculator", "📐 Derivative"],
    horizontal=True
)


# =========================================================
# BASIC CALCULATOR
# =========================================================

if mode == "🧮 Calculator":

    st.markdown(
        '<div class="calculator-box">',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="display-box">
            <div class="display-label">DON CALCULATOR</div>
            <div class="display-result">♡ Ready ♡</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # -----------------------------------------------------
    # NUMBER INPUTS
    # -----------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:
        num1 = st.number_input(
            "First number",
            value=0.0,
            key="number1"
        )

    with col2:
        num2 = st.number_input(
            "Second number",
            value=0.0,
            key="number2"
        )

    # -----------------------------------------------------
    # OPERATION
    # -----------------------------------------------------

    operation = st.selectbox(
        "Choose operation",
        [
            "➕ Addition",
            "➖ Subtraction",
            "✖️ Multiplication",
            "➗ Division"
        ]
    )

    # -----------------------------------------------------
    # CALCULATE
    # -----------------------------------------------------

    calculate = st.button(
        "💙  CALCULATE  💙",
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
                st.error("💔 Cannot divide by zero.")
                result = None

            else:
                result = num1 / num2

        if result is not None:

            st.markdown(
                f"""
                <div class="result-box">

                    <div class="result-title">
                        YOUR ANSWER 💙
                    </div>

                    <div class="result-text">
                        {result}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("</div>", unsafe_allow_html=True)


# =========================================================
# DERIVATIVE SOLVER
# =========================================================

else:

    st.markdown(
        '<div class="calculator-box">',
        unsafe_allow_html=True
    )

    st.subheader("📐 Derivative Calculator")

    st.write(
        "Enter a mathematical function in terms of **x**."
    )

    st.info(
        "Example: x^3 + 2*x^2 - 5*x"
    )

    # -----------------------------------------------------
    # FUNCTION INPUT
    # -----------------------------------------------------

    expression = st.text_input(
        "Enter your function",
        placeholder="Example: x^2 + 3*x + 5"
    )

    variable = st.text_input(
        "Variable",
        value="x"
    )

    solve = st.button(
        "💙  FIND DERIVATIVE  💙",
        use_container_width=True
    )

    # -----------------------------------------------------
    # SOLVE DERIVATIVE
    # -----------------------------------------------------

    if solve:

        if expression.strip() == "":
            st.warning(
                "💙 Please enter a function first."
            )

        else:

            try:

                # Create mathematical variable
                x = sp.Symbol(variable)

                # Convert ^ into **
                expression_python = expression.replace(
                    "^",
                    "**"
                )

                # Convert text into SymPy expression
                function = sp.sympify(
                    expression_python,
                    locals={variable: x}
                )

                # Calculate derivative
                derivative = sp.diff(
                    function,
                    x
                )

                # Simplify
                derivative = sp.simplify(
                    derivative
                )

                # -------------------------------------------------
                # DISPLAY ANSWER
                # -------------------------------------------------

                st.markdown(
                    f"""
                    <div class="derivative-box">

                        <div class="result-title">
                            ORIGINAL FUNCTION
                        </div>

                        <div class="result-text">
                            $${sp.latex(function)}$$
                        </div>

                        <br>

                        <div class="result-title">
                            DERIVATIVE
                        </div>

                        <div class="result-text">
                            $${sp.latex(derivative)}$$
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
                    "💔 I couldn't understand that function. "
                    "Please check your mathematical notation."
                )

    st.markdown("</div>", unsafe_allow_html=True)


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.markdown(
    """
    <div style="
        text-align:center;
        color:#4c7892;
        font-size:13px;
    ">
        💙 DON CALCULATOR 💙<br>
        Built with Python • Streamlit • SymPy
    </div>
    """,
    unsafe_allow_html=True
)
