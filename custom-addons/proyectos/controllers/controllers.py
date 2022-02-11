# -*- coding: utf-8 -*-
# from odoo import http


# class .\custom-addons\proyectos(http.Controller):
#     @http.route('/.\custom-addons\proyectos/.\custom-addons\proyectos/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/.\custom-addons\proyectos/.\custom-addons\proyectos/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('.\custom-addons\proyectos.listing', {
#             'root': '/.\custom-addons\proyectos/.\custom-addons\proyectos',
#             'objects': http.request.env['.\custom-addons\proyectos..\custom-addons\proyectos'].search([]),
#         })

#     @http.route('/.\custom-addons\proyectos/.\custom-addons\proyectos/objects/<model(".\custom-addons\proyectos..\custom-addons\proyectos"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('.\custom-addons\proyectos.object', {
#             'object': obj
#         })
