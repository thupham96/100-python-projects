from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.choices import SelectField
from wtforms.validators import DataRequired, URL
import csv


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    opening_time = StringField('Opening Time e.g. 8AM', validators=[DataRequired()])
    closing_time = StringField('Closing Time e.g. 5PM', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating',
                                choices=['☕', '☕☕', '☕☕☕', '☕☕☕☕', '☕☕☕☕☕'],
                                validators=[DataRequired()])
    wifi_rating = SelectField('Wifi Strength Rating',
                                choices=['💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪'],
                                validators=[DataRequired()])
    power_socket_availability = SelectField('Power Socket Availability',
                                choices=['🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'],
                                validators=[DataRequired()])
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        cafe_name = form.cafe.data
        location = form.location.data
        opening_time = form.opening_time.data
        closing_time = form.closing_time.data
        coffee_rating = form.coffee_rating.data
        wifi_rating = form.wifi_rating.data
        power_socket_availability = form.power_socket_availability.data
        new_row = [cafe_name, location, opening_time, closing_time, coffee_rating, wifi_rating, power_socket_availability]
        with open("cafe-data.csv", mode="a", newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(new_row)
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
