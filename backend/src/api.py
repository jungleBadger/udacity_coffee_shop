import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS
from werkzeug.datastructures import ImmutableMultiDict

from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)
'''
@TODO uncomment the following line to initialize the datbase [DONE]
'''
db_drop_and_create_all()

## ROUTES
'''
@TODO implement endpoint GET /drinks [DONE]
'''


@app.route('/drinks', methods=['GET'], endpoint='get_drinks')
def drinks():
    """
    Public permission
    This API fetches all drinks with a short description
    Return the drinks array or the error handler
    """
    try:
        return json.dumps({
            'success':
            True,
            'drinks': [drink.short() for drink in Drink.query.all()]
        }), 200
    except:
        return json.dumps({
            'success': False,
            'error': "An error occurred"
        }), 500


'''
@TODO implement endpoint POST /drinks [DONE]
'''


@app.route('/drinks', methods=['POST'], endpoint='post_drink')
@requires_auth('post:drinks')
def drinks(f):
    """
     post:drinks permission
     This API creates a new drink and returns its long description
     Return the created drink info or the error handler
     """

    data = dict(request.form or request.json or request.data)
    drink = Drink(title=data.get('title'),
                  recipe=data.get('recipe') if type(data.get('recipe')) == str
                  else json.dumps(data.get('recipe')))
    try:
        drink.insert()
        return json.dumps({'success': True, 'drink': drink.long()}), 200
    except:
        return json.dumps({
            'success': False,
            'error': "An error occurred"
        }), 500


'''
@TODO implement endpoint GET /drinks-detail [DONE]
'''


@app.route('/drinks-detail', methods=['GET'], endpoint='drinks_detail')
@requires_auth('get:drinks-detail')
def drinks_detail(f):
    """
        Public permission
        This API fetches all drinks with a long description
        Return the drinks array or the error handler
        """
    try:
        return json.dumps({
            'success':
            True,
            'drinks': [drink.long() for drink in Drink.query.all()]
        }), 200
    except:
        return json.dumps({
            'success': False,
            'error': "An error occurred"
        }), 500


'''
@TODO implement endpoint PATCH /drinks/<id> [DONE]
'''


@app.route('/drinks/<id>', methods=['PATCH'], endpoint='patch_drink')
@requires_auth('patch:drinks')
def drinks(f, id):
    """
     patch:drinks permission
     This API updates a drink if it exists
     Return the updated drink info or the error handler
     OBS: I would rather return a single object instead of an array, but POSTman test once again enforces it
     """
    try:
        data = dict(request.form or request.json or request.data)
        drink = drink = Drink.query.filter(Drink.id == id).one_or_none()
        if drink:
            drink.title = data.get('title') if data.get(
                'title') else drink.title
            recipe = data.get('recipe') if data.get('recipe') else drink.recipe
            drink.recipe = recipe if type(recipe) == str else json.dumps(
                recipe)
            drink.update()
            return json.dumps({'success': True, 'drinks': [drink.long()]}), 200
        else:
            return json.dumps({
                'success':
                False,
                'error':
                'Drink #' + id + ' not found to be edited'
            }), 404
    except:
        return json.dumps({
            'success': False,
            'error': "An error occurred"
        }), 500


'''
@TODO implement endpoint DELETE /drinks/<id> [DONE]
'''


@app.route('/drinks/<id>', methods=['DELETE'], endpoint='delete_drink')
@requires_auth('patch:drinks')
def drinks(f, id):
    """
     delete:drinks permission
     This API deletes a drink if it exists
     Return the deleted drink info or the error handler
     """
    try:
        drink = drink = Drink.query.filter(Drink.id == id).one_or_none()
        if drink:
            drink.delete()
            return json.dumps({'success': True, 'drink': id}), 200
        else:
            return json.dumps({
                'success':
                False,
                'error':
                'Drink #' + id + ' not found to be deleted'
            }), 404
    except:
        return json.dumps({
            'success': False,
            'error': "An error occurred"
        }), 500


## Error Handling
'''
Example error handling for unprocessable entity
'''


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


@app.errorhandler(400)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": "Check the body request"
    }), 400


'''
@TODO implement error handler for Not Found - DONE 
'''


@app.errorhandler(404)
def unprocessable(error):
    """
     Propagates the formatted 404 error to the response
     """
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404


'''
@TODO implement error handler for AuthError - DONE 
'''


@app.errorhandler(AuthError)
def handle_auth_error(ex):
    """
    Receive the raised authorization error and propagates it as response
    """
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response
