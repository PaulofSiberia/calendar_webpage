import os, sys
activate_this = '/home/username/python/bin/activate_this.py'
with open(activate_this) as f:
   exec(f.read(), {'__file__': activate_this})
sys.path.insert(0, os.path.join('/home/username/domains/domain.ru/public_html/'))
from myapp import app as application
if __name__ == "__main__":
    application.run()