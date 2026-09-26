import streamlit as st
import sympy as sp
import re

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="DON CALCULATOR",
    page_icon="💙",
    layout="centered"
)


# =========================================================
# CSS - LIGHT BLUE + HEART CALCULATOR
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');

/* =====================================================
   MAIN PAGE
   ===================================================== */

.stApp {
    background: linear-gradient(
        135deg,
        #e9f9ff 0%,
        #c9efff 50%,
        #a9e1fa 100%
    );

    color: #16445c;
    font-family: 'Poppins', sans-serif;
}


/* =====================================================
   TITLE
   ===================================================== */

.main-title {
    text-align: center;
    color: #1877a5;
    font-size: 38px;
    font-weight: 700;
    letter-spacing: 2px;
    margin-top: 5px;
}

.subtitle {
    text-align: center;
    color: #5d8da3;
    font-size: 14px;
    margin-bottom: 25px;
}


/* =====================================================
   CALCULATOR BODY
   ===================================================== */

.calculator {
    background: rgba(255, 255, 255, 0.65);
    padding: 22px;
    border-radius: 30px;

    box-shadow:
        0 18px 40px rgba(49, 130, 165, 0.20),
        inset 0 1px 2px rgba(255,255,255,0.9);

    border: 1px solid rgba(255,255,255,0.8);
}


/* =====================================================
   DISPLAY
   ===================================================== */

.display {
    background: #f4fcff;

    border-radius: 22px;

    min-height: 105px;

    padding: 18px 22px;

    margin-bottom: 25px;

    border: 2px solid #b8e5f5;

    box-shadow:
        inset 0 4px 10px rgba(55, 140, 180, 0.10);
}

.display-small {
    text-align: right;
    color: #7aa5b7;
    font-size: 14px;
    min-height: 20px;
}

.display-large {
    text-align: right;
    color: #155d7d;
    font-size: 38px;
    font-weight: 700;

    overflow-x: auto;
    white-space: nowrap;
}


/* =====================================================
   CALCULATOR BUTTONS
   ===================================================== */

/*
   Heart-shaped buttons.
   The shape is created using clip-path.
*/

.stButton > button {

    height: 65px;

    width: 100%;

    border: none !important;

    background: #ffffff !important;

    color: #17688f !important;

    font-family: 'Poppins', sans-serif;

    font-size: 17px;

    font-weight: 700;

    clip-path: polygon(
        50% 92%,
        8% 52%,
        8% 30%,
        15% 15%,
        30% 10%,
        50% 25%,
        70% 10%,
        85% 15%,
        92% 30%,
        92% 52%
    );

    box-shadow:
        0 5px 10px rgba(50, 130, 165, 0.18);

    transition: all 0.15s ease;
}


/* Hover */

.stButton > button:hover {

    background: #d9f5ff !important;

    color: #0d638e !important;

    transform: scale(1.05);
}


/* Click */

.stButton > button:active {

    transform: scale(0.95);
}


/* =====================================================
   OPERATOR BUTTONS
   ===================================================== */

.operator-button > button {

    background: #69c4eb !important;

    color: white !important;
}


/* =====================================================
   EQUAL BUTTON
   ===================================================== */

.equal-button > button {

    background: #187ca9 !important;

    color: white !important;
}


/* =====================================================
   CLEAR BUTTON
   ===================================================== */

.clear-button > button {

    background: #8ed8f5 !important;

    color: white !important;
}


/* =====================================================
   DERIVATIVE SECTION
   ===================================================== */

.derivative-card {

    background: rgba(255,255,255,0.72);

    border-radius: 28px;

    padding: 25px;

    margin-top: 30px;

    border: 2px solid #b9e6f5;

    box-shadow:
        0 12px 30px rgba(50,130,165,0.15);
}


/* =====================================================
   DERIVATIVE RESULT
   ===================================================== */

.derivative-result {

    background: #f3fcff;

    border-radius: 20px;

    padding: 20px;

    margin-top: 20px;

    border: 2px solid #b7e3f2;

    text-align: center;
}


/* =====================================================
   INPUTS
   ===================================================== */

input {

    background-color: #f7fdff !important;

    color: #174f6b !important;

    border-radius: 14px !important;
}


/* =====================================================
   FOOTER
   ===================================================== */

.footer {

    text-align: center;

    color: #5d8da3;

    font-size: 13px;

    margin-top: 25px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# TITLE
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
# SESSION STATE
# =========================================================

if "display" not in st.session_state:
    st.session_state.display = "0"

if "expression" not in st.session_state:
    st.session_state.expression = ""

if "last_result" not in st.session_state:
    st.session_state.last_result = ""


# =========================================================
# CALCULATOR FUNCTIONS
# =========================================================

def add_number(number):
    """
    Add a number to the calculator display.
    """

    if st.session_state.display == "0":

        st.session_state.display = number

    else:

        st.session_state.display += number


def add_decimal():
    """
    Add a decimal point.
    """

    current = st.session_state.display

    # Get the last number in the expression
    last_number = re.split(
        r'[+\-×÷*/]',
        current
    )[-1]

    if "." not in last_number:

        st.session_state.display += "."


def add_operator(operator):
    """
    Add a mathematical operator.
    """

    current = st.session_state.display

    # Don't allow two operators next to each other
    if current[-1] in "+-×÷*/":

        st.session_state.display = (
            current[:-1] + operator
        )

    else:

        st.session_state.display += operator


def clear_calculator():
    """
    Reset calculator.
    """

    st.session_state.display = "0"

    st.session_state.expression = ""

    st.session_state.last_result = ""


def toggle_sign():
    """
    Change positive number to negative
    and negative number to positive.
    """

    current = st.session_state.display

    if current == "0":
        return

    # If the whole display is a number
    try:

        value = float(current)

        if value > 0:

            st.session_state.display = "-" + current

        elif value < 0:

            st.session_state.display = current[1:]

        return

    except ValueError:
        pass

    # If expression contains an operator,
    # change the last number.
    match = re.search(
        r'(-?\d+\.?\d*)$',
        current
    )

    if match:

        number = match.group(1)

        start = match.start()

        if number.startswith("-"):

            number = number[1:]

        else:

            number = "-" + number

        st.session_state.display = (
            current[:start] + number
        )


def percentage():
    """
    Convert the current number to percentage.
    """

    current = st.session_state.display

    try:

        value = float(current)

        st.session_state.display = str(
            value / 100
        )

    except ValueError:

        st.warning(
            "Percentage works on a number."
        )


def calculate_result():
    """
    Calculate the expression safely using SymPy.
    """

    expression = st.session_state.display

    try:

        # Convert calculator symbols
        expression = expression.replace(
            "×",
            "*"
        )

        expression = expression.replace(
            "÷",
            "/"
        )

        # Evaluate using SymPy
        result = sp.sympify(expression)

        result = sp.N(result)

        # Remove unnecessary .0
        if float(result).is_integer():

            result = int(result)

        st.session_state.last_result = (
            st.session_state.display
        )

        st.session_state.display = str(result)

    except Exception:

        st.session_state.display = "Error"


# =========================================================
# CALCULATOR UI
# =========================================================

st.markdown(
    '<div class="calculator">',
    unsafe_allow_html=True
)


# =========================================================
# DISPLAY
# =========================================================

st.markdown(
    f"""
    <div class="display">

        <div class="display-small">
            {st.session_state.last_result}
        </div>

        <div class="display-large">
            {st.session_state.display}
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# ROW 1
# =========================================================

col1, col2, col3, col4 = st.columns(4)

with col1:

    if st.button(
        "AC",
        key="clear",
        use_container_width=True
    ):

        clear_calculator()
        st.rerun()

with col2:

    if st.button(
        "±",
        key="sign",
        use_container_width=True
    ):

        toggle_sign()
        st.rerun()

with col3:

    if st.button(
        "%",
        key="percent",
        use_container_width=True
    ):

        percentage()
        st.rerun()

with col4:

    if st.button(
        "÷",
        key="divide",
        use_container_width=True
    ):

        add_operator("÷")
        st.rerun()


# =========================================================
# ROW 2
# =========================================================

col1, col2, col3, col4 = st.columns(4)

with col1:

    if st.button(
        "7",
        key="7",
        use_container_width=True
    ):

        add_number("7")
        st.rerun()

with col2:

    if st.button(
        "8",
        key="8",
        use_container_width=True
    ):

        add_number("8")
        st.rerun()

with col3:

    if st.button(
        "9",
        key="9",
        use_container_width=True
    ):

        add_number("9")
        st.rerun()

with col4:

    if st.button(
        "×",
        key="multiply",
        use_container_width=True
    ):

        add_operator("×")
        st.rerun()


# =========================================================
# ROW 3
# =========================================================

col1, col2, col3, col4 = st.columns(4)

with col1:

    if st.button(
        "4",
        key="4",
        use_container_width=True
    ):

        add_number("4")
        st.rerun()

with col2:

    if st.button(
        "5",
        key="5",
        use_container_width=True
    ):

        add_number("5")
        st.rerun()

with col3:

    if st.button(
        "6",
        key="6",
        use_container_width=True
    ):

        add_number("6")
        st.rerun()

with col4:

    if st.button(
        "−",
        key="minus",
        use_container_width=True
    ):

        add_operator("-")
        st.rerun()


# =========================================================
# ROW 4
# =========================================================

col1, col2, col3, col4 = st.columns(4)

with col1:

    if st.button(
        "1",
        key="1",
        use_container_width=True
    ):

        add_number("1")
        st.rerun()

with col2:

    if st.button(
        "2",
        key="2",
        use_container_width=True
    ):

        add_number("2")
        st.rerun()

with col3:

    if st.button(
        "3",
        key="3",
        use_container_width=True
    ):

        add_number("3")
        st.rerun()

with col4:

    if st.button(
        "+",
        key="plus",
        use_container_width=True
    ):

        add_operator("+")
        st.rerun()


# =========================================================
# ROW 5
# =========================================================

col1, col2, col3, col4 = st.columns(4)

with col1:

    if st.button(
        "0",
        key="0",
        use_container_width=True
    ):

        add_number("0")
        st.rerun()

with col2:

    if st.button(
        ".",
        key="decimal",
        use_container_width=True
    ):

        add_decimal()
        st.rerun()

with col3:

    if st.button(
        "⌫",
        key="backspace",
        use_container_width=True
    ):

        if len(st.session_state.display) > 1:

            st.session_state.display = (
                st.session_state.display[:-1]
            )

        else:

            st.session_state.display = "0"

        st.rerun()

with col4:

    if st.button(
        "=",
        key="equals",
        use_container_width=True
    ):

        calculate_result()
        st.rerun()


st.markdown(
    "</div>",
    unsafe_allow_html=True
)


# =========================================================
# DERIVATIVE CALCULATOR
# =========================================================

st.markdown(
    '<div class="derivative-card">',
    unsafe_allow_html=True
)

st.markdown(
    "## 📐 Derivative Calculator"
)

st.write(
    "Find the derivative of a mathematical function "
    "without leaving the calculator."
)

st.info(
    "Examples:  x^2 + 3*x   •   sin(x)   •   "
    "x^3 + 2*x^2 - 5*x"
)


# =========================================================
# FUNCTION INPUT
# =========================================================

expression = st.text_input(
    "Enter your function",
    placeholder="Example: x^2 + 3*x"
)

variable = st.text_input(
    "Variable",
    value="x"
)


# =========================================================
# DERIVATIVE BUTTON
# =========================================================

if st.button(
    "💙 FIND DERIVATIVE",
    use_container_width=True
):

    if expression.strip() == "":

        st.warning(
            "Please enter a mathematical function."
        )

    else:

        try:

            # Create variable
            x = sp.Symbol(variable)

            # Convert ^ to **
            expression_python = expression.replace(
                "^",
                "**"
            )

            # Convert text into SymPy expression
            function = sp.sympify(
                expression_python,
                locals={
                    variable: x
                }
            )

            # Find derivative
            derivative = sp.diff(
                function,
                x
            )

            # Simplify
            derivative = sp.simplify(
                derivative
            )

            # =================================================
            # DISPLAY DERIVATIVE
            # =================================================

            st.markdown(
                f"""
                <div class="derivative-result">

                    <div style="
                        color:#6794a9;
                        font-size:14px;
                    ">
                        ORIGINAL FUNCTION
                    </div>

                    <div style="
                        color:#17688f;
                        font-size:28px;
                        font-weight:700;
                        margin:10px;
                    ">
                        $${sp.latex(function)}$$
                    </div>

                    <hr>

                    <div style="
                        color:#6794a9;
                        font-size:14px;
                    ">
                        DERIVATIVE
                    </div>

                    <div style="
                        color:#12648b;
                        font-size:32px;
                        font-weight:700;
                        margin:10px;
                    ">
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


st.markdown(
    "</div>",
    unsafe_allow_html=True
)


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">

        💙 DON CALCULATOR 💙<br>

        Python • Streamlit • SymPy

    </div>
    """,
    unsafe_allow_html=True
)
