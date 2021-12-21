from flask import *
import pickle
import numpy as np
app = Flask(__name__)
app.config["CACHE_TYPE"] = "null"
model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def hello():
 return render_template ('index.html')

# prediction function
@app.route('/predict', methods = ['POST'])
def predict():
 A = [float(x) for x in request.form.values()]
 model_probability = model.predict_proba([A])
 result = 'Probability of having Diabetes is %0.2f'%model_probability[0][1]
 return render_template('result.html', result1 = result)
if __name__ == "__main__":
    app.run(debug=True)
