import streamlit as st

st.set_page_config(page_title="AI Quiz (Guess Your Birthday)", page_icon="🎂")

st.title("🎂 AI Quiz (Guess Your Birthday)Made by AnshJ.tm")
st.caption("Hello, I am Java! I am here to assist you in this mini game (*-*)")
st.write("In the end, I will tell you your date of birth!")

# Initialize month detection state
if "month" not in st.session_state:
    st.session_state.month = None

# STEP 1: GUESS THE MONTH
if st.session_state.month is None:
    st.subheader("Part 1: Guessing Your Birth Month")

    # Character Count Question
    i = st.number_input(
        "First question: How many characters does your birth month have?",
        min_value=1,
        max_value=20,
        value=3,
        step=1
    )

    if i == 3:
        if st.button("Confirm Month"):
            st.session_state.month = "May"
            st.rerun()

    elif i == 6:
        if st.button("Confirm Month"):
            st.session_state.month = "August"
            st.rerun()

    elif i == 9:
        if st.button("Confirm Month"):
            st.session_state.month = "September"
            st.rerun()

    elif i == 7:
        x = st.radio("Second question: Does your birth month contain the letter 'O'?", ["Yes", "No"], key="q_7")
        if st.button("Submit Answer"):
            if x == "Yes":
                st.session_state.month = "October"
            else:
                st.session_state.month = "January"
            st.rerun()

    elif i == 8:
        x = st.radio("Second question: Does your birth month contain the letter 'O'?", ["Yes", "No"], key="q_8")
        if st.button("Submit Answer"):
            if x == "Yes":
                st.session_state.month = "November"
            else:
                st.session_state.month = "December"
            st.rerun()

    elif i == 5:
        o = st.radio("Fourth question: Does your birth month contain the letter 'M'?", ["Yes", "No"], key="q_5")
        if st.button("Submit Answer"):
            if o == "Yes":
                st.session_state.month = "March"
            else:
                st.session_state.month = "April"
            st.rerun()

    elif i == 4:
        p = st.radio("Fifth question: Does your birth month contain the letter 'L'?", ["Yes", "No"], key="q_4")
        if st.button("Submit Answer"):
            if p == "Yes":
                st.session_state.month = "July"
            else:
                st.session_state.month = "June"
            st.rerun()

# STEP 2: GUESS THE DAY
else:
    month_name = st.session_state.month
    st.info(f"So now I found your birth month: **{month_name}**!")
    st.subheader("Part 2: Now time to find your birth day (*-*)")

    op = st.radio("First Question: Is your birth date less than or equal to number '7'?", ["Yes", "No"], key="op")

    if op == "Yes":
        s = st.radio("Second Question: Is it an Even number?", ["Yes", "No"], key="s")
        if s == "Yes":
            yp = st.radio("Third Question: Is it less than number '6'?", ["Yes", "No"], key="yp")
            if yp == "Yes":
                ul = st.radio("Fourth Question: Is it a square number?", ["Yes", "No"], key="ul")
                if ul == "Yes":
                    st.success(f"🎉 Your birthday is on **4 {month_name}**")
                else:
                    st.success(f"🎉 Your birthday is on **2 {month_name}**")
            else:
                st.success(f"🎉 Your birthday is on **6 {month_name}**")
        else:
            xs = st.radio("Is your number less than number '7'?", ["Yes", "No"], key="xs")
            if xs == "Yes":
                xa = st.radio("Is your number a triangular number?", ["Yes", "No"], key="xa")
                if xa == "Yes":
                    xz = st.radio("Is your number greater than number '2'?", ["Yes", "No"], key="xz")
                    if xz == "Yes":
                        st.success(f"🎉 Your birthday is on **3 {month_name}**")
                    else:
                        st.success(f"🎉 Your birthday is on **1 {month_name}**")
                else:
                    st.success(f"🎉 Your birthday is on **5 {month_name}**")
            else:
                st.success(f"🎉 Your birthday is on **7 {month_name}**")

    else:
        bd = st.radio("Is your number less than or equal to number '14'?", ["Yes", "No"], key="bd")
        if bd == "Yes":
            zs = st.radio("Is your number Odd?", ["Yes", "No"], key="zs")
            if zs == "Yes":
                qs = st.radio("Is your number less than '12'?", ["Yes", "No"], key="qs")
                if qs == "Yes":
                    pw = st.radio("Is your number a multiple of '3'?", ["Yes", "No"], key="pw")
                    if pw == "Yes":
                        st.success(f"🎉 Your birthday is on **9 {month_name}**")
                    else:
                        st.success(f"🎉 Your birthday is on **11 {month_name}**")
                else:
                    st.success(f"🎉 Your birthday is on **13 {month_name}**")
            else:
                av = st.radio("Is your number less than number '14'?", ["Yes", "No"], key="av")
                if av == "Yes":
                    mn = st.radio("Is your number coming in the Table of '4'?", ["Yes", "No"], key="mn")
                    if mn == "Yes":
                        nb = st.radio("Does your number contain digit '0'?", ["Yes", "No"], key="nb")
                        if nb == "Yes":
                            st.success(f"🎉 Your birthday is on **10 {month_name}**")
                        else:
                            st.success(f"🎉 Your birthday is on **8 {month_name}**")
                    else:
                        st.success(f"🎉 Your birthday is on **12 {month_name}**")
                else:
                    st.success(f"🎉 Your birthday is on **14 {month_name}**")
        else:
            pm = st.radio("Is your number less than or equal to number '22'?", ["Yes", "No"], key="pm")
            if pm == "Yes":
                la = st.radio("Is your number less than 22?", ["Yes", "No"], key="la")
                if la == "Yes":
                    ed = st.radio("Is your number even?", ["Yes", "No"], key="ed")
                    if ed == "Yes":
                        js = st.radio("Is the digit sum of your number even?", ["Yes", "No"], key="js")
                        if js == "Yes":
                            fdt = st.radio("Is your number's digit sum greater than number '3'?", ["Yes", "No"], key="fdt")
                            if fdt == "Yes":
                                st.success(f"🎉 Your birthday is on **22 {month_name}**")
                            else:
                                st.success(f"🎉 Your birthday is on **20 {month_name}**")
                        else:
                            ur = st.radio("Is the digit sum of your number greater than number '8'?", ["Yes", "No"], key="ur")
                            if ur == "Yes":
                                st.success(f"🎉 Your birthday is on **18 {month_name}**")
                            else:
                                st.success(f"🎉 Your birthday is on **16 {month_name}**")
                    else:
                        xc = st.radio("Is your number's digit sum even?", ["Yes", "No"], key="xc")
                        if xc == "Yes":
                            cx = st.radio("Is your number's digit sum less than number '10'?", ["Yes", "No"], key="cx")
                            if cx == "Yes":
                                sd = st.radio("Is your number a multiple of 5?", ["Yes", "No"], key="sd")
                                if sd == "Yes":
                                    st.success(f"🎉 Your birthday is on **15 {month_name}**")
                                else:
                                    st.success(f"🎉 Your birthday is on **17 {month_name}**")
                            else:
                                st.success(f"🎉 Your birthday is on **19 {month_name}**")
                        else:
                            st.success(f"🎉 Your birthday is on **21 {month_name}**")
                else:
                    st.success(f"🎉 Your birthday is on **22 {month_name}**")
            else:
                os = st.radio("Is your number less than or equal to number 31?", ["Yes", "No"], key="os")
                if os == "Yes":
                    cv = st.radio("Is your number less than number 31?", ["Yes", "No"], key="cv")
                    if cv == "Yes":
                        io = st.radio("Is your number even?", ["Yes", "No"], key="io")
                        if io == "Yes":
                            ds = st.radio("Is your number's digit sum even?", ["Yes", "No"], key="ds")
                            if ds == "Yes":
                                hj = st.radio("Is your number's digit sum less than number '10'?", ["Yes", "No"], key="hj")
                                if hj == "Yes":
                                    vc = st.radio("Does your number come in 6's table?", ["Yes", "No"], key="vc")
                                    if vc == "Yes":
                                        st.success(f"🎉 Your birthday is on **24 {month_name}**")
                                    else:
                                        st.success(f"🎉 Your birthday is on **26 {month_name}**")
                                else:
                                    st.success(f"🎉 Your birthday is on **28 {month_name}**")
                            else:
                                st.success(f"🎉 Your birthday is on **30 {month_name}**")
                        else:
                            kl = st.radio("Is your number's digit sum odd?", ["Yes", "No"], key="kl")
                            if kl == "Yes":
                                xu = st.radio("Is your number's digit sum less than number 11?", ["Yes", "No"], key="xu")
                                if xu == "Yes":
                                    ko = st.radio("Is your number a multiple of 5?", ["Yes", "No"], key="ko")
                                    if ko == "Yes":
                                        st.success(f"🎉 Your birthday is on **25 {month_name}**")
                                    else:
                                        st.success(f"🎉 Your birthday is on **23 {month_name}**")
                                else:
                                    st.success(f"🎉 Your birthday is on **29 {month_name}**")
                            else:
                                st.success(f"🎉 Your birthday is on **27 {month_name}**")
                    else:
                        st.success(f"🎉 Your birthday is on **31 {month_name}**")
                else:
                    st.warning("Don't cheat!")

    if st.button("Play Again"):
        st.session_state.clear()
        st.rerun()