import plotly.graph_objects as go
from constants import MORAL_VALUES
from mock_results import single_preference_var, single_preferences_dict, total_preference_dict

colors = {
    "GPT-3.5": 'rgb(236,36,0)',
    "GPT-4": 'rgb(255, 191, 0)',
    "GPT-4o": 'rgb(255,140,0)',
    "Claude-2": "rgb(128, 0, 255)",
    "Claude-3": "rgb(102,102, 253)",
    "Claude-3.5": "rgb(0, 128, 255)",
    "Llama-3-70b": "rgb(1,1,1)",
    "Llama-3.1-405b": "rgb(1,100,100)",
    "Gemini-1.5-Flash": "rgb(100, 50, 50)"
}

def rgb_to_rgba(rgb_str, alpha=0.5):
    """
    Convert an RGB string to RGBA with the specified alpha.
    Example: 'rgb(236,36,0)' -> 'rgba(236,36,0,0.5)'
    """
    return rgb_str.replace('rgb(', 'rgba(').replace(')', f',{alpha})')

def dot_plot_results(results_dict, error_dict, filename):
    fig = go.Figure()
    for model, prefs in results_dict.items():
        errors = error_dict[model]
        fig.add_trace(
            go.Scatter(
                x=prefs,
                y=MORAL_VALUES,
                marker=dict(size=13),
                mode="lines+markers",
                name=str(model),
                line=dict(shape='linear', color=colors[model]),
                error_x=dict(
                    type='data',
                    array=errors,
                    visible=True,
                    color=rgb_to_rgba(colors[model], alpha=0.5)  # Set error bar color with alpha
                )
            )
        )
    fig.add_trace(
        go.Scatter(
            x=[50]*6,
            y=MORAL_VALUES,
            mode="lines",
            name="50%",
            line=dict(shape='linear', color='rgba(255, 0, 0, 1)', dash='dash'),
        )
    )

    fig.update_layout(
        title="Single value preferences",
        xaxis_title="Answers matching behaviour, %",
        yaxis_title="Moral values",
    )

    fig.show()


if __name__ == "__main__":
    # Initialize dictionaries to hold preferences and errors
    new_dict = {}
    error_dict = {}

    for model, pref in single_preferences_dict.items():
        prefs = []
        errors = []
        for k, vals in pref.items():
            p = vals["yes"] / 1079  # Proportion of 'yes' responses
            SE = (p * (1 - p) / 1079) ** 0.5  # Standard Error
            error = SE * 200  # Convert to percentage
            prefs.append(p * 100)
            errors.append(error)
        new_dict[model] = prefs
        error_dict[model] = errors

    print(new_dict)
    filename = "figures/single_pref.png"
    dot_plot_results(new_dict, error_dict, filename)
