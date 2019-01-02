"""

Wrapper for C++ library

Authors: Pauline Guntzburger, Lucie Van Nieuwenhuyze and Alban Gossard
Date: 2018july27
"""


# setup.py

import distutils
from distutils.core import setup, Extension
import distutils.sysconfig
import numpy



cfg_vars = distutils.sysconfig.get_config_vars()
for key, value in cfg_vars.items():
    if type(value) == str:        
        # cfg_vars[key] = value.replace("-O2", "")
        cfg_vars[key] = value.replace("-O3", "")

for key, value in cfg_vars.items():
    if type(value) == str:        
        cfg_vars[key] = value.replace("-DNDEBUG", "")

cfg_vars = distutils.sysconfig.get_config_vars()
for key, value in cfg_vars.items():
    if type(value) == str:        
        cfg_vars[key] = value.replace("-Wstrict-prototypes", "")



try:
    numpy_include = numpy.get_include()
except AttributeError:
    numpy_include = numpy.get_numpy_include()

setup(
    name = "Alban's C++ Library wrapped up all nice for python",
    author = 'Pauline Guntzburger, Lucie Van Nieuwenhuyze and Alban Gossard',
    author_email = 'alban.gossard@hotmail.fr',
    license='GPL v3 :: GNU General Public License',  
    version = "0.1",
    ext_modules = [
        Extension(
            "_MC",
            libraries=["gmp","gomp"],
            extra_compile_args = ["-g","-ffast-math","-fopenmp","-std=c++11"],
            sources = ["MC.i","MC.cxx"],
            swig_opts=["-c++"],
            include_dirs = [numpy_include]
        )
    ]
)