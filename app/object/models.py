from app import db


class Object(db.Model):
    """
    `objects` table
    """
    __tablename__ = 'objects'
    id = db.Column(db.Integer, primary_key=True)
    alias = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime,  default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime,  default=db.func.current_timestamp(), 
            onupdate=db.func.current_timestamp())

    def __init__(self, alias, name, type, status): 
        self.alias = alias
        self.name = name
        self.type = type
        self.status = status

