from flask import Flask, render_template

BillardAPI = Flask(__name__)

@BillardAPI.route("/")
def index():
    return render_template('index.html')

if __name__=="__main__":
    BillardAPI.run()