from flask import render_template, flash, redirect, url_for
from flask_app.forms import GameForm
from flask_app import app, db
from flask_app.models import Game

# %%

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html', title='about')


@app.route("/gamelog")
def gamelog():
    # Get games from database
    with app.app_context():
        games = Game.query.all()
        print(games)
    return render_template('gamelog.html', title='gamelog', games=games)


@app.route("/newgame", methods=['GET','POST'])
def newgame():
    form = GameForm()

    # Check for submission
    if form.validate_on_submit():
        # Add game to database
        game = Game(
            WO=form.WO.data, WD=form.WD.data, LO=form.LO.data, LD=form.LD.data, 
            color=form.color.data, score=form.score.data
        )
        with app.app_context():
            db.session.add(game)
            db.session.commit()


        # Redirect to home page
        flash('Game submitted!', 'success')
        return redirect(url_for('gamelog'))
    
    return render_template('newgame.html', title='Submit Game', form=form)