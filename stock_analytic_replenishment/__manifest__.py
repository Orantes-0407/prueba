{
    'name': 'Stock Analytic Replenishment',
    'version': '1.0',
    'category': 'Inventory',
    'summary': 'Propaga la analítica a las órdenes de compra desde reglas de reordenamiento',
    'depends': ['stock', 'purchase', 'purchase_stock', 'analytic'],
    'data': [
        'views/purchase_order_views.xml',
    ],
    'installable': True,
    'application': False,
}