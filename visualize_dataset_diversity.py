import pandas as pd
import json
from openai import OpenAI
import numpy as np
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans

import plotly.express as px
from mock_results import dataset_embeds
import matplotlib.pyplot as plt
from pprint import PrettyPrinter
import ast
from functions import query_model


def format_hover_text(text):
    formatted_text = ""
    n = len(text) // 200
    for i in range(n):
        formatted_text += text[i * 200 : (i + 1) * 200] + "<br>"
    formatted_text += text[n * 200 :]
    return formatted_text


def get_embeddings(scenarios, outfile):
    client = OpenAI()
    embeds = []
    for i in range(len(scenarios)):
        response = client.embeddings.create(
            input=scenarios[i], model="text-embedding-3-small"
        )
        embeds.append(response.data[0].embedding)
        print(response.data[0].embedding)

    X = np.array(embeds)
    np.save(file=f"numpy_embeddings_{outfile}.npy", arr=X)
    return np.array(embeds)


def run_tsne_plots(file, X=dataset_embeds, n_clusters=3):
    data = pd.read_csv(file)
    N = len(data)
    scenarios = data["responses"][:N]
    if X is None:
        X = get_embeddings(scenarios, file[:-4])

    X_embedded = TSNE(
        n_components=2, learning_rate="auto", init="random", perplexity=3
    ).fit_transform(X)

    new_scenarios = []
    for scenario in scenarios:
        # scenario  = json.loads(scenario)
        hover_text = format_hover_text(scenario)
        new_scenarios.append(hover_text)
    new_scenarios = pd.Series(new_scenarios)

    df = pd.DataFrame(X_embedded, columns=["TSNE1", "TSNE2"])
    df["labels"] = new_scenarios
    # # Initialize the KMeans model
    if n_clusters > 1:
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        #
        # # Fit and predict the clusters
        df["cluster"] = kmeans.fit_predict(df[["TSNE1", "TSNE2"]])
        keywords = [""] * len(df)

        if X is None:
            df.to_csv(f"df_embeddings_{file}.csv")

        for i in range(n_clusters):
            cluster_values = df[df["cluster"] == i]["labels"].values
            scenarios = []
            for val in cluster_values:
                try:
                    scenarios.append(json.loads(val)["scenario"])
                except json.decoder.JSONDecodeError:
                    continue
            prompt = f"The following text is a list of Moral Foundations Theory moral dilemma scenarios with 6 options representing 6 moral foundation. Summarize the moral dilemma text in 5 unique keywords that best describe its contents and output format is 'word, word, word, word, word'. The words must represent the text itself and not the format or the moral values. \n\n {scenarios}"
            response = query_model(model="gpt-4o-mini", message=prompt, system="")
            keywords[df[df["cluster"] == i].index[0]] = response
            a=1
        df["keywords"] = keywords
        # Step 4: Visualize with Plotly
        fig = px.scatter(
            df,
            x="TSNE1",
            y="TSNE2",
            hover_name="labels",
            color="cluster",
            labels={"cluster": "Cluster"},
            color_continuous_scale=px.colors.qualitative.Set1,
            text="keywords"
        )
    else:
        # Step 4: Visualize with Plotly
        fig = px.scatter(
            df,
            x="TSNE1",
            y="TSNE2",
            hover_name="labels",
        )
    fig.show()


def find_best_k_means(data):
    # Define the range of k values to try
    k_values = range(1, 11)

    # List to store the inertia (WCSS) values
    inertia_values = []

    # Run K-means for each k value and store the inertia
    for k in k_values:
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(data)
        inertia_values.append(kmeans.inertia_)

    # Plot the Elbow Curve
    plt.figure(figsize=(8, 5))
    plt.plot(k_values, inertia_values, "bo-", markersize=8)
    plt.xlabel("Number of clusters (k)")
    plt.ylabel("Inertia (WCSS)")
    plt.title("Elbow Method For Optimal k")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":

    file = "final_data_27d_21h.csv"
    # file1 = "mft_generated_100_examples_aug_21_gpt4_3.csv"
    # embs = "numpy_embeddings_final_data_27d_16h.npy"
    # X = np.load(embs)

    run_tsne_plots(file=file, X=None, n_clusters=30)
    # run_tsne_plots(file=file1, X=None)
    # with open(f"numpy_embeddings_mft_generated_100_examples_aug_21_gptm.npy", "wb") as f:

    # data = pd.read_csv(file)
    # scenarios = data["responses"]
    # X = get_embeddings(scenarios=scenarios, outfile=file)
    # find_best_k_means(X)
