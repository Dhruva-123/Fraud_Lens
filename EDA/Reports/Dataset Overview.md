
## Overview

This repository contains SQL-based exploratory data analysis (EDA) performed on the `creditcard_transactions` dataset. The dataset includes 284,807 transactions, labeled as either **non-fraud (Class 0)** or **fraud (Class 1)**, with 28 anonymized features (`V1` to `V28`), `Amount`, and `Time`.

---

## Key Findings

### 1. Null Values

- Verified that **there are no nulls** in any column.
    
- Implication: All aggregation functions (`AVG`, `STDDEV`, `MIN`, `MAX`) produce reliable results.
    

### 2. Class Distribution

- Non-Fraud (Class 0): 284,315 rows (~99.83%)
    
- Fraud (Class 1): 492 rows (~0.17%)
    
- Observation: The dataset is **extremely imbalanced**, highlighting the need for careful modeling strategies.
    

### 3. Feature Averages (AVG)

- For every feature (`V1`–`V28`) and `Amount`, **fraud transactions have significantly higher average values** compared to non-fraud transactions.
    
- Implication: Fraudulent transactions tend to deviate strongly from typical behavior, making feature averages potential indicators.
    

### 4. Standard Deviations (STDDEV)

- Fraud transactions show **higher standard deviation across most features**, except `Amount`.
    
- Implication: Fraud features are more variable and less consistent than non-fraud features, which can aid in anomaly detection.
    

### 5. Minimum Values (MIN)

- Non-fraud rows reach **lower minimums** across most columns compared to fraud rows.
    
- Observation: Fraud rows rarely hit the extreme low values that non-fraud transactions do.
    

### 6. Maximum Values (MAX)

- Maximum values are slightly higher for non-fraud in most features, though differences are less pronounced than for minimums.
    
- Implication: Extreme highs alone are not as strong an indicator for fraud as averages and standard deviations.
    

---

## Fraud Indicators (Key Hallmarks)

From the analysis, rows likely to be fraudulent exhibit:

1. **Abnormally high averages** in multiple features.
    
2. **Higher standard deviations**, indicating variable behavior.
    
3. **Distinct minimum and maximum patterns**, usually not reaching the extreme lows of non-fraud transactions.
    

---

## Notes

- All SQL queries were executed on the `FraudLens` database.
    
- This is **introductory EDA**; deeper analyses and modeling are required for fraud detection.