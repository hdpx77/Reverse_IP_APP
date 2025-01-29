from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def get_reverse_ip():
    client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    reversed_ip = ".".join(client_ip.split(".")[::-1])
    return reversed_ip, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
