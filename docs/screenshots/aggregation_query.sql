
SELECT 
    strftime('%Y-%m', sale_date) as month,
    COUNT(*) as transactions,
    SUM(amount) as monthly_revenue,
    AVG(amount) as avg_transaction
FROM transactions
WHERE sale_date >= '2024-01-01'
GROUP BY month
ORDER BY month DESC


-- Results:
      month  transactions  monthly_revenue  avg_transaction
0   2024-12           178    433009.479966      2432.637528
1   2024-11           219    566687.085151      2587.612261
2   2024-10           252    628092.356333      2492.429985
3   2024-09           213    542908.427169      2548.865855
4   2024-08           191    486288.701012      2546.014141
5   2024-07           243    623989.295840      2567.857185
6   2024-06           189    505190.758807      2672.966978
7   2024-05           227    585011.490951      2577.143132
8   2024-04           188    483633.717506      2572.519774
9   2024-03           213    551710.819030      2590.191639
10  2024-02           202    477741.639336      2365.057620
11  2024-01           212    515089.428934      2429.667118