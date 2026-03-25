#Bharat mata ki jai
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Smart Village Insights", layout="centered")

st.title("Smart Village Insights")
st.write("Enter your own values for Electricity Cuts, Water Usage, and Crop Yield. Graphs update live!")


# Section 1: Electricity Cuts

st.header("Electricity Cut Analysis")

days_elec = st.number_input("How many days of electricity cut data?", min_value=1, max_value=30, value=7)

elec_values = []
for day in range(1, days_elec+1):
    val = st.number_input(f"Day {day} (hours without power)", min_value=0, max_value=24, value=0, key=f"elec{day}")
    elec_values.append(val)

df = pd.DataFrame({"Day": list(range(1, days_elec+1)), "Electricity_Cut_Hours": elec_values})

fig1, ax1 = plt.subplots(figsize=(8,4))
ax1.plot(df["Day"], df["Electricity_Cut_Hours"], marker='o', color='red')
ax1.set_title("Daily Electricity Cut Hours")
ax1.set_xlabel("Day")
ax1.set_ylabel("Hours Without Power")
ax1.grid(True)
st.pyplot(fig1)


# Section 2: Water Usage

st.header("Water Usage vs Wastage")

days_water = st.number_input("How many days of water data?", min_value=1, max_value=15, value=5)

water_used, water_wasted = [], []
for day in range(1, days_water+1):
    used = st.number_input(f"Day {day} - Water Used (L)", min_value=0, value=0, key=f"used{day}")
    wasted = st.number_input(f"Day {day} - Water Wasted (L)", min_value=0, value=0, key=f"wasted{day}")
    water_used.append(used)
    water_wasted.append(wasted)

water_df = pd.DataFrame({"Day": list(range(1, days_water+1)), "Water_Used": water_used, "Water_Wasted": water_wasted})

fig2, ax2 = plt.subplots(figsize=(8,4))
water_df.plot(x="Day", y=["Water_Used", "Water_Wasted"], kind="bar", ax=ax2)
ax2.set_title("Water Usage vs Wastage")
ax2.set_xlabel("Day")
ax2.set_ylabel("Liters")
st.pyplot(fig2)


# Section 3: Crop Yield

st.header("Rainfall vs Crop Yield")

entries_crop = st.number_input("How many crop data points?", min_value=1, max_value=10, value=5)

rainfall, yield_list = [], []
for i in range(entries_crop):
    rain = st.number_input(f"Entry {i+1} - Rainfall (mm)", min_value=0, value=0, key=f"rain{i}")
    yield_val = st.number_input(f"Entry {i+1} - Crop Yield (quintals/acre)", min_value=0, value=0, key=f"yield{i}")
    rainfall.append(rain)
    yield_list.append(yield_val)

crop_df = pd.DataFrame({"Rainfall (mm)": rainfall, "Crop_Yield (quintals/acre)": yield_list})

fig3, ax3 = plt.subplots(figsize=(8,4))
ax3.plot(crop_df["Rainfall (mm)"], crop_df["Crop_Yield (quintals/acre)"], marker='o', color='green')
ax3.set_title("Rainfall vs Crop Yield")
ax3.set_xlabel("Rainfall (mm)")
ax3.set_ylabel("Yield (quintals/acre)")
ax3.grid(True)
st.pyplot(fig3)

st.success("Dashboard ready! All values are entered directly by the user.")
