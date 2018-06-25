import numpy

try:
    import pyproj
except ImportError:
    from mpl_toolkits.basemap import pyproj

import numpy.testing as nptest
import pytest

import pygridgen


@pytest.fixture
def options():
    options = {
        'ul_idx': 0,
        'focus': None,
        'proj': None,
        'nnodes': 14,
        'precision': 1e-12,
        'nppe': 3,
        'newton': True,
        'thin': True,
        'checksimplepoly': True,
        'verbose': False,
        'autogen': True
    }
    return options


@pytest.fixture
def grid_basic(options):
    beta = [1.0, 1.0, 0.0, 1.0, 1.0]
    shape = (10, 5)
    x, y = known_xy_basic()['boundary']
    grid = pygridgen.Gridgen(x, y, beta, shape, **options)
    return grid


@pytest.fixture
def grid_autogenFalse(options):
    beta = [1.0, 1.0, 0.0, 1.0, 1.0]
    shape = (10, 5)

    options.update({'autogen': False})
    x, y = known_xy_basic()['boundary']
    grid = pygridgen.Gridgen(x, y, beta, shape, **options)
    grid.generate_grid()
    return grid


@pytest.fixture
def known_xy_basic():
    x = [0.0, 1.0, 2.0, 1.0, 0.0]
    y = [0.0, 0.0, 0.5, 1.0, 1.0]

    known_x = numpy.array([
        [ 1.  ,  1.12,  2.  ,  1.12,  1.  ],
        [ 0.96,  1.03,  1.17,  1.03,  0.96],
        [ 0.87,  0.91,  0.96,  0.91,  0.87],
        [ 0.77,  0.78,  0.8 ,  0.78,  0.77],
        [ 0.65,  0.65,  0.66,  0.65,  0.65],
        [ 0.52,  0.52,  0.53,  0.52,  0.52],
        [ 0.39,  0.39,  0.39,  0.39,  0.39],
        [ 0.26,  0.26,  0.26,  0.26,  0.26],
        [ 0.13,  0.13,  0.13,  0.13,  0.13],
        [ 0.  ,  0.  ,  0.  ,  0.  ,  0.  ]
    ])

    known_y = numpy.array([
        [ 0.  ,  0.06,  0.5 ,  0.94,  1.  ],
        [-0.  ,  0.16,  0.5 ,  0.84,  1.  ],
        [-0.  ,  0.21,  0.5 ,  0.79,  1.  ],
        [-0.  ,  0.23,  0.5 ,  0.77,  1.  ],
        [-0.  ,  0.24,  0.5 ,  0.76,  1.  ],
        [-0.  ,  0.25,  0.5 ,  0.75,  1.  ],
        [-0.  ,  0.25,  0.5 ,  0.75,  1.  ],
        [-0.  ,  0.25,  0.5 ,  0.75,  1.  ],
        [-0.  ,  0.25,  0.5 ,  0.75,  1.  ],
        [-0.  ,  0.25,  0.5 ,  0.75,  1.  ]
    ])

    known_x_psi = numpy.array([
        [ 1.03,  1.17,  1.03],
        [ 0.91,  0.96,  0.91],
        [ 0.78,  0.8 ,  0.78],
        [ 0.65,  0.66,  0.65],
        [ 0.52,  0.53,  0.52],
        [ 0.39,  0.39,  0.39],
        [ 0.26,  0.26,  0.26],
        [ 0.13,  0.13,  0.13]
    ])

    known_y_psi = numpy.array([
        [ 0.16,  0.5 ,  0.84],
        [ 0.21,  0.5 ,  0.79],
        [ 0.23,  0.5 ,  0.77],
        [ 0.24,  0.5 ,  0.76],
        [ 0.25,  0.5 ,  0.75],
        [ 0.25,  0.5 ,  0.75],
        [ 0.25,  0.5 ,  0.75],
        [ 0.25,  0.5 ,  0.75]
    ])

    known_x_rho = numpy.array([
        [ 1.03,  1.33,  1.33,  1.03],
        [ 0.94,  1.02,  1.02,  0.94],
        [ 0.83,  0.87,  0.87,  0.83],
        [ 0.71,  0.73,  0.73,  0.71],
        [ 0.59,  0.59,  0.59,  0.59],
        [ 0.46,  0.46,  0.46,  0.46],
        [ 0.33,  0.33,  0.33,  0.33],
        [ 0.2 ,  0.2 ,  0.2 ,  0.2 ],
        [ 0.07,  0.07,  0.07,  0.07]
    ])

    known_y_rho = numpy.array([
        [ 0.05,  0.3 ,  0.7 ,  0.95],
        [ 0.09,  0.34,  0.66,  0.91],
        [ 0.11,  0.36,  0.64,  0.89],
        [ 0.12,  0.37,  0.63,  0.88],
        [ 0.12,  0.37,  0.63,  0.88],
        [ 0.12,  0.37,  0.63,  0.88],
        [ 0.12,  0.37,  0.63,  0.88],
        [ 0.12,  0.37,  0.63,  0.88],
        [ 0.12,  0.37,  0.63,  0.88]
    ])

    known_x_u = numpy.array([
        [ 1.08,  1.58,  1.08],
        [ 0.97,  1.06,  0.97],
        [ 0.85,  0.88,  0.85],
        [ 0.72,  0.73,  0.72],
        [ 0.59,  0.59,  0.59],
        [ 0.46,  0.46,  0.46],
        [ 0.33,  0.33,  0.33],
        [ 0.2 ,  0.2 ,  0.2 ],
        [ 0.07,  0.07,  0.07]
    ])

    known_x_v = numpy.array([
        [ 1.  ,  1.1 ,  1.1 ,  1.  ],
        [ 0.89,  0.94,  0.94,  0.89],
        [ 0.78,  0.79,  0.79,  0.78],
        [ 0.65,  0.66,  0.66,  0.65],
        [ 0.52,  0.53,  0.53,  0.52],
        [ 0.39,  0.39,  0.39,  0.39],
        [ 0.26,  0.26,  0.26,  0.26],
        [ 0.13,  0.13,  0.13,  0.13]
    ])

    known_y_u = numpy.array([
        [ 0.11,  0.5 ,  0.89],
        [ 0.18,  0.5 ,  0.82],
        [ 0.22,  0.5 ,  0.78],
        [ 0.24,  0.5 ,  0.76],
        [ 0.24,  0.5 ,  0.76],
        [ 0.25,  0.5 ,  0.75],
        [ 0.25,  0.5 ,  0.75],
        [ 0.25,  0.5 ,  0.75],
        [ 0.25,  0.5 ,  0.75]
    ])

    known_y_v = numpy.array([
        [ 0.08,  0.33,  0.67,  0.92],
        [ 0.1 ,  0.35,  0.65,  0.9 ],
        [ 0.12,  0.37,  0.63,  0.88],
        [ 0.12,  0.37,  0.63,  0.88],
        [ 0.12,  0.37,  0.63,  0.88],
        [ 0.12,  0.37,  0.63,  0.88],
        [ 0.12,  0.37,  0.63,  0.88],
        [ 0.12,  0.37,  0.63,  0.88]
    ])

    known_ortho = numpy.array([
        [ 3.559e-01,  3.231e-01, -3.231e-01, -3.559e-01],
        [ 1.044e-01,  6.510e-02, -6.510e-02, -1.044e-01],
        [ 3.690e-02,  2.920e-02, -2.920e-02, -3.690e-02],
        [ 1.490e-02,  1.340e-02, -1.340e-02, -1.490e-02],
        [ 6.300e-03,  6.000e-03, -6.000e-03, -6.300e-03],
        [ 2.700e-03,  2.700e-03, -2.700e-03, -2.700e-03],
        [ 1.200e-03,  1.200e-03, -1.200e-03, -1.200e-03],
        [ 5.000e-04,  5.000e-04, -5.000e-04, -5.000e-04],
        [ 1.000e-04,  1.000e-04, -1.000e-04, -1.000e-04]
    ])

    known = {
        'boundary': (x, y),
        'vert': (known_x, known_y),
        'psi': (known_x_psi, known_y_psi),
        'rho': (known_x_rho, known_y_rho),
        'u': (known_x_u, known_y_u),
        'v': (known_x_v, known_y_v),
        'ortho': known_ortho
    }
    return known


@pytest.fixture
def grid_focused(options):
    beta = [1.0, 1.0, 0.0, 1.0, 1.0]
    shape = (9, 9)
    focus = pygridgen.Focus()
    focus.add_focus(0.50, 'x', factor=2.0, extent=3.0)
    focus.add_focus(0.75, 'y', factor=0.5, extent=2.0)

    options.update({'ul_idx': 0, 'focus': focus})
    x, y = known_xy_focused()['boundary']
    grid = pygridgen.Gridgen(x, y, beta, shape, **options)
    return grid


@pytest.fixture
def known_xy_focused():
    x = [0.0, 1.0, 2.0, 1.0, 0.0]
    y = [0.0, 0.0, 0.5, 1.0, 1.0]

    known_x = numpy.array([
        [ 1.  ,  1.04,  1.12,  1.27,  2.  ,  1.27,  1.12,  1.04,  1.  ],
        [ 0.95,  0.97,  1.02,  1.1 ,  1.15,  1.1 ,  1.02,  0.97,  0.95],
        [ 0.86,  0.87,  0.89,  0.92,  0.93,  0.92,  0.89,  0.87,  0.86],
        [ 0.73,  0.74,  0.75,  0.76,  0.76,  0.76,  0.75,  0.74,  0.73],
        [ 0.59,  0.59,  0.6 ,  0.6 ,  0.6 ,  0.6 ,  0.6 ,  0.59,  0.59],
        [ 0.45,  0.45,  0.45,  0.45,  0.45,  0.45,  0.45,  0.45,  0.45],
        [ 0.3 ,  0.3 ,  0.3 ,  0.3 ,  0.3 ,  0.3 ,  0.3 ,  0.3 ,  0.3 ],
        [ 0.15,  0.15,  0.15,  0.15,  0.15,  0.15,  0.15,  0.15,  0.15],
        [ 0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  ]
    ])

    known_y = numpy.array([
        [ 0.  ,  0.02,  0.06,  0.14,  0.5 ,  0.86,  0.94,  0.98,  1.  ],
        [-0.  ,  0.07,  0.16,  0.3 ,  0.5 ,  0.7 ,  0.84,  0.93,  1.  ],
        [-0.  ,  0.1 ,  0.21,  0.35,  0.5 ,  0.65,  0.79,  0.9 ,  1.  ],
        [-0.  ,  0.12,  0.24,  0.37,  0.5 ,  0.63,  0.76,  0.88,  1.  ],
        [-0.  ,  0.12,  0.25,  0.37,  0.5 ,  0.63,  0.75,  0.88,  1.  ],
        [-0.  ,  0.12,  0.25,  0.37,  0.5 ,  0.63,  0.75,  0.88,  1.  ],
        [-0.  ,  0.13,  0.25,  0.38,  0.5 ,  0.62,  0.75,  0.87,  1.  ],
        [-0.  ,  0.13,  0.25,  0.38,  0.5 ,  0.62,  0.75,  0.87,  1.  ],
        [-0.  ,  0.13,  0.25,  0.38,  0.5 ,  0.62,  0.75,  0.87,  1.  ]
    ])

    known_x_psi = numpy.array([
        [ 0.97,  1.02,  1.1 ,  1.15,  1.1 ,  1.02,  0.97],
        [ 0.87,  0.89,  0.92,  0.93,  0.92,  0.89,  0.87],
        [ 0.74,  0.75,  0.76,  0.76,  0.76,  0.75,  0.74],
        [ 0.59,  0.6 ,  0.6 ,  0.6 ,  0.6 ,  0.6 ,  0.59],
        [ 0.45,  0.45,  0.45,  0.45,  0.45,  0.45,  0.45],
        [ 0.3 ,  0.3 ,  0.3 ,  0.3 ,  0.3 ,  0.3 ,  0.3 ],
        [ 0.15,  0.15,  0.15,  0.15,  0.15,  0.15,  0.15]
    ])

    known_y_psi = numpy.array([
        [ 0.07,  0.16,  0.3 ,  0.5 ,  0.7 ,  0.84,  0.93],
        [ 0.1 ,  0.21,  0.35,  0.5 ,  0.65,  0.79,  0.9 ],
        [ 0.12,  0.24,  0.37,  0.5 ,  0.63,  0.76,  0.88],
        [ 0.12,  0.25,  0.37,  0.5 ,  0.63,  0.75,  0.88],
        [ 0.12,  0.25,  0.37,  0.5 ,  0.63,  0.75,  0.88],
        [ 0.13,  0.25,  0.38,  0.5 ,  0.62,  0.75,  0.87],
        [ 0.13,  0.25,  0.38,  0.5 ,  0.62,  0.75,  0.87]
    ])

    known_x_rho = numpy.array([
        [ 0.99,  1.04,  1.13,  1.38,  1.38,  1.13,  1.04,  0.99],
        [ 0.91,  0.94,  0.98,  1.02,  1.02,  0.98,  0.94,  0.91],
        [ 0.8 ,  0.81,  0.83,  0.84,  0.84,  0.83,  0.81,  0.8 ],
        [ 0.66,  0.67,  0.68,  0.68,  0.68,  0.68,  0.67,  0.66],
        [ 0.52,  0.52,  0.52,  0.53,  0.53,  0.52,  0.52,  0.52],
        [ 0.37,  0.37,  0.37,  0.37,  0.37,  0.37,  0.37,  0.37],
        [ 0.22,  0.22,  0.22,  0.22,  0.22,  0.22,  0.22,  0.22],
        [ 0.07,  0.07,  0.07,  0.07,  0.07,  0.07,  0.07,  0.07]
    ])

    known_y_rho = numpy.array([
        [ 0.02,  0.08,  0.16,  0.36,  0.64,  0.84,  0.92,  0.98],
        [ 0.04,  0.14,  0.26,  0.41,  0.59,  0.74,  0.86,  0.96],
        [ 0.05,  0.17,  0.29,  0.43,  0.57,  0.71,  0.83,  0.95],
        [ 0.06,  0.18,  0.3 ,  0.43,  0.57,  0.7 ,  0.82,  0.94],
        [ 0.06,  0.19,  0.31,  0.44,  0.56,  0.69,  0.81,  0.94],
        [ 0.06,  0.19,  0.31,  0.44,  0.56,  0.69,  0.81,  0.94],
        [ 0.06,  0.19,  0.31,  0.44,  0.56,  0.69,  0.81,  0.94],
        [ 0.06,  0.19,  0.31,  0.44,  0.56,  0.69,  0.81,  0.94]
    ])

    known_x_u = numpy.array([
        [ 1.  ,  1.07,  1.19,  1.57,  1.19,  1.07,  1.  ],
        [ 0.92,  0.96,  1.01,  1.04,  1.01,  0.96,  0.92],
        [ 0.8 ,  0.82,  0.84,  0.85,  0.84,  0.82,  0.8 ],
        [ 0.66,  0.67,  0.68,  0.68,  0.68,  0.67,  0.66],
        [ 0.52,  0.52,  0.53,  0.53,  0.53,  0.52,  0.52],
        [ 0.37,  0.37,  0.37,  0.38,  0.37,  0.37,  0.37],
        [ 0.22,  0.22,  0.22,  0.22,  0.22,  0.22,  0.22],
        [ 0.07,  0.07,  0.07,  0.07,  0.07,  0.07,  0.07]
    ])

    known_x_v = numpy.array([
        [ 0.96,  1.  ,  1.06,  1.12,  1.12,  1.06,  1.  ,  0.96],
        [ 0.86,  0.88,  0.9 ,  0.92,  0.92,  0.9 ,  0.88,  0.86],
        [ 0.73,  0.74,  0.75,  0.76,  0.76,  0.75,  0.74,  0.73],
        [ 0.59,  0.6 ,  0.6 ,  0.6 ,  0.6 ,  0.6 ,  0.6 ,  0.59],
        [ 0.45,  0.45,  0.45,  0.45,  0.45,  0.45,  0.45,  0.45],
        [ 0.3 ,  0.3 ,  0.3 ,  0.3 ,  0.3 ,  0.3 ,  0.3 ,  0.3 ],
        [ 0.15,  0.15,  0.15,  0.15,  0.15,  0.15,  0.15,  0.15]
    ])

    known_y_u = numpy.array([
        [ 0.04,  0.11,  0.22,  0.5 ,  0.78,  0.89,  0.96],
        [ 0.09,  0.19,  0.32,  0.5 ,  0.68,  0.81,  0.91],
        [ 0.11,  0.23,  0.36,  0.5 ,  0.64,  0.77,  0.89],
        [ 0.12,  0.24,  0.37,  0.5 ,  0.63,  0.76,  0.88],
        [ 0.12,  0.25,  0.37,  0.5 ,  0.63,  0.75,  0.88],
        [ 0.13,  0.25,  0.37,  0.5 ,  0.63,  0.75,  0.87],
        [ 0.13,  0.25,  0.38,  0.5 ,  0.62,  0.75,  0.87],
        [ 0.13,  0.25,  0.38,  0.5 ,  0.62,  0.75,  0.87]
    ])

    known_y_v = numpy.array([
        [ 0.04,  0.12,  0.23,  0.4 ,  0.6 ,  0.77,  0.88,  0.96],
        [ 0.05,  0.16,  0.28,  0.42,  0.58,  0.72,  0.84,  0.95],
        [ 0.06,  0.18,  0.3 ,  0.43,  0.57,  0.7 ,  0.82,  0.94],
        [ 0.06,  0.18,  0.31,  0.44,  0.56,  0.69,  0.82,  0.94],
        [ 0.06,  0.19,  0.31,  0.44,  0.56,  0.69,  0.81,  0.94],
        [ 0.06,  0.19,  0.31,  0.44,  0.56,  0.69,  0.81,  0.94],
        [ 0.06,  0.19,  0.31,  0.44,  0.56,  0.69,  0.81,  0.94]
    ])

    known_ortho = numpy.array([
        [ 3.234e-01,  4.930e-02,  3.200e-02,  3.006e-01, -3.006e-01, -3.200e-02, -4.930e-02, -3.234e-01],
        [ 3.450e-02,  4.170e-02,  3.210e-02,  1.920e-02, -1.920e-02, -3.210e-02, -4.170e-02, -3.450e-02],
        [ 8.700e-03,  1.750e-02,  1.550e-02,  6.400e-03, -6.400e-03, -1.550e-02, -1.750e-02, -8.700e-03],
        [ 3.000e-03,  6.900e-03,  6.500e-03,  2.600e-03, -2.600e-03, -6.500e-03, -6.900e-03, -3.000e-03],
        [ 1.200e-03,  2.700e-03,  2.600e-03,  1.100e-03, -1.100e-03, -2.600e-03, -2.700e-03, -1.200e-03],
        [ 4.000e-04,  1.100e-03,  1.000e-03,  4.000e-04, -4.000e-04, -1.000e-03, -1.100e-03, -4.000e-04],
        [ 2.000e-04,  4.000e-04,  4.000e-04,  2.000e-04, -2.000e-04, -4.000e-04, -4.000e-04, -2.000e-04],
        [ 0.000e+00,  1.000e-04,  1.000e-04,  0.000e+00, -0.000e+00, -1.000e-04, -1.000e-04, -0.000e+00]
    ])

    known = {
        'boundary': (x, y),
        'vert': (known_x, known_y),
        'psi': (known_x_psi, known_y_psi),
        'rho': (known_x_rho, known_y_rho),
        'u': (known_x_u, known_y_u),
        'v': (known_x_v, known_y_v),
        'ortho': known_ortho
    }
    return known


@pytest.fixture
def grid_with_proj(options):
    beta = [1.0, 1.0, 0.0, 0.0, 1.0, 1.0]
    shape = (10, 4)
    utm10 = pyproj.Proj(proj='utm', zone=10, ellps='WGS84')

    options.update({'ul_idx': 2, 'proj': utm10})
    x, y = known_xy_with_proj()['boundary']
    grid = pygridgen.Gridgen(x, y, beta, shape, **options)
    return grid


@pytest.fixture
def known_xy_with_proj():
    x = [-122.7, -122.5, -122.1, -121.7, -122.1, -122.3]
    y = [44.5, 45.0, 45.5, 45.5, 45.0, 44.5]

    known_x = numpy.array([
        [ 523849.33,  537634.03,  547839.75,  555648.45],
        [ 526581.75,  538098.95,  548230.37,  556959.19],
        [ 528706.88,  539280.4 ,  549285.71,  558586.48],
        [ 530680.14,  540779.61,  550703.53,  560332.94],
        [ 532573.13,  542376.34,  552276.84,  562147.52],
        [ 534399.75,  543920.09,  553868.86,  564017.21],
        [ 536134.21,  545225.84,  555367.56,  565953.24],
        [ 537693.4 ,  545930.59,  556686.9 ,  567971.74],
        [ 538892.32,  545175.68,  557971.63,  569945.95],
        [ 539407.65,  541507.67,  553438.74,  570933.77]
    ])

    known_y = numpy.array([
        [ 4927452.94,  4927537.26,  4927599.69,  4927647.45],
        [ 4937221.02,  4935113.05,  4933970.41,  4932423.55],
        [ 4944818.07,  4942360.57,  4940479.26,  4938353.08],
        [ 4951872.24,  4949330.44,  4947109.6 ,  4944716.87],
        [ 4958639.43,  4956134.07,  4953832.9 ,  4951328.87],
        [ 4965169.39,  4962831.75,  4960667.24,  4958141.67],
        [ 4971369.87,  4969442.43,  4967703.75,  4965196.22],
        [ 4976943.77,  4975952.38,  4975210.77,  4972551.26],
        [ 4981229.76,  4982185.84,  4984280.65,  4979744.91],
        [ 4983071.99,  4986864.71,  5008412.78,  4983344.35]
    ])

    known_x_psi = numpy.array([
        [ 538098.95,  548230.37],
        [ 539280.4 ,  549285.71],
        [ 540779.61,  550703.53],
        [ 542376.34,  552276.84],
        [ 543920.09,  553868.86],
        [ 545225.84,  555367.56],
        [ 545930.59,  556686.9 ],
        [ 545175.68,  557971.63]
    ])

    known_y_psi = numpy.array([
        [ 4935113.05,  4933970.41],
        [ 4942360.57,  4940479.26],
        [ 4949330.44,  4947109.6 ],
        [ 4956134.07,  4953832.9 ],
        [ 4962831.75,  4960667.24],
        [ 4969442.43,  4967703.75],
        [ 4975952.38,  4975210.77],
        [ 4982185.84,  4984280.65]
    ])

    known_x_rho = numpy.array([
        [ 531541.02,  542950.78,  552169.44],
        [ 533166.99,  543723.86,  553265.44],
        [ 534861.76,  545012.31,  554727.16],
        [ 536602.3 ,  546534.08,  556365.21],
        [ 538317.33,  548110.53,  558077.61],
        [ 539919.98,  549595.59,  559801.72],
        [ 541246.01,  550802.72,  561494.86],
        [ 541923.  ,  551441.2 ,  563144.06],
        [ 541245.83,  549523.43,  563072.52]
    ])

    known_y_rho = numpy.array([
        [ 4931831.07,  4931055.1 ,  4930410.27],
        [ 4939878.18,  4937980.82,  4936306.57],
        [ 4947095.33,  4944819.97,  4942664.7 ],
        [ 4953994.04,  4951601.75,  4949247.06],
        [ 4960693.66,  4958366.49,  4955992.67],
        [ 4967203.36,  4965161.29,  4962927.22],
        [ 4973427.11,  4972077.33,  4970165.5 ],
        [ 4979077.94,  4979407.41,  4977946.9 ],
        [ 4983338.07,  4990436.  ,  4988945.67]
    ])

    known_x_u = numpy.array([
        [ 537866.49,  548035.06],
        [ 538689.67,  548758.04],
        [ 540030.  ,  549994.62],
        [ 541577.97,  551490.18],
        [ 543148.21,  553072.85],
        [ 544572.97,  554618.21],
        [ 545578.22,  556027.23],
        [ 545553.13,  557329.27],
        [ 543341.67,  555705.19]
    ])

    known_x_v = numpy.array([
        [ 532340.35,  543164.66,  552594.78],
        [ 533993.64,  544283.05,  553936.1 ],
        [ 535729.88,  545741.57,  555518.23],
        [ 537474.73,  547326.59,  557212.18],
        [ 539159.92,  548894.47,  558943.03],
        [ 540680.03,  550296.7 ,  560660.4 ],
        [ 541812.  ,  551308.74,  562329.32],
        [ 542034.  ,  551573.65,  563958.79]
    ])

    known_y_u = numpy.array([
        [ 4931325.16,  4930785.05],
        [ 4938736.81,  4937224.83],
        [ 4945845.51,  4943794.43],
        [ 4952732.25,  4950471.25],
        [ 4959482.91,  4957250.07],
        [ 4966137.09,  4964185.49],
        [ 4972697.41,  4971457.26],
        [ 4979069.11,  4979745.71],
        [ 4984525.28,  4996346.71]
    ])

    known_y_v = numpy.array([
        [ 4936167.04,  4934541.73,  4933196.98],
        [ 4943589.32,  4941419.92,  4939416.17],
        [ 4950601.34,  4948220.02,  4945913.24],
        [ 4957386.75,  4954983.48,  4952580.89],
        [ 4964000.57,  4961749.5 ,  4959404.45],
        [ 4970406.15,  4968573.09,  4966449.98],
        [ 4976448.08,  4975581.57,  4973881.01],
        [ 4981707.8 ,  4983233.25,  4982012.78]
    ])

    known_ortho = numpy.array([
        [-7.960e-02, -8.200e-03, -7.990e-02],
        [-1.250e-02, -1.210e-02, -1.420e-02],
        [-4.900e-03, -8.300e-03, -5.100e-03],
        [-3.300e-03, -5.900e-03, -2.900e-03],
        [-4.200e-03, -6.400e-03, -2.200e-03],
        [-9.000e-03, -1.040e-02, -6.000e-04],
        [-2.600e-02, -2.160e-02,  1.110e-02],
        [-9.170e-02, -5.680e-02,  9.250e-02],
        [-4.120e-01, -1.884e-01,  6.207e-01]
    ])

    known = {
        'boundary': (x, y),
        'vert': (known_x, known_y),
        'psi': (known_x_psi, known_y_psi),
        'rho': (known_x_rho, known_y_rho),
        'u': (known_x_u, known_y_u),
        'v': (known_x_v, known_y_v),
        'ortho': known_ortho
    }
    return known


@pytest.fixture
def grid_with_changed_params(options):
    grid = grid_focused(options)
    grid.focus = None
    grid.ny = 10
    grid.nx = 5
    grid.generate_grid()
    return grid


GENERATORS = [
    grid_basic,
    grid_autogenFalse,
    grid_focused,
    grid_with_changed_params,
    grid_with_proj,
]

KNOWN_XYS = [
    known_xy_basic,
    known_xy_basic,
    known_xy_focused,
    known_xy_basic,
    known_xy_with_proj,
]

KNOWN_SHAPES = [
    (10, 5),
    (10, 5),
    (9, 9),
    (10, 5),
    (10, 4),
]


@pytest.mark.parametrize(('gg', 'known_shape'), zip(GENERATORS, KNOWN_SHAPES))
def test_shape(gg, known_shape, options):
    grid = gg(options)
    assert (grid.ny, grid.nx) == known_shape


@pytest.mark.parametrize('gg', GENERATORS)
def test_nnodes(gg, options):
    grid = gg(options)
    assert grid.nnodes == options['nnodes']


@pytest.mark.parametrize('gg', GENERATORS)
def test_precision(gg, options):
    grid = gg(options)
    assert grid.precision == options['precision']


@pytest.mark.parametrize('gg', GENERATORS)
def test_nppe(gg, options):
    grid = gg(options)
    assert grid.nppe == options['nppe']


@pytest.mark.parametrize('gg', GENERATORS)
def test_newton(gg, options):
    grid = gg(options)
    assert grid.newton == options['newton']


@pytest.mark.parametrize('gg', GENERATORS)
def test_thin(gg, options):
    grid = gg(options)
    assert grid.thin == options['thin']


@pytest.mark.parametrize('gg', GENERATORS)
def test_checksimplepoly(gg, options):
    grid = gg(options)
    assert grid.checksimplepoly == options['checksimplepoly']


@pytest.mark.parametrize('gg', GENERATORS)
def test_verbose(gg, options):
    grid = gg(options)
    assert grid.verbose == options['verbose']


@pytest.mark.parametrize(('gg', 'known'), zip(GENERATORS, KNOWN_XYS))
def test_xy(gg, known, options):
    grid = gg(options)
    known_xy = known()
    nptest.assert_array_almost_equal(
        grid.x,
        known_xy['vert'][0],
        decimal=2
    )

    nptest.assert_array_almost_equal(
        grid.y,
        known_xy['vert'][1],
        decimal=2
    )


@pytest.mark.parametrize(('gg', 'known'), zip(GENERATORS, KNOWN_XYS))
def test_xy_vert(gg, known, options):
    grid = gg(options)
    known_xy = known()
    nptest.assert_array_almost_equal(
        grid.x_vert,
        known_xy['vert'][0],
        decimal=2
    )

    nptest.assert_array_almost_equal(
        grid.y_vert,
        known_xy['vert'][1],
        decimal=2
    )


@pytest.mark.parametrize(('gg', 'known'), zip(GENERATORS, KNOWN_XYS))
def test_xy_psi(gg, known, options):
    grid = gg(options)
    known_xy = known()
    nptest.assert_array_almost_equal(
        grid.x_psi,
        known_xy['psi'][0],
        decimal=2
    )

    nptest.assert_array_almost_equal(
        grid.y_psi,
        known_xy['psi'][1],
        decimal=2
    )


@pytest.mark.parametrize(('gg', 'known'), zip(GENERATORS, KNOWN_XYS))
def test_xy_rho(gg, known, options):
    grid = gg(options)
    known_xy = known()
    nptest.assert_array_almost_equal(
        grid.x_rho,
        known_xy['rho'][0],
        decimal=2
    )

    nptest.assert_array_almost_equal(
        grid.y_rho,
        known_xy['rho'][1],
        decimal=2
    )


@pytest.mark.parametrize(('gg', 'known'), zip(GENERATORS, KNOWN_XYS))
def test_xy_u(gg, known, options):
    grid = gg(options)
    known_xy = known()
    nptest.assert_array_almost_equal(
        grid.x_u,
        known_xy['u'][0],
        decimal=2
    )

    nptest.assert_array_almost_equal(
        grid.y_u,
        known_xy['u'][1],
        decimal=2
    )


@pytest.mark.parametrize(('gg', 'known'), zip(GENERATORS, KNOWN_XYS))
def test_xy_v(gg, known, options):
    grid = gg(options)
    known_xy = known()
    nptest.assert_array_almost_equal(
        grid.x_v,
        known_xy['v'][0],
        decimal=2
    )

    nptest.assert_array_almost_equal(
        grid.y_v,
        known_xy['v'][1],
        decimal=2
    )


@pytest.mark.parametrize(('gg', 'known'), zip(GENERATORS, KNOWN_XYS))
def test_boundary(gg, known, options):
    grid = gg(options)
    known_xy = known()
    known_x, known_y = known_xy['boundary']
    if grid.proj is not None:
        known_x, known_y = grid.proj(known_x, known_y)

    nptest.assert_array_almost_equal(
        grid.xbry,
        known_x,
        decimal=2
    )

    nptest.assert_array_almost_equal(
        grid.ybry,
        known_y,
        decimal=2
    )


@pytest.mark.parametrize(('gg', 'known'), zip(GENERATORS, KNOWN_XYS))
def test_orthogonality (gg, known, options):
    grid = gg(options)
    known_xy = known()
    known_ortho = known_xy['ortho']
    nptest.assert_array_almost_equal(
        grid.orthogonality,
        known_ortho,
        decimal=2
    )


def test_mask_poylgon(grid_basic):
    island = numpy.array([(5, 10), (10, 10), (10, 5), (5, 5)]) / 10.
    known_mask_rho = numpy.array([
        [ 1.,  1.,  1.,  1.],
        [ 1.,  1.,  1.,  0.],
        [ 1.,  1.,  0.,  0.],
        [ 1.,  1.,  0.,  0.],
        [ 1.,  1.,  0.,  0.],
        [ 1.,  1.,  1.,  1.],
        [ 1.,  1.,  1.,  1.],
        [ 1.,  1.,  1.,  1.],
        [ 1.,  1.,  1.,  1.],
    ])
    grid_basic.mask_polygon(island)

    nptest.assert_array_almost_equal(
        known_mask_rho,
        grid_basic.mask_rho
    )
