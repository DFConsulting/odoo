from odoo import models, fields, api

class HotelRoomType(models.Model):
    _name = 'hotel.room.type'
    _description = 'Hotel Room Type'

    name = fields.Char(string='Room Type', required=True)
    description = fields.Text(string='Description')
    max_occupancy = fields.Integer(string='Maximum Occupancy', required=True)
    base_price = fields.Float(string='Base Price', required=True)
    amenities = fields.Text(string='Amenities')
    active = fields.Boolean(default=True) 