from flask import Flask
from flask import request

app=Flask(__name__)

@app.route("/")
def hello():
    return{
        "Result": "First Route"
    }

# receive data from Twilio when it hits the endpoint
@app.route("/webhook", methods=["POST"])
def webhook():
    message = request.form["message"]
    return{
        "Result": message
    }

if __name__=="__main__":
    app.run(debug=True)