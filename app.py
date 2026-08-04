import streamlit as st
import numpy as np
import pandas as pd

# --- Page Setup ---
st.set_page_config(page_title="Testing the Code: Chandler Park Academy", page_icon="🕹️")

# --- Developer / School Credit Header ---
st.markdown("""
<div style='background: linear-gradient(135deg, #002D72 0%, #003DA5 100%); 
            padding: 20px; 
            border-radius: 10px; 
            margin-bottom: 20px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
    <div style='color: white;'>
        <h2 style='margin: 0; color: #FFC72C; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);'>
            🕹️ Testing the Code: Solving Equations Through Substitution & Translation
        </h2>
        <p style='margin: 5px 0; font-size: 1.1em; font-weight: 500;'>
            Chandler Park Academy | Detroit, Michigan | Home of the Eagles 🦅
        </p>
        <p style='margin: 5px 0; opacity: 0.95;'>
            6th Grade Mathematics | Mr. Honablue
        </p>
        <hr style='border: 1px solid rgba(255,255,255,0.3); margin: 10px 0;'>
        <p style='margin: 5px 0; font-size: 0.95em;'>
            🎮 Theme: Game Developer Code Check | Unit: Expressions &amp; Equations
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# --- Title and Lesson Snapshot ---
st.title("🦅 Eagle Coders: Testing the Code")
st.markdown("""
Welcome, **Chandler Park Eagles**!  
Today you're not just doing math — you're **debugging game code**. Every equation we test today is really a line of code from a video game, and your job is to prove whether it's TRUE (the game works) or FALSE (the game glitches).

By the end of this 40-minute session, you will be able to:
- **Use substitution** to prove whether a number makes an equation true
- **Translate** real-world sentences — including the sneaky "less than" phrase — into equations
- **Design and solve** your own original equation, starring people from our own building
""")

col1, col2, col3 = st.columns(3)
with col1:
    st.info("⏱️ **Duration**\n\n40 minutes")
with col2:
    st.info("📐 **Primary Standard**\n\nMI.6.EE.B.5")
with col3:
    st.info("🎯 **Practice Standard**\n\nMP.4 - Model with Math")

st.success("**🎯 Learning Target:** I can use substitution to prove whether a given number makes an equation true, and I can translate a real-world statement — including a 'less than' turnaround phrase — into an equation.")

st.markdown("---")

# --- Standards Dropdown (MOVED ABOVE THE GOAL STATEMENT) ---
st.subheader("📋 Explore the Standards Behind Today's Lesson")
standard_choice = st.selectbox("Select a Michigan Standard (with its Common Core equivalent) to see how it connects to the big-picture goal:", [
    "MI.6.EE.B.5 — Use substitution to determine whether a given number makes an equation true",
    "MI.6.EE.B.6 — Use variables to represent numbers; write expressions/equations for real-world problems",
    "MI.6.EE.B.7 — Solve real-world problems by writing and solving equations of the form x + p = q and px = q",
    "MI.6.RP.A.3.c — Find a percent of a quantity; solve problems involving a part and a percent",
    "MP.1 — Make sense of problems and persevere in solving them",
    "MP.4 — Model with mathematics",
    "MP.6 — Attend to precision"
])

standard_details = {
    "MI.6.EE.B.5": {
        "cc": "CCSS.MATH.CONTENT.6.EE.B.5",
        "rigor": "Justification through evidence — the core of today's Hook and Guided Practice.",
        "where": "Hook (APPROVED/REJECTED vote), Model (Pac-Man), Guided Practice (Donkey Kong/Q*bert)"
    },
    "MI.6.EE.B.6": {
        "cc": "CCSS.MATH.CONTENT.6.EE.B.6",
        "rigor": "Representation flexibility — moving fluently between plain language and symbolic code.",
        "where": "Mini-Lesson (Turnaround Word Trap), Worksheet 1"
    },
    "MI.6.EE.B.7": {
        "cc": "CCSS.MATH.CONTENT.6.EE.B.7",
        "rigor": "Structural problem-solving — isolating an unknown to reveal its true value.",
        "where": "Worksheet 1, Exit Ticket"
    },
    "MI.6.RP.A.3.c": {
        "cc": "CCSS.MATH.CONTENT.6.RP.A.3.c",
        "rigor": "Proportional reasoning — a preview connection for tomorrow's spiral review.",
        "where": "Previewed at Close (IXL breadth sprint)"
    },
    "MP.1": {
        "cc": "CCSS.MATH.PRACTICE.MP1",
        "rigor": "Perseverance — trying, checking, and revising before giving up on a verdict.",
        "where": "Guided Practice pair-work and justification"
    },
    "MP.4": {
        "cc": "CCSS.MATH.PRACTICE.MP4",
        "rigor": "Original modeling — the highest-leverage move in the whole lesson: authoring your own equation instead of consuming someone else's.",
        "where": "Exit Ticket — Design Your Own Equation"
    },
    "MP.6": {
        "cc": "CCSS.MATH.PRACTICE.MP6",
        "rigor": "Precision of language — using terms like variable, quotient, and balanced equation exactly and correctly.",
        "where": "Model segment vocabulary anchoring"
    }
}

selected_code = standard_choice.split(" — ")[0]
details = standard_details[selected_code]

st.markdown(f"""
<div style='background-color: #f0f4fa; padding: 15px; border-radius: 8px; border-left: 5px solid #002D72;'>
    <p style='margin: 4px 0;'><strong>Michigan Standard:</strong> {selected_code}</p>
    <p style='margin: 4px 0;'><strong>Common Core Equivalent:</strong> {details['cc']}</p>
    <p style='margin: 4px 0;'><strong>🧭 Rigor Skill It Builds:</strong> {details['rigor']}</p>
    <p style='margin: 4px 0;'><strong>📍 Where in Today's Lesson:</strong> {details['where']}</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# --- Overarching Goal Statement (NOW BELOW THE DROPDOWN) ---
st.markdown("""
<div style='background: linear-gradient(135deg, #FFC72C 0%, #E8A317 100%); 
            padding: 18px; border-radius: 10px; margin-bottom: 15px;'>
    <h4 style='color: #002D72; margin-top: 0;'>🧭 The Big Picture: Why This Lesson Matters</h4>
    <p style='color: #002D72; margin: 0; font-size: 0.98em;'>
    Every activity today — voting on a suspect value, debugging Pac-Man code, translating a tricky sentence, 
    designing your own equation — is really building the <strong>same underlying rigor skill: mathematical justification.</strong> 
    That's the ability to <strong>prove a claim is true using evidence</strong> (substitution), 
    <strong>convert between representations</strong> (words ⇄ symbols), and <strong>construct your own original model</strong> 
    of a real situation (MP.4) rather than just following someone else's steps. This is the same reasoning skill 
    that underlies science conclusions, financial decisions, and coding logic — not just today's worksheet.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ============================================================
# SEGMENT 1: HOOK (0:00-0:05)
# ============================================================
st.header("🚨 Segment 1: The Hook — Fraud Detective / Code Glitch (0:00–0:05)")
st.markdown("""
**Mr. Patillo** is coding a brand-new trivia game for the school. He wrote a line of code, but nobody has checked it yet.  
The "suspect" value on trial today is **p = 70**.

Your job: vote whether this suspect value is **APPROVED** (makes the equation true) or **REJECTED** (breaks the game).
""")

st.markdown("#### 🕵️ The Equation on Trial:")
st.latex(r"\frac{p}{7} = 10")

hook_vote = st.radio("Is **p = 70** the correct code?", ["I haven't voted yet", "✅ APPROVED (TRUE)", "❌ REJECTED (FALSE)"], key="hook_vote")

if hook_vote == "✅ APPROVED (TRUE)":
    st.success("🎉 Correct verdict! Let's prove it together below.")
elif hook_vote == "❌ REJECTED (FALSE)":
    st.warning("Let's check the math together before we lock in that verdict...")

with st.expander("🔍 Reveal the Verdict"):
    st.markdown("""
    **Substitute p = 70 into the equation:**
    """)
    st.latex(r"\frac{70}{7} = 10 \;\rightarrow\; 10 = 10 \;\; \checkmark")
    st.success("**TRUE — p = 70 works!** Substitution means plugging a suspect number in and checking if both sides balance.")

st.markdown("---")

# ============================================================
# SEGMENT 2: MODEL (0:05-0:12)
# ============================================================
st.header("👾 Segment 2: Model — Pac-Man 'Pellets per Level' (0:05–0:12)")
st.markdown("""
Let's model this the way Mr. Patillo would while debugging his game. The equation **p / 7 = 10** represents 
**total pellets (p) split evenly across 7 mazes**, where each maze should have **10 pellets**.

First, watch what happens with a **buggy value**:
""")

col1, col2 = st.columns(2)
with col1:
    st.markdown("##### ❌ Buggy Code: p = 14")
    st.latex(r"\frac{14}{7} = 10")
    st.latex(r"2 \neq 10")
    st.error("**FALSE — this glitches the game!** 2 pellets per maze does not equal the required 10.")

with col2:
    st.markdown("##### ✅ Patched Code: p = 70")
    st.latex(r"\frac{70}{7} = 10")
    st.latex(r"10 = 10")
    st.success("**TRUE — this patch balances the equation!**")

st.info("""
**🔑 Vocabulary Anchor:**
- **Variable** — the unknown quantity in the code (p)
- **Quotient** — the result of division (here, pellets ÷ mazes)
- **Balanced equation** — both sides equal the same value
- **Substitution** — plugging a suspect number in for the variable to test it
""")

st.markdown("---")

# ============================================================
# SEGMENT 3: GUIDED PRACTICE (0:12-0:18)
# ============================================================
st.header("🎮 Segment 3: Guided Practice — Donkey Kong & Q*bert (0:12–0:18)")
st.markdown("""
Now it's your turn to code-check with a partner! New equation, new game.

**Mr. Okamoto** is testing a new obstacle course app. Total obstacles (**x**) are split across **6 stages**, and each stage should have **8 obstacles**.

Is **x = 48** a solution to:
""")
st.latex(r"\frac{x}{6} = 8")

st.markdown("Use the Donkey Kong 'barrels per girder' story or the Q*bert 'hops per level' story to justify your verdict with your partner, then check below:")

gp_col1, gp_col2 = st.columns(2)
with gp_col1:
    left_side = st.text_input("LEFT SIDE (after substituting x = 48):", key="gp_left")
with gp_col2:
    right_side = st.text_input("RIGHT SIDE:", key="gp_right")

gp_verdict = st.radio("VERDICT:", ["I haven't decided yet", "TRUE", "FALSE"], key="gp_verdict")

if 'gp_attempts' not in st.session_state:
    st.session_state.gp_attempts = 0

if st.button("Check My Verdict", key="gp_check"):
    if gp_verdict == "TRUE":
        st.balloons()
        st.success("✅ Correct! **48 / 6 = 8 → 8 = 8** — the code is TRUE! Barrels (or hops) per girder (or level) check out perfectly.")
    else:
        st.session_state.gp_attempts += 1
        if st.session_state.gp_attempts == 1:
            st.warning("❌ Not quite! Let's try again with a hint:")
            st.info("💡 Substitute x = 48 into x / 6. What is 48 ÷ 6? Does that match the required 8 obstacles per stage?")
        else:
            st.error("❌ Still not quite right.")
            st.warning("💡 **The correct answer is: TRUE.** 48 / 6 = 8, and 8 = 8, so the code balances!")
            st.info("Review the Pac-Man model above and try again to master this concept!")

st.markdown("---")

# ============================================================
# SEGMENT 4: MINI-LESSON (0:18-0:24)
# ============================================================
st.header("🔄 Segment 4: Mini-Lesson — The 'Turnaround Word' Trap (0:18–0:24)")
st.markdown("""
Some game code doesn't come as an equation right away — it comes as a **sentence**. Your job as a Game Engine Designer 
is to translate that sentence into code (an equation).

Watch out for the trap phrase **"less than"** — it secretly **flips the order** of the sentence!
""")

st.markdown("##### 📝 Worked Example:")
st.markdown('*"211 is b less than 48"*')
st.latex(r"211 = 48 - b")
st.warning("**Why the flip?** \"b less than 48\" means you start with 48 and subtract b — even though b is mentioned first in the sentence!")

with st.expander("🧠 Turnaround Word Bank (for reference)"):
    st.markdown("""
    | Phrase | What it means |
    |---|---|
    | "is" | = |
    | "more than" | + (in the order given) |
    | "less than" | flips the order! subtract from the SECOND number |
    | "times" / "of" | × |
    | "split evenly across" | ÷ |
    """)

st.markdown("---")

# ============================================================
# SEGMENT 5: INDEPENDENT PRACTICE - WORKSHEET 1
# ============================================================
st.header("📄 Segment 5: Independent Practice — Worksheet 1: Testing the Code (0:24–0:32)")
st.markdown("""
<div style='background: linear-gradient(135deg, #002D72 0%, #003DA5 100%); 
            padding: 15px; border-radius: 8px; margin-bottom: 15px;'>
    <p style='color: white; margin: 0; font-size: 0.95em;'>
    🎮 <strong>MATH · GAME DEVELOPER EDITION</strong><br>
    These problems feature real people from our building — including <strong>Mr. Calvin Patillo</strong> and 
    <strong>Mr. Chris Okamoto</strong> — so bring your best code-testing skills!
    </p>
</div>
""", unsafe_allow_html=True)

st.info("**Quick recap:** To test if a value is a solution, substitute it in for the variable and simplify both sides. If both sides balance, the code checks out — it's a TRUE solution!")

# Worksheet 1 - Problem 1 (Worked Example, shown as reference)
st.markdown("### ① Worked Example")
st.markdown("""
**Mr. Patillo** is coding a new trivia game. The total point pool (**p**) is split evenly across **7 rounds**, 
and each round should award **10 points**. Is p = 70 the correct code?
""")
st.latex(r"70 / 7 = 10 \;\;\; 10 = 10 \;\checkmark \;\;\; \text{TRUE — p = 70 works!}")
st.caption("Substitution means finding out whether a suspect number really unlocks the equation.")

st.markdown("---")

# Worksheet 1 - Problem 2
st.markdown("### ② Your Turn")
st.markdown("""
**Mr. Okamoto** is testing a new obstacle course app. Total obstacles (**x**) are split across **6 stages**, 
and each stage should have **8 obstacles**. Is **x = 48** a solution to x / 6 = 8?
""")

w1p2_col1, w1p2_col2, w1p2_col3 = st.columns(3)
with w1p2_col1:
    w1p2_left = st.text_input("LEFT SIDE:", key="w1p2_left")
with w1p2_col2:
    w1p2_right = st.text_input("RIGHT SIDE:", key="w1p2_right")
with w1p2_col3:
    w1p2_verdict = st.selectbox("VERDICT:", ["-- choose --", "TRUE", "FALSE"], key="w1p2_verdict")

if 'w1p2_attempts' not in st.session_state:
    st.session_state.w1p2_attempts = 0

if st.button("Check Problem 2", key="w1p2_check"):
    if w1p2_verdict == "TRUE":
        st.success("✅ Correct! 48 / 6 = 8, and 8 = 8 — balanced! x = 48 is a true solution.")
        st.session_state.w1p2_attempts = 0
    else:
        st.session_state.w1p2_attempts += 1
        if st.session_state.w1p2_attempts == 1:
            st.warning("❌ Not quite! Here's a hint:")
            st.info("💡 Divide 48 by 6. Compare that quotient to the 8 obstacles required per stage.")
        else:
            st.error("❌ Still not quite right.")
            st.warning("💡 **The correct answer is: TRUE** — 48 / 6 = 8, so both sides balance.")

st.markdown("---")

# Worksheet 1 - Problem 3
st.markdown("### ③ Your Turn")
st.markdown("""
In **Ms. Naismith's** app, energy points (**y**) minus a 15-point penalty equal **92** remaining points. 
Is **y = 107** a solution to y − 15 = 92?
""")

w1p3_col1, w1p3_col2, w1p3_col3 = st.columns(3)
with w1p3_col1:
    w1p3_left = st.text_input("LEFT SIDE:", key="w1p3_left")
with w1p3_col2:
    w1p3_right = st.text_input("RIGHT SIDE:", key="w1p3_right")
with w1p3_col3:
    w1p3_verdict = st.selectbox("VERDICT:", ["-- choose --", "TRUE", "FALSE"], key="w1p3_verdict")

if 'w1p3_attempts' not in st.session_state:
    st.session_state.w1p3_attempts = 0

if st.button("Check Problem 3", key="w1p3_check"):
    if w1p3_verdict == "TRUE":
        st.success("✅ Correct! 107 − 15 = 92, and 92 = 92 — balanced! y = 107 is a true solution.")
        st.session_state.w1p3_attempts = 0
    else:
        st.session_state.w1p3_attempts += 1
        if st.session_state.w1p3_attempts == 1:
            st.warning("❌ Not quite! Here's a hint:")
            st.info("💡 Subtract 15 from 107. Does that match the 92 remaining points?")
        else:
            st.error("❌ Still not quite right.")
            st.warning("💡 **The correct answer is: TRUE** — 107 − 15 = 92, so both sides balance.")

st.markdown("---")

# Worksheet 1 - Problem 4 (Translate)
st.markdown("### ④ Turnaround Word Challenge — Translate It")
st.warning("**Watch for the trap phrase \"less than.\"** Translate this statement into an equation (don't solve yet):")
st.markdown("*\"Mr. Okamoto's final score of 350 is d points less than Mr. Patillo's score of 420.\"*")

w1p4_answer = st.text_input("MY EQUATION:", key="w1p4_equation", placeholder="e.g., 350 = 420 − d")

if 'w1p4_attempts' not in st.session_state:
    st.session_state.w1p4_attempts = 0

if st.button("Check Problem 4", key="w1p4_check"):
    cleaned = w1p4_answer.replace(" ", "")
    if cleaned in ["350=420-d", "350=420−d"]:
        st.success("✅ Correct! **350 = 420 − d**. Because of the 'less than' flip, we start with 420 and subtract d.")
        st.session_state.w1p4_attempts = 0
    else:
        st.session_state.w1p4_attempts += 1
        if st.session_state.w1p4_attempts == 1:
            st.warning("❌ Not quite! Here's a hint:")
            st.info("💡 Remember: 'd less than 420' means you start with 420 and subtract d — even though d is mentioned first in the sentence!")
        else:
            st.error("❌ Still not quite right.")
            st.warning("💡 **The correct equation is: 350 = 420 − d**")
            st.info("Review the Turnaround Word Trap section above and try again to master this concept!")

st.markdown("---")

# Worksheet 1 - Problem 5 (Solve for d)
st.markdown("### ⑤ Solve It")
st.markdown("Now solve the equation from Problem 4 for **d**. Show your work.")

w1p5_work = st.text_area("Show your work:", key="w1p5_work", height=100)
w1p5_answer = st.text_input("d = ", key="w1p5_answer")

if 'w1p5_attempts' not in st.session_state:
    st.session_state.w1p5_attempts = 0

if st.button("Check Problem 5", key="w1p5_check"):
    try:
        val = float(w1p5_answer.strip())
        correct = (val == 70)
    except:
        correct = False

    if correct:
        st.balloons()
        st.success("✅ Correct! **d = 70**. Check it: 350 = 420 − 70 → 350 = 350 ✓")
        st.session_state.w1p5_attempts = 0
    else:
        st.session_state.w1p5_attempts += 1
        if st.session_state.w1p5_attempts == 1:
            st.warning("❌ Not quite! Here's a hint:")
            st.info("💡 Starting from 350 = 420 − d, isolate d by rearranging: d = 420 − 350. What does that equal?")
        else:
            st.error("❌ Still not quite right.")
            st.warning("💡 **The correct answer is: d = 70.** Check: 350 = 420 − 70 → 350 = 350 ✓")
            st.info("Review the 'Equations Are Just Balance Checks' concept and try again!")

# Check if all Worksheet 1 problems are correct
w1_checks = [
    w1p2_verdict == "TRUE",
    w1p3_verdict == "TRUE",
    w1p4_answer.replace(" ", "") in ["350=420-d", "350=420−d"],
]
try:
    w1p5_correct = float(w1p5_answer.strip()) == 70
except:
    w1p5_correct = False
w1_checks.append(w1p5_correct)

if all(w1_checks) and w1p2_verdict != "-- choose --":
    st.success("🏆 **Worksheet 1 complete and fully correct!** You've officially earned your Game Code Tester badge!")
    st.balloons()

st.markdown("""
<div style='text-align: center; padding: 10px; margin-top: 10px;'>
<em>☆ A wrong code crashes the game — a tested code always balances! ☆</em>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ============================================================
# SEGMENT 6: EXIT TICKET - WORKSHEET 2
# ============================================================
st.header("🏆 Segment 6: Exit Ticket — Worksheet 2: Code Cracked! Design Your Own Equation (0:32–0:38)")
st.markdown("""
<div style='background: linear-gradient(135deg, #FFC72C 0%, #E8A317 100%); 
            padding: 15px; border-radius: 8px; margin-bottom: 15px;'>
    <p style='color: #002D72; margin: 0; font-size: 0.95em; font-weight: 600;'>
    🦅 GAME DESIGN POSTER · CHANDLER PARK ACADEMY — Code Cracked: What We Discovered
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("This is the **highest-leverage move** of the whole lesson — instead of testing someone else's code, *you* are the game developer now.")

# Poster Card 1 - Testing a Solution (recap)
st.markdown("#### ① Testing a Solution *(recap)*")
st.markdown("Our class tested whether **p = 70** solves the equation p / 7 = 10, based on Mr. Patillo's trivia game code.")
st.latex(r"70/7 = 10 \;\rightarrow\; \text{TRUE}")
st.caption("Substitution means plugging a suspect number in and checking if both sides balance.")

st.markdown("#### ② Translating Words to Code *(recap)*")
st.markdown("Mr. Toma's score of 350 is d points less than Mr. Patillo's score of 420.")
st.latex(r"350 = 420 - d")
st.caption('Watch the trap: "less than" flips the order of the sentence!')

st.markdown("#### ③ Solving for the Unknown *(recap)*")
st.markdown("Solve the equation from Card 2 for **d**.")
st.latex(r"350 = 420 - d \;\rightarrow\; d = 70")
st.caption("Isolate the variable to reveal the true value.")

st.markdown("#### ④ Equations Are Just Balance Checks!")
st.info("""
An equation says two things are equal. A solution is any value that keeps both sides balanced — like a scale that doesn't tip.
Every equation in our game code — pellets, barrels, scores — can be tested the exact same way: **substitute, simplify, compare.**
""")

st.markdown("---")

# Poster Card 5 - Design Your Own Equation (the actual exit ticket task)
st.markdown("#### ⑤ Design Your Own Equation!")
st.markdown("""
Pick a game or real-world context. Pick two real people (classmates, teachers, or **Mr. Patillo & Mr. Toma**). 
Write your own equation using their scores or stats — then solve it!
""")

with st.expander("💡 See the Sample Problem"):
    st.markdown("""
    **My problem:** Mr. Patillo and Mr. Toma are racing to level up in a new app. Mr. Patillo needs 15 more points than Mr. Toma to reach Level 10. Mr. Patillo has 215 points, which is exactly 15 more than Mr. Toma's total. How many points does Mr. Toma have?

    **My equation:** 215 = g + 15  
    **My answer:** g = 200 points  
    **Check it:** 215 = 200 + 15 → TRUE!
    """)

st.markdown("##### ✏️ MY PROBLEM:")
my_problem = st.text_area("Write your original word problem here:", key="my_problem", height=100,
                            placeholder="e.g., Mr. Okamoto and Ms. Naismith are competing in a trivia app...")

et_col1, et_col2, et_col3 = st.columns(3)
with et_col1:
    my_equation = st.text_input("MY EQUATION:", key="my_equation", placeholder="e.g., 215 = g + 15")
with et_col2:
    my_answer = st.text_input("MY ANSWER:", key="my_answer", placeholder="e.g., g = 200")
with et_col3:
    my_check = st.text_input("CHECK:", key="my_check", placeholder="e.g., 215 = 200 + 15 ✓")

if st.button("Submit My Original Equation", key="submit_exit_ticket"):
    if my_problem.strip() and my_equation.strip() and my_answer.strip() and my_check.strip():
        st.balloons()
        st.success("🎉 Outstanding work, Game Designer! You've authored an original equation from scratch — the highest level of mathematical thinking in today's lesson (MP.4: Model with Mathematics)!")
    else:
        st.warning("Please fill in all four fields (problem, equation, answer, and check) to complete your exit ticket.")

st.markdown("---")

# ============================================================
# SEGMENT 7: CLOSE & PREVIEW
# ============================================================
st.header("📣 Segment 7: Close & Preview (0:38–0:40)")
st.markdown("""
Great work today, Eagles! A few of you will share your self-built equations under the visualizer.

**🔭 Looking ahead:** Tomorrow we launch an **IXL breadth sprint** across related standards — equations, inequalities, 
and expressions — including a first look at **MI.6.RP.A.3.c** (percents), to help you start noticing how these skills connect.
""")

st.markdown("---")

# ============================================================
# STANDARDS REFERENCE TABLE
# ============================================================
st.header("📚 Michigan Standards Covered in This Lesson")

standards_data = {
    "Code": ["MI.6.EE.B.5", "MI.6.EE.B.6", "MI.6.EE.B.7", "MI.6.RP.A.3.c", "MP.1", "MP.4", "MP.6"],
    "Standard": [
        "Understand solving an equation as determining which values from a set make it true; use substitution to test solutions.",
        "Use variables to represent numbers; write expressions/equations to represent real-world and mathematical problems.",
        "Solve real-world and mathematical problems by writing and solving equations of the form x + p = q and px = q.",
        "Find a percent of a quantity; solve problems involving finding the whole given a part and the percent.",
        "Make sense of problems and persevere in solving them.",
        "Model with mathematics.",
        "Attend to precision (vocabulary: variable, quotient, balanced equation, substitution)."
    ],
    "Where in Lesson": [
        "Hook, Model, Guided Practice",
        "Mini-Lesson, Worksheet 1",
        "Worksheet 1, Exit Ticket",
        "IXL breadth sprint (previewed at close)",
        "Guided Practice pair-work and justification",
        "Exit Ticket — Design Your Own Equation",
        "Model segment vocabulary anchoring"
    ]
}
standards_df = pd.DataFrame(standards_data)
st.dataframe(standards_df, use_container_width=True, hide_index=True)

st.markdown("---")

# ============================================================
# DIFFERENTIATION NOTE
# ============================================================
st.header("🎯 Differentiation Support")

diff_col1, diff_col2, diff_col3 = st.columns(3)
with diff_col1:
    st.markdown("**🚀 Extending (On/Above Level)**")
    st.write("Try turning today's one-step equation into a two-step equation — what would you add?")
with diff_col2:
    st.markdown("**🛠️ Building (Approaching Level)**")
    st.write("Use the word bank: 'is → =', 'less than → flip the order'")
with diff_col3:
    st.markdown("**🤝 Support (Needs Support)**")
    st.write("Use a number line or manipulatives to test your substitution")

st.markdown("---")

# ============================================================
# FINAL SUMMARY
# ============================================================
st.header("🦅 What You've Learned Today")
st.markdown("""
**Congratulations, Eagle Coders!** Today you:
- ✅ **Tested equations using substitution** — proving values TRUE or FALSE like a code inspector
- ✅ **Translated tricky sentences into equations**, including the "less than" turnaround trap
- ✅ **Solved for an unknown variable** to reveal the true value hidden in the code
- ✅ **Designed and solved your own original equation** — the true mark of mastery

**Remember:** Every equation — whether it's about pellets, barrels, hops, or your own game — can be tested the exact same way: **substitute, simplify, compare.**

Keep your code clean, Chandler Park Eagles — see you at tomorrow's IXL sprint! 🦅🎮
""")
