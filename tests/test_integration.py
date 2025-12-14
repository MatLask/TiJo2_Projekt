import pytest
from app import create_app
from db import db
from models import Event

@pytest.fixture
def app():
    app = create_app({'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:', 'TESTING': True})
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_index_route(client):
    ev = Event(title="Event 1", date="2025-12-14")
    db.session.add(ev)
    db.session.commit()
    response = client.get('/')
    assert response.status_code == 200
    assert b'Event 1' in response.data

def test_new_event_route_get(client):
    response = client.get('/event/new')
    assert response.status_code == 200
    assert b'Add New Event' in response.data

def test_new_event_route_post(client):
    response = client.post('/event/new', data={'title':'Integration Test','date':'2025-12-20','location':'TestLoc','description':'Desc'}, follow_redirects=True)
    assert response.status_code == 200
    assert db.session.query(Event).filter_by(title='Integration Test').first() is not None

def test_edit_event_route_get(client):
    ev = Event(title="EditMe", date="2025-12-21")
    db.session.add(ev)
    db.session.commit()
    response = client.get(f'/event/edit/{ev.id}')
    assert response.status_code == 200
    assert b'Edit Event' in response.data

def test_edit_event_route_post(client):
    ev = Event(title="OldTitle", date="2025-12-22")
    db.session.add(ev)
    db.session.commit()
    client.post(f'/event/edit/{ev.id}', data={'title':'NewTitle','date':'2025-12-23','location':'Loc','description':'Desc'}, follow_redirects=True)
    updated_event = db.session.get(Event, ev.id)
    assert updated_event.title == 'NewTitle'

def test_delete_event_route(client):
    ev = Event(title="DeleteRoute", date="2025-12-24")
    db.session.add(ev)
    db.session.commit()
    client.get(f'/event/delete/{ev.id}', follow_redirects=True)
    deleted_event = db.session.get(Event, ev.id)
    assert deleted_event is None

def test_toggle_done_route(client):
    ev = Event(title="ToggleRoute", date="2025-12-25")
    db.session.add(ev)
    db.session.commit()
    client.get(f'/event/toggle_done/{ev.id}', follow_redirects=True)
    toggled_event = db.session.get(Event, ev.id)
    assert toggled_event.done is True

def test_index_shows_multiple_events(client):
    ev1 = Event(title="E1", date="2025-12-26")
    ev2 = Event(title="E2", date="2025-12-27")
    db.session.add_all([ev1, ev2])
    db.session.commit()
    response = client.get('/')
    assert b'E1' in response.data
    assert b'E2' in response.data

def test_invalid_edit_id(client):
    response = client.get('/event/edit/999')
    assert response.status_code == 404

def test_invalid_delete_id(client):
    response = client.get('/event/delete/999')
    assert response.status_code == 404
