import numpy as np
import xarray as xr
import matplotlib.pyplot as plt

file=xr.open_dataset('/Users/rowenxu/LSTM_EA_Monsoon/Data/input/adaptor.mars.internal-1698908854.9156716-11198-12-eae6fdc7-5aa0-4781-8f46-3f365ba5721b.nc')
level=file['level']
lat=file['latitude']
lon=file['longitude']
time=file['time']
u=file['u']
v=file['v']
speed=np.sqrt(u**2+v**2)
#print 850hpa wind speed average
fig=plt.figure(figsize=(10,10))
ax=fig.add_subplot()
ax.set_title('850hpa wind speed average')
# ax.gridline()
ax.quiver(lon,lat,u[0,0,:,:],v[0,0,:,:],cmap='jet')


