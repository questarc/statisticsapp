import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from utils.calculators import calculate_statistics
from utils.charts import plot_chart
from utils.explanations import get_explanations

st.title('Statistics Learning App for 10th Graders')

option = st.sidebar.selectbox('Choose a topic or tool:', ['Introduction', 'Concepts', 'Calculators', 'Charts'])

if option == 'Introduction':
    st.header('Welcome to Statistics!')
    st.write('Statistics is the science of collecting, analyzing, and interpreting data. It helps us understand the world by making sense of numbers.')

elif option == 'Concepts':
    st.header('Key Statistics Concepts')
    explanations = get_explanations()
    for concept, desc in explanations.items():
        st.markdown(f'**{concept}:** {desc}')

elif option == 'Calculators':
    st.header('Statistics Formula Calculators')
    data_input = st.text_area('Enter numbers separated by commas:', '1, 2, 3, 4, 5')
    try:
        data = np.array([float(x.strip()) for x in data_input.split(',')])
        if len(data) == 0:
            st.warning('Please enter at least one number.')
        else:
            stats = calculate_statistics(data)
            for key, value in stats.items():
                st.write(f'{key}: {value}')
    except Exception:
        st.error('Invalid input. Please enter numbers separated by commas.')

elif option == 'Charts':
    st.header('Visualize Your Data')
    data_input = st.text_area('Enter numbers separated by commas:', '1, 2, 3, 4, 5')
    chart_type = st.selectbox('Select chart type:', ['Histogram', 'Box Plot', 'Scatter Plot'])
    try:
        data = np.array([float(x.strip()) for x in data_input.split(',')])
        if len(data) == 0:
            st.warning('Please enter at least one number.')
        else:
            fig = plot_chart(data, chart_type)
            st.pyplot(fig)
    except Exception:
        st.error('Invalid input. Please enter numbers separated by commas.')
