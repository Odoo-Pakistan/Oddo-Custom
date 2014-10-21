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

class ProductTemplatePoints(models.Model):
    _inherit = "product.template"

    points_price = fields.Float(string="Points Price", digits=(6, 2), store=True,
                            help="Specifies the % to calculate the amount of points"\
                                    "according to the net price of the line\n"\
                                    "Examples: (0.2 add 20%), (-0,2 discounts 20%)")
    points_surchage = fields.Float(string="Points Surchage", digits=(12, 2), store=True,
                            help="Specify the fixed amount to add or substract(if negative)"\
                                "to the amount calculated with the net price.")