# Vaginal Microbiome Analysis: BV & UTI Signatures

## Overview
Analysis of a large-scale clinical dataset (10,003 women) investigating the vaginal microbiome in patients with Bacterial Vaginosis (BV) and Urinary Tract Infections (UTIs). 

Dataset sourced from the Gilbert Lab (WashU) and Evvy (Zenodo: 22307394).

## Pipeline & Methods
1. **Data Wrangling:** Merged clinical metadata with taxonomic relative abundance tables using `pandas`.
2. **Alpha Diversity:** Calculated the Shannon Index to measure within-sample microbial diversity.
3. **Beta Diversity:** Implemented a Bray-Curtis PCoA (Principal Coordinate Analysis) to visualize community clustering, correcting for zero-inflation issues inherent in standard PCA.
4. **Differential Abundance:** Ran Mann-Whitney U tests with FDR correction to identify statistically significant bacterial biomarkers between BV and healthy groups.

## Results
- **Alpha Diversity:** Overall diversity did not drastically differ between groups, indicating that the *type* of bacteria matters more than the total number of species.
- **Beta Diversity:** Bray-Curtis PCoA successfully separated the samples into distinct Community State Types (CSTs), showing tight clustering of healthy microbiomes vs. the dispersed nature of BV.
- **Biomarkers:** 
  - **BV Pathogens:** Confirmed a massive overgrowth of *Gardnerella* species (*G. vaginalis*, *G. piotii*, etc.) in BV patients (FDR p-value < 2.13e-77).
  - **Healthy Protectors:** Confirmed a dominance of *Lactobacillus crispatus* in healthy patients.

## Visualizations
- `alpha_diversity.png`: Boxplot of Shannon diversity by group.
- `bray_curtis_pcoa.png`: PCoA scatter plot of bacterial communities.

## How to Run
1. Download the dataset from Zenodo (Record 22307394).
2. Install dependencies: `pip install pandas numpy matplotlib seaborn scipy scikit-learn openpyxl statsmodels`
3. Run the scripts in order:
   - `evvy_analysis.py` (Alpha & Beta Diversity)
   - `bray_curtis_pcoa.py` (Bray-Curtis PCoA)
   - `differential_abundance.py` (Mann-Whitney U test)

## Author
Alana Annamanthadoo
[LinkedIn](https://linkedin.com/in/alana-annaman) | [GitHub](https://github.com/AlanaAnnaman)# Evvy-BV-UTI
Analysis of participants with BV and/or UTI using vaginal samples from Evvy participants based on the pre-print "Vaginal Microbiome in Women Recently Experiencing BV & UTI" https://www.biorxiv.org/content/10.1101/2025.11.27.690987v1.full 
