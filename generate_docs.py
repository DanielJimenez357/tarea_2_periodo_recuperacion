import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tarea_2_periodo_recuperacion.settings')
django.setup()

import pydoc
pydoc.writedoc('aplicacion.settings')