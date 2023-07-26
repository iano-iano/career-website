from flask import Flask, render_template, jsonify

app = Flask(__name__)
JOBS = [
  {
    "id": 1,
    "title": "Data Scientist",
    "salary": "ksh 500,000",
    "location": "Nakuru",
  },
  {
    "id": 2,
    "title": "Frontend engineer",
    "salary": "ksh 200,000",
    "location": "Naivasha",
  },
  {
    "id": 3,
    "title": "Data Analyst",
    "salary": "ksh 150,000",
    "location": "Mombasa"
  },
  {
    "id": 4,
    "title": "Backend engineer",
    "salary": "ksh 750,000",
    "location": "Nairobi"
  }
]

@app.route("/")
def hello_world():
    return render_template("index.html",
                          jobs=JOBS)

@app.route("/api/jobs")
def json():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)