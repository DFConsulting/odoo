from odoo import models, fields, api
from datetime import datetime, timedelta

class HotelRatePlan(models.Model):
    _name = 'hotel.rate.plan'
    _description = 'Hotel Rate Plan'

    name = fields.Char(string='Rate Plan Name', required=True)
    room_type_id = fields.Many2one('hotel.room.type', string='Room Type', required=True)
    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date', required=True)
    rate = fields.Float(string='Rate', required=True)
    min_stay = fields.Integer(string='Minimum Stay (nights)')
    max_stay = fields.Integer(string='Maximum Stay (nights)')
    is_corporate = fields.Boolean(string='Corporate Rate')
    active = fields.Boolean(default=True)

    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        for record in self:
            if record.start_date > record.end_date:
                raise models.ValidationError("End date must be after start date") 