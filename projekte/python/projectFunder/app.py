from flask import Flask, request, render_template
import user
import connect
import userStore
import threading
import csv
import re


app = Flask(__name__, template_folder='template')

userList = []
userList.append(user.User("Bill", "Gates"))
userList.append(user.User("Steve", "Jobs"))
userList.append(user.User("Larry", "Page"))
userList.append(user.User("Sergey", "Brin"))
userList.append(user.User("Larry", "Ellison"))

def csv_reader(path):
    with open(path, "r") as csvfile:
        tmp = {}
        reader = csv.reader(csvfile, delimiter='=')
        for line in reader:
            tmp[line[0]] = line[1]
    return tmp

config = csv_reader("properties.settings")

@app.route('/hello', methods=['GET'])
def helloGet():
    return render_template('hello.html', users=userList)


@app.route('/hello', methods=['POST'])
def helloPost():
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')

    if firstname is not None and lastname is not None and firstname and lastname:
        with threading.Lock():
            userList.append(user.User(firstname, lastname))

    return render_template('hello.html', users=userList)


@app.route('/projectFunder', methods=['GET'])
def project():

    try:
        dbExists = connect.DBUtil().checkDatabaseExistsExternal()
        if dbExists:
            db2exists = 'vorhanden! Supi!'
        else:
            db2exists = 'nicht vorhanden :-('
    except Exception as e:
        print(e)

    return render_template('project.html', db2exists=db2exists)

@app.route('/addUser', methods=['GET'])
def addUser():
    try:
        userSt = userStore.UserStore()
        userToAdd = user.User("Max", "Mustermann")
        userSt.addUser(userToAdd)
        userSt.completion()

        # ...
        # mach noch mehr!
    except Exception as e:
        print(e)
        return "Failed!"
    finally:
        userSt.close()


if __name__ == "__main__":
    port = int("9" + re.match(r"([a-z]+)([0-9]+)", config["username"], re.I).groups()[1])
    app.run(host='0.0.0.0', port=port, debug=True)
