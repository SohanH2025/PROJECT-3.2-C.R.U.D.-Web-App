from flask import Flask, render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///map.db'
db = SQLAlchemy(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    
    
    return render_template('index.html', map=map)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, host="0.0.0.0", port="5421")
