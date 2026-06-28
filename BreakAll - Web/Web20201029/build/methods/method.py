from flask import Flask,request,abort,make_response

app = Flask(__name__)

method = ['GET','POST','OPTIONS','FLAGISHERE']

@app.route('/', methods=method)
def method():
    if not request.method:
        abort(404)

    resp = make_response('I\'m afraid that there is nothing you want here')
                        
    if request.method == 'FLAGISHERE':
        return "Yep. Here is your secret: FLAG{Y0U_Know_h0w2requestHTTP_N0W}"
    elif request.method == 'OPTIONS':
        resp.headers['Allow'] = 'POST, OPTIONS, HEAD, FLAGISHERE, GET'
    return resp


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
