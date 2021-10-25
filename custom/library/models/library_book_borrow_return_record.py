from odoo import api, models, fields
import datetime
from dateutil.relativedelta import relativedelta


class BookBorrowReturn(models.Model):
    _name = 'library.book.borrow.return.record'
    _description = 'Record of Book Borrow and Return'

    name = fields.Char('title', compute="_get_title")
    book_ids = fields.Many2many('library.book', string='Books Borrowed')
    member_id = fields.Many2one('res.partner', string='Borrower', required=True)
    borrow_date = fields.Date('Borrow date', copy=False, default=datetime.date.today())
    return_date_deadline = fields.Date('Last date of return', copy=False, default=datetime.date.today() + relativedelta(weeks=2))
    return_date = fields.Date('Returned on', copy=False, readonly=True)
    late = fields.Integer('Late days', compute='_compute_due_days')

    @api.depends("borrow_date", "return_date_deadline", "return_date")
    def _compute_due_days(self):
        for record in self:
            record.late = 0
            if record.return_date is False:
                if record.return_date_deadline < datetime.date.today():
                    date_diff = datetime.date.today() - record.return_date_deadline
                    record.late = date_diff.days
            elif record.return_date > record.return_date_deadline:
                date_diff = record.return_date - record.return_date_deadline
                record.late = date_diff.days
            if record.late < 0:
                record.late = 0

    def name_get(self):
        res = []
        for rec in self:
            res.append((rec.id, f'{rec.member_id.name} - {rec.borrow_date}'))
        return res

    @api.depends("member_id", "borrow_date")
    def _get_title(self):
        for record in self:
            record.name = f'{record.member_id.name} ( {record.borrow_date} - {record.return_date_deadline} )'


