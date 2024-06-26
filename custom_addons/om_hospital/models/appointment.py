from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name = "hospital.appointment"
    _description = "Hospital Appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin'] #inherited models from mail module
    _rec_name = 'ref'

    patient_id = fields.Many2one('hospital.patient', string="Patient") #all the records of patients will be shown in drop down menu
    gender=fields.Selection(related='patient_id.gender') #automatically gets gender from patient_id
    appointment_time = fields.Datetime(string="appointment time", default=fields.Datetime.now)
    booking_date = fields.Date(string="Booking Date", default=fields.Date.context_today)
    ref = fields.Char(string="reference")

    @api.onchange('patient_id') #when there is change in the patient_id field, it auto set reference
    def onchange_patient_id(self):
        self.ref=self.patient_id.ref
