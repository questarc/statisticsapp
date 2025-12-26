import matplotlib.pyplot as plt

def plot_chart(data, chart_type):
    fig, ax = plt.subplots()
    if chart_type == 'Histogram':
        ax.hist(data, bins='auto', color='skyblue', edgecolor='black')
        ax.set_title('Histogram')
    elif chart_type == 'Box Plot':
        ax.boxplot(data, vert=False)
        ax.set_title('Box Plot')
    elif chart_type == 'Scatter Plot':
        ax.scatter(range(len(data)), data, color='green')
        ax.set_title('Scatter Plot')
        ax.set_xlabel('Index')
        ax.set_ylabel('Value')
    return fig
