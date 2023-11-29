# -*- coding: utf-8 -*-
# from odoo import http


# class Veterinario(http.Controller):
#     @http.route('/veterinario/veterinario/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/veterinario/veterinario/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('veterinario.listing', {
#             'root': '/veterinario/veterinario',
#             'objects': http.request.env['veterinario.veterinario'].search([]),
#         })

#     @http.route('/veterinario/veterinario/objects/<model("veterinario.veterinario"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('veterinario.object', {
#             'object': obj
#         })
