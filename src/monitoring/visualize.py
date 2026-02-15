"""
visualize.py — Visualization module.
"""

import plotly.graph_objects as go
from plotly.subplots import make_subplots

def plot_batch_monitoring(df, batch_id):
    batch_col = "Batch reference(Batch_ref:Batch ref)"
    batch_data = df[df[batch_col] == batch_id]
    
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True)
    fig.add_trace(go.Scatter(x=batch_data["Time (h)"], y=batch_data["Temperature(T:K)"], name="Temp"), row=1, col=1)
    fig.add_trace(go.Scatter(x=batch_data["Time (h)"], y=batch_data["pH(pH:pH)"], name="pH"), row=2, col=1)
    
    return fig
