from pathlib import Path

import seaborn as sns
from matplotlib import pyplot as plt

figures_dir = Path("../reports/figures")
figures_dir.mkdir(parents=True, exist_ok=True)

def save_fig(figure_name, save_dir=None):
    """
    :param figure_name: string
    :param save_dir: string or Path
    :return: saved figure
    """

    if save_dir is None:
        save_dir = Path.cwd()

    save_dir = Path(save_dir)
    save_dir.mkdir(parents=True, exist_ok=True)

    plt.savefig(
        save_dir / figure_name,
        dpi=300,
        bbox_inches="tight"
    )


def plot_age_distribution(data):
    plt.figure(figsize=(8, 5))

    mean_age = data["age"].mean()
    median_age = data["age"].median()
    mode_age = data["age"].mode().iloc[0]

    plt.hist(data["age"], bins=15, edgecolor="white")

    plt.axvline(mean_age, color="r", linestyle="--", label="Mean value [age]")
    plt.axvline(median_age, color="y", linestyle="--", label="Median value [age]")
    plt.axvline(mode_age, color="b", linestyle="--", label="Mode value [age]")

    plt.title("Distribution of Player Age")
    plt.xlabel("Age")
    plt.ylabel("Count")
    plt.legend()

    plt.savefig(
        figures_dir / "player_age_distribution.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()

def height_distribution(data):
    plt.figure(figsize=(8, 5))
    mean_height = data['height_cm'].mean()

    plt.hist(data['height_cm'], bins=10, edgecolor='white')
    plt.axvline(mean_height, color='r', linestyle='--', label='Mean value [height]')

    plt.xlabel('Height [cm]')
    plt.ylabel('Count')
    plt.title('Height [cm] distribution')
    plt.legend()

    plt.savefig(
    figures_dir / "height_distribution.png",
        dpi=300,
        bbox_inches="tight"
    )
    plt.show()

def weight_distribution(data):
    plt.figure(figsize=(8, 5))

    # Calculate the mean value of the players weight
    mean_height = data['weight_kgs'].mean()

    # Plot a histogram showing the distribution of players weight
    plt.hist(data['weight_kgs'], bins=10, edgecolor='white')

    plt.axvline(
        mean_height,
        color='r',
        linestyle='--',
        label='Mean value [weight_kgs]'
    )

    plt.xlabel('weight [kgs]')
    plt.ylabel('Count')
    plt.title('Weight [kgs] distribution')
    plt.legend()

    plt.savefig(
        figures_dir / "weight_distribution.png",
        dpi=300,
        bbox_inches="tight"
    )
    plt.show()

def football_countries(data):
    # Get the top 10 nationalities by number of players
    top_10_football_countries = data['nationality'].value_counts().head(10)
    plt.figure(figsize=(10, 5))

    plt.bar(
        top_10_football_countries.index,
        top_10_football_countries.values
    )

    plt.xlabel('Nationality')
    plt.ylabel('Number of players')
    plt.title('Top 10 football countries by number of players')
    plt.xticks(rotation=90)

    plt.savefig(
        figures_dir / "football_countries_distribution.png",
        dpi=300,
        bbox_inches="tight"
    )
    plt.show()


def show_correlation_matrix(correlation_matrix, corr_method, figure_name=None, save_dir=None):
    """
    :param corr_method: string
    :param correlation_matrix: dataframe
    :param figure_name: string
    :param save_dir: string or Path
    :return: correlation matrix
    """

    plt.figure(figsize=(18, 16))
    plt.rcParams.update({'font.size': 10})

    sns.heatmap(
        correlation_matrix,
        cmap='viridis',
        vmin=-1,
        vmax=1,
        center=0,
        annot=True,
        fmt=".2f",
        square=True,
        linewidths=.5
    )

    plt.title(f'Correlation matrix  / {figure_name} / {corr_method}')

    if figure_name:
        save_fig(figure_name, save_dir=save_dir)

    plt.show()























