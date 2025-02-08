from itertools import product
import streamlit as st

# Define the mappings
mappings = {
    '0': ['o', 'c', 'd'],
    '1': ['i', 'l'],
    '2': ['s', 'z'],
    '3': ['e'],
    '4': ['h', 'a', 'f', 'u', 'v', 'y'],
    '5': ['s', 'c', 'z'],
    '6': ['c', 'g', 'a'],
    '7': ['y', 't', 'f', 'l', 'j'],
    '8': ['b', 'a'],
    '9': ['g', 'q', 'c', 'p', 'a'],
    '%': ['b', 'p', 'q', 'd'],
    '"': ['u', 'v'],
    '$': ['r', 'b', 'k'],
    '&': ['n', 'u']
}

def generate_transpositions(input_string):
    if not all(char in mappings for char in input_string):
        return ["Invalid character in input"]
    
    # Generate all possible combinations for the input string
    combinations = [mappings[char] for char in input_string]
    all_combinations = product(*combinations)
    
    # Convert the product result to strings
    return [''.join(combo) for combo in all_combinations]

# Streamlit interface
st.title("Number to Letter Transpositions")

# Input field for the user
user_input = st.text_input("Enter a string of up to 5 characters (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, %, \", $, &):", "")

if user_input:
    results = generate_transpositions(user_input.lower())
    st.write("Possible Transpositions:")
    for result in results:
        st.write(result)
        