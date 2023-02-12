from flask import Flask, render_template, jsonify
import socket

app = Flask(__name__)


def fetch_details():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
    except:
        print("Unable to get Hostname and IP Address")
    return str(host_name), str(host_ip)


@app.route("/")
def hello_world():
    return "<p> Hello World </p>"


@app.route("/health")
def get_health():
    return jsonify(
        status= "UP"
    )

@app.route("/details")
def get_details():
    hostname, ip = fetch_details()
    return render_template("index.html", hostname=hostname, ipaddress=ip)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)