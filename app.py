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

@app.route('/', methods=['GET','POST'], defaults={'width': None, 'height': None})
@app.route('/<width>/<height>')
def handle_data(width=None, height=None):

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
        
    
    if not width or not height:
        return """
        <script>
        (() => window.location.href = window.location.href +
        ['', window.innerWidth, window.innerHeight].join('/'))()
        </script>
        """
    #return 'Hello %s (%s, %s)' %(user, width, height)
    #print( width, height)
    #dots = Dot.query.all()
    #return render_template('index.html', dots=dots)
    
    is_full = True
    dots = Dot.query.all()

    for x in range(0,int(width)+1):
        for y in range(-int(height),1): ##for each pixel
            print(x,y)
            print(int(width),int(height))
            is_in_dot = False

            for dot in dots:
                print(dot.id)
                #print(type(dot.x))
                if ((x-dot.x)**2 + (y+dot.y)**2 <= dot.size**2): #if the pixel is in any dot then set is_in_dot = True
                    is_in_dot = True
                    print("is in dot")
                    break

            if not is_in_dot: #if still not in any dot then the screen isn't full
                is_full = False
                print("is not full")
                break
        if not is_in_dot: #if still not in any dot then the screen isn't full
            is_full = False
            print("is not full")
            break

    
    if is_full:
        return "Page is Full"
    else:
        return render_template('index.html', dots=dots)


@app.route('/user/<user>', defaults={'width': None, 'height': None})
@app.route('/user/<user>/<width>/<height>')
def user(user, width=None, height=None):
    if not width or not height:
        return """
        <script>
        (() => window.location.href = window.location.href +
        ['', window.innerWidth, window.innerHeight].join('/'))()
        </script>
        """
    return 'Hello %s (%s, %s)' %(user, width, height)

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
