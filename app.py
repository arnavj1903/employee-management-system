from flask import Flask, render_template, redirect, request

app = Flask(__name__)

employeeData = {
    1: {
        'name':'John Doe',
        'ID':'1RVU23CSE076',
        'dept':'SoCSE',
        'job_title':'Student',
        'DOJ':'11/04/23',
        'SalaryPD': 0,
    }
}

@app.route('/')
def home():
    return render_template('index.html', employeeData = employeeData)

@app.route('/add', methods=['GET','POST'])
def add():
    if request.method == 'POST':
        slno = request.form['slno']
        ID = request.form['ID']
        name = request.form['name']
        username = request.form['username']
        dept = request.form['dept']
        email= request.form['email']
        job_title = request.form['job_title']

        employeeData.append({slno:{
        'ID':ID,
        'name':name,
        'username':username,
        'dept':dept,
        'email':email,
        'job_title':job_title,
    }})

    return render_template('add.html', employeeData = employeeData)


@app.route('/update/<int:slno>', methods=['GET', 'POST'])
def update(slno):

    return render_template('update.html', employeeData = employeeData, slno = slno)

if __name__ == "__main__":
    app.run(debug=True)