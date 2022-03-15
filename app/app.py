from flask import Flask, request
from flask.templating import render_template
from joblib import load
from sklearn.pipeline import Pipeline
import warnings
warnings.filterwarnings('ignore')
app = Flask(__name__)
model = load('../model.joblib')
colTr = load('../col_transformer.joblib')


@app.route('/', methods=['GET'])
def welcome():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = []
    text = request.form
    for i in text:
        i = text[i]
        if i.isdigit():
            i=int(i)
        data.append(i)
    res =  do_pred(data, model)
    return render_template('predict.html', result=res)

def do_pred(inp, model):
    try:
        pip = Pipeline(steps=[
            ('coltr', colTr),
            ('model', model)
        ])

        if pip.predict([inp])==0:
            return 'You wouldn\'t survive ;('
        else:
            return 'You would survive🥳'
    except ValueError:
        return "You have entered incorrect data :("


if __name__=='__main__':
    app.run(debug=True)
