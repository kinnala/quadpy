# -*- coding: utf-8 -*-
#
from __future__ import division

import numpy
import sympy

from .helpers import untangle2


class LynessJespersen(object):
    """
    J.N. Lyness, D. Jespersen,
    Moderate Degree Symmetric Quadrature Rules for the Triangle,
    J. Inst. Maths Applies (1975) 15, 19-32,
    doi: 10.1093/imamat/15.1.19,
    <https://doi.org/10.1093/imamat/15.1.19>.

    Abstract:
    A variant formulation of the moment fitting equations for the construction
    of D3 (triangularly symmetric) quadrature rules for the triangle is
    derived. These equations are solved to produce weights and abscissas for
    quadrature rules of polynomial degree up to 11 for the triangle, some of
    which require fewer function evaluations than any presently available rule
    of the same polynomial degree. Cytolic rules of degrees up to 9 are also
    derived.
    """

    def __init__(self, index, symbolic=False):
        frac = sympy.Rational if symbolic else lambda x, y: x / y
        sqrt = numpy.vectorize(sympy.sqrt) if symbolic else numpy.sqrt

        self.name = "LJ(%d)" % index
        if index == 1:
            self.degree = 2
            data = {"s2": [[frac(1, 3), frac(1, 2)]]}
        elif index == 2:
            self.degree = 2
            data = {"s3": [[frac(3, 4)]], "s2": [[frac(1, 12), 0]]}
        elif index == 3:
            self.degree = 3
            data = {"s3": [[-frac(9, 16)]], "s2": [[frac(25, 48), frac(1, 5)]]}
        elif index == 4:
            self.degree = 3
            data = {
                "s3": [[frac(9, 20)]],
                "s2": [[frac(1, 20), 0], [frac(2, 15), frac(1, 2)]],
            }
        elif index == 5:
            self.degree = 4
            data = {
                "s2": [
                    [3.298552309659655E-01 / 3, 9.157621350977073E-02],
                    [6.701447690340345E-01 / 3, 4.459484909159649E-01],
                ]
            }
        elif index == 6:
            self.degree = 4
            a0, a1 = [(3 + i * sqrt(3)) / 6 for i in [+1, -1]]
            data = {
                "s3": [[+frac(9, 20)]],
                "s2": [[-frac(1, 60), 0]],
                "s1": [[+frac(1, 10), a0, a1]],
            }
        elif index == 7:
            self.degree = 4
            sqrt13 = sqrt(13)
            data = {
                "s2": [
                    [(11 - sqrt13) / 360, 0],
                    [(10 - 2 * sqrt13) / 45, frac(1, 2)],
                    [(29 + 17 * sqrt13) / 360, (7 - sqrt13) / 18],
                ]
            }
        elif index == 8:
            self.degree = 5
            sqrt15 = sqrt(15)
            a1, a2 = [(155 - i * sqrt15) / 1200 for i in [+1, -1]]
            r1, r2 = [(6 - i * sqrt15) / 21 for i in [+1, -1]]
            data = {"s3": [[frac(9, 40)]], "s2": [[a1, r1], [a2, r2]]}
        elif index == 9:
            self.degree = 5
            data = {
                "s3": [[frac(81, 320)]],
                "s2": [
                    [frac(1, 90), 0],
                    [frac(16, 225), frac(1, 2)],
                    [frac(2401, 14400), frac(1, 7)],
                ],
            }
        elif index == 10:
            self.degree = 6
            data = {
                "s2": [
                    [3.503588271790222E-01 / 3, 2.492867451709329E-01],
                    [1.525347191106164E-01 / 3, 6.308901449150177E-02],
                ],
                "s1": [
                    [
                        4.971064537103375E-01 / 6,
                        6.365024991213939E-01,
                        5.314504984483216E-02,
                    ]
                ],
            }
        elif index == 11:
            self.degree = 6
            a, b = [(3 + i * sqrt(6)) / 6 for i in [+1, -1]]
            data = {
                "s3": [[-frac(81, 140)]],
                "s2": [
                    [-frac(5, 252), 0],
                    [frac(17, 315), frac(1, 2)],
                    [frac(128, 315), frac(1, 4)],
                ],
                "s1": [[frac(9, 210), a, b]],
            }
        elif index == 12:
            self.degree = 6
            data = {
                "s3": [[1.527089667883523E-01]],
                "s2": [
                    [2.944076042366762E-01 / 3, 4.738308139536513E-01],
                    [3.887052878418766E-01 / 3, 1.721176696308175E-01],
                ],
                "s1": [[1.641781411330949E-01 / 6, 0, 8.653073540834571E-01]],
            }
        elif index == 13:
            self.degree = 7
            data = {
                "s3": [[-1.495700444677495E-01]],
                "s2": [
                    [+5.268457722996328E-01 / 3, 2.603459660790466E-01],
                    [+1.600417068265167E-01 / 3, 6.513010290221623E-02],
                ],
                "s1": [
                    [
                        +4.626825653415500E-01 / 6,
                        6.384441885698096E-01,
                        4.869031542531756E-02,
                    ]
                ],
            }
        elif index == 14:
            self.degree = 7
            data = {
                "s3": [[1.763126156005252E-01]],
                "s2": [
                    [1.210901532763310E-02 / 3, 0],
                    [3.499561757697094E-01 / 3, 1.549360602237604E-01],
                    [3.195119754425220E-01 / 3, 4.691507461438120E-01],
                ],
                "s1": [[1.421102178595603E-01 / 6, 0, 8.392991722729236E-01]],
            }
        elif index == 15:
            self.degree = 8
            data = {
                "s3": [[1.443156076777862E-01]],
                "s2": [
                    [2.852749028018549E-01 / 3, 4.592925882927229E-01],
                    [9.737549286959440E-02 / 3, 5.054722831703103E-02],
                    [3.096521116041552E-01 / 3, 1.705693077517601E-01],
                ],
                "s1": [
                    [
                        1.633818850466092E-01 / 6,
                        8.394777409957211E-03,
                        7.284923929554041E-01,
                    ]
                ],
            }
        elif index == 16:
            self.degree = 8
            data = {
                "s2": [
                    [+1.207273935292775E-02 / 3, 0],
                    [-8.491579879151455E-01 / 3, frac(1, 2)],
                    [+1.042367468891334E+00 / 3, 4.956813941755582E-01],
                    [+1.947229791412260E-01 / 3, 9.032775751426533E-02],
                    [+4.511852767201322E-01 / 3, 2.341547497073052E-01],
                ],
                "s1": [[+1.488095238055238E-01 / 6, 0, 7.236067977499750E-01]],
            }
        elif index == 17:
            self.degree = 8
            data = {
                "s3": [[-2.834183851113958E-01]],
                "s2": [
                    [2.097208857979572E-01 / 3, 4.766654393821525E-01],
                    [5.127273801480265E-02 / 3, 3.377184405448033E-02],
                    [6.564896469913508E-01 / 3, 2.703478891654040E-01],
                ],
                "s1": [
                    [
                        3.659351143072855E-01 / 6,
                        5.146433548666149E-02,
                        7.458294907672514E-01,
                    ]
                ],
            }
        elif index == 18:
            self.degree = 9
            data = {
                "s3": [[9.713579628279610E-02]],
                "s2": [
                    [9.400410068141950E-02 / 3, 4.896825191987370E-01],
                    [2.334826230143263E-01 / 3, 4.370895914929355E-01],
                    [2.389432167816271E-01 / 3, 1.882035356190322E-01],
                    [7.673302697609430E-02 / 3, 4.472951339445297E-02],
                ],
                "s1": [
                    [
                        2.597012362637364E-01 / 6,
                        3.683841205473626E-02,
                        7.411985987844980E-01,
                    ]
                ],
            }
        elif index == 19:
            self.degree = 9
            data = {
                "s3": [[1.133624844599192E-01]],
                "s2": [
                    [1.062573789846330E-03 / 3, 0],
                    [4.803411513859279E-02 / 3, frac(1, 2)],
                    [2.524243006337300E-01 / 3, 4.497793381870162E-01],
                    [7.819254371487040E-02 / 3, 4.694744319909033E-02],
                    [2.472227459993048E-01 / 3, 1.918719127374489E-01],
                ],
                "s1": [
                    [
                        2.597012362637364E-01 / 6,
                        3.683841205473626E-02,
                        7.411985987844980E-01,
                    ]
                ],
            }
        elif index == 20:
            self.degree = 11
            data = {
                "s2": [
                    [4.097919300803106E-02 / 3, 3.236494811127173E-02],
                    [1.085536215102866E-01 / 3, 1.193509122825931E-01],
                    [2.781018986881812E-03 / 3, 5.346110482707572E-01],
                    [1.779689321422668E-01 / 3, 2.033099004312816E-01],
                    [2.314486047444677E-01 / 3, 3.989693029658558E-01],
                ],
                "s1": [
                    [
                        3.140226717732234E-01 / 6,
                        5.017813831049474E-02,
                        5.932012134282132E-01,
                    ],
                    [
                        1.242459578348437E-01 / 6,
                        2.102201653616613E-02,
                        8.074890031597923E-01,
                    ],
                ],
            }
        else:
            assert index == 21
            self.degree = 11
            data = {
                "s3": [[8.797730116222190E-02]],
                "s2": [
                    [2.623293466120857E-02 / 3, 2.598914092828833E-02],
                    [1.142447159818060E-01 / 3, 9.428750264792270E-02],
                    [5.656634416839376E-02 / 3, 4.946367750172147E-01],
                    [2.164790926342230E-01 / 3, 2.073433826145142E-01],
                    [2.079874161166116E-01 / 3, 4.389078057004907E-01],
                ],
                "s1": [
                    [4.417430269980344E-02 / 6, 0, 8.588702812826364E-01],
                    [
                        2.463378925757316E-01 / 6,
                        4.484167758913055E-02,
                        6.779376548825902E-01,
                    ],
                ],
            }

        self.bary, self.weights = untangle2(data)
        self.points = self.bary[:, 1:]
        return
