from odoo import models, fields


class MembershipReg(models.Model):

    _name = "library.membership.registration"
    _description = "Registration for Membership"

    name = fields.Char('Name')
    email = fields.Char('Email')
    contactNo = fields.Char('Contact Number')
    address = fields.Char('Address')
    department = fields.Selection(
        string='Department',
        selection=[('cse', 'CSE'), ('bba', 'BBA'), ('english', 'English'), ('eee', 'EEE')],
    )
