import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.manifold import MDS
from scipy.spatial.distance import pdist, squareform

print("Loading data...")
# 1. Load the data
df = pd.read_excel("SampleAbundance1.xlsx", engine="openpyxl")
groups = df['Groups (assigned)']
X = df.drop(columns=['Groups (assigned)'])

# 2. Filter out the noise (rare bacteria)
# We only keep bacteria that are present in at least 5% of the samples
# This removes the rare taxa that were drowning out the biological signal
min_prevalence = 0.05
X_filtered = X.loc[:, (X > 0).mean() >= min_prevalence]
print(f"Kept {X_filtered.shape[1]} out of {X.shape[1]} bacteria after filtering for prevalence.")

# 3. Calculate Bray-Curtis Distance Matrix
print("Calculating Bray-Curtis distances...")
# pdist calculates pairwise distances. 'braycurtis' is built into scipy.
bray_curtis_dist = pdist(X_filtered, metric='braycurtis')
# Convert the condensed distance array to a square matrix
bray_curtis_matrix = squareform(bray_curtis_dist)

# 4. Run PCoA (Using MDS with precomputed distances)
print("Running PCoA...")
# MDS (Multidimensional Scaling) is the algorithm used for PCoA
mds = MDS(n_components=2, dissimilarity='precomputed', random_state=42, n_init=1, max_iter=300)
X_pcoa = mds.fit_transform(bray_curtis_matrix)

# 5. Plot the results
plt.figure(figsize=(10, 8))
sns.scatterplot(x=X_pcoa[:, 0], y=X_pcoa[:, 1], hue=groups, palette='Set1', alpha=0.5, s=15)
plt.title('Beta Diversity: Bray-Curtis PCoA')
plt.xlabel('PCoA 1')
plt.ylabel('PCoA 2')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig("bray_curtis_pcoa.png")
print("Saved bray_curtis_pcoa.png")
