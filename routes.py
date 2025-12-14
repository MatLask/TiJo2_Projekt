from flask import Blueprint, render_template, request, redirect, url_for
from db import db
from models import Event

main = Blueprint('main', __name__)

@main.route('/')
def index():
    events = Event.query.order_by(Event.date).all()
    return render_template('index.html', events=events)

@main.route('/event/new', methods=['GET', 'POST'])
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
        return redirect(url_for('main.index'))

    return render_template('new.html')

@main.route('/event/edit/<int:event_id>', methods=['GET', 'POST'])
def edit_event(event_id):
    ev = Event.query.get_or_404(event_id)

    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        date = request.form.get('date', '').strip()
        location = request.form.get('location', '').strip()
        description = request.form.get('description', '').strip()

        if not title or not date:
            return render_template('edit.html', error="Title and date required", form=request.form, event=ev)

        ev.title = title
        ev.date = date
        ev.location = location
        ev.description = description
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('edit.html', event=ev)

@main.route('/event/delete/<int:event_id>')
def delete_event(event_id):
    ev = Event.query.get_or_404(event_id)
    db.session.delete(ev)
    db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/event/toggle_done/<int:event_id>')
def toggle_done(event_id):
    ev = Event.query.get_or_404(event_id)
    ev.done = not ev.done
    db.session.commit()
    return redirect(url_for('main.index'))
