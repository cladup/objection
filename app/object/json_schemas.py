from marshmallow import Schema, fields


class ObjectSchema(Schema):
    """
    JSON Schema for Object model
    """
    id = fields.Integer()
    alias = fields.Str()
    name = fields.Str()
    type = fields.Str()
    status = fields.Str()
    
