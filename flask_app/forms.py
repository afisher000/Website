from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange


class GameForm(FlaskForm):
    # Change to menus...
    player_validators = [DataRequired(), Length(min=2, max=20)]
    WO = StringField('Winner Offense', validators=player_validators)
    WD = StringField('Winner Defense', validators=player_validators)
    LO = StringField('Loser Offense', validators=player_validators)
    LD = StringField('Loser Defense', validators=player_validators)

    color = SelectField('Winning Color', choices=['Blue','Red'], validators=[DataRequired(), Length(min=2, max=20)])
    score = IntegerField('Score', validators=[NumberRange(min=0, max=9)])
    submit = SubmitField('Add Game')