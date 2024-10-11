import streamlit as st
import pandas 

# Set webpage layout to wide
st.set_page_config(layout= "wide")

# Add a header and some other text
st.header("The Best Company")
st.write("""
Lorem ipsum dolor sit amet,consectetur adipiscing elit , sed do eiusmode
tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam , quis nostrud exercitation ullamco laboris nisi ut
aliguip ex ea commodo consequat. Duis aute irure dolor in reprehenderit
in voluptate velit esse cillum dolore eu fugiat nulla pariature.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui
officia deserunt mollit anim id est laborum.""")

st.subheader("Our Teams")

# Prepare te columns
col1, col2, col3 = st.columns(3)

# Make a dataframe with the company members
df = pandas.read_csv("venu\data (1).csv")

# Add content to the first column
with col1:
    # Iterate over only the first four rows
    for index, row in df[:4].iterrows():
        # Add member's first and last names
        st.subheader(f'{row['first name'].title()}{row['last name'].title()}')
        # Add member's role in the company
        st.write(row["role"])
        # Add member's photo
        st.image("image/" + row['image'])

# Add Content to the second column
with col2:
    # iterate over rows 4 to 7
    for index, row in df[4:9].iterrows():
        # Add member's first and last names
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        # Add member's role in the company
        st.write(row['role'])
        # Add member's photo
        st.image("image/"+ row["image"])


with col3:
    # iterate over rows 4 to 7
    for index, row in df[8:].iterrows():
        # Add member's first and last names
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        # Add member's role in the company
        st.write(row['role'])
        # Add member's photo
        st.image("image/"+ row["image"])
