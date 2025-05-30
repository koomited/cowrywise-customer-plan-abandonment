# cowrywise-customer-plan-abandonment
Predicting Cowrywise customer plan abondonment
---

[![Linux](https://img.shields.io/badge/Linux-FCC624?logo=linux&logoColor=black)](#)
[![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?logo=visual-studio-code&logoColor=white)](#)
[![GitHub](https://img.shields.io/badge/GitHub-%23121011.svg?logo=github&logoColor=white)](#)
[![Git](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white)](#)
[![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?logo=githubactions&logoColor=white)](#)
[![MySQL](https://img.shields.io/badge/MySQL-4479A1?logo=mysql&logoColor=white)](#)
[![phpMyAdmin](https://img.shields.io/badge/phpMyAdmin-6C78AF?logo=phpmyadmin&logoColor=white)](#)
[![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)](#)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)](#)
[![Flask](https://img.shields.io/badge/Flask-000000?logo=flask&logoColor=white)](#)
[![DagsHub](https://img.shields.io/badge/DagsHub-FF6A00?logo=dagsHub&logoColor=white)](#)
![Awesome](https://img.shields.io/badge/Awesome-ffd700?logo=awesome&logoColor=black)

---
![Project Screenshot](https://www.internationalaccountingbulletin.com/wp-content/uploads/sites/9/2023/11/shutterstock_22739995191.jpg)


# Problem

One key insight observed during the exploration of Cowrywise customer data is that nearly 60% (specifically, 58.97%) of customer plans have had no transactions for over one year (365 days). These inactive plans carry a significant risk of being abandoned by the customers. This poses a potential waste of time and resources for both the company and its clients.

To mitigate this risk, we propose defining plans with over 365 days of inactivity as either abandoned or at high risk of abandonment. Based on this definition, we aim to develop a machine learning model that predicts the likelihood of a plan being abandoned. With such a predictive tool, the company can proactively assess the viability of customer plans and more effectively guide clients toward plans that are better aligned with their goals. This project focuses on enabling that capability.


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




# How to run?
### STEPS:


Clone the repository

```bash
https://github.com/koomited/cowrywise-customer-plan-abandonment.git
```
### STEP 01- Create a conda environment after opening the repository

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
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


In Case you want to try training
```bash
# run the containers to create the database and tables
docker compose up -d
```
Then 
```bash
# run the main.py
python main.py
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

