import plotly.graph_objects as go
from constants import MORAL_VALUES


def dot_plot_results():
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=[72, 67, 73, 80, 76, 79],
            y=MORAL_VALUES,
            marker=dict(color="crimson", size=12),
            mode="lines+markers",
            name="GPT-4o",
            error_x=dict(
                type='data',
                symmetric=False,
                array=[0.1, 0.2, 0.1, 0.1],
                arrayminus=[0.2, 0.4, 1, 0.2])
        )
    )

    fig.add_trace(
        go.Scatter(
            x=[92, 94, 100, 107, 112, 114],
            y=MORAL_VALUES,
            marker=dict(color="gold", size=12),
            mode="lines+markers",
            name="GPT-3.5",
            error_x=dict(
                type='data',
                symmetric=False,
                array=[0.1, 0.2, 0.1, 0.1],
                arrayminus=[0.2, 0.4, 1, 0.2])
        )
    )

    fig.update_layout(
        title="GPT value preferences",
        xaxis_title="Percentage of questions chosen",
        yaxis_title="Moral values",
        xaxis=dict(
            showgrid=False,
        )
    )

    fig.show()
