import xarray as xr
import numpy as np
from xarrayutils.utils import coord_remapping
import warnings


def interpolate_to_pressure(ds, p=np.arange(0, 2000,2)):
    warnings.warn("`xargofloat` will be decprecated in favor of `argopy` (https://argopy.readthedocs.io/en/latest/data_manipulation.html#Interpolation-to-standard-levels). Please update your code accordingly",DeprecationWarning) 
    ds = ds.copy()
    ds_out = xr.Dataset()
    
    # the qc variables cannot be interpolated...
    datavars = [dv for dv in list(ds.variables) if set(['N_LEVELS', 'N_PROF']) == set(ds[dv].dims) and 'QC' not in dv]
    coords = [dv for dv in list(ds.variables) if not dv in datavars and 'QC' not in dv]
    
    for dv in datavars:
        ds_out[dv] = coord_remapping(ds.PRES_ADJUSTED, ds[dv], ds.PRES_ADJUSTED, p, x_dim='N_LEVELS')
        
    ds_out = ds_out.rename({'remapped_dim': 'PRESSURE_INTERPOLATED'})
        
    for co in coords:
        ds_out.coords[co] = ds[co]
        
    return ds_out
