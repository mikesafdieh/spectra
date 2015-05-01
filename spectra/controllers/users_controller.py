from spectra import app
from spectra.models import db
from spectra.models.user import User
from flask import render_template, redirect, url_for, request
from IPython import embed

#
# List Users
#

@app.route("/users")
def index():
    users = User.query.all()
    return render_template("users/index.html", users=users)

#
# Show a User
#

@app.route("/users/<int:id>")
def show(id):
    user = User.query.get_or_404(id)
    return render_template("users/show.html", user=user)

#
# Create a User
#

@app.route("/users/new", methods=["GET"])
def new():
    return render_template("users/new.html")

@app.route("/users/new", methods=["POST"])
def create():
    user = User(request.form["email"])
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('show', id=user.id))

#
# Edit a User
#

@app.route("/users/<int:id>/edit")
def edit(id):
    user = User.query.get_or_404(id)
    return render_template("users/edit.html", user=user)

@app.route("/users/<int:id>/update", methods=['POST'])
def update(id):
    user = User.query.get_or_404(id)
    user.email = request.form["email"]
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('show', id=id))

#
# Delete a User
#

@app.route("/users/<int:id>/destroy")
def destroy(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('index'))