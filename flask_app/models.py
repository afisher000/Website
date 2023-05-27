from flask_app import db, app

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    WO = db.Column(db.String(20), nullable=False)
    WD = db.Column(db.String(20), nullable=False)
    LO = db.Column(db.String(20), nullable=False)
    LD = db.Column(db.String(20), nullable=False) 
    score = db.Column(db.Integer, nullable=False)
    color = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"{self.id}: {self.WO},{self.WD} beat {self.LO},{self.LD} 10-{self.score} with {self.color}"

with app.app_context():
    db.create_all()
#     #game1 = Games(WO='andy', score=5)
#     db.session.add(game1)
#     db.session.commit()

#     games = Games.query.all()
#     for game in games:
#         print(game)