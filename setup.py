from pathlib import Path
import glob

from setuptools import setup, find_packages

# find all of the "_default" files
defaults = []
for path in Path("pyro").rglob("_default*"):
    defaults.append(str(path.relative_to("./pyro")))

# find all of the problem "_pname.defaults" files
# note: pathlib doesn't work here, because of symlinks
for f in glob.glob("pyro/**/_*.defaults", recursive=True):
    defaults.append(f.replace("pyro/", ""))

# find all of the "inputs" files
inputs = []
for f in glob.glob("pyro/**/inputs*", recursive=True):
    if not f.endswith("inputs.auto"):
        inputs.append(f.replace("pyro/", ""))

benchmarks = ["advection/tests/*.h5",
              "advection_fv4/tests/*.h5",
              "advection_nonuniform/tests/*.h5",
              "advection_rk/tests/*.h5",
              "compressible/tests/*.h5",
              "compressible/tests/*.h5",
              "compressible/tests/*.h5",
              "compressible_fv4/tests/*.h5",
              "compressible_rk/tests/*.h5",
              "compressible_sdc/tests/*.h5",
              "diffusion/tests/*.h5",
              "incompressible/tests/*.h5",
              "lm_atm/tests/*.h5",
              "multigrid/tests/*.h5",
              "swe/tests/*.h5"]

setup(name='pyro',
      description='A python hydrodynamics code for teaching and prototyping',
      url='https://github.com/python-hydro/pyro2',
      license='BSD',
      packages=find_packages(),
      scripts=["pyro/pyro_sim.py"],
      package_data={"pyro": benchmarks + defaults + inputs},
      install_requires=['numpy', 'numba', 'matplotlib', 'h5py'],
      use_scm_version={"version_scheme": "post-release",
                       "write_to": "pyro/_version.py"},
      setup_requires=["setuptools_scm"],
      zip_safe=False)
