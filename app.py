from flask import Flask
from flask import request

app=Flask(__name__)

# @app.route("/")
# def hello():
#     return{
#         "Result": "First Route"
#     }

# receive data from Twilio when it hits the endpoint
@app.route("/webhook", methods=["POST"])
def webhook():
    # python debugger
    import pdb
    # execution stops here and we can analyze the data received here
    pdb.set_trace()
    
    return "OK",200

if __name__=="__main__":
    app.run(debug=True)