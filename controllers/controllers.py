# -*- coding: utf-8 -*-
# from odoo import http


# class Heroes(http.Controller):
#     @http.route('/heroes/heroes', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/heroes/heroes/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('heroes.listing', {
#             'root': '/heroes/heroes',
#             'objects': http.request.env['heroes.heroes'].search([]),
#         })

#     @http.route('/heroes/heroes/objects/<model("heroes.heroes"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('heroes.object', {
#             'object': obj
#         })

