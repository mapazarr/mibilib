"""Constants used in mibidata module.

Copyright (C) 2020 Ionpath, Inc.  All rights reserved."""

COLORS = {
    'Cyan': (0.0, 1.0, 1.0),
    'Yellow': (1.0, 1.0, 0.0),
    'Magenta': (1.0, 0.0, 1.0),
    'Green': (0.0, 1.0, 0.0),
    'Orange': (1.0, 0.6470588235294118, 0.0),
    'Violet': (0.6980392156862745, 0.5058823529411764, 0.9333333333333333),
    'Red': (1.0, 0.0, 0.0),
    'Blue': (0.0, 0.0, 1.0),
    'Gray': (1.0, 1.0, 1.0),
}

OVERLAY_MIN_BRIGHTNESS = -0.9

# The kernels below are those used by WegGL convolution in MIBItracker.
# pylint: disable=line-too-long
OVERLAY_SMOOTHING_KERNELS = [
    # A blur of 0 still gets a convolution to mimic browser rendering.
    [
        [0.05, 0.1, 0.05],
        [0.1, 0.4, 0.1],
        [0.05, 0.1, 0.05]
    ],
    [
        [0.001631, 0.03713, 0.001631],
        [0.03713, 0.845, 0.03713],
        [0.001631, 0.03713, 0.001631],
    ],
    [
        [0.01134, 0.08382, 0.01134],
        [0.08382, 0.6193, 0.08382],
        [0.01134, 0.08382, 0.01134],
    ],
    [
        [0.02768, 0.111, 0.02768],
        [0.111, 0.4452, 0.111],
        [0.02768, 0.111, 0.02768],
    ],
    [
        [9.255e-05, 0.001976, 0.005483, 0.001976, 9.255e-05],
        [0.001976, 0.0422, 0.1171, 0.0422, 0.001976],
        [0.005483, 0.1171, 0.3248, 0.1171, 0.005483],
        [0.001976, 0.0422, 0.1171, 0.0422, 0.001976],
        [9.255e-05, 0.001976, 0.005483, 0.001976, 9.255e-05],
    ],
    [
        [0.0008714, 0.006948, 0.01388, 0.006948, 0.0008714],
        [0.006948, 0.0554, 0.1107, 0.0554, 0.006948],
        [0.01388, 0.1107, 0.2211, 0.1107, 0.01388],
        [0.006948, 0.0554, 0.1107, 0.0554, 0.006948],
        [0.0008714, 0.006948, 0.01388, 0.006948, 0.0008714],
    ],
    [
        [0.002969, 0.01331, 0.02194, 0.01331, 0.002969],
        [0.01331, 0.05963, 0.09832, 0.05963, 0.01331],
        [0.02194, 0.09832, 0.1621, 0.09832, 0.02194],
        [0.01331, 0.05963, 0.09832, 0.05963, 0.01331],
        [0.002969, 0.01331, 0.02194, 0.01331, 0.002969],
    ],
    [
        [0.0002145, 0.001217, 0.00345, 0.004882, 0.00345, 0.001217, 0.0002145],
        [0.001217, 0.006909, 0.01958, 0.02771, 0.01958, 0.006909, 0.001217],
        [0.00345, 0.01958, 0.05549, 0.07852, 0.05549, 0.01958, 0.00345],
        [0.004882, 0.02771, 0.07852, 0.1111, 0.07852, 0.02771, 0.004882],
        [0.00345, 0.01958, 0.05549, 0.07852, 0.05549, 0.01958, 0.00345],
        [0.001217, 0.006909, 0.01958, 0.02771, 0.01958, 0.006909, 0.001217],
        [0.0002145, 0.001217, 0.00345, 0.004882, 0.00345, 0.001217, 0.0002145],
    ],
    [
        [0.001342, 0.004077, 0.00794, 0.009916, 0.00794, 0.004077, 0.001342],
        [0.004077, 0.01238, 0.02412, 0.03012, 0.02412, 0.01238, 0.004077],
        [0.00794, 0.02412, 0.04698, 0.05867, 0.04698, 0.02412, 0.00794],
        [0.009916, 0.03012, 0.05867, 0.07327, 0.05867, 0.03012, 0.009916],
        [0.00794, 0.02412, 0.04698, 0.05867, 0.04698, 0.02412, 0.00794],
        [0.004077, 0.01238, 0.02412, 0.03012, 0.02412, 0.01238, 0.004077],
        [0.001342, 0.004077, 0.00794, 0.009916, 0.00794, 0.004077, 0.001342],
    ],
    [
        [0.0007634, 0.001831, 0.003422, 0.004978, 0.005641, 0.004978, 0.003422, 0.001831, 0.0007634],
        [0.001831, 0.004393, 0.008208, 0.01194, 0.01353, 0.01194, 0.008208, 0.004393, 0.001831],
        [0.003422, 0.008208, 0.01533, 0.02231, 0.02528, 0.02231, 0.01533, 0.008208, 0.003422],
        [0.004978, 0.01194, 0.02231, 0.03246, 0.03678, 0.03246, 0.02231, 0.01194, 0.004978],
        [0.005641, 0.01353, 0.02528, 0.03678, 0.04168, 0.03678, 0.02528, 0.01353, 0.005641],
        [0.004978, 0.01194, 0.02231, 0.03246, 0.03678, 0.03246, 0.02231, 0.01194, 0.004978],
        [0.003422, 0.008208, 0.01533, 0.02231, 0.02528, 0.02231, 0.01533, 0.008208, 0.003422],
        [0.001831, 0.004393, 0.008208, 0.01194, 0.01353, 0.01194, 0.008208, 0.004393, 0.001831],
        [0.0007634, 0.001831, 0.003422, 0.004978, 0.005641, 0.004978, 0.003422, 0.001831, 0.0007634],
    ],
    [
        [0.002276, 0.003984, 0.005944, 0.007556, 0.008186, 0.007556, 0.005944, 0.003984, 0.002276],
        [0.003984, 0.006975, 0.01041, 0.01323, 0.01433, 0.01323, 0.01041, 0.006975, 0.003984],
        [0.005944, 0.01041, 0.01552, 0.01973, 0.02138, 0.01973, 0.01552, 0.01041, 0.005944],
        [0.007556, 0.01323, 0.01973, 0.02509, 0.02718, 0.02509, 0.01973, 0.01323, 0.007556],
        [0.008186, 0.01433, 0.02138, 0.02718, 0.02944, 0.02718, 0.02138, 0.01433, 0.008186],
        [0.007556, 0.01323, 0.01973, 0.02509, 0.02718, 0.02509, 0.01973, 0.01323, 0.007556],
        [0.005944, 0.01041, 0.01552, 0.01973, 0.02138, 0.01973, 0.01552, 0.01041, 0.005944],
        [0.003984, 0.006975, 0.01041, 0.01323, 0.01433, 0.01323, 0.01041, 0.006975, 0.003984],
        [0.002276, 0.003984, 0.005944, 0.007556, 0.008186, 0.007556, 0.005944, 0.003984, 0.002276],
    ],
]
