import matplotlib.pyplot as plt
import pandas as pd

# 1. Chargement des données
df = pd.read_csv("dataset.csv")

# 2. Sélection des catégories clés
categories = ["Global", "Urbain", "Femmes", "15-24 ans", "Diplômés"]
df_filtered = df[df["Sous_Categorie"].isin(categories)]

# 3. Génération du graphique
x = range(len(df_filtered))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))
rects1 = ax.bar(
    [i - width / 2 for i in x],
    df_filtered["Taux_2024"],
    width,
    label="2024",
    color="#3498db",
)
rects2 = ax.bar(
    [i + width / 2 for i in x],
    df_filtered["Taux_2025"],
    width,
    label="2025",
    color="#e74c3c",
)

ax.set_ylabel("Taux de chômage (%)")
ax.set_title("Évolution du taux de chômage au Maroc (2024-2025)")
ax.set_xticks(list(x))
ax.set_xticklabels(df_filtered["Sous_Categorie"])
ax.legend()
ax.grid(axis="y", linestyle="--", alpha=0.7)


def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(
            f"{height}%",
            xy=(rect.get_x() + rect.get_width() / 2, height),
            xytext=(0, 3),
            textcoords="offset points",
            ha="center",
            va="bottom",
        )


autolabel(rects1)
autolabel(rects2)

plt.tight_layout()
plt.savefig("chomage_maroc.png")
plt.show()
