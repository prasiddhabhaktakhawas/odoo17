from odoo import api, fields, models
from datetime import date


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Hospital Patient"
    _inherit = ['mail.thread', 'mail.activity.mixin'] #inherited models from mail module

    name = fields.Char(string='Name', tracking=True)
    date_of_birth = fields.Date(string='Date of brith')
    ref = fields.Char(string='Ref', defualt="Odoo Mates")
    age = fields.Integer(string="Age", compute='_compute_age', tracking=True)
    gender = fields.Selection([('male','Male'),('female','Female')], string="Gender", tracking=True, default="female")
    active = fields.Boolean(string="Active", default=True) #used for archiving
    appointment = fields.Many2one('hospital.appointment',string='Appointments')
    image=fields.Image(string="Image")
    tag_ids = fields.Many2many('patient.tag',string='Tags')

    @api.depends('date_of_birth') #resonsible for instant change in computed field. otherwise, the field value only changes when saved
    def _compute_age(self): # computes age automatically
        for rec in self:    # self represents all the records, so we need to loop
            today = date.today()
            if rec.date_of_birth:
                rec.age= today.year - rec.date_of_birth.year
            else:
                rec.age = 0