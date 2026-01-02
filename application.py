from flask import Flask, request, render_template
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'POST':
        form_data = request.form.to_dict()

        data = CustomData(
            gender=form_data.get('gender'),
            race_ethnicity=form_data.get('ethnicity'),
            parental_level_of_education=form_data.get('parental_level_of_education'),
            lunch=form_data.get('lunch'),
            test_preparation_course=form_data.get('test_preparation_course'),
            reading_score=float(form_data.get('reading_score')),
            writing_score=float(form_data.get('writing_score'))
        )

        pred_df = data.get_data_as_data_frame()
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)

        return render_template(
            'home.html',
            results=results[0],
            form_data=form_data
        )

    return render_template('home.html', form_data={})
