import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import kruskal
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

print("Loading data...")
# 1. Load the data
df = pd.read_excel("SampleAbundance1.xlsx", engine="openpyxl")

# 2. Separate groups and bacteria
groups = df['Groups (assigned)']
X = df.drop(columns=['Groups (assigned)'])
X.columns = X.columns.str.replace(r'[\[\]<]', '', regex=True) # Clean names

# --- ALPHA DIVERSITY ---
print("Calculating Alpha Diversity...")
# We calculate the Shannon Diversity Index (a standard measure of diversity)
# We add a tiny number (1e-9) to avoid errors with zero values
shannon_diversity = -np.sum(X * np.log(X + 1e-9), axis=1)
df['Shannon_Diversity'] = shannon_diversity

# Plot Alpha Diversity
plt.figure(figsize=(10, 6))
sns.boxplot(x='Groups (assigned)', y='Shannon_Diversity', data=df)
plt.title('Alpha Diversity (Shannon Index) by Infection Group')
plt.ylabel('Shannon Diversity')
plt.xlabel('Group')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("alpha_diversity.png")
print("Saved alpha_diversity.png")

# --- BETA DIVERSITY (PCA) ---
print("Calculating Beta Diversity (PCA)...")
# Scale the data and run PCA to see if groups separate
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Plot PCA
plt.figure(figsize=(10, 8))
sns.scatterplot(x=X_pca[:, 0], y=X_pca[:, 1], hue=groups, palette='Set1', alpha=0.5, s=10)
plt.title('Beta Diversity: PCA of Bacterial Communities')
plt.xlabel(f'PC1 ({pca.explained_variance_ratio_[0]*100:.1f}% variance)')
plt.ylabel(f'PC2 ({pca.explained_variance_ratio_[1]*100:.1f}% variance)')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig("beta_diversity_pca.png")
print("Saved beta_diversity_pca.png")
