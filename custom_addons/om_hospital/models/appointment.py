from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name = "hospital.appointment"
    _description = "Hospital Appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin'] #inherited models from mail module

    patient_id = fields.Many2one('hospital.patient', string="Patient") #all the records of patients will be shown in drop down menu
    appointment_time = fields.Datetime(string="appointment time", default=fields.Datetime.now)
    booking_date = fields.Date(string="Booking Date", default=fields.Date.context_today)