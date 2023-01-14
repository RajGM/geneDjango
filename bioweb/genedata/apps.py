from django.apps import AppConfig

# project configuration to allow it to mapped to the bioweb settings

class GenedataConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'genedata'
