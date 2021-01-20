# define the package following the PEP 420 recommendation:
#   https://www.python.org/dev/peps/pep-0420/#namespace-packages-today
from pkgutil import extend_path

__path__ = extend_path(__path__, __name__)