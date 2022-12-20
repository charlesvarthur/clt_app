#############################
# Central limit theorum app #
#############################

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title('Illustrating Central Limit Theorum with Streamlit')
st.subheader('An App by Charles Arthur')

st.write(('This app simulates a thousand coin flips using the chance of heads input below,'
' and then samples with replacement from that population and plots the historgram of the ' 
'mean of the samples, in order to illustratge the Central Limit Theorem!'))

#Allows user input to set the probability of each value
perc_heads = st.number_input(label = ' Chance of a Coin Landing on Heads', min_value = 0.0, max_value = 1.0, value = .5)

#Add a graph title with user input
graph_title = st.text_input(label = 'Graph Title')

#Create variable assigning the values of binomial distribution
binom_dist = np.random.binomial(1, perc_heads, 1000)
list_of_means = []

#Loop through the coin toss 1000 times and store the mean in the list_of_means variable
for i in range(0, 1000):
     list_of_means.append(np.random.choice(binom_dist, 100, replace=True).mean())


#Create variable to store the bar chart and within that call the list_of_means variable data to be displayed
fig1, ax1 = plt.subplots()
ax1 = plt.hist(list_of_means, range=[0,1])
plt.title(graph_title)
st.pyplot(fig1)

#Create a second variable to store the the 1's and call the list to be displayed as a bar chart
fig2, ax2 = plt.subplots()
ax2 = plt.hist([1,1,1,1])
st.pyplot(fig2)