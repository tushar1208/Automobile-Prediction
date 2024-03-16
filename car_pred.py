from flask import Flask, request, jsonify, render_template
import  pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model123.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index1.html')

# @app.route('/prediction')
# def prediction():
# 	return render_template('index2.html')


@app.route('/prediction',methods=['POST'])
def prediction():
    '''
    For rendering results on HTML GUI
    '''
    # a = request.form['city_mpg']
    # b = request.form['engine_size']
    # print("a>",a, b)
    int_features = [int(x) for x in request.form.values()]
    print(">",int_features)
    final_features = [np.array(int_features)]
    print(">>>>>>",final_features)
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    # return render_template('index1.html', prediction_text='The Car Price should be $ {}'.format(output))
    return render_template('index1.html', prediction_text = output)



if __name__ == "__main__":
    app.run(debug=True)