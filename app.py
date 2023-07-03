from check_requirements import check_and_install
file = open('requirements.txt', 'r')
reader = file.readlines()
check_and_install(reader)

from flask import Flask, render_template, request
from tensorflow import reshape
from tensorflow import keras
from os import environ
from webbrowser import open

app = Flask(__name__, template_folder='template', static_folder='template/static')

@app.route('/')
def display_gui():
    return render_template('template.html')

@app.route('/pred', methods=['POST'])
def get_pred():
    form = [float(request.form['radius_mean']),
            float(request.form['texture_mean']),
            float(request.form['perimeter_mean']),
            float(request.form['area_mean']),
            float(request.form['smoothness_mean']),
            float(request.form['compactness_mean']),
            float(request.form['concavity_mean']),
            float(request.form['concave_points_mean']),
            float(request.form['symmetry_mean']),
            float(request.form['fractal_dimension_mean']),
            float(request.form['radius_se']),
            float(request.form['texture_se']),
            float(request.form['perimeter_se']),
            float(request.form['area_se']),
            float(request.form['smoothness_se']),
            float(request.form['compactness_se']),
            float(request.form['concavity_se']),
            float(request.form['concave_points_se']),
            float(request.form['symmetry_se']),
            float(request.form['fractal_dimension_se']),
            float(request.form['radius_worst']),
            float(request.form['texture_worst']),
            float(request.form['perimeter_worst']),
            float(request.form['area_worst']),
            float(request.form['smoothness_worst']),
            float(request.form['compactness_worst']),
            float(request.form['concavity_worst']),
            float(request.form['concave_points_worst']),
            float(request.form['symmetry_worst']),
            float(request.form['fractal_dimension_worst'])]
    
    model = keras.models.load_model('neural_model')

    pred = model.predict(reshape(form,shape=(1,30)))
    binary_pred = (pred >= 0.5).astype(int)
    
    if binary_pred == 0:
        print_pred = 'Benign'
    else:
        print_pred = 'Malignant'

    return render_template('template2.html', prediction=print_pred)

if __name__ == '__main__':
    open('http://localhost:5000')
    port = int(environ.get('PORT', 5000))
    app.run(host='localhost', port=port, debug=True, use_reloader=False)