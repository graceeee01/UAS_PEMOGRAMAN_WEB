# UAS_PEMOGRAMAN_WEB
## Margaretta Rhestu Dinda P 23.83.0956
## Petrisia Okta Paulina 23.83.0978
## Gracia Rachelina S 23.83.0957

1. code untuk database MySQL 
```sql
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    skin_type TEXT,
    skin_problem TEXT
);
```
2. code untuk konfigurasi WSGI
```wsgi
import sys
import os

path = '/home/lcwproject/project_uas'
if path not in sys.path:
    sys.path.append(path)

os.chdir(path)

from aaaaa import app as application  # Pastikan nama file dan variabel sesuai

