from marshmallow import Schema, fields


class BookSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    author = fields.Str()
    description = fields.Str()
    painter = fields.Str()
    release_year = fields.Int()
