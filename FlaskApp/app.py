from flask import Flask, render_template
app = Flask(__name__)

# basic route
@app.route("/")
def main():
    return render_template('index.html')
   #return "Hello from myblog.com"

if __name__ == "__main__":
   app.run()
