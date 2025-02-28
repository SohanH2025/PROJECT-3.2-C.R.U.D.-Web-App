from flask import Flask, render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dots.db'
db = SQLAlchemy(app)

class Dot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    x = db.Column(db.Integer)
    y = db.Column(db.Integer)
    def __repr__(self):
        return {"x":self.x, "y":self.y}

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        x = request.form['x']
        y = request.form['y']
        new_dot = Dot(x=x, y=y)
        try:
            db.session.add(new_dot)
            db.session.commit()
            return redirect('/')
        except:
            return 'Error adding dot'
        
    dots = Dot.query.all()
    return render_template('index.html', dots=dots)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, host="0.0.0.0", port="5421")
