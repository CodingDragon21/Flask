from flask import Flask,jsonify,request

app = Flask(__name__)
tasks = [
    {
        'contact' : '3849502948',
        'name' : u'Bob',
        'id' : 1,
        'done' : False

    },
    {
        'contact': '3940392882',
        'name' : u'Larry',
        'id' : 2,
        'done': False

    }

]
@app.route("/")
def function():
    return "Contacts"


@app.route('/add-task',methods = ['POST'])
def addTask():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Add Data!"
        },400)

    task = {
        'id': tasks[-1]['id'] + 1,
        'name': request.json['name'],
        'contact': request.json.get('contact',''),
        'done': False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully"
    })
            

if (__name__ == "__main__"):
    app.run(debug=True)