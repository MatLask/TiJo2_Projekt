from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(32), nullable=False)
    location = db.Column(db.String(120))
    description = db.Column(db.Text)
    done = db.Column(db.Boolean, default=False)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    events = Event.query.order_by(Event.date).all()
    return render_template('index.html', events=events)

@app.route('/event/new', methods=['GET', 'POST'])
def new_event():
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        date = request.form.get('date', '').strip()
        location = request.form.get('location', '').strip()
        description = request.form.get('description', '').strip()
        if not title or not date:
            return render_template('new.html', error="Title and date required", form=request.form)
        ev = Event(title=title, date=date, location=location, description=description)
        db.session.add(ev)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('new.html')

@app.route('/event/delete/<int:event_id>')
def delete_event(event_id):
    ev = Event.query.get_or_404(event_id)
    db.session.delete(ev)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/event/toggle_done/<int:event_id>')
def toggle_done(event_id):
    ev = Event.query.get_or_404(event_id)
    ev.done = not ev.done
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
