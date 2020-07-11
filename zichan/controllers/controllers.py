# -*- coding: utf-8 -*-
# from odoo import http


# class Zichan(http.Controller):
#     @http.route('/zichan/zichan/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/zichan/zichan/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('zichan.listing', {
#             'root': '/zichan/zichan',
#             'objects': http.request.env['zichan.zichan'].search([]),
#         })

#     @http.route('/zichan/zichan/objects/<model("zichan.zichan"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('zichan.object', {
#             'object': obj
#         })
