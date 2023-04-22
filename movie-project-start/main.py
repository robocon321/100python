from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, NumberRange
import requests
import os

API_KEY = os.environ['API_KEY']

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_ECHO'] = True

Bootstrap(app)
db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, db.Sequence('seq_reg_id', start = 1, increment = 1), primary_key=True)
    title = db.Column(db.String(250), nullable=False, unique=True)
    year = db.Column(db.Integer, nullable = False)
    description = db.Column(db.String(1000))
    rating = db.Column(db.Float, nullable = False)
    ranking = db.Column(db.Integer)
    review = db.Column(db.Integer)
    img_url = db.Column(db.String(1000), nullable = False)

class MovieFormUpdate(FlaskForm):
    rating = FloatField(label = "Rating", validators=[DataRequired(), NumberRange(min=0, max=10)])
    review = StringField(label = "Review", validators=[DataRequired()])
    submit = SubmitField(label = "Submit")

class MovieFormAdd(FlaskForm):
    title = StringField(label = "Title", validators=[DataRequired()])
    submit = SubmitField(label = "Submit")

db.create_all()

@app.route("/")
def home():
    movies = Movie.query.order_by(Movie.rating.desc()).all()
    return render_template("index.html", movies = movies)

@app.route("/edit", methods=["GET", "POST"])
def update():
    form = MovieFormUpdate()
    id = request.args['id']
    movie = Movie.query.get(id)
    if(request.method == "GET"):
        return render_template("edit.html", movie = movie, form = form)
    else:
        if form.validate_on_submit():
            movie.rating = request.form['rating']
            movie.review = request.form['review']
            db.session.commit()
            return redirect('/')
        else:
            return render_template("edit.html", movie=movie, form=form)


@app.route('/delete')
def delete():
    id = request.args['id']
    movie = Movie.query.get(id)
    db.session.delete(movie)
    db.session.commit()
    return redirect('/')

@app.route('/add', methods = ['POST', 'GET'])
def add():
    form = MovieFormAdd()
    if request.method == 'POST':
        if form.validate_on_submit():
            query = request.form['title']
            response = requests.get(url = f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&language=en-US&query={query}&page=1&include_adult=false')
            response.raise_for_status()
            movies = response.json()['results']
            return render_template('select.html', movies=movies)
        else:
            return render_template('add.html', form = form)
    else:
        if 'id' in request.args:
            id = request.args["id"]
            response = requests.get(url = f'https://api.themoviedb.org/3/movie/{id}?api_key={API_KEY}&language=en-US')
            response.raise_for_status
            data = response.json()

            movie = Movie()
            movie.id = data['id']
            movie.title = data['title']
            movie.description = data['overview']
            movie.rating = data['vote_average']
            movie.year = data['release_date'][0:5]
            movie.review = ''
            movie.ranking = data['runtime']
            if not data['backdrop_path'] == None:
                movie.img_url = data['backdrop_path']
            else:
                movie.img_url = 'https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg'
            db.session.add(movie)
            db.session.commit()

            return redirect('/')
        else:
            return render_template('add.html', form = form)


if __name__ == '__main__':
    app.run(debug=True)
