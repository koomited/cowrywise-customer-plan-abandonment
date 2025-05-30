# cowrywise-customer-plan-abandonment
Predicting customer plan abondonment

## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the app.py

In this study, we assume any plan without transaction for more than 365 day is more likely to be abandoned.
Find below the commmented sql query used to featch the data used.



```sql
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
```
That would be great to include variables like  address_city, 
    address_country in our model but they are full of missing values, 47.05% and 71% respectively.
Also not surprising, there is a high correlation between monthly expenses and salary. In this study we keep monthely expenses because strongly related to our focus to predict plan abandonment. Furthermore, we want be using last transaction date in the model.












# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/entbappy/End-to-end-Machine-Learning-Project-with-MLflow
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n mlproj python=3.8 -y
```

```bash
conda activate mlproj
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```



## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/koomi/cowrywise-customer-plan-abandonment.mlflow
MLFLOW_TRACKING_USERNAME=koomi \
MLFLOW_TRACKING_PASSWORD=b918e1b0fdebad41476188587e7a2996300c6ee2\
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/koomi/cowrywise-customer-plan-abandonment.mlflow

export MLFLOW_TRACKING_USERNAME=koomi

export MLFLOW_TRACKING_PASSWORD=b918e1b0fdebad41476188587e7a2996300c6ee2

```



# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 566373416292.dkr.ecr.ap-south-1.amazonaws.com/mlproj

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app




## About MLflow 
MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & tagging your model

