> :warning: **This package is deprecated in favor of [argopy](https://argopy.readthedocs.io/en/latest/index.html)**. Please see their documentation on [interpolating argo floats](https://argopy.readthedocs.io/en/latest/data_manipulation.html#Interpolation-to-standard-levels)


xargofloat
==============================
[![Build Status](https://travis-ci.com/jbusecke/xargofloat.svg?branch=master)](https://travis-ci.com/jbusecke/xargofloat)
[![codecov](https://codecov.io/gh/jbusecke/xargofloat/branch/master/graph/badge.svg)](https://codecov.io/gh/jbusecke/xargofloat)
[![License:MIT](https://img.shields.io/badge/License-MIT-lightgray.svg?style=flt-square)](https://opensource.org/licenses/MIT)

Tools to work with argo float data in xarray

--------

## Install on jupyter.rc

1. Open a fresh notebook and paste and execute the following into a new cell:
```
! pip install git+https://github.com/jbusecke/xargofloat.git
! pip install git+https://github.com/astropy/astropy.git
! pip install git+https://github.com/jbusecke/xarrayutils.git
```
This has to be done at the beginning of each session (not every time you restart your notebook)

2. In another notebook (make sure to restart if it was running) you can now import the functions as usual

# Using the functions
Check out the [demo_notebook](notebooks/demo.ipynb) for examples.


<p><small>Project based on the <a target="_blank" href="https://github.com/jbusecke/cookiecutter-science-project">cookiecutter science project template</a>.</small></p>


## Contributing to 'xargofloats' (assumes installed versions of git and [conda](https://docs.conda.io/en/latest/miniconda.html))
1. Fork the repository on github.
2. Clone your fork to your local machine with `git clone ...`
3. Navigate to your local `xargofloat` folder and install the test environment with `conda env create -f envrionment.yml`
4. Activate the environment with `conda activate xargofloat`
5. Run the local tests with `py.test -v`
6. Create a new git branch with `git checkout -b <branchname>
7. Add tests/modify code
8. Run tests to confirm that all tests pass locally
9. Push the branch back to your fork with `git push -u origin <branchname>`
10. Start a pull request on github.
