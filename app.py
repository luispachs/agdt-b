from flask import Flask,jsonify
from src.routes.auth import register,login,logout,authorize
from src.routes.Plan import getPlanes
from src.routes.Store import getAll
from flask_cors import CORS
from dotenv import load_dotenv
import os


os.environ['AGENDATE_DIR']= os.getcwd()
load_dotenv()

app = Flask(__name__)
CORS(app=app,resources={ "/api/v1/*": {
    'Access-Control-Allow-Origin':'*',
    'Access-Control-Allow-Methods': '*',
    'Access-Control-Allow-Headers': 'Content-type,Application-Content'
    }},methods=['POST','GET','DELETE','PATH'],supports_credentials=True)
apiPrefix = '/api/v1/'




@app.route("/",methods=["GET","PUT","POST","DELETE"])
def main():
    return jsonify({"message":"method had not been implemented","status":400})

app.add_url_rule(apiPrefix+"auth/register",view_func=register,methods=['POST'])
app.add_url_rule(apiPrefix+"plan",view_func=getPlanes,methods=['GET'])
app.add_url_rule(apiPrefix+"stores",view_func=getAll,methods=['GET'])
app.add_url_rule(apiPrefix+"auth/login",view_func=login,methods=['POST'])
app.add_url_rule(apiPrefix+"auth/logout",view_func= logout, methods=['POST'])
app.add_url_rule(apiPrefix+"auth/authorize",view_func=authorize,methods=['POST'])
# Secure Routes, this need to authentication Bearer
# Use auth.authorize function to validate



if __name__ == '__main__':
    app.run()