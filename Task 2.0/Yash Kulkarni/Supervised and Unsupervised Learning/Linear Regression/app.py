from flask import Flask, render_template, request
import pandas as pd 
import pickle

app = Flask(__name__)

model = pickle.load(open("LinearRegressionModel.pkl",'rb'))
car = pd.read_csv('cleaned_data.csv')

@app.route('/')
def index():
    companies = sorted(car['company'].unique())
    car_model = sorted(car['name'].unique())
    years = sorted(car['year'].unique(), reverse=True)
    fuel_type = sorted(car['fuel_type'].unique())
    return render_template ('index.html', companies=companies, car_model=car_model, years=years, fuel_type=fuel_type )

@app.route('/predict', methods = ['POST'])
def predict():
    company = request.form.get('company')
    car_model = request.form.get('car_model')
    years = int(request.form.get('year'))
    fuel_type = request.form.get('fuel_type')
    kms_driven = int(request.form.get('kilo_driven'))

    prediction = model.predict(pd.DataFrame([[car_model, company, years, kms_driven, fuel_type]],columns=['name','company','year','kms_driven','fuel_type']))
    print(prediction)

    return str(prediction[0])



if __name__ == "__main__":
    app.run(debug=True)
