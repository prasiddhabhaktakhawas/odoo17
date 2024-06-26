from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name = "hospital.appointment"
    _description = "Hospital Appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin'] #inherited models from mail module

    patient_id = fields.Many2one('hospital.patient', string="Patient")