import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("📊 Data Visualizer - Tips Dataset Example")

# File uploader
uploaded_file = st.file_uploader("Upload your CSV file (with columns like total_bill, tip, sex, day):", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully!")
    st.write("### Preview of your data")
    st.dataframe(df.head())

    # Check if required columns exist
    required = {"total_bill", "tip", "sex", "day"}
    if not required.issubset(df.columns):
        st.error(f"⚠️ Your file must contain these columns: {required}")
    else:
        # Create the 2x2 plot
        fig, axs = plt.subplots(2, 2, figsize=(12, 6))

        # Plot 1: Histogram of Total Bill
        axs[0, 0].hist(df["total_bill"], bins=10, color="lightblue", edgecolor="black")
        axs[0, 0].set_title("Histogram of Total Bill")
        axs[0, 0].set_xlabel("Total Bill")
        axs[0, 0].set_ylabel("Frequency")

        # Plot 2: Horizontal Boxplot of Tips
        axs[0, 1].boxplot(df["tip"], vert=False)
        axs[0, 1].set_title("Boxplot of Tips")
        axs[0, 1].set_xlabel("Tip Amount")

        # Plot 3: Pie chart of gender distribution
        gender_cnt = df["sex"].value_counts()
        axs[1, 0].pie(gender_cnt, labels=gender_cnt.index, autopct="%1.1f%%", colors=["lightblue", "lightcoral"])
        axs[1, 0].set_title("Pie Chart: Gender Distribution")

        # Plot 4: Bar chart of average bill by day
        day_avg_bill = df.groupby("day")["total_bill"].mean()
        axs[1, 1].bar(day_avg_bill.index, day_avg_bill.values, color="plum", edgecolor="black")
        axs[1, 1].set_title("Bar Plot: Avg Total Bill by Day")
        axs[1, 1].set_xlabel("Day")
        axs[1, 1].set_ylabel("Average Bill")

        plt.tight_layout()
        st.pyplot(fig)
else:
    st.info("📁 Please upload a CSV file to begin.")
