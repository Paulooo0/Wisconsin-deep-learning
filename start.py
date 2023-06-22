import flask
from tensorflow import keras
import pandas as pd
import os
from rebuild_dataset import get_data

app = flask.Flask(__name__, template_folder='template', static_folder='template/static')
model = keras.models.load_model('neural_model')

data = get_data('dataset/rebuilted_cancer_wisconsin.csv')

@app.route('/')
def display_gui():
    return flask.render_template('template.html')

@app.route('/pred', methods=['POST'])
def get_pred():
    radius_mean = flask.request.form['radius_mean'],
    texture_mean = flask.request.form['texture_mean'],
    perimeter_mean = flask.request.form['perimeter_mean'],
    area_mean = flask.request.form['area_mean'],
    smoothness_mean = flask.request.form['smoothness_mean']
    compactness_mean = flask.request.form['compactness_mean']
    concavity_mean = flask.request.form['concavity_mean']
    concave_points_mean = flask.request.form['concave_points_mean']
    symmetry_mean = flask.request.form['symmetry_mean']
    fractal_dimension_mean = flask.request.form['fractal_dimension_mean']
    radius_se = flask.request.form['radius_se']
    texture_se = flask.request.form['texture_se']
    perimeter_se = flask.request.form['perimeter_se']
    area_se = flask.request.form['area_se']
    smoothness_se = flask.request.form['smoothness_se']
    compactness_se = flask.request.form['compactness_se']
    concavity_se = flask.request.form['concavity_se']
    concave_points_se = flask.request.form['concave_points_se']
    symmetry_se = flask.request.form['symmetry_se']
    fractal_dimension_se = flask.request.form['fractal_dimension_se']
    radius_worst = flask.request.form['radius_worst']
    texture_worst = flask.request.form['texture_worst']
    perimeter_worst = flask.request.form['perimeter_worst']
    area_worst = flask.request.form['area_worst']
    smoothness_worst = flask.request.form['smoothness_worst']
    compactness_worst = flask.request.form['compactness_worst']
    concavity_worst = flask.request.form['concavity_worst']
    concave_points_worst = flask.request.form['concave_points_worst']
    symmetry_worst = flask.request.form['symmetry_worst']
    fractal_dimension_worst = flask.request.form['fractal_dimension_worst']

    pred = [radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean,
            compactness_mean, concavity_mean, concave_points_mean, symmetry_mean,
            fractal_dimension_mean, radius_se, texture_se, perimeter_se,
            area_se, smoothness_se, compactness_se, concavity_se, concave_points_se,
            symmetry_se, fractal_dimension_se, radius_worst, texture_worst,
            perimeter_worst, area_worst, smoothness_worst, compactness_worst,
            concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst]

    model = keras.models.load_model('neural_model')

    # Need test and fix. ValueError: Failed to convert a NumPy array to a Tensor (Unsupported object type tuple).
    prediction = model.predict(pred)
    return flask.render_template('template.html', prediction)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='localhost', port=port, debug=True)