import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

#st.set_page_config(layout="wide")

st.title("Vector Addition Visualizer")

st.sidebar.header("Vector Properties")

# Sliders for vector magnitudes
magnitude1 = st.sidebar.slider("Magnitude of Vector 1 (V1)", 0.0, 10.0, 5.0, 0.1)
magnitude2 = st.sidebar.slider("Magnitude of Vector 2 (V2)", 0.0, 10.0, 3.0, 0.1)

# Slider for the angle between vectors
angle_degrees = st.sidebar.slider("Angle Between Vectors (degrees)", 0, 360, 45, 1)
angle_radians = np.deg2rad(angle_degrees)

# Define the two vectors
# Vector 1 is always along the x-axis for simplicity
v1 = np.array([magnitude1, 0])

# Vector 2 is defined by its magnitude and the angle
v2 = np.array([magnitude2 * np.cos(angle_radians), magnitude2 * np.sin(angle_radians)])

# Calculate the resultant vector
resultant_vector = v1 + v2

# Calculate the magnitude of the resultant vector
resultant_magnitude = np.linalg.norm(resultant_vector)

# Calculate the angle of the resultant vector
resultant_angle_radians = np.arctan2(resultant_vector[1], resultant_vector[0])
resultant_angle_degrees = np.rad2deg(resultant_angle_radians)


# Display the results
st.header("Resultant Vector")
col1, col2 = st.columns(2)
with col1:
    st.metric("Magnitude", f"{resultant_magnitude:.2f}")
with col2:
    st.metric("Angle (degrees)", f"{resultant_angle_degrees:.2f}°")


# Plotting the vectors
st.header("Vector Visualization")
fig, ax = plt.subplots(figsize=(8, 8))

# Plot Vector 1
ax.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='r', label=f'V1 ({magnitude1:.1f})')

# Plot Vector 2
ax.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='b', label=f'V2 ({magnitude2:.1f})')

# Plot Resultant Vector
ax.quiver(0, 0, resultant_vector[0], resultant_vector[1], angles='xy', scale_units='xy', scale=1, color='g', label=f'Resultant ({resultant_magnitude:.2f})')

# Plot the parallelogram for visualization
ax.plot([v1[0], resultant_vector[0]], [v1[1], resultant_vector[1]], 'b--')
ax.plot([v2[0], resultant_vector[0]], [v2[1], resultant_vector[1]], 'r--')


# Set plot limits
#max_val = max(magnitude1 + abs(v2[0]), magnitude2 + abs(v1[0]), abs(v2[1])) * 1.2
max_val = 20
ax.set_xlim(-max_val, max_val)
ax.set_ylim(-max_val, max_val)
ax.set_aspect('equal', adjustable='box')
ax.grid(True)
ax.axhline(0, color='black',linewidth=0.5)
ax.axvline(0, color='black',linewidth=0.5)
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_title("Vectors and their Resultant")
ax.legend()

st.pyplot(fig)

st.info(
    """
    **How to Use:**
    1.  Use the sliders in the sidebar to adjust the magnitudes of the two vectors (V1 and V2).
    2.  Use the angle slider to change the angle between V1 and V2.
    3.  The plot will update automatically to show the vectors and their resultant.
    4.  The magnitude and angle of the resultant vector are displayed above the plot.
    """
)
