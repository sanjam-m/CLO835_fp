from flask import Flask
import os
import json
import subprocess
from flask import render_template
import socket
import mysql.connector
import boto3

app = Flask(__name__)

DB_Host = os.environ.get('DB_Host') or "localhost"
DB_Database = os.environ.get('DB_Database') or "mysql"
DB_User = os.environ.get('DB_User') or "root"
DB_Password = os.environ.get('DB_Password') or "paswrd"
clo835 = os.environ.get('clo835')
group_name = os.environ.get('GROUP_NAME')
if os.path.exists('/clo835/config/image_url'):
    s3_url_file = open('/clo835/config/image_url') 
    json_data = json.load(s3_url_file)
else: 
    json_data = {}

print("Background image urls from S3 bucket: ", json_data)

@app.route("/")
def main():
    db_connect_result = False
    err_message = ""
    try:
        mysql.connector.connect(host=DB_Host, database=DB_Database, user=DB_User, password=DB_Password)
        color = '#39b54b'
        db_connect_result = True
        image_url = json_data[""] if json_data else "Not Available"
    except Exception as e:
        color = '#ff3f3f'
        err_message = str(e)
        image_url = json_data[""] if json_data else "Not Available"

    return render_template('hello.html', debug="Environment Variables: DB_Host=" + (os.environ.get('DB_Host') or "Not Set") + "; DB_Database=" + (os.environ.get('DB_Database')  or "Not Set") + "; DB_User=" + (os.environ.get('DB_User')  or "Not Set") + "; DB_Password=" + (os.environ.get('DB_Password')  or "Not Set") + "; " + err_message, db_connect_result=db_connect_result, name=socket.gethostname(), color=color, group=group, image_url=image_url, clo835=clo835)

@app.route("/debug")
def debug():
    color = '#2196f3'
    return render_template('hello.html', debug="Environment Variables: DB_Host=" + (os.environ.get('DB_Host') or "Not Set") + "; DB_Database=" + (os.environ.get('DB_Database')  or "Not Set") + "; DB_User=" + (os.environ.get('DB_User')  or "Not Set") + "; DB_Password=" + (os.environ.get('DB_Password')  or "Not Set"), color=color)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81)
