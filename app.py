import streamlit as st
import pandas as pd
import altair as alt
from entry import Entry

if "entries" not in st.session_state:
    st.session_state["entries"] = []
    # st.session_state.entries = [] # also works

entries = st.session_state.entries

name = st.text_input("Enter your name: ")
amount = st.number_input("Enter an amount: ")
type = st.selectbox("Choose the type:", ["Income", "Expense"])
category = st.selectbox("Choose a category:", ["Food", "Rent",
                        "Utilities", "Payment", "Misc"])

if st.button("Add Entry"):
    new_entry = Entry(name, amount, type, category)
    st.session_state.entries.append(new_entry)

if entries:
    st.dataframe([{
        "Name": e.name,
        "Amount": e.amount,
        "Type": e.type,
        "Category": e.category
    } for e in entries])

total_income = 0
total_expenses = 0

category_totals = {}

for entry in entries:
    if (entry.get_type() == "Income"):
        total_income += entry.get_amount()
    else:
        total_expenses += entry.get_amount()

        if entry.get_category() in category_totals:
            category_totals[entry.get_category()] += entry.get_amount()
        else:
            category_totals[entry.get_category()] = entry.get_amount()

net_balance = total_income - total_expenses

if st.button("Clear all"):
    st.session_state.entries.clear()

df = pd.DataFrame({
    "Category": list(category_totals.keys()),
    "Amount": list(category_totals.values())
})

chart = alt.Chart(df).mark_bar().encode(
    x = "Category",
    y = "Amount",
    color = "Category"
)

st.altair_chart(chart, use_container_width = True)