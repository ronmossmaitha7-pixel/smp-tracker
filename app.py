import streamlit as st

st.title("SMP Tracker")
st.caption("Daily Performance & AI Coaching Tool")

name = st.text_input("Type in your name")
protocol = st.selectbox(
    "Select your daily protocol",
    ["2MAD (Two Meals a Day)", "OMAD (One Meal a Day)"]
)
sleep = st.slider("How many hours did you sleep?", 0, 12, 7)
water = st.slider("How many glasses of water did you drink?", 0, 15, 8)
goal_done = st.checkbox("Did you complete today's protocol target?")

if st.button("Get Coaching"):
    st.subheader(f"Daily Report for {name or 'Athlete'}")
    st.write(f"**Protocol:** {protocol} | **Target Hit:** {'Yes' if goal_done else 'No'}")
    st.write(f"**Sleep:** {sleep} hrs | **Water:** {water} glasses")

    # Protocol-specific coaching tip
    if protocol == "OMAD (One Meal a Day)":
        if water < 10:
            st.warning("OMAD Alert: Longer fasting windows demand extra hydration and electrolytes. Aim for at least 10 glasses of water today.")
        else:
            st.info("OMAD Protocol: Strong hydration for an extended fast. Make sure your single meal is nutrient-dense and protein-rich.")
    else:
        if water < 8:
            st.warning("2MAD Alert: Keep hydration at 8+ glasses between your two meals to prevent energy dips.")
        else:
            st.info("2MAD Protocol: Solid hydration across your eating window. Keep both meals balanced for steady energy.")

    # Recovery & sleep feedback
    if sleep >= 7 and goal_done:
        st.success("Peak state! Recovery and protocol execution are both locked in.")
    elif sleep < 7:
        st.warning("Recovery Note: Sleep is under 7 hours. Prioritize an earlier bedtime tonight to protect fasting energy.")
