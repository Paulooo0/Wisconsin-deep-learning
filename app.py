import flask
from tensorflow import reshape
from tensorflow import keras
import os
from rebuild_dataset import get_data
from re import escape

app = flask.Flask(__name__, template_folder='template', static_folder='template/static')
model = keras.models.load_model('neural_model')

data = get_data('dataset/rebuilted_cancer_wisconsin.csv')

@app.route('/')
def display_gui():
    return flask.render_template('template.html')

@app.route('/pred', methods=['POST'])
def get_pred():
    form = [float(flask.request.form['radius_mean']),
            float(flask.request.form['texture_mean']),
            float(flask.request.form['perimeter_mean']),
            float(flask.request.form['area_mean']),
            float(flask.request.form['smoothness_mean']),
            float(flask.request.form['compactness_mean']),
            float(flask.request.form['concavity_mean']),
            float(flask.request.form['concave_points_mean']),
            float(flask.request.form['symmetry_mean']),
            float(flask.request.form['fractal_dimension_mean']),
            float(flask.request.form['radius_se']),
            float(flask.request.form['texture_se']),
            float(flask.request.form['perimeter_se']),
            float(flask.request.form['area_se']),
            float(flask.request.form['smoothness_se']),
            float(flask.request.form['compactness_se']),
            float(flask.request.form['concavity_se']),
            float(flask.request.form['concave_points_se']),
            float(flask.request.form['symmetry_se']),
            float(flask.request.form['fractal_dimension_se']),
            float(flask.request.form['radius_worst']),
            float(flask.request.form['texture_worst']),
            float(flask.request.form['perimeter_worst']),
            float(flask.request.form['area_worst']),
            float(flask.request.form['smoothness_worst']),
            float(flask.request.form['compactness_worst']),
            float(flask.request.form['concavity_worst']),
            float(flask.request.form['concave_points_worst']),
            float(flask.request.form['symmetry_worst']),
            float(flask.request.form['fractal_dimension_worst'])]
    
    model = keras.models.load_model('neural_model')

    # Need test and fix. ValueError: Failed to convert a NumPy array to a Tensor (Unsupported object type tuple).
    pred = model.predict(reshape(form,shape=(1,30)))
    
    # for pred in range(len(2:-2)):
        
    
    printable_pred = str(pred).replace('[[', '')
    printable_pred = printable_pred.replace(']]', '')
    
    print(model.predict(reshape(form,shape=(1,30))))

    return flask.render_template('template.html', prediction=printable_pred)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='localhost', port=port, debug=True)