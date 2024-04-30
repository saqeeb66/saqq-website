from flask import Flask, render_template,jsonify

app = Flask(__name__)
COURSES = [{
    'id': 1,
    'title': 'Data Analyst',
    'cost': 'Rs-5000',
    'Maxhours': '86hrs'
}, {
    'id': 2,
    'title': 'python full course',
    'cost': 'Rs-6000',
    'Maxhours': '60hrs'
}, {
    'id': 3,
    'title': 'java full course',
    'cost': '7000',
    'Maxhours': '50hrs'
}, {
    'id': 4,
    'title': 'c-programming',
    'cost': 'Rs-3000',
    'Maxhours': '48hrs'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', courses=COURSES ,company_name='SYEDS')

@app.route("/api/COURSES")
def course_list():
  return jsonify(COURSES)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
