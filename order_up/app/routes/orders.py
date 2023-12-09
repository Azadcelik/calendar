from flask import Blueprint
from flask_login import login_required
from flask import render_template

bp = Blueprint('orders',__name__,url_prefix='')

@bp.route("/")
@login_required
def index():
    return render_template('orders.html')