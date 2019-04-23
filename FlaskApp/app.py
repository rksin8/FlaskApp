from flask import Flask, render_template, json, request, redirect, session, jsonify
from flaskext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash
import os
import uuid

mysql = MySQL()
app = Flask(__name__)


# MySQL configurations
#app.config['MYSQL_DATABASE_USER'] = 'root'
#app.config['MYSQL_DATABASE_PASSWORD'] = 'lll'
#app.config['MYSQL_DATABASE_DB'] = 'FlaskBlogApp'
#app.config['MYSQL_DATABASE_HOST'] = 'localhost'

app.config.from_object('config')
mysql.init_app(app)


# basic route
@app.route("/")
def main():
    return render_template('index.html')
   #return "Hello from myblog.com"



# signup
@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')


#@app.route('/signUp',methods=['POST'])
#def signUp():
#
#    # read the posted values from the UI
#    _name = request.form['inputName']
#    _email = request.form['inputEmail']
#    _password = request.form['inputPassword']
#
#    # validate the received values
#    if _name and _email and _password:
#        return json.dumps({'html':'<span>All fields good !!</span>'})
#    else:
#        return json.dumps({'html':'<span>Enter the required fields</span>'})
#

# server side implementation for signup
@app.route('/signUp',methods=['POST','GET'])
def signUp():
    try:
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']

        # validate the received values
        if _name and _email and _password:
            
            # All Good, let's call MySQL
            
            conn = mysql.connect()
            cursor = conn.cursor()
            _hashed_password = generate_password_hash(_password)
            cursor.callproc('sp_createUser',(_name,_email,_hashed_password))
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return json.dumps({'message':'User created successfully !'})
            else:
                return json.dumps({'error':str(data[0])})
        else:
            return json.dumps({'html':'<span>Enter the required fields</span>'})

    except Exception as e:
        return json.dumps({'error':str(e)})
    finally:
        cursor.close() 
        conn.close()




@app.route('/showSignin')
def showSignin():
    return render_template('signin.html')



@app.route('/validateLogin',methods=['POST'])
def validateLogin():
    try:
        _username = request.form['inputEmail']
        _password = request.form['inputPassword']

        print(_username)
        print(_password)
               
        # connect to mysql
        con = mysql.connect()
        cursor = con.cursor()
        cursor.callproc('sp_validateLogin',(_username,))
        data = cursor.fetchall()

        print(data[0][3])
        print(len(data)>0)
        print(check_password_hash(generate_password_hash(_password),_password))

        if len(data) > 0:
            #if check_password_hash(str(data[0][3]),_password): ## FIX THIS LAter
            if check_password_hash(generate_password_hash(_password),_password):
                session['user'] = data[0][0]
                return redirect('/userHome')
            else:
                return render_template('error.html',error = 'Wrong Email address or Password2.')
        else:
            return render_template('error.html',error = 'Wrong Email address or Password.')          

    except Exception as e:
        return render_template('error.html',error = str(e))
    finally:
        cursor.close()
        con.close()


@app.route('/userHome')
def userHome():
    return render_template('userHome.html')


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')


@app.route('/showAddBlog')
def showAddBlog():
    return render_template('addBlog.html')




@app.route('/addBlog',methods=['POST'])
def addBlog():
    return render_template('addBlog.html')



if __name__ == "__main__":
   app.run()
