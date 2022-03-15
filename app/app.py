from flask import Flask, request
from flask.templating import render_template
from joblib import load
from sklearn.pipeline import Pipeline

app = Flask(__name__)
model = load('../../model.joblib')
colTr = load('../../col_transformer.joblib')


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
    res = do_pred(data, model)
    return render_template('predict.html', result=res)


def validate_input(inp):
    """
    :param inp: input data
    :return: ValueError/True
    """
    if (int(inp[2])<1 or int(inp[2])>100) or \
        (int(inp[0])<1 or int(inp[0])>3) or  \
        (int(inp[3])<0 or int(inp[3])>10) or \
        (int(inp[4])<0 or int(inp[4])>10) or \
        (int(inp[5])<1):
            raise ValueError
    return True
def do_pred(inp, model):
    """
    :param inp: input data
    :param model: ml-model
    :return: prediction
    """
    try:
        if validate_input(inp):
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
    app.run()
