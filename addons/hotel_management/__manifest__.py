{
    'name': 'Hotel Management',
    'version': '1.0',
    'category': 'Services',
    'summary': 'Hotel Management System',
    'description': """
        Hotel Management System
        - Room types (Single, Double, Suite, etc.)
        - Room status (Available, Booked, Cleaning, Maintenance)
        - Configurable pricing and occupancy rules
        - Rate plans (seasonal, corporate, etc.)
    """,
    'author': 'YDL Corp',
    'website': 'https://www.yourdatalead.com',
    'license': 'LGPL-3', 
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/hotel_room_type_views.xml',
        'views/hotel_room_views.xml',
        'views/hotel_rate_plan_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
} 