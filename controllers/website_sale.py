from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale

class WebsiteSaleGraduacion(WebsiteSale):

    @http.route(['/shop/cart/update'], type='http', auth="public", methods=['POST'], website=True, csrf=False)
    def cart_update(self, product_id, add_qty=1, set_qty=0, **kw):
        # Capturar datos de graduación
        graduacion_data = {
            'misma_graduacion': kw.get('misma_graduacion') == 'true',
            'od_esfera': kw.get('od_esfera'),
            'od_cilindro': kw.get('od_cilindro'),
            'od_eje': kw.get('od_eje'),
            'oi_esfera': kw.get('oi_esfera'),
            'oi_cilindro': kw.get('oi_cilindro'),
            'oi_eje': kw.get('oi_eje'),
        }
        
        # Llamar al método original
        result = super(WebsiteSaleGraduacion, self).cart_update(product_id, add_qty, set_qty, **kw)
        
        # Guardar graduación en la línea de orden
        if any(graduacion_data.values()):
            order = request.website.sale_get_order()
            if order and order.order_line:
                last_line = order.order_line[-1]
                last_line.write(graduacion_data)
        
        return result
