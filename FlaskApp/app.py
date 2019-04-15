from flask import Flask
app = Flask(__name__)

# basic route
@app.route("/")
def main():
   return "Hello from myblog.com"

if __name__ == "__main__":
   app.run()
