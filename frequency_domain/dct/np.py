import numpy as np


def idct_1d_transform(p=8):
    """
    origin = np.einsum("xu, u -> x", transform, coeff)
    :param p: length of coeff
    :return: idct1d transform
    """
    fp = lambda i: np.sqrt(i / 8.)
    alpha = np.array([fp(1.), *fp(2. * np.ones(p - 1))]).reshape((1, p))
    x = np.array(np.linspace(1, p, p, dtype=float)).reshape((p, 1))
    u = np.array(np.linspace(1, p, p, dtype=float)).reshape((1, p))
    transform = alpha * np.cos(np.pi * (2. * x - 1.) * (u - 1.) / (2. * p))

    return transform


def idct_2d_transform(q=8, p=8):
    """
    origin = np.einsum("yxvu, vu -> yx", transform, coeff)
    :param q: q->coeff[q, p]
    :param p: p->coeff[q, p]
    :return: idct2d transform
    """
    fq = lambda i: np.sqrt(i / q)
    fp = lambda i: np.sqrt(i / p)
    beta = np.array([fq(1.), *fq(2. * np.ones(q - 1))]).reshape((1, 1, q, 1))
    alpha = np.array([fp(1.), *fp(2. * np.ones(p - 1))]).reshape((1, 1, 1, p))
    y = np.array(np.linspace(1, q, q, dtype=float)).reshape((q, 1, 1, 1))
    x = np.array(np.linspace(1, p, p, dtype=float)).reshape((1, p, 1, 1))
    v = np.array(np.linspace(1, q, q, dtype=float)).reshape((1, 1, q, 1))
    u = np.array(np.linspace(1, p, p, dtype=float)).reshape((1, 1, 1, p))
    transform = alpha * np.cos(np.pi * (2. * x - 1.) * (u - 1.) / (2. * p)) * \
                beta * np.cos(np.pi * (2. * y - 1.) * (v - 1.) / (2. * q))

    return transform
