import xarray as xr
import numpy as np
import pytest
from xarrayutils.utils import coord_remapping
from xargofloat.utils import interpolate_to_pressure


@pytest.mark.parametrize('p',[np.arange(0,1000, 3), np.arange(300, 2000)])
def test_interpolate_to_pressure(p):
    ds = xr.open_dataset('data/5903711_Mprof.nc')
    
    ds_new = interpolate_to_pressure(ds, p=p)
    
    expected_data_vars = []
    for var in ['PRES', 'TEMP', 'PSAL', 'DOXY', 'CHLA', 'BBP700', 'NITRATE']:
        for mode in ['', '_ADJUSTED', '_ADJUSTED_ERROR']:
            expected_data_vars.append(var+mode)
    
    for var in expected_data_vars:
        expected = coord_remapping(ds.PRES_ADJUSTED, ds[var], ds.PRES_ADJUSTED, p, x_dim='N_LEVELS')
        np.testing.assert_allclose(expected.data, ds_new[var].data)      
    assert set(expected_data_vars) == set(ds_new.data_vars)