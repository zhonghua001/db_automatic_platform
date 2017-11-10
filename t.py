import sys; print('Python %s on %s' % (sys.version, sys.platform))
import django; print('Django %s' % django.get_version())
sys.path.extend(['/root/PycharmProjects/db_automatic_platform', '/pycharm-2016.3.2/helpers/pycharm', '/pycharm-2016.3.2/helpers/pydev'])
if 'setup' in dir(django): django.setup()
