# -*- coding: utf-8 -*-
import pickle
import bz2

map_512 = {"temperature": None, "density": None, "metallicity": None, "entropy": None}

with bz2.BZ2File("data/temperature.pkl.bz2", 'rb') as f:
    map_512["temperature"] = pickle.load(f)
with bz2.BZ2File("data/metal.pkl.bz2", 'rb') as f:
    map_512["metallicity"] = pickle.load(f)
with bz2.BZ2File("data/density.pkl.bz2", 'rb') as f:
    map_512["density"] = pickle.load(f)
with bz2.BZ2File("data/entropy.pkl.bz2", 'rb') as f:
    map_512["entropy"] = pickle.load(f)


__all__ = ["map_512"]
