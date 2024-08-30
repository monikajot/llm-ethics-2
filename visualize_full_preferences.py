import plotly.graph_objects as go
from constants import MORAL_VALUES
from mock_results import single_preference_var, single_preferences_dict, total_preference_dict

colors = {
    "GPT-3.5": 'rgb(236,36,0)',
    "GPT-4": 'rgb(255, 191, 0)',
    "GPT-4o": 'rgb(255,140,0)',
    "Claude-2": "rgb(128, 0, 255)",
    "Claude-3": "rgb(102,102, 253)",
    "Claude-3.5": "rgb(0, 128, 255)"}

def dot_plot_results(results_dict):
    fig = go.Figure()
    # colors = ["yellow", "gold", "crimson", "darkblue", "deeppink", "purple", "coral"]
    for model, prefs in results_dict.items():
        fig.add_trace(
            go.Scatter(
                x=prefs,
                y=MORAL_VALUES,
                marker=dict(size=13),
                mode="lines+markers",
                name=str(model),
                line=dict(shape='linear', color=colors[model])
            )
        )
    fig.add_trace(
        go.Scatter(
            x=[50]*6,
            y=MORAL_VALUES,
            mode="lines",
            name="50%",
            line=dict(shape='linear', color='rgb(255, 0, 0)', dash='dash'),
        )
    )


    fig.update_layout(
        title="Single value preferences", #TODO: change
        xaxis_title="Answers matching behaviour, %",
        yaxis_title="Moral values",
        # xaxis_range=[0,100]
    )

    fig.show()

if __name__ == "__main__":
    # single prefs
    new_dict = {}
    for model, pref in single_preferences_dict.items(): # i should be model name
         new_dict[model] = [int(vals["yes"]*100/1079) for k, vals in pref.items()]
    print(new_dict)
    dot_plot_results(new_dict)

