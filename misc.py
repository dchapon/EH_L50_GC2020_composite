# -*- coding: utf-8 -*-
import numpy as N
from PIL import Image
from matplotlib import pyplot as P
from colormaps import CustomColormaps
from data_reader import map_512


def display_density_histogram(drop_percentile=0.5):
    rho = map_512["density"]
    flat_d = N.sort(rho.reshape(rho.shape[0] * rho.shape[1]))
    b, e, coll = P.hist(N.log10(flat_d), density=True, cumulative=True, bins=500, log=True, weights=flat_d)
    drop_rho = drop_percentile / 100.0
    dmin = e[:-1][b > drop_rho][0]
    xmin, xmax = P.xlim()
    ymin, ymax = P.ylim()
    P.plot([xmin, dmin], [drop_rho, drop_rho], 'k--')
    P.plot([dmin, dmin], [ymin, drop_rho], 'k--')
    P.plot([dmin, ], [drop_rho, ], 'r.')
    P.xlabel("log(density map pixel value)")
    P.title("Density map value cumulative histogram")
    P.ylabel("cumulative pixel value histogram")
    P.xlim(xmin, xmax)
    P.ylim(ymin, ymax)
    P.figure()
    print("Minimum density : rho_min = {dmin:g} ; log(rho_min) = {ldmin:g}".format(dmin=10.0 ** dmin, ldmin=dmin))

    P.imshow(N.log10(rho.T), cmap=CustomColormaps.get_cmap("Viridis_dark"), vmin=dmin, origin="lower")
    P.colorbar()
    P.tight_layout()


def value_range(arr, drop_percentile=1.0):
    values = N.sort(arr[arr > 0.0])
    weights = (values - values[0]) / (values[-1] - values[0])
    cumval = N.cumsum(weights)
    cumval /= cumval[-1]
    mask = (cumval >= drop_percentile/100.0)
    vmin = values[mask][0]
    return vmin, values[-1]


def pil_img(a, amin, cmap_name):
    cmap = CustomColormaps.get_cmap(cmap_name)
    lamin = N.log10(amin)
    la = N.log10(a.T)
    la[la < lamin] = lamin
    lamax = la.max()
    a_arr = (la-lamin)/(lamax-lamin)
    ima_arr = N.clip(cmap(a_arr)*255.0, 0, 255).astype('uint8')
    ima = Image.fromarray(ima_arr[:, :, :3], "RGB").transpose(Image.FLIP_TOP_BOTTOM)
    return ima


__all__ = ["value_range", "pil_img"]
