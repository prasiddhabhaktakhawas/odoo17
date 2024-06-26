from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Hospital Patient"
    _inherit = ['mail.thread', 'mail.activity.mixin'] #inherited models from mail module

    name = fields.Char(string='Name', tracking=True)
    ref = fields.Char(string='Ref', defualt="Odoo Mates")
    age = fields.Integer(string="Age", tracking=True)
    gender = fields.Selection([('male','Male'),('female','Female')], string="Gender", tracking=True, default="female")
    active = fields.Boolean(string="Active", default=True) #used for archiving