from flask import Flask, render_template,request,redirect,jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dots.db'
db = SQLAlchemy(app)

class Dot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    x = db.Column(db.Integer)
    y = db.Column(db.Integer)
    def __repr__(self):
        #{"x":self.x, "y":self.y}
        return self.id

@app.route('/data', methods=['GET','POST'])
def handle_data():

    if request.method == 'POST':
        data = request.get_json()
        #print(f"the x corrdinate is {data['x']}")
        new_dot = Dot(x=data['x'], y=data['y'])
        try:
            db.session.add(new_dot)
            db.session.commit()
            return redirect('/')
        except:
            return 'Error adding dot'

@app.route('/')
def index():
    dots = Dot.query.all()
    return render_template('index.html', dots=dots)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, host="0.0.0.0", port="5421")
