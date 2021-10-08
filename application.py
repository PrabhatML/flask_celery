import celery
from flask import Flask,jsonify
from tasks import make_celery


app = Flask(__name__)
app.secret_key = "dev"

celery = make_celery(app)

@app.route("/")
def hello_world():

    scrap.delay()

    message = {
        'message':'hello_world'
    }
    resp = jsonify(message)
    return resp

@celery.task()
def scrap():
    print("done!")

app.run(port=5000,debug=True)
