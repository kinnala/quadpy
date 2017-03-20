# -*- coding: utf-8 -*-
#
from helpers import \
        create_monomial_exponents2, \
        integrate_monomial_over_unit_circle, \
        check_degree

import pytest
import quadpy


def _integrate_exact(k):
    '''We have

    I = \int_0^1 \int_0^2pi r * (r cos(phi))**k[0] (r sin(phi))**k[1]
      = 1.0/(2+k[0]+k[1]) * \int_0^2pi cos(phi)**k[0] sin(phi)**k[1]
    '''
    return 1.0/(2 + k[0] + k[1]) * integrate_monomial_over_unit_circle(k)


@pytest.mark.parametrize(
    'scheme',
    [quadpy.disk.Peirce(k) for k in range(1, 6)]
    + [quadpy.disk.Lether(k) for k in range(1, 6)]
    )
def test_scheme(scheme):
    degree = check_degree(
            lambda poly: quadpy.disk.integrate(
                poly, [0.0, 0.0], 1.0, scheme
                ),
            _integrate_exact,
            create_monomial_exponents2,
            scheme.degree + 1
            )
    assert degree == scheme.degree
    return


@pytest.mark.parametrize(
    'scheme',
    [quadpy.disk.Lether(3)]
    )
def test_show(scheme):
    quadpy.disk.show(scheme)
    return


if __name__ == '__main__':
    scheme = quadpy.disk.Lether(5)
    test_scheme(scheme)
    # test_show(scheme)
