import logging
import numpy as np

import plotly
import plotly.plotly as py
import plotly.graph_objs as go

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def simple_line_chart():
    
    N = 500
    random_x = np.linspace(0, 1, N)
    random_y = np.random.randn(N)

    # Create a trace
    trace = go.Scatter(
        x = random_x,
        y = random_y
    )

    data = [trace]

    plotly.offline.plot(data, filename='basic-line')