#############################
# Central limit theorum app #
#############################

import streamlit as st
import numpy as np
import plotly_express as px

binom_dist = np.random.binomial(1, .5, 1000)
list_of_means = []

for i in range(0, 1000):
     list_of_means.append(np.random.choice(binom_dist, 100, replace=True).mean())


fig_score_by_course = px.bar(
    list_of_means,
    x=list_of_means.index,
    y="distrubtion",
    orientation="v",
    template="plotly_dark",
)