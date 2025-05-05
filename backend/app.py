from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


# from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)