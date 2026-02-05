
# init marks a file as a package

__version__ = "1.0.0"
__author__ = "Master Pythonicus"


from .elements import create_fire, create_water
__all__ = ["create_fire", "create_water"]
# __all__ = list of public names a module exports
