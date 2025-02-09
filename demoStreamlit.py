import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Title
st.title("💡 Modernizing Financial Analysis with Streamlit")
# Intro
st.write("This demo showcases how analysts can replace outdated legacy tools with a modern, interactive Streamlit tool.")
# Sample Financial Data
data = pd.DataFrame({
   "Date": pd.date_range(start="1/1/2024", periods=12, freq="M"),
   "Revenue ($M)": np.random.randint(80, 120, size=12),
   "Expenses ($M)": np.random.randint(50, 90, size=12)
})
data["Profit ($M)"] = data["Revenue ($M)"] - data["Expenses ($M)"]
# User input for filtering date range
st.sidebar.header("Filters")
start_date, end_date = st.sidebar.slider("Select Date Range:",
                                       min_value=data.Date.min().to_pydatetime(),
                                       max_value=data.Date.max().to_pydatetime(),
                                       value=(data.Date.min().to_pydatetime(), data.Date.max().to_pydatetime()),
                                       format="MM/YYYY")
filtered_data = data[(data.Date >= start_date) & (data.Date <= end_date)]
# Show filtered data
st.write("### Financial Overview (Filtered)")
st.dataframe(filtered_data)
# Plot Revenue & Expenses
fig, ax = plt.subplots()
ax.plot(filtered_data["Date"], filtered_data["Revenue ($M)"], label="Revenue", marker="o")
ax.plot(filtered_data["Date"], filtered_data["Expenses ($M)"], label="Expenses", marker="s")
ax.set_title("Revenue & Expenses Over Time")
ax.set_xlabel("Date")
ax.set_ylabel("Amount ($M)")
ax.legend()
st.pyplot(fig)
# Key Metrics
st.write("### Key Metrics")
st.metric("Total Revenue ($M)", f"{filtered_data['Revenue ($M)'].sum():,.2f}")
st.metric("Total Expenses ($M)", f"{filtered_data['Expenses ($M)'].sum():,.2f}")
st.metric("Total Profit ($M)", f"{filtered_data['Profit ($M)'].sum():,.2f}")
