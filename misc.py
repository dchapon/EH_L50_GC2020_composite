# -*- coding: utf-8 -*-
import numpy as N
from PIL import Image
from matplotlib import pyplot as P
from colormaps import CustomColormaps


def value_range(arr, drop_percentile=1.0):
    values = N.sort(arr[arr > 0.0])
    weights = (values - values[0]) / (values[-1] - values[0])
    cumval = N.cumsum(weights)
    cumval /= cumval[-1]
    mask = (cumval >= drop_percentile/100.0)
    vmin = values[mask][0]
    return vmin, values[-1]


def pil_img(a, lamin, cmap_name):
    cmap = CustomColormaps.get_cmap(cmap_name)
    la = N.log10(a.T)
    la[la<lamin] = lamin
    lamax = la.max()
    a_arr = (la-lamin)/(lamax-lamin)
    ima_arr = N.clip(cmap(a_arr)*255.0, 0, 255).astype('uint8')
    ima = Image.fromarray(ima_arr[:, :, :3], "RGB").transpose(Image.FLIP_TOP_BOTTOM)
    return ima


__all__ = ["value_range", "pil_img"]
