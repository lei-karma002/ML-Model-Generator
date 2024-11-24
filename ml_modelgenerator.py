import streamlit as st

# Set the page title and layout
st.set_page_config(page_title="Modeling and Simulation Project", layout="centered")

# Project Title
st.title("📊 Modeling and Simulation Project")

# Introduction Section
st.subheader("Introduction")
st.write("""
Welcome to the **Modeling and Simulation Project**!  
This project is focused on exploring the principles of modeling and simulation using **Python**. 
The goal is to provide hands-on experience with Python libraries and tools that are commonly used 
for such tasks, enabling us to understand complex systems and their behavior.
""")

# Purpose of the Project
st.subheader("Purpose")
st.write("""
- To develop an understanding of modeling and simulation concepts.
- To leverage Python's capabilities for implementing models and simulations.
- To gain practical knowledge of Python libraries such as **NumPy**, **Pandas**, **Matplotlib**, 
  **SciPy**, and others.
""")

# Tools and Libraries Section
st.subheader("Tools and Libraries")
st.write("""
In this project, we will use the following tools and libraries:
- **Streamlit** for creating interactive visualizations and dashboards.
- **NumPy** for numerical computations.
- **Matplotlib** and **Seaborn** for data visualization.
- **SciPy** for scientific computing.
- Other libraries as needed for specific modeling and simulation tasks.
""")

# Call to Action
st.markdown("---")
st.info("Stay tuned as we build models, simulate systems, and create visualizations step by step!")

