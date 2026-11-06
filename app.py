from flask import Flask, request

app = Flask(__name__)
registrations = []
@app.route('/')
def home():
    return '''
    <option>Artificial Intelligence</option>
    <form action="/register" method="post">
        Student Name: <input name="name" required><br><br>
        Roll No: <input name="roll" required><br><br>
        Select Course:
        <select name="course">
            <option>Python</option>
            <option>Java</option>
            <option>Data Science</option>
            <option>Web Development</option>
        </select><br><br>
        <button>Register</button>
    </form>
    <br>
    <a href="/students">View Registrations</a>
    '''
@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    roll = request.form['roll']
    course = request.form['course']
    registrations.append((name, roll, course))
    return 'Registration Successful! <a href="/">Home</a>'
@app.route('/students')
def students():
    result = '<h2>Registered Students</h2>'
    for name, roll, course in registrations:
        result += f'<p>{roll} - {name} - {course}</p>'
    return result + '<a href="/">Home</a>'
if __name__ == '__main__':
    app.run(debug=True)