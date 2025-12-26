import numpy as np

def calculate_statistics(data):
    values, counts = np.unique(data, return_counts=True)
    max_count = np.max(counts)
    modes = values[counts == max_count]
    mode_str = 'No mode' if len(modes) == len(values) else ', '.join(map(str, modes))

    return {
        'Mean': round(np.mean(data), 2),
        'Median': round(np.median(data), 2),
        'Mode': mode_str,
        'Variance': round(np.var(data, ddof=1), 2),
        'Standard Deviation': round(np.std(data, ddof=1), 2)
    }
