from ninja_extra import NinjaExtraAPI

api = NinjaExtraAPI(
    title="Capricci API",
    description="API for Capricci e-commerce platform",
)

api.auto_discover_controllers()
