
SELECT 
    product_category,
    COUNT(*) as total_transactions,
    SUM(amount) as total_revenue,
    AVG(amount) as avg_transaction_value
FROM transactions
GROUP BY product_category
ORDER BY total_revenue DESC
LIMIT 5


-- Results:
  product_category  total_transactions  total_revenue  avg_transaction_value
0         Clothing                 909   2.275596e+06            2503.405686
1      Electronics                 822   2.178162e+06            2649.832467
2             Toys                 826   2.099023e+06            2541.190484
3           Sports                 818   2.079419e+06            2542.077316
4            Books                 832   2.052569e+06            2467.030017