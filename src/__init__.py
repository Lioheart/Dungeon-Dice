import os.path

__author__ = "Jakub Hawro"
__copyright__ = "Copyright 2020-2020 Jakub Hawro (The Compiler)"
__license__ = "MIT"
__maintainer__ = __author__
__email__ = "caco7.lioheart@gmail.com"
__version__ = "0.0.2"
__version_info__ = tuple(int(part) for part in __version__.split('.'))
__description__ = "Lista zaklęć z settingu D&D 3.5."

# Zmienia główny folder z nadrzędnego na src
# Wymaga .. zamiast . przy podawaniu ścieżki
basedir = os.path.dirname(os.path.realpath(__file__))
os.chdir(basedir)
