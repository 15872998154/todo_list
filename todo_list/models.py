from todo_list import db
from datetime import datetime


class List(db.Model):
    _tablename_ =  'To-do-list'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.now, nullable=False)
    title = db.Column(db.String(250),index=True,unique=True)
    description = db.Column(db.Text,index=True)
    status = db.Column(db.String(20), index=True)

    def __repr__(self):
        return    ' ' + self.title