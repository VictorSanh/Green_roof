from os import path
resources_dir = path.join(path.dirname(__file__), 'resources')
code_fortran_dir = path.join(path.dirname(__file__), 'code_fortran')
data_base_dir = path.join(path.dirname(__file__), 'data_base')

from .donnees_json import *
from .irradiance import *
