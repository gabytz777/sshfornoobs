from flask import Flask, render_template, request, jsonify
from ssh_client import run_ssh_commands
import webbrowser
import threading

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/fetch", methods=["POST"])
def fetch():
    data = request.json
    host = data.get("host")
    username = data.get("username")
    password = data.get("password")

    try:
        stats = run_ssh_commands(host, username, password)
        return jsonify({"ok": True, "stats": stats})
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)})

def open_browser():
    webbrowser.open("http://localhost:80085")

if __name__ == "__main__":
    threading.Timer(1.2, open_browser).start()
    app.run(port=80085, debug=False)
