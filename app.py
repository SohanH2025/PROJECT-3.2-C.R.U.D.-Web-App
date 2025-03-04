from flask import Flask, render_template,request,redirect,jsonify
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dots.db'
db = SQLAlchemy(app)

def random_hex_color():
  """Generates a random hex color code."""
  hex_color = '#'
  for _ in range(6):
    hex_color += random.choice('0123456789abcdef')
  return hex_color

class Dot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String(20), nullable=False)
    size = db.Column(db.Integer)
    x = db.Column(db.Integer)
    y = db.Column(db.Integer)
    def __repr__(self):
        #{"x":self.x, "y":self.y}
        return self.id

@app.route('/', methods=['GET','POST'])
def handle_data():

    if request.method == 'POST':
        data = request.get_json()
        #print(f"the x corrdinate is {data['x']}")
        new_dot = Dot(x=data['x'], y=data['y'], color=random_hex_color(), size=random.randint(1, 250))
        try:
            db.session.add(new_dot)
            db.session.commit()
            return redirect('/')
        except:
            return 'Error adding dot'
        
    dots = Dot.query.all()
    return render_template('index.html', dots=dots)


@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Dot.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, host="0.0.0.0", port="5421")
