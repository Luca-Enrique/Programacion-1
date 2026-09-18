import os
from pathlib import Path

def _cargar_env():
    archivo = Path(__file__).parent / '.env'
    if not archivo.exists():
        return
    for linea in archivo.read_text(encoding='utf-8').splitlines():
        linea = linea.strip()
        if not linea or linea.startswith('#') or '=' not in linea:
            continue
        clave, _, valor = linea.partition('=')
        os.environ.setdefault(clave.strip(), valor.strip().strip('"\''))

_cargar_env()

DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_USER = os.getenv('DB_USER', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', '')