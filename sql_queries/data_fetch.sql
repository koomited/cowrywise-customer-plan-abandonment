SELECT 

    -- User profile details
    U.gender_id,
    U.risk_apetite,
    U.address_city,
    U.address_country,
    U.fraud_score,
    U.monthly_expense,
    U.monthly_salary,

    -- Determine account type
    CASE 
        WHEN P.is_regular_savings = 1 THEN 'Savings'
        WHEN P.is_a_fund = 1 THEN 'Investment'
        ELSE NULL
    END AS type,

    -- Last transaction date
    MAX(S.transaction_date) AS last_transaction_date,

    -- Days since last transaction or since plan start_date if no transaction
    DATEDIFF(
        CURDATE(), 
        COALESCE(MAX(S.transaction_date), P.start_date)
    ) AS inactivity_days,

    -- Total number of transactions per plan
    COUNT(DISTINCT S.id) AS total_transactions,

    -- Total confirmed amount of all transactions per plan
    COALESCE(SUM(S.confirmed_amount), 0) AS total_transaction_amount,

    -- Total amount withdrawn per plan
    COALESCE(SUM(W.amount_withdrawn), 0) AS total_withdrawn_amount

FROM 
    plans_plan P

-- LEFT JOIN to include plans with zero transactions
LEFT JOIN 
    savings_savingsaccount S 
    ON S.plan_id = P.id 

-- LEFT JOIN to include plans with or without withdrawals
LEFT JOIN 
    withdrawals_withdrawal W 
    ON W.plan_id = P.id

-- JOIN users to get user details and filter on account age
INNER JOIN 
    users_customuser U 
    ON P.owner_id = U.id

WHERE
    -- Only include plans with at least a transaction or withdrawal
    (S.transaction_date IS NOT NULL OR W.amount IS NOT NULL)
    AND
    -- Only include users who signed up more than 30 days ago
    U.date_joined < CURDATE() - INTERVAL 1 MONTH

GROUP BY 
    P.id,
    P.owner_id

HAVING 
    type IS NOT NULL;
