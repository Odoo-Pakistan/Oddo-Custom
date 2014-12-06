# -*- encoding: utf-8 -*-
##############################################################################
#
#    Author: Jesus Ramiro
#    Copyright 2014 bilbonet.NET
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################
from openerp.osv import orm


class purchase_update_cost(orm.Model):
    _inherit = 'purchase.order'

    def wkf_confirm_order(self, cr, uid, ids, context=None):
        product_obj = self.pool['product.template']
        res = super(purchase_update_cost, self).wkf_confirm_order(cr, uid, ids, context)

        for o in self.browse(cr, uid, ids, context):
            for line in o.order_line:
                if line.product_id:
                    vals = {'standard_price': line.price_unit}

                    product_obj.write(cr, uid, [line.product_id.product_tmpl_id.id], vals, context)
        return res