# -*- coding: utf-8 -*-

from matplotlib import cm
from matplotlib.colors import Colormap, LinearSegmentedColormap


# (0.0 -> white), (0.64 -> dark blue), (1.0 -> yellow)
_cdict_WhiBlueYellow = {'red': [(0.0, 0.9686274528503418, 0.9686274528503418),
                                (0.08, 0.8705882430076599, 0.8705882430076599),
                                (0.16, 0.7764706015586853, 0.7764706015586853),
                                (0.24, 0.6196078658103943, 0.6196078658103943),
                                (0.32, 0.41960784792900085, 0.41960784792900085),
                                (0.40, 0.25882354378700256, 0.25882354378700256),
                                (0.48, 0.12941177189350128, 0.12941177189350128),
                                (0.56, 0.0313725508749485, 0.0313725508749485),
                                (0.64, 0.0313725508749485, 0.0313725508749485),
                                (1.0, 1.0, 1.0)],
                        'green': [(0.0, 0.9843137264251709, 0.9843137264251709),
                                  (0.08, 0.9215686321258545, 0.9215686321258545),
                                  (0.16, 0.8588235378265381, 0.8588235378265381),
                                  (0.24, 0.7921568751335144, 0.7921568751335144),
                                  (0.32, 0.6823529601097107, 0.6823529601097107),
                                  (0.40, 0.572549045085907, 0.572549045085907),
                                  (0.48, 0.4431372582912445, 0.4431372582912445),
                                  (0.56, 0.3176470696926117, 0.3176470696926117),
                                  (0.64, 0.1882352977991104, 0.1882352977991104),
                                  (1.0, 1.0, 1.0)],
                        'blue': [(0.0, 1.0, 1.0),
                                 (0.08, 0.9686274528503418, 0.9686274528503418),
                                 (0.16, 0.9372549057006836, 0.9372549057006836),
                                 (0.24, 0.8823529481887817, 0.8823529481887817),
                                 (0.32, 0.8392156958580017, 0.8392156958580017),
                                 (0.40, 0.7764706015586853, 0.7764706015586853),
                                 (0.48, 0.7098039388656616, 0.7098039388656616),
                                 (0.56, 0.6117647290229797, 0.6117647290229797),
                                 (0.64, 0.41960784792900085, 0.41960784792900085),
                                 (1.0, 0.0, 0.0)]
                        }

# (0.0 -> black), (0.05 -> dark blue), (0.5 -> white), (1.0 -> dark red)
_cdict_BlackBlueWhiteRed = {'red': [(0.0, 0.0, 0.0),
                                    (0.05, 0.019607843831181526, 0.019607843831181526),
                                    (0.1, 0.12941177189350128, 0.12941177189350128),
                                    (0.2, 0.26274511218070984, 0.26274511218070984),
                                    (0.3, 0.572549045085907, 0.572549045085907),
                                    (0.4, 0.8196078538894653, 0.8196078538894653),
                                    (0.5, 0.9686274528503418, 0.9686274528503418),
                                    (0.6, 0.9921568632125854, 0.9921568632125854),
                                    (0.7, 0.95686274766922, 0.95686274766922),
                                    (0.8, 0.8392156958580017, 0.8392156958580017),
                                    (0.9, 0.6980392336845398, 0.6980392336845398),
                                    (1.0, 0.40392157435417175, 0.40392157435417175)],
                            'green': [(0.0, 0.0, 0.0),
                                      (0.05, 0.1882352977991104, 0.1882352977991104),
                                      (0.1, 0.4000000059604645, 0.4000000059604645),
                                      (0.2, 0.5764706134796143, 0.5764706134796143),
                                      (0.3, 0.772549033164978, 0.772549033164978),
                                      (0.4, 0.8980392217636108, 0.8980392217636108),
                                      (0.5, 0.9686274528503418, 0.9686274528503418),
                                      (0.6, 0.8588235378265381, 0.8588235378265381),
                                      (0.7, 0.6470588445663452, 0.6470588445663452),
                                      (0.8, 0.3764705955982208, 0.3764705955982208),
                                      (0.9, 0.0941176488995552, 0.0941176488995552),
                                      (1.0, 0.0, 0.0)],
                            'blue': [(0.0, 0.0, 0.0),
                                     (0.05, 0.3803921639919281, 0.3803921639919281),
                                     (0.1, 0.6745098233222961, 0.6745098233222961),
                                     (0.2, 0.7647058963775635, 0.7647058963775635),
                                     (0.3, 0.8705882430076599, 0.8705882430076599),
                                     (0.4, 0.9411764740943909, 0.9411764740943909),
                                     (0.5, 0.9686274528503418, 0.9686274528503418),
                                     (0.6, 0.7803921699523926, 0.7803921699523926),
                                     (0.7, 0.5098039507865906, 0.5098039507865906),
                                     (0.8, 0.3019607961177826, 0.3019607961177826),
                                     (0.9, 0.16862745583057404, 0.16862745583057404),
                                     (1.0, 0.12156862765550613, 0.12156862765550613)]
                            }

# (0.0 -> black), (0.05 -> blue), (0.5 -> yellow), (1.0 -> red)
_cdict_BlackBlueYellowRed = {'red': [(0.0, 0.0, 0.0),
                                     (0.05, 0.1921568661928177, 0.1921568661928177),
                                     (0.1, 0.2705882489681244, 0.2705882489681244),
                                     (0.2, 0.45490196347236633, 0.45490196347236633),
                                     (0.3, 0.6705882549285889, 0.6705882549285889),
                                     (0.4, 0.8784313797950745, 0.8784313797950745),
                                     (0.5, 1.0, 1.0),
                                     (0.6, 0.9921568632125854, 0.9921568632125854),
                                     (0.7, 0.95686274766922, 0.95686274766922),
                                     (0.8, 0.8392156958580017, 0.8392156958580017),
                                     (0.9, 0.6980392336845398, 0.6980392336845398),
                                     (1.0, 0.40392157435417175, 0.40392157435417175)],
                             'green': [(0.0, 0.0, 0.0),
                                       (0.05, 0.21176470816135406, 0.21176470816135406),
                                       (0.1, 0.4588235318660736, 0.4588235318660736),
                                       (0.2, 0.6784313917160034, 0.6784313917160034),
                                       (0.3, 0.8509804010391235, 0.8509804010391235),
                                       (0.4, 0.9529411792755127, 0.9529411792755127),
                                       (0.5, 1.0, 1.0),
                                       (0.6, 0.8588235378265381, 0.8588235378265381),
                                       (0.7, 0.6470588445663452, 0.6470588445663452),
                                       (0.8, 0.3764705955982208, 0.3764705955982208),
                                       (0.9, 0.0941176488995552, 0.0941176488995552),
                                       (1.0, 0.0, 0.0)],
                             'blue': [(0.0, 0.0, 0.0),
                                      (0.05, 0.5843137502670288, 0.5843137502670288),
                                      (0.1, 0.7058823704719543, 0.7058823704719543),
                                      (0.2, 0.8196078538894653, 0.8196078538894653),
                                      (0.3, 0.9137254953384399, 0.9137254953384399),
                                      (0.4, 0.9725490212440491, 0.9725490212440491),
                                      (0.5, 0.7490196228027344, 0.7490196228027344),
                                      (0.6, 0.7803921699523926, 0.7803921699523926),
                                      (0.7, 0.5098039507865906, 0.5098039507865906),
                                      (0.8, 0.3019607961177826, 0.3019607961177826),
                                      (0.9, 0.16862745583057404, 0.16862745583057404),
                                      (1.0, 0.12156862765550613, 0.12156862765550613)]
                             }

# (0.0 -> black), (0.05 -> dark blue), (0.5 -> green), (1.0 -> yellow)
_cdict_BlackBlueGreenYellow = {'red': [(0.0, 0.0, 0.0),
                                       (0.05, 0.0313725508749485, 0.0313725508749485),
                                       (0.125, 0.14509804546833038, 0.14509804546833038),
                                       (0.25, 0.13333334028720856, 0.13333334028720856),
                                       (0.375, 0.11372549086809158, 0.11372549086809158),
                                       (0.5, 0.2549019753932953, 0.2549019753932953),
                                       (0.625, 0.49803921580314636, 0.49803921580314636),
                                       (0.75, 0.7803921699523926, 0.7803921699523926),
                                       (0.875, 0.929411768913269, 0.929411768913269),
                                       (1.0, 1.0, 1.0)],
                               'green': [(0.0, 0.0, 0.0),
                                         (0.05, 0.11372549086809158, 0.11372549086809158),
                                         (0.125, 0.20392157137393951, 0.20392157137393951),
                                         (0.25, 0.3686274588108063, 0.3686274588108063),
                                         (0.375, 0.5686274766921997, 0.5686274766921997),
                                         (0.5, 0.7137255072593689, 0.7137255072593689),
                                         (0.625, 0.8039215803146362, 0.8039215803146362),
                                         (0.75, 0.9137254953384399, 0.9137254953384399),
                                         (0.875, 0.9725490212440491, 0.9725490212440491),
                                         (1.0, 1.0, 1.0)],
                               'blue': [(0.0, 0.0, 0.0),
                                        (0.05, 0.3450980484485626, 0.3450980484485626),
                                        (0.125, 0.5803921818733215, 0.5803921818733215),
                                        (0.25, 0.658823549747467, 0.658823549747467),
                                        (0.375, 0.7529411911964417, 0.7529411911964417),
                                        (0.5, 0.7686274647712708, 0.7686274647712708),
                                        (0.625, 0.7333333492279053, 0.7333333492279053),
                                        (0.75, 0.7058823704719543, 0.7058823704719543),
                                        (0.875, 0.6941176652908325, 0.6941176652908325),
                                        (1.0, 0.8509804010391235, 0.8509804010391235)]
                               }

# Adapted from matplotlib 'Spectral' colormap
# (0.0 -> black), (0.2 -> dark red), (0.5 -> white), (1.0 -> blue green)
_cdict_dark_thermal = {'red': [(0.0, 0.0, 0.0),
                               (0.09, 0.6196078658103943, 0.6196078658103943),
                               (0.18, 0.8352941274642944, 0.8352941274642944),
                               (0.27, 0.95686274766922, 0.95686274766922),
                               (0.36, 0.9921568632125854, 0.9921568632125854),
                               (0.45, 0.9960784316062927, 0.9960784316062927),
                               (0.54, 1.0, 1.0),
                               (0.63, 0.9019607901573181, 0.9019607901573181),
                               (0.72, 0.6705882549285889, 0.6705882549285889),
                               (0.81, 0.4000000059604645, 0.4000000059604645),
                               (0.90, 0.19607843458652496, 0.19607843458652496),
                               (1.0, 0.3686274588108063, 0.3686274588108063)],
                       'green': [(0.0, 0.0, 0.0),
                                 (0.09, 0.003921568859368563, 0.003921568859368563),
                                 (0.18, 0.24313725531101227, 0.24313725531101227),
                                 (0.27, 0.4274509847164154, 0.4274509847164154),
                                 (0.36, 0.6823529601097107, 0.6823529601097107),
                                 (0.45, 0.8784313797950745, 0.8784313797950745),
                                 (0.54, 1.0, 1.0),
                                 (0.63, 0.9607843160629272, 0.9607843160629272),
                                 (0.72, 0.8666666746139526, 0.8666666746139526),
                                 (0.81, 0.7607843279838562, 0.7607843279838562),
                                 (0.90, 0.5333333611488342, 0.5333333611488342),
                                 (1.0, 0.30980393290519714, 0.30980393290519714)],
                       'blue': [(0.0, 0.0, 0.0),
                                (0.09, 0.25882354378700256, 0.25882354378700256),
                                (0.18, 0.30980393290519714, 0.30980393290519714),
                                (0.27, 0.26274511218070984, 0.26274511218070984),
                                (0.36, 0.3803921639919281, 0.3803921639919281),
                                (0.45, 0.545098066329956, 0.545098066329956),
                                (0.54, 0.7490196228027344, 0.7490196228027344),
                                (0.63, 0.5960784554481506, 0.5960784554481506),
                                (0.72, 0.6431372761726379, 0.6431372761726379),
                                (0.81, 0.6470588445663452, 0.6470588445663452),
                                (0.90, 0.7411764860153198, 0.7411764860153198),
                                (1.0, 0.6352941393852234, 0.6352941393852234)]
                       }

# (0.0 -> black), (0.05 -> purple red), (0.5 -> white), (1.0 -> blue green)
_cdict_BlackPurplWhitBlGreen = {'red': [(0.0, 0.0, 0.0),
                                        (0.05, 0.250980406999588, 0.250980406999588),
                                        (0.1, 0.4627451002597809, 0.4627451002597809),
                                        (0.2, 0.6000000238418579, 0.6000000238418579),
                                        (0.3, 0.7607843279838562, 0.7607843279838562),
                                        (0.4, 0.9058823585510254, 0.9058823585510254),
                                        (0.5, 0.9686274528503418, 0.9686274528503418),
                                        (0.6, 0.7803921699523926, 0.7803921699523926),
                                        (0.7, 0.501960813999176, 0.501960813999176),
                                        (0.8, 0.2078431397676468, 0.2078431397676468),
                                        (0.9, 0.003921568859368563, 0.003921568859368563),
                                        (1.0, 0.0, 0.0)],
                                'green': [(0.0, 0.0, 0.0),
                                          (0.05, 0.0, 0.0),
                                          (0.1, 0.16470588743686676, 0.16470588743686676),
                                          (0.2, 0.43921568989753723, 0.43921568989753723),
                                          (0.3, 0.6470588445663452, 0.6470588445663452),
                                          (0.4, 0.8313725590705872, 0.8313725590705872),
                                          (0.5, 0.9686274528503418, 0.9686274528503418),
                                          (0.6, 0.9176470637321472, 0.9176470637321472),
                                          (0.7, 0.8039215803146362, 0.8039215803146362),
                                          (0.8, 0.5921568870544434, 0.5921568870544434),
                                          (0.9, 0.4000000059604645, 0.4000000059604645),
                                          (1.0, 0.23529411852359772, 0.23529411852359772)],
                                'blue': [(0.0, 0.0, 0.0),
                                         (0.05, 0.29411765933036804, 0.29411765933036804),
                                         (0.1, 0.5137255191802979, 0.5137255191802979),
                                         (0.2, 0.6705882549285889, 0.6705882549285889),
                                         (0.3, 0.8117647171020508, 0.8117647171020508),
                                         (0.4, 0.9098039269447327, 0.9098039269447327),
                                         (0.5, 0.9607843160629272, 0.9607843160629272),
                                         (0.6, 0.8980392217636108, 0.8980392217636108),
                                         (0.7, 0.7568627595901489, 0.7568627595901489),
                                         (0.8, 0.5607843399047852, 0.5607843399047852),
                                         (0.9, 0.3686274588108063, 0.3686274588108063),
                                         (1.0, 0.1882352977991104, 0.1882352977991104)]
                                }

_jet_black_cdict = {'red': [(0., 0., 0.),
                            (0.30, 0.000, 0.000),
                            (0.40, 0.2778, 0.2778),
                            (0.52, 0.2778, 0.2778),
                            (0.64, 1.000, 1.000),
                            (0.76, 1.000, 1.000),
                            (0.88, 0.944, 0.944),
                            (1., 0.5, 0.5)],
                    'green': [(0., 0., 0.),
                              (0.10, 0.000, 0.000),
                              (0.25, 0.389, 0.389),
                              (0.32, 0.833, 0.833),
                              (0.40, 1.000, 1.000),
                              (0.52, 1.000, 1.000),
                              (0.64, 0.803, 0.803),
                              (0.76, 0.389, 0.389),
                              (0.88, 0.000, 0.000),
                              (1., 0., 0.)],
                    'blue': [(0., 0.00, 0.00),
                             (0.001, 0., 0.),
                             (0.07, 0.500, 0.500),
                             (0.12, 0.900, 0.900),
                             (0.23, 1.000, 1.000),
                             (0.28, 1.000, 1.000),
                             (0.40, 0.722, 0.722),
                             (0.52, 0.2778, 0.2778),
                             (0.64, 0.000, 0.000),
                             (1., 0., 0.)]
                    }

_viridis_dark_data = [[0, 0, 0],
                      [0.0161514, 0, 0.0112014],
                      [0.0318496, 0, 0.0224607],
                      [0.0467742, 0, 0.0337536],
                      [0.0603049, 0, 0.0444809],
                      [0.0729055, 0, 0.0541351],
                      [0.0847256, 0, 0.0633756],
                      [0.0958802, 0, 0.0723286],
                      [0.106443, 0, 0.0810819],
                      [0.116466, 0, 0.0896948],
                      [0.125987, 0, 0.0982081],
                      [0.13505, 0, 0.106701],
                      [0.143587, 0, 0.114985],
                      [0.151458, 0, 0.123056],
                      [0.1587, 0, 0.130931],
                      [0.165354, 0, 0.138632],
                      [0.171458, 0, 0.146177],
                      [0.177053, 0, 0.153584],
                      [0.182175, 0, 0.16087],
                      [0.186861, 0, 0.168052],
                      [0.191252, 0, 0.175213],
                      [0.195571, 0, 0.182487],
                      [0.199821, 0, 0.18987],
                      [0.203995, 0, 0.197352],
                      [0.208054, 0, 0.204922],
                      [0.211995, 0, 0.212572],
                      [0.215823, 0, 0.220295],
                      [0.219544, 0, 0.228085],
                      [0.223161, 0, 0.235936],
                      [0.226681, 0, 0.243841],
                      [0.230107, 0, 0.251794],
                      [0.233445, 0, 0.259788],
                      [0.236701, 0, 0.267816],
                      [0.23988, 0, 0.275873],
                      [0.242988, 0, 0.283951],
                      [0.24603, 0, 0.292045],
                      [0.249014, 0, 0.300147],
                      [0.251945, 0, 0.308252],
                      [0.253819, 0, 0.315371],
                      [0.255065, 0, 0.321905],
                      [0.256255, 0.000565296, 0.328397],
                      [0.257346, 0.00564151, 0.334803],
                      [0.258347, 0.0110731, 0.34113],
                      [0.259259, 0.016872, 0.347374],
                      [0.260095, 0.0230161, 0.353546],
                      [0.260816, 0.0296044, 0.35961],
                      [0.26145, 0.0365879, 0.365583],
                      [0.261991, 0.0438428, 0.37146],
                      [0.262435, 0.0508283, 0.377239],
                      [0.262785, 0.0575676, 0.382914],
                      [0.263039, 0.0641126, 0.388485],
                      [0.263197, 0.0705, 0.393948],
                      [0.263264, 0.076753, 0.399306],
                      [0.263235, 0.0829015, 0.404551],
                      [0.263111, 0.088961, 0.409682],
                      [0.262892, 0.0949461, 0.414695],
                      [0.262579, 0.100867, 0.419591],
                      [0.262171, 0.106732, 0.424367],
                      [0.261672, 0.112548, 0.429023],
                      [0.26108, 0.118322, 0.433556],
                      [0.260395, 0.124059, 0.437964],
                      [0.259621, 0.129762, 0.442247],
                      [0.258757, 0.135436, 0.446403],
                      [0.257805, 0.14108, 0.450434],
                      [0.256766, 0.146699, 0.454338],
                      [0.255643, 0.152293, 0.458114],
                      [0.254436, 0.157864, 0.461763],
                      [0.253147, 0.163413, 0.465286],
                      [0.25178, 0.16894, 0.468682],
                      [0.250337, 0.174445, 0.471954],
                      [0.248818, 0.179929, 0.475102],
                      [0.247228, 0.185392, 0.478127],
                      [0.245568, 0.190833, 0.481031],
                      [0.243842, 0.196254, 0.483815],
                      [0.24205, 0.201653, 0.486483],
                      [0.240201, 0.207029, 0.489037],
                      [0.238293, 0.212383, 0.491479],
                      [0.23633, 0.217714, 0.49381],
                      [0.234315, 0.223023, 0.496034],
                      [0.232252, 0.228309, 0.498154],
                      [0.230146, 0.233571, 0.500175],
                      [0.227999, 0.238808, 0.502098],
                      [0.225814, 0.244022, 0.503927],
                      [0.223593, 0.249211, 0.505664],
                      [0.221339, 0.254376, 0.507313],
                      [0.219058, 0.259517, 0.508877],
                      [0.216756, 0.264631, 0.510364],
                      [0.214431, 0.269721, 0.511773],
                      [0.212088, 0.274786, 0.513107],
                      [0.209729, 0.279827, 0.514372],
                      [0.207356, 0.284844, 0.515568],
                      [0.204977, 0.289835, 0.516702],
                      [0.202594, 0.294801, 0.517778],
                      [0.200207, 0.299744, 0.518797],
                      [0.197819, 0.304663, 0.519762],
                      [0.195432, 0.309558, 0.520675],
                      [0.19305, 0.314432, 0.52154],
                      [0.190676, 0.319282, 0.522361],
                      [0.188312, 0.324109, 0.523142],
                      [0.185959, 0.328916, 0.523881],
                      [0.183617, 0.333701, 0.524584],
                      [0.181291, 0.338466, 0.525251],
                      [0.178981, 0.343211, 0.525886],
                      [0.176692, 0.347936, 0.526493],
                      [0.174423, 0.352643, 0.527071],
                      [0.172172, 0.357332, 0.527621],
                      [0.169942, 0.362003, 0.528146],
                      [0.167732, 0.366658, 0.528647],
                      [0.165547, 0.371297, 0.529126],
                      [0.163385, 0.37592, 0.529586],
                      [0.161245, 0.380529, 0.530025],
                      [0.159128, 0.385125, 0.530445],
                      [0.157032, 0.389707, 0.530846],
                      [0.154958, 0.394276, 0.531229],
                      [0.152906, 0.398834, 0.531595],
                      [0.150876, 0.403381, 0.531945],
                      [0.148864, 0.407918, 0.532278],
                      [0.146872, 0.412445, 0.532596],
                      [0.144896, 0.416963, 0.532896],
                      [0.142938, 0.421472, 0.533179],
                      [0.140994, 0.425974, 0.533446],
                      [0.139064, 0.430469, 0.533697],
                      [0.137146, 0.434958, 0.533929],
                      [0.135238, 0.43944, 0.534144],
                      [0.133339, 0.443918, 0.534338],
                      [0.131446, 0.44839, 0.534513],
                      [0.12956, 0.452859, 0.534669],
                      [0.127677, 0.457324, 0.534801],
                      [0.125795, 0.461786, 0.534911],
                      [0.123915, 0.466245, 0.534996],
                      [0.122034, 0.470702, 0.535056],
                      [0.120151, 0.475158, 0.53509],
                      [0.118267, 0.479611, 0.535094],
                      [0.116381, 0.484064, 0.53507],
                      [0.114493, 0.488516, 0.535014],
                      [0.112603, 0.492967, 0.534927],
                      [0.110713, 0.497418, 0.534804],
                      [0.108821, 0.50187, 0.534645],
                      [0.106931, 0.506321, 0.534447],
                      [0.105046, 0.510773, 0.534211],
                      [0.103168, 0.515225, 0.533931],
                      [0.101301, 0.519679, 0.533608],
                      [0.0994569, 0.524132, 0.533242],
                      [0.0976322, 0.528586, 0.532827],
                      [0.0958394, 0.533041, 0.532364],
                      [0.0940846, 0.537496, 0.531849],
                      [0.092379, 0.541952, 0.531281],
                      [0.0907335, 0.546409, 0.530658],
                      [0.0891595, 0.550866, 0.529978],
                      [0.0876746, 0.555323, 0.52924],
                      [0.0862923, 0.55978, 0.52844],
                      [0.0850294, 0.564236, 0.527579],
                      [0.0839037, 0.568692, 0.526653],
                      [0.0829353, 0.573147, 0.52566],
                      [0.0821463, 0.577601, 0.524599],
                      [0.0815589, 0.582054, 0.523468],
                      [0.0811942, 0.586504, 0.522267],
                      [0.0810737, 0.590952, 0.520992],
                      [0.0812191, 0.595398, 0.51964],
                      [0.0816505, 0.59984, 0.518213],
                      [0.0823856, 0.604279, 0.516706],
                      [0.083444, 0.608713, 0.515122],
                      [0.0848357, 0.613142, 0.513455],
                      [0.0865737, 0.617567, 0.511704],
                      [0.0886636, 0.621985, 0.50987],
                      [0.0911124, 0.626396, 0.507951],
                      [0.0939178, 0.630801, 0.505943],
                      [0.09708, 0.635198, 0.503848],
                      [0.100593, 0.639586, 0.501663],
                      [0.104449, 0.643966, 0.499387],
                      [0.108641, 0.648335, 0.497019],
                      [0.113158, 0.652694, 0.494558],
                      [0.11799, 0.657041, 0.492004],
                      [0.123124, 0.661377, 0.489354],
                      [0.128544, 0.6657, 0.486608],
                      [0.134243, 0.670009, 0.483764],
                      [0.140206, 0.674304, 0.480824],
                      [0.146425, 0.678584, 0.477784],
                      [0.152887, 0.682848, 0.474646],
                      [0.15958, 0.687095, 0.471406],
                      [0.166494, 0.691324, 0.468066],
                      [0.17362, 0.695535, 0.464623],
                      [0.180952, 0.699727, 0.461079],
                      [0.18848, 0.703898, 0.457434],
                      [0.196197, 0.708049, 0.453686],
                      [0.204095, 0.712177, 0.449831],
                      [0.212168, 0.716283, 0.445873],
                      [0.22041, 0.720365, 0.441809],
                      [0.228818, 0.724422, 0.437643],
                      [0.237385, 0.728453, 0.433373],
                      [0.246106, 0.732458, 0.428995],
                      [0.254978, 0.736436, 0.424511],
                      [0.263995, 0.740385, 0.419919],
                      [0.273156, 0.744305, 0.415221],
                      [0.282459, 0.748194, 0.41042],
                      [0.291897, 0.752052, 0.405511],
                      [0.301468, 0.755878, 0.400496],
                      [0.311168, 0.759671, 0.395373],
                      [0.320996, 0.76343, 0.390142],
                      [0.330953, 0.767154, 0.384805],
                      [0.341034, 0.770841, 0.379363],
                      [0.351235, 0.774491, 0.373813],
                      [0.361553, 0.778104, 0.368157],
                      [0.371988, 0.781678, 0.362394],
                      [0.382535, 0.785212, 0.356525],
                      [0.393198, 0.788705, 0.350553],
                      [0.403974, 0.792156, 0.344474],
                      [0.414857, 0.795564, 0.338289],
                      [0.425845, 0.798929, 0.331999],
                      [0.436936, 0.80225, 0.325605],
                      [0.448129, 0.805526, 0.319108],
                      [0.459424, 0.808755, 0.312514],
                      [0.470816, 0.811937, 0.305816],
                      [0.482302, 0.815072, 0.29902],
                      [0.49388, 0.818158, 0.292123],
                      [0.505547, 0.821196, 0.285128],
                      [0.517304, 0.824183, 0.27804],
                      [0.529148, 0.827119, 0.27086],
                      [0.541072, 0.830005, 0.26359],
                      [0.553072, 0.83284, 0.256231],
                      [0.565146, 0.835623, 0.248789],
                      [0.57729, 0.838354, 0.241266],
                      [0.589505, 0.841033, 0.233675],
                      [0.601782, 0.843659, 0.226015],
                      [0.614117, 0.846232, 0.218294],
                      [0.626506, 0.848754, 0.210518],
                      [0.638942, 0.851224, 0.202699],
                      [0.651423, 0.853642, 0.19485],
                      [0.663947, 0.856008, 0.18699],
                      [0.676502, 0.858323, 0.179129],
                      [0.689084, 0.860589, 0.171289],
                      [0.701685, 0.862806, 0.163494],
                      [0.714302, 0.864975, 0.155776],
                      [0.72693, 0.867097, 0.148174],
                      [0.73956, 0.869174, 0.14073],
                      [0.752184, 0.871207, 0.133492],
                      [0.764795, 0.873199, 0.126526],
                      [0.777386, 0.87515, 0.119903],
                      [0.78995, 0.877064, 0.113707],
                      [0.802484, 0.878941, 0.108045],
                      [0.814975, 0.880785, 0.103016],
                      [0.827419, 0.882597, 0.0987365],
                      [0.839808, 0.884381, 0.0953251],
                      [0.852135, 0.886139, 0.0928926],
                      [0.864394, 0.887874, 0.0915341],
                      [0.876581, 0.889587, 0.0913155],
                      [0.888688, 0.891282, 0.0922687],
                      [0.900709, 0.892962, 0.0943853],
                      [0.912641, 0.894628, 0.0976211],
                      [0.924473, 0.896286, 0.101902],
                      [0.936203, 0.897936, 0.107134],
                      [0.94783, 0.899582, 0.113207],
                      [0.959351, 0.901224, 0.12002],
                      [0.970762, 0.902867, 0.127472],
                      [0.982061, 0.90451, 0.135471],
                      [0.993248, 0.906157, 0.143936]]


_cdict_dark_Green = {"green": lambda x: x, "red": lambda x: 6*x-5.2, "blue": lambda x: 4*x-3.2}


custom_cmaps = {"BlackBlueWhiteRed": LinearSegmentedColormap('BlackBlueWhiteRed', _cdict_BlackBlueWhiteRed, 512),
                "BlackBlueYellowRed": LinearSegmentedColormap('BlackBlueYellowRed', _cdict_BlackBlueYellowRed, 512),
                "BlueYellowTanager": LinearSegmentedColormap('BlueYellowTanager', _cdict_BlackBlueGreenYellow, 512),
                "BlackPurpWhiBlGreen": LinearSegmentedColormap('BlackPurpWhiBlGreen', _cdict_BlackPurplWhitBlGreen, 512),
                "Dark_thermal": LinearSegmentedColormap('Dark_thermal', _cdict_dark_thermal, 512),
                'Viridis_dark': LinearSegmentedColormap.from_list('Viridis_dark', _viridis_dark_data),
                "JetBlack": LinearSegmentedColormap('JetBlack', _jet_black_cdict, 512),
                "WhiteBlueYellow": LinearSegmentedColormap("WhiteBlueYellow", _cdict_WhiBlueYellow, 512),
                "Dark_green": LinearSegmentedColormap("Dark_green", _cdict_dark_Green, 512)
}


class CustomColormaps(object):
    @classmethod
    def cmap_list(cls):
        l = list(custom_cmaps.keys()) + list(cm.cmap_d.keys())
        l.sort()
        return l

    @classmethod
    def get_cmap(cls, cmap):
        if isinstance(cmap, Colormap):
            colormap = cmap
        else:
            # Sanity check
            if not isinstance(cmap, str):
                raise AttributeError("'name' must be a valid colormap name (string) !")

            if cmap in custom_cmaps:
                # Try to find colormap in custom catalog
                colormap = custom_cmaps[cmap]
            else:
                # Try to find the colormap in matplotlib colormap catalog
                try:
                    colormap = cm.get_cmap(cmap)
                except ValueError:
                    raise AttributeError(
                        "'%s' colormap neither found in custom colormap table :\n%s\n nor in "
                        "matplotlib colormaps :\n%s" % (cmap, list(custom_cmaps.keys()),
                                                        list(cm.cmap_d.keys())))
        return colormap


__all__ = ["CustomColormaps"]
