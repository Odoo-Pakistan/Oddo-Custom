# -*- encoding: utf-8 -*-
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
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################
from openerp.osv import orm

class SaleLastPrice(orm.Model):
    _inherit = "product.pricelist"

    def _sale_last_price(self, cr, uid, prod_id, partner, context=None):
        ids = self.pool.get('account.invoice.line').search(cr, uid, [('product_id', '=', prod_id), ('partner_id', '=', partner)], order = 'write_date desc')
        if ids:
            last_prices = self.pool.get('account.invoice.line').browse(cr, uid, ids)
            return last_prices[0].price_unit
        else:
            return False

    def price_get(self, cr, uid, ids, prod_id, qty, partner=None, context=None):
        pricelist = self.pool.get('product.pricelist').browse(cr, uid, ids, context=context)
        if pricelist.type == 'sale':
            lastprice = self._sale_last_price(cr,uid, prod_id, partner, context=context)
            if lastprice:
                price = {ids[0]:lastprice}
                return price

        return dict((key, price[0]) for key,
                    price in self.price_rule_get(cr, uid, ids, prod_id, qty, partner=partner, context=context).items())
