#############################
# Central limit theorum app #
#############################

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

#Create variable assigning the values of binomial distribution
binom_dist = np.random.binomial(1, .5, 1000)
list_of_means = []

#Loop through the coin toss 1000 times and store the mean in the list_of_means variable
for i in range(0, 1000):
     list_of_means.append(np.random.choice(binom_dist, 100, replace=True).mean())


#Create variable to store the bar chart and within that call the list_of_means variable data to be displayed
fig1, ax1 = plt.subplots()
ax1 = plt.hist(list_of_means)
st.pyplot(fig1)

#Create a second variable to store the the 1's and call the list to be displayed as a bar chart
fig2, ax2 = plt.subplots()
ax2 = plt.hist([1,1,1,1])
st.pyplot(fig2)