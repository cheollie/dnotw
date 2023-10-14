import enlilviz as ev
from pathlib import Path
import imageio,PIL
import enlilviz.plotting as evplot
import matplotlib as mpl
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
# 'den' -> density; 'vel' -> velocity
evplot.plots._cm1 = mpl.colormaps['pink'](np.linspace(0.5, 1, 128))
evplot.plots._cm2 = mpl.colormaps['spring'](np.linspace(0., 1, 128))
evplot.plots.ENLIL_CMAP = LinearSegmentedColormap.from_list('enlil_cmap',
                                               np.vstack((mpl.colormaps['spring'](np.linspace(0., 1, 128)), mpl.colormaps['pink'](np.linspace(0., 1, 128)))))

run = ev.read_enlil2d('wsa_enlil.latest.suball.nc')
evplot.TimeSeries(run, 'Earth', 'den')
evplot.LongitudeSlice(run, 'den')
evplot.LatitudeSlice(run, 'vel')
evplot.RadialSlice(run, 'vel')
evplot.Title(run)

forecaster = evplot.ForecasterPlot(run,watermark="lonely duck - 2023")
#forecaster.save()

ct = 0
for plot in iter(forecaster):
    print(plot.time)
    (plot).save()
    #if ct == 24:
    #    break
    #ct += 1

image_path = Path('.')
images = list(image_path.glob('*.png'))
image_list = []
for file_name in images:
    image_list.append(imageio.imread(file_name))
imageio.mimwrite('animated_from_images.gif', image_list)