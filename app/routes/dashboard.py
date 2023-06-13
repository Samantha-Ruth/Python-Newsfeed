from flask import Blueprint, render_template, session

bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@bp.route('/')
def dash():
  return render_template(
    'dashboard.html',
    loggedIn=session.get('loggedIn')
  )


@bp.route('/edit/<id>')
def edit(id):
  return render_template('edit-post.html')