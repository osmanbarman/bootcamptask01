from flask import Flask
from flask import jsonify
helloworld = Flask(__name__)

data = {
  "users": [
    {
      "username": "Osman",
      "mail": "osman@test.com"
    },
    {
      "username": "Barman",
      "mail": "barman@test1.com"
    },
    {
      "status": "running",
      "source": "test@test.com"
    }
  ]
}

@helloworld.route("/data")
def run():
    return jsonify(data)
if __name__ == "__main__":
    helloworld.run(host="0.0.0.0", port=int("5000"), debug=True)
