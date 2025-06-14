# -*- coding: utf-8 -*-
"""
Módulo pydatajson
Conjunto de herramientas para validar y manipular la información presente en
el archivo `data.json` de un Portal de Datos
"""

from __future__ import absolute_import

import logging

from . import helpers
from .core import DataJson
from .helpers import parse_repeating_time_interval

__author__ = """Datos Argentina"""
__email__ = 'datosargentina@jefatura.gob.ar'
__version__ = '0.4.67'

"""
Logger base para librería pydatajson
https://docs.python.org/2/howto/logging.html#configuring-logging-for-a-library
"""
logger = logging.getLogger('pydatajson')
logger.addHandler(logging.NullHandler())
