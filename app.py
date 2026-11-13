import streamlit as st

st.title("SMP Tracker")
st.caption("Daily Performance & AI Coaching Tool")

name = st.text_input("Type in your name")
sleep = st.slider("How many hours did you sleep?", 0, 12, 7)
water = st.slider("How many glasses of water did you drink?", 0, 15, 8)
protocol = st.selectbox(
    "Select your daily protocol",
    ["Recovery & Hydration", "Deep Focus & Productivity", "Strength & Conditioning", "Custom Goal"]
)
goal_done = st.checkbox("Did you complete today's protocol target?")

if st.button("Get Coaching"):
    st.subheader(f"Daily Report for {name or 'Athlete'}")
    st.write(f"**Protocol:** {protocol}")
    st.write(f"**Sleep:** {sleep} hrs | **Water:** {water} glasses | **Target Hit:** {'Yes' if goal_done else 'No'}")

    if sleep >= 7 and water >= 8 and goal_done:
        st.success("Peak state! Sleep, hydration, and protocol are all locked in. Keep this momentum going.")
    elif sleep < 7 and water < 8:
        st.warning("Low fuel detected: Both sleep (<7h) and hydration (<8 glasses) are below baseline. Prioritize water now and an earlier bedtime tonight.")
    elif sleep < 7:
        st.info("Hydration is solid, but sleep is under 7 hours. Keep today's workload focused and protect your recovery window tonight.")
    elif water < 8:
        st.info("Good rest, but hydration is lagging (<8 glasses). Drink 2 glasses of water right now to sharpen focus.")
    else:
        st.info("Your physical baseline (sleep & water) is strong—lock in your remaining protocol task before wrapping up the day.")
