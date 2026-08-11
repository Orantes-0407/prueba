from odoo import models, api, fields

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    @api.model
    def _prepare_purchase_order_line_from_procurement(self, product_id, product_qty, product_uom, location_dest_id, name, origin, company_id, values, po):
        # Llamamos al método original primero
        res = super()._prepare_purchase_order_line_from_procurement(
            product_id, product_qty, product_uom, location_dest_id, name, origin, company_id, values, po
        )
        
        # Odoo 19 ya intenta aplicar el modelo de distribución si está configurado en el producto.
        # Propagamos la analítica desde el orderpoint (regla de reordenamiento) o la regla de stock si están definidos.
        orderpoint = values.get('orderpoint_id')
        rule = values.get('rule_id')
        
        analytic_dist = False
        if orderpoint:
            analytic_dist = getattr(orderpoint, 'analytic_distribution', False) or getattr(orderpoint, 'x_analytic_distribution', False)
        if not analytic_dist and rule:
            analytic_dist = getattr(rule, 'analytic_distribution', False) or getattr(rule, 'x_analytic_distribution', False)
            
        if analytic_dist:
            res['analytic_distribution'] = analytic_dist
            
        return res