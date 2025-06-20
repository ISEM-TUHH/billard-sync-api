from flask import Flask, render_template, request, jsonify

BillardAPI = Flask(__name__)

@BillardAPI.route("/")
def index():
    return render_template('index.html')

@BillardAPI.route("/ask_for_game")
def ask_for_game():
    return jsonify({"state": 0})

if __name__=="__main__":
    BillardAPI.run()