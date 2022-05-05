#convertir archivo python a .exe
from distutils.core import setup
import py2exe
#importar librerias del codigo


setup(zipfile=None,
      options={'py2exe': {"bundle_files": 1}},
      windows=["nombrearchivo.py"])

#escribir en la consola: python setup.py py2exe


