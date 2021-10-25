from odoo import models, fields


class Genre(models.Model):

    _name = "library.book.genre"
    _description = "Book Genre type"

    name = fields.Char(string='Genre', required=True)
