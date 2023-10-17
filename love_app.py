import streamlit as st

# Total number of single women in the age range 29-34 (assuming it's half of the total number of single women aged 25-34)
total_women_in_pool = 6236544

st.title("Love Story Probability Calculator with Optional MBTI and Unique Matches")

# User input for probability of finding a compatible match
prob_compatible = st.slider("Probability of finding a compatible match (%)", min_value=0.0, max_value=100.0, value=5.0, step=0.1)

# Checkbox for including MBTI
include_mbti = st.checkbox("Include Myers-Briggs Type Indicator (MBTI)")

# Convert to a fraction
prob_compatible /= 100

# Base probability equation
combined_probability = (prob_compatible ** 2) * (1/10) * (1/365)

# Include MBTI if checked
if include_mbti:
    combined_probability *= (1/16)

# Display the result
st.write(f"The combined probability of meeting two 'dream matches' born on the same specific day, month, year{' and having the same MBTI type' if include_mbti else ''} is approximately {combined_probability:.10f} or {combined_probability * 100:.10f}%")

# Display the probability equations and explanations
st.markdown("### Probability Equation")
if include_mbti:
    st.latex(r"\text{Combined Probability} = (p)^2 \times \frac{1}{10} \times \frac{1}{365} \times \frac{1}{16}")
else:
    st.latex(r"\text{Combined Probability} = (p)^2 \times \frac{1}{10} \times \frac{1}{365}")

st.markdown("Where \( p \) is the probability of finding a compatible match.")

# Add explanations for 1/10 and 1/365
st.markdown("### Explanation of Terms")
st.markdown("- 1/10: Represents the probability of a woman being born in a specific year within the 10-year age range (25-34).")
st.markdown("- 1/365: Represents the probability of a woman being born on a specific day within that year.")

# Add a divider
st.divider()


# Additional Calculation for Unique Matches with Same Birthday (only 2 women like this in the whole pool)
st.markdown("### Probability for Unique Matches with Same Birthday (Only 2 women like this in the whole pool)")

# Calculate the probability for this unique scenario with same birthday
combined_probability_unique_matches_birthday = ((2 / total_women_in_pool) ** 2) * (1/365) * (1/10)

# Display the result for unique matches with same birthday
st.write(f"The combined probability of meeting the two unique 'dream matches' in the whole pool of women aged 29-34, who also share the same birthday, is approximately {combined_probability_unique_matches_birthday:.10f} or {combined_probability_unique_matches_birthday * 100:.10f}%")

# Display the probability equation for unique matches with same birthday
st.latex(r"\text{Combined Probability for Unique Matches with Same Birthday} = \left( \frac{2}{\text{Total Women in Pool}} \right)^2 \times \frac{1}{365} \times \frac{1}{10}")
