# -*- coding: utf-8 -*-
from odoo import http

# class OutProcess(http.Controller):
#     @http.route('/out_process/out_process/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/out_process/out_process/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('out_process.listing', {
#             'root': '/out_process/out_process',
#             'objects': http.request.env['out_process.out_process'].search([]),
#         })

#     @http.route('/out_process/out_process/objects/<model("out_process.out_process"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('out_process.object', {
#             'object': obj
#         })