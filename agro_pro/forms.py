from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, FloatField
from wtforms.validators import Length, EqualTo, DataRequired


class GetClimateForm(FlaskForm):
    lat = FloatField(label='Latitude', validators=[DataRequired()])
    lon = FloatField(label='Longitude', validators=[DataRequired()])
    submit = SubmitField(label='Get Climate Details')


class GetForecastForm(FlaskForm):
    lat = FloatField(label='Latitude', validators=[DataRequired()])
    lon = FloatField(label='Longitude', validators=[DataRequired()])
    submit = SubmitField(label='Get Weather Forecast')
