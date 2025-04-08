from odoo import models, fields, api

class HotelRoom(models.Model):
    _name = 'hotel.room'
    _description = 'Hotel Room'

    name = fields.Char(string='Room Number', required=True)
    room_type_id = fields.Many2one('hotel.room.type', string='Room Type', required=True)
    floor = fields.Integer(string='Floor')
    status = fields.Selection([
        ('available', 'Available'),
        ('booked', 'Booked'),
        ('cleaning', 'Cleaning'),
        ('maintenance', 'Maintenance')
    ], string='Status', default='available')
    notes = fields.Text(string='Notes')
    active = fields.Boolean(default=True) 