import numpy as np


def generate_curve(theta, M, X, num_points=1500):
    """
    Generate the parametric curve using uniformly sampled t.
    """

    theta = np.radians(theta)

    t = np.linspace(6, 60, num_points)

    x = (
        t * np.cos(theta)
        - np.exp(M * np.abs(t))
        * np.sin(0.3 * t)
        * np.sin(theta)
        + X
    )

    y = (
        42
        + t * np.sin(theta)
        + np.exp(M * np.abs(t))
        * np.sin(0.3 * t)
        * np.cos(theta)
    )

    return x, y