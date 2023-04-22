from flask import Flask, render_template, request
from LoginForm import LoginForm
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = "Hiphopneverdie123"
email = 'robocon321n@gmail.com'
password = '123456789'
Bootstrap(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods = ["GET", "POST"])
def login():
    login_form = LoginForm()
    login_form.validate_on_submit()
    if request.method == 'POST':
        if login_form.errors:
            return render_template('login.html', form=login_form)

        if email == login_form.email.data and login_form.password.data == password:
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form = login_form)


# @app.route('/register', methods=["GET", "POST"])
# def register():
#     if request.method == "POST":
#         new_user = User(
#             email=request.form.get('email'),
#             name=request.form.get('name'),
#             password=request.form.get('password')
#         )
#
#         db.session.add(new_user)
#         db.session.commit()
#
#         return redirect(url_for("secrets"))
#
#     return render_template("register.html")

if __name__ == '__main__':
    app.run(debug=True)