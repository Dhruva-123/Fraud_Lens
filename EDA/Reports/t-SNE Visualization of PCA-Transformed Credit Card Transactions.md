
This plot shows how fraud and non-fraud transactions organize themselves in the latent feature space after PCA reduction. Using t-SNE, we map the high-dimensional data into 2D to reveal structure, clustering, and separability trends.

---

## **1. Clear Fraud Cluster (Left Side)**

Fraud transactions form a **dense, compact cluster**, indicating highly similar behavioral patterns.  
This consistency implies:

- Fraud behavior is structured, not random
    
- Attack vectors are repetitive (scripts, stolen profiles, coordinated actors)
    
- Fraud detection is fundamentally learnable
    

Models can exploit this tight structure to achieve strong recall and precision.

---

## **2. Broad, Diverse Non-Fraud Distribution (Right Side)**

Legitimate transactions spread widely with no dominant center.  
This reflects:

- Diverse user behavior patterns
    
- Varied transaction contexts (time, amount, merchant types, device fingerprints)
    

This heterogeneity increases the importance of robust generalization in modeling.

---

## **3. Overlap Region (Challenging Zone)**

A small region where fraud and non-fraud mix exists.  
This zone represents:

- Fraud cases intentionally mimicking normal behavior
    
- Legitimate transactions with suspicious patterns
    

Most false positives/negatives will originate here.

---

## **4. PCA Preserves Discriminative Structure**

Even after dimensionality reduction to 28 components, t-SNE reveals clear separation.  
This confirms:

- PCA preprocessing is effective
    
- Latent fraud signatures remain intact
    
- No meaningful fraud behavior was lost
    

---

## **5. Implications for Modeling**

- Fraud cluster compactness → **models can achieve high accuracy**
    
- Overlap region → **threshold tuning is crucial**
    
- Non-fraud spread → **avoid overfitting on majority class**
    
- Ensemble or weighted models recommended