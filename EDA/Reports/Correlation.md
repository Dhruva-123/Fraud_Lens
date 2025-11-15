**1. Data Extraction:**

- Extracted the 28 numerical features (`v1` to `v28`) from the `creditcard_transactions` table in MySQL using Python (`pandas` + `SQLAlchemy` + `pymysql`).
    
- This allowed us to perform flexible analysis directly in Python while keeping the data connected to the database.
    

**2. Correlation Computation:**

- Computed **pairwise Pearson correlation coefficients** for all column combinations using `pandas.DataFrame.corr()`.
    
- This produced a **28×28 correlation matrix** showing the linear relationship between every pair of features.
    

**3. Reshaping for Visualization:**

- Converted the long-format correlation table (`col1`, `col2`, `correlation`) into a square 28×28 matrix with ordered rows and columns (`v1` → `v28`).
    
- This makes the data suitable for heatmap visualization and easier interpretation.
    

**4. Visualization:**

- Plotted the correlation matrix as a **heatmap** using `Seaborn` with annotated values and a `coolwarm` colormap.
    
- This visual representation quickly highlights the degree of correlation (or lack thereof) between features.
    

**5. Observations and Conclusions:**

- The heatmap and correlation matrix reveal that **all pairwise correlations are negligible**, i.e., very close to zero.
    
- This indicates that the features are largely **uncorrelated**, suggesting that prior **PCA or feature engineering** successfully decorrelated the data.
    
- The dataset is therefore **well-structured and decorrelated**, suitable for further modeling without concerns about multicollinearity.
    
- Each feature contributes **independently** to the information content.
    

**6. Data Storage and Future Use:**

- The computed correlation table has been **saved back into our MySQL database** (`correlation_table`) for easy access.
    
- This allows future scripts or analyses to **directly use the precomputed correlations** without recomputing.
    

**7. Reproducibility:**

- All scripts used to compute the correlation and generate the heatmap, along with the charts, are **available in our repository**.
    
- This ensures that team members can **reproduce the analysis** or adapt it for additional datasets.