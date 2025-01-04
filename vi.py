import matplotlib.pyplot as plt
import numpy as np

# Data for V-I characteristics
voltage_forward = np.linspace(0, 1, 100)  # Forward bias (0 to 1V)
current_forward = np.exp(40 * (voltage_forward - 0.7))  # Exponential increase after 0.7V
current_forward[current_forward < 0] = 0  # Clamp current below threshold

voltage_reverse = np.linspace(-1, 0, 100)  # Reverse bias (-1 to 0V)
current_reverse = -1e-6 * np.ones_like(voltage_reverse)  # Small leakage current
breakdown_voltage = -0.8  # Breakdown at -0.8V
current_breakdown = np.linspace(-1e-6, -0.01, 100)  # Current during breakdown

# Zener diode in reverse
voltage_reverse_zener = np.linspace(-2, 0, 100)  # Wider reverse range
current_reverse_zener = np.piecewise(
    voltage_reverse_zener,
    [voltage_reverse_zener > -1.2, voltage_reverse_zener <= -1.2],
    [lambda v: -1e-6, lambda v: -10 * (v + 1.2)],
)

# Plot
plt.figure(figsize=(10, 6))

# PN Junction Diode Characteristics
plt.plot(voltage_forward, current_forward, label="PN Junction Diode (Forward Bias)", color="blue")
plt.plot(voltage_reverse, current_reverse, label="PN Junction Diode (Reverse Bias)", color="red")
plt.plot([breakdown_voltage], [-0.01], "ro", label="Breakdown Point (PN Diode)")

# Zener Diode Characteristics
plt.plot(voltage_reverse_zener, current_reverse_zener, label="Zener Diode (Reverse Bias)", color="green")

# Labels and legend
plt.axhline(0, color="black", linewidth=0.5, linestyle="--")
plt.axvline(0, color="black", linewidth=0.5, linestyle="--")
plt.title("V-I Characteristics of PN Junction and Zener Diodes", fontsize=14)
plt.xlabel("Voltage (V)", fontsize=12)
plt.ylabel("Current (A)", fontsize=12)  # Ensure consistent labeling
plt.legend(fontsize=10, loc='upper left')
plt.grid(alpha=0.3)

plt.tight_layout()
plt.show()
import matplotlib.pyplot as plt
import numpy as np

# Data for V-I characteristics
voltage_forward = np.linspace(0, 1, 100)  # Forward bias (0 to 1V)
current_forward = np.exp(40 * (voltage_forward - 0.7))  # Exponential increase after 0.7V
current_forward[current_forward < 0] = 0  # Clamp current below threshold

voltage_reverse = np.linspace(-1, 0, 100)  # Reverse bias (-1 to 0V)
current_reverse = -1e-6 * np.ones_like(voltage_reverse)  # Small leakage current
breakdown_voltage = -0.8  # Breakdown at -0.8V
current_breakdown = np.linspace(-1e-6, -0.01, 100)  # Current during breakdown

# Zener diode in reverse
voltage_reverse_zener = np.linspace(-2, 0, 100)  # Wider reverse range
current_reverse_zener = np.piecewise(
    voltage_reverse_zener,
    [voltage_reverse_zener > -1.2, voltage_reverse_zener <= -1.2],
    [lambda v: -1e-6, lambda v: -10 * (v + 1.2)],
)

# Plot
plt.figure(figsize=(10, 6))

# PN Junction Diode Characteristics
plt.plot(voltage_forward, current_forward, label="PN Junction Diode (Forward Bias)", color="blue")
plt.plot(voltage_reverse, current_reverse, label="PN Junction Diode (Reverse Bias)", color="red")
plt.plot([breakdown_voltage], [-0.01], "ro", label="Breakdown Point (PN Diode)")

# Zener Diode Characteristics
plt.plot(voltage_reverse_zener, current_reverse_zener, label="Zener Diode (Reverse Bias)", color="green")

# Labels and legend
plt.axhline(0, color="black", linewidth=0.5, linestyle="--")
plt.axvline(0, color="black", linewidth=0.5, linestyle="--")
plt.title("V-I Characteristics of PN Junction and Zener Diodes", fontsize=14)
plt.xlabel("Voltage (V)", fontsize=12)
plt.ylabel("Current (A)", fontsize=12)  # Ensure consistent labeling
plt.legend(fontsize=10, loc='upper left')
plt.grid(alpha=0.3)

plt.tight_layout()
plt.show()
