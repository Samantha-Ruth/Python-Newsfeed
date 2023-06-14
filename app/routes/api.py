from flask import Blueprint, request, jsonify, session
from app.models import User, Post, Comment, Vote
from app.db import get_db

import sys

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/users', methods=['POST'])
def signup():
  data = request.get_json()
  db = get_db()

  try:
  # Attempt to create a new user
    newUser = User(
        username = data['username'],
        email = data['email'],
        password = data['password']
    )
    # save in database
    db.add(newUser)
    db.commit()
  except:
    # insert failed, send error message to CLI
    print(sys.exe_info()[0])
    # insert failed, so rollback and send error message to front end
    db.rollback()
    return jsonify(message = 'Signup failed'), 500
  
  session.clear()
  session['user_id'] = newUser.id
  session['loggedIn'] = True
  
  print(newUser.id)
  return jsonify(id = newUser.id) 

@bp.route('/users/logout', methods=['POST'])
def logout():
  # remove session variables
  session.clear()
  return '', 204

@bp.route('/users/login', methods=['POST'])
def login():
  data = request.get_json()
  db = get_db()
  try:
    user = db.query(User).filter(User.email == data['email']).one()
  except:
    print(sys.exc_info()[0])
    return jsonify(message = 'Incorrect credentials'), 400

  if user.verify_password(data['password']) == False:
    return jsonify(message = 'Incorrect credentials'), 400

  session.clear()
  session['user_id'] = user.id
  session['loggedIn'] = True

  return jsonify(id = user.id)

@bp.route('/comments', methods=['POST'])
def comment():
  data = request.get_json()
  db = get_db()

  try:
    # Attempt to create a new comment
        newComment = Comment(
            comment_text = data['comment_text'],
            post_id = data['post_id'],
            user_id = session.get('user_id')
        )
        # save in database
        db.add(newComment)
        db.commit()
  except:
        # insert failed, send error message to CLI
        print(sys.exe_info()[0])
        # insert failed, so rollback and send error message to front end
        db.rollback()
        return jsonify(message = 'Comment failed'), 500
  
  return jsonify(id = newComment.id)
