import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#loading/grabing  data/reading from csv file and plot
data = pd.read_csv("Lab2_ecg.csv")
t = data["t"]
lead_I = data["lead_I"]

plt.plot(t, lead_I)
plt.xlabel("Time")
plt.ylabel("Lead I")
plt.title("Original ECG Signal")
plt.show()

# 4.3.2 Remove anomalies (subset)
clean_data = data.iloc[1000:].reset_index(drop=True)#start from index 1000 and on / change indexing 

# 4.3.6 Baseline (DC) removal and plot
mean_val = np.mean(clean_data["lead_I"])
dc_removed = clean_data["lead_I"] - mean_val

plt.plot(clean_data["t"], dc_removed)
plt.xlabel("Time")
plt.ylabel("Lead I (DC Removed)")
plt.title("ECG After DC Removal")
plt.show()

#smoothing signal and pllot
window_size = 7# kinda in the middle not to high not too low 
smoothed = np.convolve(
    dc_removed,
    np.ones(window_size) / window_size,
    mode='same'
)

plt.plot(clean_data["t"], smoothed)
plt.xlabel("Time")
plt.ylabel("Lead I (Smoothed)")
plt.title("Smoothed ECG Signal")
plt.show()

# 500 point of the smooth signal analysis
plt.plot(clean_data["t"][:500], dc_removed[:500], label="Original")
plt.plot(clean_data["t"][:500], smoothed[:500], label="Smoothed")
plt.xlabel("Time")
plt.ylabel("Lead I")
plt.title("ECG Segment Comparison")
plt.legend()
plt.show()

#saving data into a new file
processed = pd.DataFrame({
    "t": clean_data["t"],
    "lead_I": smoothed
})

processed.to_csv("processd_ecg.csv", index=False)
