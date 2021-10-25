from odoo import models, fields


class Member(models.Model):
    _inherit = "res.partner"

    isMember = fields.Boolean('Is Member?')
