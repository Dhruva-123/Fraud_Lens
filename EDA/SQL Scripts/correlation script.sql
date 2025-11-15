USE FraudLens;
/*
SELECT
    a.col AS col1,
    b.col AS col2,
    SUM((a.val - a.avg_val) * (b.val - b.avg_val)) /
    SQRT(SUM(POW(a.val - a.avg_val, 2)) * SUM(POW(b.val - b.avg_val, 2))) AS correlation
FROM
    (
        SELECT 'v1' AS col, v1 AS val, (SELECT AVG(v1) FROM creditcard_transactions) AS avg_val FROM creditcard_transactions
        UNION ALL SELECT 'v2', v2, (SELECT AVG(v2) FROM creditcard_transactions) FROM creditcard_transactions
        UNION ALL SELECT 'v3', v3, (SELECT AVG(v3) FROM creditcard_transactions) FROM creditcard_transactions
        UNION ALL SELECT 'v4', v4, (SELECT AVG(v4) FROM creditcard_transactions) FROM creditcard_transactions
        UNION ALL SELECT 'v5', v5, (SELECT AVG(v5) FROM creditcard_transactions) FROM creditcard_transactions
        UNION ALL SELECT 'v6', v6, (SELECT AVG(v6) FROM creditcard_transactions) FROM creditcard_transactions
        UNION ALL SELECT 'v7', v7, (SELECT AVG(v7) FROM creditcard_transactions) FROM creditcard_transactions
        UNION ALL SELECT 'v8', v8, (SELECT AVG(v8) FROM creditcard_transactions) FROM creditcard_transactions
        UNION ALL SELECT 'v9', v9, (SELECT AVG(v9) FROM creditcard_transactions) FROM creditcard_transactions
        UNION ALL SELECT 'v10', v10, (SELECT AVG(v10) FROM creditcard_transactions) FROM creditcard_transactions
        UNION ALL SELECT 'v11', v11, (SELECT AVG(v11) FROM creditcard_transactions) FROM creditcard_transactions
        UNION ALL SELECT 'v12', v12, (SELECT AVG(v12) FROM creditcard_transactions) FROM creditcard_transactions
        UNION ALL SELECT 'v13', v13, (SELECT AVG(v13) FROM creditcard_transactions) FROM creditcard_transactions
        UNION ALL SELECT 'v14', v14, (SELECT AVG(v14) FROM creditcard_transactions) FROM creditcard_transactions
        UNION ALL SELECT 'v15', v15, (SELECT AVG(v15) FROM creditcard_transactions) FROM creditcard_transactions
        UNION ALL SELECT 'v16', v16, (SELECT AVG(v16) FROM creditcard_transactions) FROM creditcard_transactions
        UNION ALL SELECT 'v17', v17, (SELECT AVG(v17) FROM creditcard_transactions) FROM creditcard_transactions
        UNION ALL SELECT 'v18', v18, (SELECT AVG(v18) FROM creditcard_transactions) FROM creditcard_transactions
        UNION ALL SELECT 'v19', v19, (SELECT AVG(v19) FROM creditcard_transactions) FROM creditcard_transactions
        UNION ALL SELECT 'v20', v20, (SELECT AVG(v20) FROM creditcard_transactions) FROM creditcard_transactions
        UNION ALL SELECT 'v21', v21, (SELECT AVG(v21) FROM creditcard_transactions) FROM creditcard_transactions
        UNION ALL SELECT 'v22', v22, (SELECT AVG(v22) FROM creditcard_transactions) FROM creditcard_transactions
        UNION ALL SELECT 'v23', v23, (SELECT AVG(v23) FROM creditcard_transactions) FROM creditcard_transactions
        UNION ALL SELECT 'v24', v24, (SELECT AVG(v24) FROM creditcard_transactions) FROM creditcard_transactions
        UNION ALL SELECT 'v25', v25, (SELECT AVG(v25) FROM creditcard_transactions) FROM creditcard_transactions
        UNION ALL SELECT 'v26', v26, (SELECT AVG(v26) FROM creditcard_transactions) FROM creditcard_transactions
        UNION ALL SELECT 'v27', v27, (SELECT AVG(v27) FROM creditcard_transactions) FROM creditcard_transactions
        UNION ALL SELECT 'v28', v28, (SELECT AVG(v28) FROM creditcard_transactions) FROM creditcard_transactions
    ) AS a
JOIN
    (
        SELECT 'v1' AS col, v1 AS val, (SELECT AVG(v1) FROM creditcard_transactions) AS avg_val FROM creditcard_transactions
        UNION ALL SELECT 'v2', v2, (SELECT AVG(v2) FROM creditcard_transactions) FROM creditcard_transactions
        UNION ALL SELECT 'v3', v3, (SELECT AVG(v3) FROM creditcard_transactions) FROM creditcard_transactions
        UNION ALL SELECT 'v4', v4, (SELECT AVG(v4) FROM creditcard_transactions) FROM creditcard_transactions
        UNION ALL SELECT 'v5', v5, (SELECT AVG(v5) FROM creditcard_transactions) FROM creditcard_transactions
        UNION ALL SELECT 'v6', v6, (SELECT AVG(v6) FROM creditcard_transactions) FROM creditcard_transactions
        UNION ALL SELECT 'v7', v7, (SELECT AVG(v7) FROM creditcard_transactions) FROM creditcard_transactions
        UNION ALL SELECT 'v8', v8, (SELECT AVG(v8) FROM creditcard_transactions) FROM creditcard_transactions
        UNION ALL SELECT 'v9', v9, (SELECT AVG(v9) FROM creditcard_transactions) FROM creditcard_transactions
        UNION ALL SELECT 'v10', v10, (SELECT AVG(v10) FROM creditcard_transactions) FROM creditcard_transactions
        UNION ALL SELECT 'v11', v11, (SELECT AVG(v11) FROM creditcard_transactions) FROM creditcard_transactions
        UNION ALL SELECT 'v12', v12, (SELECT AVG(v12) FROM creditcard_transactions) FROM creditcard_transactions
        UNION ALL SELECT 'v13', v13, (SELECT AVG(v13) FROM creditcard_transactions) FROM creditcard_transactions
        UNION ALL SELECT 'v14', v14, (SELECT AVG(v14) FROM creditcard_transactions) FROM creditcard_transactions
        UNION ALL SELECT 'v15', v15, (SELECT AVG(v15) FROM creditcard_transactions) FROM creditcard_transactions
        UNION ALL SELECT 'v16', v16, (SELECT AVG(v16) FROM creditcard_transactions) FROM creditcard_transactions
        UNION ALL SELECT 'v17', v17, (SELECT AVG(v17) FROM creditcard_transactions) FROM creditcard_transactions
        UNION ALL SELECT 'v18', v18, (SELECT AVG(v18) FROM creditcard_transactions) FROM creditcard_transactions
        UNION ALL SELECT 'v19', v19, (SELECT AVG(v19) FROM creditcard_transactions) FROM creditcard_transactions
        UNION ALL SELECT 'v20', v20, (SELECT AVG(v20) FROM creditcard_transactions) FROM creditcard_transactions
        UNION ALL SELECT 'v21', v21, (SELECT AVG(v21) FROM creditcard_transactions) FROM creditcard_transactions
        UNION ALL SELECT 'v22', v22, (SELECT AVG(v22) FROM creditcard_transactions) FROM creditcard_transactions
        UNION ALL SELECT 'v23', v23, (SELECT AVG(v23) FROM creditcard_transactions) FROM creditcard_transactions
        UNION ALL SELECT 'v24', v24, (SELECT AVG(v24) FROM creditcard_transactions) FROM creditcard_transactions
        UNION ALL SELECT 'v25', v25, (SELECT AVG(v25) FROM creditcard_transactions) FROM creditcard_transactions
        UNION ALL SELECT 'v26', v26, (SELECT AVG(v26) FROM creditcard_transactions) FROM creditcard_transactions
        UNION ALL SELECT 'v27', v27, (SELECT AVG(v27) FROM creditcard_transactions) FROM creditcard_transactions
        UNION ALL SELECT 'v28', v28, (SELECT AVG(v28) FROM creditcard_transactions) FROM creditcard_transactions
    ) AS b
ON 1=1
GROUP BY a.col, b.col
ORDER BY a.col, b.col;*/
/*This code is proving to be too heavy for my setup. So we will export this table to python and find correlations via python and get back a new correlation table into mysql.*/

