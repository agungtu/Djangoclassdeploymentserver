import sys
import os

# Tambahkan root project ke path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Tambahkan folder Django
sys.path.append(os.path.join(os.path.dirname(__file__), "djangowebite2026"))

from djangowebite2026.wsgi import application

app = application