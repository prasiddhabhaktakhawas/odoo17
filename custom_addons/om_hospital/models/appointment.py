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
    ref = fields.Char(string="reference", help="reference from patient record") #help is for text that appears when hovering over the label. It can also be done from xml field.
    prescription = fields.Html(string='Prescription')
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High')], string='Priority')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In consultation'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')], default='draft', string='Status', required=True)
    doctor_id = fields.Many2one('res.users', string='Doctor')

    @api.onchange('patient_id') #when there is change in the patient_id field, it auto set reference
    def onchange_patient_id(self):
        self.ref=self.patient_id.ref

    def action_test(self):
        return {
            'effect':{  #rainbow effect when button clicked
                'fadeout': 'slow',
                'message': 'Click Successful',
                'type': 'rainbow_man'
            }
        }

    def action_in_consultation(self):
        for rec in self:
            rec.state="in_consultation"

    def action_done(self):
        for rec in self:
            rec.state="done"

    def action_cancel(self):
        for rec in self:
            rec.state="cancel"

    def action_draft(self):
        for rec in self:
            rec.state="draft"