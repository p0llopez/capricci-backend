from ninja_extra import NinjaExtraAPI
from ninja_jwt.controller import NinjaJWTDefaultController

api = NinjaExtraAPI(
    title="Capricci API",
    description="API for Capricci e-commerce platform",
    version="1.0.0",
)
api.register_controllers(NinjaJWTDefaultController)

api.auto_discover_controllers()
