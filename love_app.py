import streamlit as st

st.title("Love Story Probability Calculator with Optional MBTI")

# User input for probability of finding a compatible match
prob_compatible = st.slider("Probability of finding a compatible match (%)", min_value=0.0, max_value=100.0, value=5.0, step=0.1)

# Checkbox for including MBTI
include_mbti = st.checkbox("Include Myers-Briggs Type Indicator (MBTI)")

# Convert to a fraction
prob_compatible /= 100

# Base probability equation
combined_probability = (prob_compatible ** 2) * (1/5) * (1/365)

# Include MBTI if checked
if include_mbti:
    combined_probability *= (1/16)

# Display the result
st.write(f"The combined probability of meeting two 'dream matches' born on the same specific day, month, year{' and having the same MBTI type' if include_mbti else ''} is approximately {combined_probability:.10f} or {combined_probability * 100:.10f}%")

# Display the probability equations
st.markdown("### Probability Equation")
if include_mbti:
    st.latex(r"\text{Combined Probability} = (p)^2 \times \frac{1}{5} \times \frac{1}{365} \times \frac{1}{16}")
else:
    st.latex(r"\text{Combined Probability} = (p)^2 \times \frac{1}{5} \times \frac{1}{365}")

st.markdown("Where \( p \) is the probability of finding a compatible match.")
