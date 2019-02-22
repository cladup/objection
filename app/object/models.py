from app import db


STATUS_STAGING = 'staging'
STATUS_ALIASED = 'aliased'
STATUS_UNALIASED = 'unaliased'


class Object(db.Model):
    """
    `objects` table
    """
    __tablename__ = 'objects'
    id = db.Column(db.Integer, primary_key=True)
    alias_link = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime,  default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime,  default=db.func.current_timestamp(), 
            onupdate=db.func.current_timestamp())

    def __init__(self, alias_link, name, type):
        self.alias_link = alias_link
        self.name = name
        self.type = type
        self.status = STATUS_STAGING

    def save(self):
        """
        Save object information
        """
        db.session.add(self)
        db.session.commit()

    def alias(self, alias_link):
        """
        Alias object with name
        """
        self.alias_link = alias_link
        self.status = STATUS_ALIASED
        db.session.add(self)
        db.session.commit()

    def unalias(self):
        """
        Unalias object and change state
        """
        self.status = STATUS_UNALIASED
        db.session.add(self)
        db.session.commit()

