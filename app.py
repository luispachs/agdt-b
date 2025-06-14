from flask import Flask,jsonify
from src.routes.auth import register
from src.routes.Plan import getPlanes
from flask_cors import CORS
from dotenv import load_dotenv
import os


os.environ['AGENDATE_DIR']= os.getcwd()
load_dotenv()

app = Flask(__name__)
CORS(app=app,resources="/api/v1/*",methods=['POST','GET','DELETE','PATH'],supports_credentials=True)
apiPrefix = '/api/v1/'




@app.route("/",methods=["GET","PUT","POST","DELETE"])
def main():
    return jsonify({"message":"method had not been implemented","status":400})

app.add_url_rule(apiPrefix+"auth/register",view_func=register,methods=['POST'])
app.add_url_rule(apiPrefix+"plan",view_func=getPlanes,methods=['GET'])

if __name__ == '__main__':
    app.run()