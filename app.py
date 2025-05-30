from flask import Flask, render_template, request
import os 
import pandas as pd
from mlProject.pipeline.prediction import PredictionPipeline


app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
def homePage():
    return render_template("index.html")


# @app.route('/train',methods=['GET'])  # route to train the pipeline
# def training():
#     os.system("python main.py")
#     return "Training Successful!" 


@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
           # Reading the inputs given by the user
            gender_id = int(request.form['gender_id'])
            risk_apetite = float(request.form['risk_apetite'])
            fraud_score = float(request.form['fraud_score'])
            monthly_expense = float(request.form['monthly_expense'])
            account_type = request.form['type']  # assuming it's categorical
            total_transactions = int(request.form['total_transactions'])
            total_transaction_amount = float(request.form['total_transaction_amount'])
            total_withdrawn_amount = float(request.form['total_withdrawn_amount'])

           # Constructing the input data
            data = {
                'gender_id': [gender_id],
                'risk_apetite': [risk_apetite],
                'fraud_score': [fraud_score],
                'monthly_expense': [monthly_expense],
                'type': [account_type],
                'total_transactions': [total_transactions],
                'total_transaction_amount': [total_transaction_amount],
                'total_withdrawn_amount': [total_withdrawn_amount]
            }

            input_df = pd.DataFrame(data)

            
            obj = PredictionPipeline()
            predicted_prob = obj.predict(input_df)[0]


            if predicted_prob > 0.5:
                message = "⚠️ High Risk of Plan Abandonment"
                color = "danger"
            else:
                message = "✅ Low Risk of Plan Abandonment"
                color = "success"

            return render_template('results.html', prediction=round(predicted_prob*100, 2), message=message, color=color)



        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'

    else:
        return render_template('index.html')


if __name__ == "__main__":
	# app.run(host="0.0.0.0", port = 8080, debug=True)
	app.run(host="0.0.0.0", port = 8080)