from celery import Celery

app = Celery('basic', broker='redis://:Somya@123MdPdP@668209257756@localhost:6379/0')

@app.task
def add(x,y):
    return x+y