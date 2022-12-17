#############################
# Central limit theorum app #
#############################

import streamlit as st
import numpy as np

st.set_page_config(page_title="Central Limit Theorum",
                    page_icon=":bar_chart:",
                    layout="wide"
                    )


binom_dist = np.random.binomial(1, .5, 100)
st.write(np.mean(binom_dist))