import numpy as np
from scipy.spatial import cKDTree

from model import generate_curve


def objective(params, actual_points):
    """
    Objective function using nearest-neighbor matching.

    params = [theta, M, X]
    """

    theta, M, X = params

    # Reject invalid parameters
    if not (0 <= theta <= 50):
        return 1e12

    if not (-0.05 <= M <= 0.05):
        return 1e12

    if not (0 <= X <= 100):
        return 1e12

    # Generate predicted curve
    pred_x, pred_y = generate_curve(theta, M, X)

    predicted_points = np.column_stack((pred_x, pred_y))

    # Build KD-Tree for fast nearest-neighbor search
    tree = cKDTree(actual_points)

    # Distance from every predicted point
    distances, _ = tree.query(predicted_points)

    # L1 distance
    error = np.sum(np.abs(distances))

    return error