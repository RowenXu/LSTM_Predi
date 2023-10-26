#plot the graph of the world
import numpy as np #number processing
import matplotlib.pyplot as plt #to plot
import cartopy.crs as ccrs
import cartopy.feature as cfeat

#setting the background
fig=plt.figure(dpi=100)
ax=fig.add_subplot(projection=ccrs.PlateCarree())

#input the data 
with open("")