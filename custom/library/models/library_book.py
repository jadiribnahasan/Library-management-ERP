from odoo import models, fields


class Book(models.Model):

    _name = "library.book"
    _description = "Book"

    name = fields.Char(string='Book Title', required=True)
    description = fields.Text('Description')
    no_of_pages = fields.Integer('No. of pages')
    publications = fields.Char('Publisher')

    paper_type = fields.Selection(
        string='Paper type',
        selection=[('newsprint', 'News print'), ('fineart', 'Fine art')],
    )
    genre_ids = fields.Many2many("library.book.genre", string="Genre", default=None)
    author_id = fields.Many2many("res.partner", string="Author", copy=False)
