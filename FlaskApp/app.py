from flask import Flask, render_template, json, request
from flaskext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash

mysql = MySQL()
app = Flask(__name__)


# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'khong'
app.config['MYSQL_DATABASE_PASSWORD'] = 'khong'
app.config['MYSQL_DATABASE_DB'] = 'FlaskBlogApp'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
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


@app.route('/signUp',methods=['POST'])
def signUp():

    # read the posted values from the UI
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']

    # validate the received values
    if _name and _email and _password:
        return json.dumps({'html':'<span>All fields good !!</span>'})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})

## server side implementation for signup
#@app.route('/signUp',methods=['POST'])
#def signUp():
#
#    try:
#
#        # read the posted values from the UI
#        _name = request.form['inputName']
#        _email = request.form['inputEmail']
#        _password = request.form['inputPassword']
#
#        # validate the received values
#        if _name and _email and _password:
#
#            # all good, lets call MySQL
#            conn = mysql.connect()
#            cursor = conn.cursor()
#            _hashed_password = generate_password_hash(_password)
#            cursor.callproc('sp_createUser',(_name,_email,_hashed_password))
#            data = cursor.fetchall()
#
#            if len(data) is 0:
#                conn.commit()
#                return json.dumps({'message':'User created successfully !'})
#            else:
#                return json.dumps({'error':str(data[0])})
#        else:
#            return json.dumps({'html':'<span>Enter the required fields</span>'})
#    except Exception as e:
#        return json.dumps({'error':str(e)})
#    finally:
#        cursor.close()
#        conn.close()
#
#


@app.route('/showSignin')
def showSignin():
    return render_template('signin.html')



@app.route('/userHome')
def userHome():
    return render_template('userHome.html')


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

if __name__ == "__main__":
   app.run()
