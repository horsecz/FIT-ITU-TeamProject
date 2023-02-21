from flask import Flask
from flask import request
from controller import Users, Trips

app = Flask(__name__)
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'


@app.route('/login', methods=["POST"])
def login():
    login_data = request.get_json()
    users = Users()
    user_id = users.login(login_data["user"], login_data["pass"])

    return {"user": user_id}


@app.route('/trips/<user_id>')
def trips(user_id: int):
    controller = Trips()
    return controller.get_trips(user_id)


@app.route('/trips')
def all_trips():
    controller = Trips()
    return controller.get_all_trips()


@app.route('/trip/<trip_id>')
def trip(trip_id):
    controller = Trips()
    return controller.get_trip(trip_id)


@app.route('/trip/<trip_id>/<day>', methods=["POST", "OPTIONS"])
def trip_update(trip_id, day):
    controller = Trips()
    return controller.update_trip(trip_id, day)

@app.route('/new%<cityname>%<imgid>%<triplen>')
def trip_add(cityname: str, imgid: str, triplen: str):
    controller = Trips()
    return controller.add_trip(cityname, imgid, triplen)

@app.route('/trip/restore/<trip_id>')
def trip_restore(trip_id):
    controller = Trips()
    return controller.restore_trip(trip_id)

@app.route('/trip/reset/<trip_id>')
def trip_reset(trip_id):
    controller = Trips()
    return controller.reset_trip(trip_id)

@app.route('/delete%<trip_id>')
def trip_delete(trip_id: str):
    controller = Trips()
    return controller.delete_trip(trip_id)