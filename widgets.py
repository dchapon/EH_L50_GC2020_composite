# -*- coding: utf-8 -*-
from IPython.display import display
import ipywidgets
from PIL import Image, ImageChops
from data_reader import map_512
from misc import value_range, pil_img


def interactive_density_widget(min_pct=0.0, default_pct=1.0, max_pct=10.0):
    def show_density(drop_pct):
        rho = map_512["density"]
        vmin, vmax = value_range(rho, drop_percentile=drop_pct)
        img = pil_img(rho, vmin, "Viridis_dark")
        display(img)
        return img

    w = ipywidgets.interactive(show_density, drop_pct=ipywidgets.FloatSlider(min=min_pct, max=max_pct,
                                                                             value=default_pct, step=0.001,
                                                                             continuous_update=False,
                                                                             readout_format='.3f',
                                                                             description="dropped percentile (rho)"))

    output = w.children[-1]
    output.layout.height = '512px'
    return w


def interactive_composite_widget(min_pct=0.0, default_pct=1.0, max_pct=10.0):
    cm_list = ["Dark_green", "gist_heat", "hot", "bone", "BlueYellowTanager", "magma", "inferno", "Viridis_dark",
               "viridis", "plasma", "BlackBlueYellowRed", "BlackBlueWhiteRed", "Dark_thermal", "JetBlack",
               "BlackPurpWhiBlGreen"]
    rho = map_512["density"]
    temperature = map_512["temperature"]
    entropy = map_512["entropy"]
    metallicity = map_512["metallicity"]

    def show_composite(ch1_cmap, drop_pct_rho, ch2_cmap, temp_channel, drop_pct_temp, has_metal, ch3_cmap, drop_pct_metal):
        vmin, vmax = value_range(rho, drop_percentile=drop_pct_rho)
        rho_img = pil_img(rho, vmin, ch1_cmap)

        if temp_channel == "temperature":
            vmin, vmax = value_range(temperature, drop_percentile=drop_pct_temp)
            T_img = pil_img(temperature, vmin, ch2_cmap)
        else:
            vmin, vmax = value_range(entropy, drop_percentile=drop_pct_temp)
            T_img = pil_img(entropy, vmin, ch2_cmap)

        composite = ImageChops.lighter(rho_img, T_img)
        if has_metal:
            vmin, vmax = value_range(metallicity, drop_percentile=drop_pct_metal)
            m_img = pil_img(metallicity, vmin, ch3_cmap)
            composite = ImageChops.lighter(composite, m_img)

        display(composite)
        return composite

    w = ipywidgets.interactive(show_composite, ch1_cmap=ipywidgets.Dropdown(options=cm_list, value="Viridis_dark",
                                                                            description="Density colormap"),
                               drop_pct_rho=ipywidgets.FloatSlider(min=min_pct, max=max_pct, value=default_pct,
                                                                   step=0.001, readout_format='.3f',
                                                                   continuous_update=False,
                                                                   description="dropped percentile (rho)"),
                               ch2_cmap=ipywidgets.Dropdown(options=cm_list, value="inferno",
                                                            description="P/rho^gamma colormap"),
                               temp_channel=ipywidgets.RadioButtons(options=['temperature', 'entropy'],
                                                                    value='temperature',
                                                                    description="P/rho^gamma channel"),
                               drop_pct_temp=ipywidgets.FloatSlider(min=min_pct, max=max_pct, value=default_pct,
                                                                    step=0.001, continuous_update=False,
                                                                    readout_format='.3f',
                                                                    description="dropped percentile (T/entropy)"),
                               has_metal=ipywidgets.Checkbox(value=True, description="Add metallicity channel ?"),
                               ch3_cmap=ipywidgets.Dropdown(options=cm_list, value="Dark_green",
                                                            description="metallicity colormap"),
                               drop_pct_metal=ipywidgets.FloatSlider(min=min_pct, max=max_pct, value=default_pct,
                                                                     step=0.001, continuous_update=False,
                                                                     readout_format='.3f',
                                                                     description="dropped percentile (metal)"))

    output = w.children[-1]
    output.layout.height = '512px'
    return w


__all__ = ["interactive_density_widget", "interactive_composite_widget"]
