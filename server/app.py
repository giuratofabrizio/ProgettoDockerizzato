from flask import Flask, jsonify
from pymongo import MongoClient
import os 

app = Flask(__name__)



def get_db():
    client = MongoClient(host='test_mongodb',
                         port=27017, 
                         username='root', 
                         password='pass',
                        authSource="admin")
    db = client["animal_db"]
    return db


@app.route('/')
def ping_server():
    return "Welcome to the world of animals."

@app.route('/simple_json')
def simple_json():
    return jsonify('{saluto:ciao}')

@app.route('/animals')
def get_stored_animals():
    db=""
    try:
        db = get_db()
        _animals = db.animal_tb.find()
        animals = [{"id": animal["id"], "name": animal["name"], "type": animal["type"]} for animal in _animals]
        return jsonify({"animals": animals})
    except:
        pass
    finally:
        if type(db)==MongoClient:
            db.close()

@app.route('/environment')
def env():
    return jsonify(
            {"env":[
                {"MONGO_INITDB_DATABASE": os.environ["MONGO_INITDB_DATABASE"]},
                {"MONGO_INITDB_ROOT_USERNAME": os.environ["MONGO_INITDB_ROOT_USERNAME"]},
                {"MONGO_INITDB_ROOT_PASSWORD": os.environ["MONGO_INITDB_ROOT_PASSWORD"]}
            ]})

@app.route('/newAnimal', methods = ['POST'])
def newAnimal():
    db=""
    db = get_db() #Ottengo l'istanza del DB
    #Cerco l'id maggiore 
    last_animal = db.animal_tb.find_one(sort=[("id", -1)])
    #print(last_animal, flush=True) # In caso di test aggiungere Flush
    #aggiorno l'id
    request.json['id'] = int(last_animal['id']) + 1 
    #inserisco la richiesta
    x = db.animal_tb.insert_one(request.json)
    #creo la risposta per il client
    resp = app.response_class(
        response= json.dumps({"id":request.json['id'], "name":request.json['id'], "type":request.json['type']}),
        status=200,
        mimetype='application/json'
    )
    return resp
    
if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)