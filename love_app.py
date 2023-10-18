import streamlit as st
from scipy.stats import binom

# Total number of single women in the age range 29-34 (assuming it's half of the total number of single women aged 25-34)
total_women_in_pool = 6236544 // 2

st.title("Love Story Probability Calculator with Optional MBTI and Unique Matches")

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

# Display the probability equations and explanations
st.markdown("### Probability Equation")
if include_mbti:
    st.latex(r"\text{Combined Probability} = (p)^2 \times \frac{1}{5} \times \frac{1}{365} \times \frac{1}{16}")
else:
    st.latex(r"\text{Combined Probability} = (p)^2 \times \frac{1}{5} \times \frac{1}{365}")

st.markdown("Where \( p \) is the probability of finding a compatible match.")

# Add explanations for 1/5 and 1/365
st.markdown("### Explanation of Terms")
st.markdown("- 1/5: Represents the probability of a woman being born in a specific year within the 5-year age range (29-34).")
st.markdown("- 1/365: Represents the probability of a woman being born on a specific day within that year.")

# Add a divider
st.divider()


# Additional Calculation for Unique Matches with Same Birthday (only 2 women like this in the whole pool)
st.markdown("### Probability for Unique Matches with Same Birthday (Only 2 women like this in the whole pool)")

# Calculate the probability for this unique scenario with same birthday
combined_probability_unique_matches_birthday = ((2 / total_women_in_pool) ** 2) * (1/365) * (1/5)

# Display the result for unique matches with same birthday
st.write(f"The combined probability of meeting the two unique 'dream matches' in the whole pool of women aged 29-34, who also share the same birthday, is approximately {combined_probability_unique_matches_birthday:.10f} or {combined_probability_unique_matches_birthday * 100:.10f}%")

# Display the probability equation for unique matches with same birthday
st.latex(r"\text{Combined Probability for Unique Matches with Same Birthday} = \left( \frac{2}{\text{Total Women in Pool}} \right)^2 \times \frac{1}{365} \times \frac{1}{5}")


st.divider()

# New Section: Probability of Finding Compatible Matches with the Same Birthday-Year
st.markdown("### Probability of Finding Compatible Matches with the Same Birthday-Year")

# User inputs for the new section
num_dates = st.number_input('Number of dates:', min_value=1, max_value=1000, value=100)
probability_compatible = st.slider('Probability of being compatible (%)', min_value=1, max_value=100, value=10)

# Calculations for the new section
probability_birthday_year = 1 / 3650  # The probability of having a specific birthday and year
probability_both_criteria = (probability_compatible / 100) * probability_birthday_year
probability_at_least_one = 1 - ((1 - probability_both_criteria) ** num_dates)
probability_exactly_two = binom.pmf(2, num_dates, probability_both_criteria)

# Display results for the new section
st.write(f'Probability of both criteria (compatible and same birthday-year) for a single date: {probability_both_criteria:.10f}')
st.write(f'Probability of finding at least one compatible match with the same birthday-year in {num_dates} dates: {probability_at_least_one:.10f}')
st.write(f'Probability of finding exactly two compatible matches with the same birthday-year in {num_dates} dates: {probability_exactly_two:.10f}')

# Display the probability equations and explanations for the new section
st.markdown("#### Probability Equation")
st.latex(r"\text{Probability of both criteria} = \left(\text{Probability of being compatible} \right) \times \frac{1}{3650}")
st.latex(r"\text{Probability of at least one match in \( N \) dates} = 1 - \left(1 - \text{Probability of both criteria}\right)^N")
st.latex(r"\text{Probability of exactly two matches in \( N \) dates} = \binom{N}{2} \times \left( \text{Probability of both criteria} \right)^2 \times \left(1 - \text{Probability of both criteria}\right)^{(N-2)}")
