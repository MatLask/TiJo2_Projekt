import pytest
from app import create_app
from db import db
from models import Event

@pytest.fixture
def app():
    test_app = create_app({'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:', 'TESTING': True})
    with test_app.app_context():
        db.create_all()
        yield test_app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_event_creation(app):
    event = Event(title="Test Event", date="2025-12-14", location="Test", description="Desc")
    db.session.add(event)
    db.session.commit()
    assert Event.query.count() == 1
    assert Event.query.first().title == "Test Event"

def test_event_default_done(app):
    event = Event(title="Event 2", date="2025-12-15")
    db.session.add(event)
    db.session.commit()
    assert Event.query.first().done is False

def test_event_edit_title(app):
    event = Event(title="Old", date="2025-12-16")
    db.session.add(event)
    db.session.commit()
    event.title = "New"
    db.session.commit()
    assert Event.query.first().title == "New"

def test_event_edit_date(app):
    event = Event(title="Event", date="2025-12-16")
    db.session.add(event)
    db.session.commit()
    event.date = "2025-12-20"
    db.session.commit()
    assert Event.query.first().date == "2025-12-20"

def test_event_edit_location(app):
    event = Event(title="Event", date="2025-12-16", location="OldLoc")
    db.session.add(event)
    db.session.commit()
    event.location = "NewLoc"
    db.session.commit()
    assert Event.query.first().location == "NewLoc"

def test_event_edit_description(app):
    event = Event(title="Event", date="2025-12-16", description="OldDesc")
    db.session.add(event)
    db.session.commit()
    event.description = "NewDesc"
    db.session.commit()
    assert Event.query.first().description == "NewDesc"

def test_event_delete(app):
    event = Event(title="DeleteMe", date="2025-12-17")
    db.session.add(event)
    db.session.commit()
    db.session.delete(event)
    db.session.commit()
    assert Event.query.count() == 0

def test_event_toggle_done(app):
    event = Event(title="Toggle", date="2025-12-18")
    db.session.add(event)
    db.session.commit()
    event.done = not event.done
    db.session.commit()
    assert Event.query.first().done is True

def test_multiple_events(app):
    ev1 = Event(title="E1", date="2025-12-19")
    ev2 = Event(title="E2", date="2025-12-20")
    db.session.add_all([ev1, ev2])
    db.session.commit()
    assert Event.query.count() == 2

def test_query_ordering(app):
    ev1 = Event(title="First", date="2025-12-19")
    ev2 = Event(title="Second", date="2025-12-18")
    db.session.add_all([ev1, ev2])
    db.session.commit()
    events = Event.query.order_by(Event.date).all()
    assert events[0].title == "Second"
