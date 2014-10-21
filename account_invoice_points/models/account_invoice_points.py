# -*- coding: utf-8 -*-
##############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp import models, fields, api, _

class AccountInvoicePoints(models.Model):
    _inherit = 'account.invoice'

    @api.multi
    @api.depends('invoice_line.price_subtotal', 'invoice_line.product_id.product_tmpl_id.points_price', 'invoice_line.product_id.product_tmpl_id.points_surchage')
    def _get_points(self):
        points = 0.0
        for line in self.invoice_line:
            points += (line.price_subtotal * line.product_id.product_tmpl_id.points_price) + line.product_id.product_tmpl_id.points_surchage
        self.points = points

    points = fields.Float(string='Points', compute=_get_points, readonly=True, digits=(12, 2),
                            store=True,
                            help="Points are calculated automatically whit the net price of each line.")
