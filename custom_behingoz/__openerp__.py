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
{
    'name': 'Module Custom Behingoz Odoo',
    'summary': """
        Modulo con las personalizaciones de Odoo para el cliente.
        """,
    'author': 'bilbonet.NET',
    'website': 'http://www.bilbonet.net',
    'contributors': ['Jesus Ramiro Martinez <jesus@bilbonet.net>',],
    'version': '1.0',
    'complexity': 'normal',
    'category': 'Custom Modules',
    'depends': ['base','report','sale'],
    'description': """
Vistas
======================
Solo usuarios de compras pueden ver abastecimientos de ficha artículos.

Seguridad
====================
* Comerciales solo pueden ver sus propias empresas.
* Crear grupo Gerencia.
* Grupo Gerencia puede modificar los datos de la empresa.

Funcionalidad
====================
Al validar un pedido de compra se actualiza el precio coste de la ficha del articulo.

Qweb Reports
====================
* Presupuesto/Albaran de venta
* Almacen orden de entrga
* Factura ventas
        """,
    'data': [
        'views/product_template_form.xml',
        #Seguridad
        'security/custom_behingoz_security.xml',
        'security/ir.model.access.csv',

        # cargamos las vistas de los reportes
        'views/layouts.xml',
        'views/report_saleorder.xml',
        'views/report_picking.xml',
        'views/report_invoice.xml',
        # cargamos los reportes
        'custom_behingoz_report.xml',
    ],
    "installable": True,
    "auto_install": False,
}
