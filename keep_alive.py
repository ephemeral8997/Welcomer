from flask import Flask
from threading import Thread

print('Hosted Forever!')

app = Flask(__name__)

@app.route('/')
def home():
    return "Hosted 24/7!"

def run():
  app.run(host='8.8.8.8',port=8888)

def keep_alive():
    server = Thread(target=run)
    server.start()

    """
    HOSTING
    
    THAT IS USING A PORT TO MAKE IT ONLINE FOREVER
    
    IT STILLS UNDER DEVELOPING
    """
    