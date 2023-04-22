from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe_name = StringField(label = 'Cafe Name', validators=[DataRequired()])
    location = StringField(label = 'Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    open = StringField(label = 'Opening time e.g: 8AM', validators=[DataRequired()])
    close = StringField(label = 'Close Time e.g: 5:30PM', validators=[DataRequired()])
    coffee = SelectField(label = 'Coffee Rating', validators=[DataRequired()], choices=["☕", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"])
    wifi = SelectField(label = 'Wifi Strength Rating', validators=[DataRequired()], choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪"])
    power = SelectField(label = 'Power Socket Availability', validators=[DataRequired()], choices=["🔌","🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌"])
    submit = SubmitField(label='Submit', )



# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["POST", "GET"])
def add_cafe():
    form = CafeForm()
    if request.method == 'POST':
        if not form.validate_on_submit():
            return render_template('add.html', form=form)
        else:
            row = f"{request.form['cafe_name']},{request.form['location']},{request.form['open']},{request.form['close']},{request.form['coffee']},{request.form['wifi']},{request.form['power']}\n"
            with open('cafe-data.csv', 'a', encoding='utf8') as file:
                file.writelines(row)
            return render_template('add.html', form=form)
    else:
        return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    print(list_of_rows)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
