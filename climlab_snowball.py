## Helper functions to clean up demo notebook
## 28 Nov 2020  EHU

import matplotlib.patches as patches
import numpy as np
import matplotlib.pyplot as plt


def state_plot(model, figsize=(12,5), show=True, ice_temp=True):
    """Plot the temperature and albedo at the current state of the model.
    Shade the current ice line in grey."""
    templimits = -30,35
    alimits = min(model.albedo)-0.05, max(model.albedo)+0.05
    latlimits = -90,90
    lat_ticks = np.arange(-90,90,30)
    
    Ts = np.array(model.Ts).flatten()
    if ice_temp:
    	Tf = float(model.param['Tf'])
    else:
    	Tf=0
    
    fig = plt.figure(figsize=figsize)
    
    ax1 = fig.add_subplot(1,2,1)
    ax1.plot(model.lat, Ts)
    ax1.set(xlim=latlimits, ylim=templimits,
           ylabel='Temperature [deg C]', xlabel='Latitude', xticks=lat_ticks)
    ax1.fill_between(model.lat, Ts, y2=Tf, where=Ts<Tf, color='LightGrey', alpha=0.5)
    ax1.grid()
    
    ax2 = fig.add_subplot(1,2,2)
    icerect1 = patches.Rectangle((latlimits[0], 0), width=model.icelat[0]-latlimits[0], height=1,
                            color='LightGrey', alpha=0.5)
    icerect2 = patches.Rectangle((model.icelat[1], 0), width=latlimits[1]-model.icelat[1], height=1,
                            color='LightGrey', alpha=0.5)
    ax2.add_patch(icerect1)
    ax2.add_patch(icerect2)
    ax2.plot(model.lat, model.albedo)
    ax2.set(xlim=latlimits, ylim=alimits,
           ylabel='Albedo', xlabel='Latitude', xticks=lat_ticks)
    ax2.grid()