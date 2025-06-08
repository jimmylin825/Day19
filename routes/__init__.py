from .orders import orders_bp
from .export import export_bp
from .dashboard import dashboard_bp

def register_routes(app):
    app.register_blueprint(orders_bp)
    app.register_blueprint(export_bp)
    app.register_blueprint(dashboard_bp)