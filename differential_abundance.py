import pandas as pd
import numpy as np
from scipy.stats import mannwhitneyu
from statsmodels.stats.multitest import multipletests

print("Loading data...")
df = pd.read_excel("SampleAbundance1.xlsx", engine="openpyxl")

# Split into BV_only and Never_Diagnosed
bv = df[df['Groups (assigned)'] == 'BV_only'].drop(columns=['Groups (assigned)'])
healthy = df[df['Groups (assigned)'] == 'Never_Diagnosed'].drop(columns=['Groups (assigned)'])

print(f"Comparing {len(bv)} BV patients vs {len(healthy)} Healthy patients...")

results = []
# Run the test for every bacterium
for bacteria in bv.columns:
    # Get the abundance values for this bacteria
    bv_vals = bv[bacteria]
    healthy_vals = healthy[bacteria]
    
    # Run Mann-Whitney U test
    stat, p_val = mannwhitneyu(bv_vals, healthy_vals, alternative='two-sided')
    
    # Calculate mean abundance for effect size direction
    mean_bv = bv_vals.mean()
    mean_healthy = healthy_vals.mean()
    
    results.append({
        'Bacteria': bacteria,
        'Mean_BV': mean_bv,
        'Mean_Healthy': mean_healthy,
        'P_value': p_val
    })

# Create dataframe and correct for multiple testing (FDR)
res_df = pd.DataFrame(results)
res_df['FDR_P_value'] = multipletests(res_df['P_value'], method='fdr_bh')[1]

# Sort by most significant
res_df = res_df.sort_values(by='FDR_P_value')

# Show top 10 bacteria significantly enriched in BV
print("\n--- TOP 10 BACTERIA ENRICHED IN BV ---")
top_bv = res_df[res_df['Mean_BV'] > res_df['Mean_Healthy']].head(10)
print(top_bv[['Bacteria', 'Mean_BV', 'Mean_Healthy', 'FDR_P_value']])

# Show top 10 bacteria significantly enriched in Healthy
print("\n--- TOP 10 BACTERIA ENRICHED IN HEALTHY ---")
top_healthy = res_df[res_df['Mean_Healthy'] > res_df['Mean_BV']].head(10)
print(top_healthy[['Bacteria', 'Mean_Healthy', 'Mean_BV', 'FDR_P_value']])

