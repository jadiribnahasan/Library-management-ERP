{
    'name': 'library',
    'depends': ['base'],
    'application': True,
    'data': [
        'data/security/ir.model.access.csv',
        'views/library_book_views.xml',
        'views/library_book_menus.xml',
        'views/library_membership_registration_views.xml',
        'views/library_membership_registration_menus.xml',
        'views/library_member_views.xml',
        'views/library_book_borrow_return_record_views.xml',
        'views/library_book_borrow_return_record_menus.xml'
    ]
}