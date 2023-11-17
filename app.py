import os
from flask import Flask, request, jsonify
import boto3
import hashlib
import time
from botocore.exceptions import ClientError 

app = Flask(__name__)

	
USERS_TABLE = os.environ['USERS_TABLE']
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(USERS_TABLE)

	
@app.route("/")
def hello():
    return "Hello World!"

@app.route('/users/create', methods=['POST'])
def createUser():
    try:
        # recupero il body
        data = request.get_json()

        # genero un hash del timestamp corrente da usare come id
        next_id = hashlib.sha1(str(int(time.time() * 1000)).encode()).hexdigest() 

        # salvo il record
        table.put_item(
            Item={
                'id': next_id,
                'firstname': data['firstname'],
                'lastname': data['lastname'],
                'email': data['email'],
                'password': hashlib.sha1(str(data['password']).encode()).hexdigest()
            }
        )

        return jsonify({'message':'User "'+str(next_id)+'" created successfully'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/users/<string:user_id>', methods=['GET'])
def getUserById(user_id):

    try:
        # recupero l'utente
        result = table.get_item(
            Key={
                'id': user_id
            }
        )
        item = result.get('Item')
    except ClientError as e:
        return jsonify({'error': str(e)}), 500

    # utente non trovato
    if not item:
        return jsonify({'error': 'User not found'}), 404

    
    item.pop('password') # rimuovo la password dai dati

    return jsonify(item), 200