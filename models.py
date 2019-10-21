from app import db


class Statistic(db.Model):
    __tablename__ = 'statistics'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    email = db.Column(db.String())
    subject = db.Column(db.String())
    message = db.Column(db.Text())

    def __init__(self, name, email, subject, message):
        self.name = name
        self.email = email
        self.subject = subject
        self.message = message

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'subject': self.subject,
            'message': self.message
        }