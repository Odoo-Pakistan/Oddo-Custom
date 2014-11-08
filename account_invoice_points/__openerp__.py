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

{
    "name": "Calculate Points in Sale invoices",
    "summary": "",
    "version": "1.0",
    "author": "bilbonet.NET",
    "contributors": ["Jesus Ramiro Martinez <jesus@bilbonet.net>",],
    "license": "AGPL-3",
    "category": "Custom Module",
    "website": "http://www.bilbonet.net",
    "complexity": "normal",
    "description": """
    In the product form set parameters of the calculation formula.
    In invoice sales the points are calculated according to the formula.
    """,
    "depends": ["sale", "product",],
    "data": [
        "views/product_template_form_points.xml",
        "views/account_invoice_form_points.xml",
        "views/account_invoice_tree_view_points.xml",
    ],
    "installable": True,
}
