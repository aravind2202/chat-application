from flask import Flask, render_template
from flask_socketio import SocketIO, send

# create flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

# use threading mode (best for Windows)
socketio = SocketIO(app, async_mode='threading')

# homepage
@app.route('/')
def index():
    return render_template("index.html")

# receive and broadcast messages
@socketio.on("message")
def handle_message(msg):
    print("Message:", msg)
    send(msg, broadcast=True)

# run server
if __name__ == "__main__":
    socketio.run(app, host="127.0.0.1", port=8000, debug=True)