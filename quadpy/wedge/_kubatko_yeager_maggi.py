from sympy import Rational as frac
from sympy import sqrt

from ..helpers import article, untangle
from ._helpers import WedgeScheme

citation = article(
    authors=["Ethan J. Kubatko", "Benjamin A. Yeager", "Ashley L. Maggi"],
    title="New computationally efficient quadrature formulas for triangular prism elements",
    journal="Computers & Fluids",
    volume="73",
    year="2013",
    pages="187–201",
    url="https://doi.org/10.1016/j.compfluid.2013.01.002",
)


def kubatko_yeager_maggi_1():
    data = [(4, [[-frac(1, 3), -frac(1, 3), 0]])]
    points, weights = untangle(data)
    # quadpy's reference wedge is 0 <= X, 0 <= Y, X + Y <= 1, -1 <= Z <= 1.
    weights = weights / 4
    points[:, :2] += 1
    points[:, :2] /= 2
    return WedgeScheme("Kubatko-Yeager-Maggi 1", weights, points, 1, citation)


def kubatko_yeager_maggi_2a():
    data = [
        (1, [[0.483163247594393, -0.741581623797196, 0]]),
        (1, [[-0.605498860309242, 0.469416096821288, 0]]),
        (1, _zeta_pm(-0.605498860309242, -0.530583903178712, 0.816496580927726)),
    ]
    points, weights = untangle(data)
    weights = weights / 4
    points[:, :2] += 1
    points[:, :2] /= 2
    return WedgeScheme("Kubatko-Yeager-Maggi 2a", weights, points, 2, citation)


def kubatko_yeager_maggi_2b():
    data = [(frac(1, 3), _s21(-1)), (frac(3, 2), _s3_z(frac(2, 3)))]
    points, weights = untangle(data)
    weights = weights / 4
    points[:, :2] += 1
    points[:, :2] /= 2
    return WedgeScheme("Kubatko-Yeager-Maggi 2b", weights, points, 2, citation)


def kubatko_yeager_maggi_3a():
    data = [
        (
            0.742534890852309,
            [[0.240692796349625, -0.771991660873412, 0.614747128207527]],
        ),
        (
            0.375143463443327,
            [[-0.968326281451138, -0.568046512457875, 0.676689529541421]],
        ),
        (
            0.495419047908462,
            [[0.467917833640195, -0.549342790168347, -0.599905857322635]],
        ),
        (
            0.523999970843238,
            [[-0.786144119530819, 0.362655041695561, -0.677609795694786]],
        ),
        (
            0.980905839025611,
            [[-0.484844897886675, -0.707931130717342, -0.502482717716373]],
        ),
        (
            0.881996787927053,
            [[-0.559053711932125, 0.260243325246813, 0.493010512161538]],
        ),
    ]
    points, weights = untangle(data)
    weights = weights / 4
    points[:, :2] += 1
    points[:, :2] /= 2
    return WedgeScheme("Kubatko-Yeager-Maggi 3a", weights, points, 3, citation)


def kubatko_yeager_maggi_3b():
    data = [
        (-frac(43, 12), _s3(symbolic=True)),
        (frac(25, 12), _s21(-frac(3, 5))),
        (frac(2, 3), _s3_z(1)),
    ]
    points, weights = untangle(data)
    weights = weights / 4
    points[:, :2] += 1
    points[:, :2] /= 2
    return WedgeScheme("Kubatko-Yeager-Maggi 3b", weights, points, 3, citation)


def kubatko_yeager_maggi_3c():
    alpha = 4 * sqrt(3) / 15
    data = [
        (-frac(9, 4), _s3(symbolic=True)),
        (frac(25, 24), _s21_z(-frac(3, 5), alpha)),
    ]
    points, weights = untangle(data)
    weights = weights / 4
    points[:, :2] += 1
    points[:, :2] /= 2
    return WedgeScheme("Kubatko-Yeager-Maggi 3c", weights, points, 3, citation)


def kubatko_yeager_maggi_3d():
    data = [
        (frac(4, 9), _s30(-0.525248027124695, -0.924672547414225, 0.449920574538920)),
        (frac(2, 3), _s3_z(1)),
    ]
    points, weights = untangle(data)
    weights = weights / 4
    points[:, :2] += 1
    points[:, :2] /= 2
    return WedgeScheme("Kubatko-Yeager-Maggi 3d", weights, points, 3, citation)


def kubatko_yeager_maggi_4a():
    data = [
        (
            0.111155943811228,
            [[0.812075900047562, -0.986242751499303, 0.850716248413834]],
        ),
        (
            0.309060899887509,
            [[-0.792166223585545, 0.687201105597868, -0.115214772515700]],
        ),
        (
            0.516646862442958,
            [[-0.756726179789306, -0.731311840596107, -0.451491675441927]],
        ),
        (
            0.567975205132714,
            [[-0.552495167978340, 0.015073398439985, -0.824457000064439]],
        ),
        (
            0.382742555939017,
            [[-0.357230019521233, 0.126888850505978, 0.855349689995606]],
        ),
        (
            0.355960928492268,
            [[-0.987225392999058, 0.082647545710800, 0.452976444667786]],
        ),
        (
            0.108183228294342,
            [[-0.816603728785918, -0.915066171481315, 0.997939285245240]],
        ),
        (
            0.126355242780924,
            [[0.423489172633859, -1.112801167237130, -0.963298774205756]],
        ),
        (
            0.587370828592853,
            [[0.363041084609230, -0.499011410082669, -0.299892769705443]],
        ),
        (
            0.934548304626188,
            [[-0.175780343149613, -0.654971142379686, 0.367947041936472]],
        ),
    ]
    points, weights = untangle(data)
    weights = weights / 4
    points[:, :2] += 1
    points[:, :2] /= 2
    return WedgeScheme("Kubatko-Yeager-Maggi 4a", weights, points, 4, citation)


def kubatko_yeager_maggi_4b():
    data = [
        (0.545658450421913, _s21(-0.062688380276010)),
        (0.431647899262139, _s3_z(0.866861974009030)),
        (0.249954808368331, _s21_z(-0.798519188402179, 0.675639823682265)),
    ]
    points, weights = untangle(data)
    weights = weights / 4
    points[:, :2] += 1
    points[:, :2] /= 2
    return WedgeScheme("Kubatko-Yeager-Maggi 4b", weights, points, 4, citation)


def kubatko_yeager_maggi_5a():
    data = [
        (
            0.087576186678730,
            [[-0.955901336867574, -0.955901336867577, 0.000000000000286]],
        ),
        (
            0.229447629454892,
            _abz(-0.051621305926029, -1.017063354038640, 0.000000000000038),
        ),
        (
            0.833056798542985,
            [[-0.297388746460523, -0.297388746460521, 0.000000000000008]],
        ),
        (
            0.166443428304729,
            _abz(0.774849157169622, -0.849021640062096, 0.000000000000080),
        ),
        (0.376993270712316, _az(-0.665292008657551, 0.756615409654429)),
        (0.170410864470884, _az(-0.012171148087349, 0.600149379161583)),
        (
            0.298194157223163,
            _abz_pm(-0.734122164680096, 0.334122164680066, 0.808115770496521),
        ),
    ]
    points, weights = untangle(data)
    weights = weights / 4
    points[:, :2] += 1
    points[:, :2] /= 2
    return WedgeScheme("Kubatko-Yeager-Maggi 5a", weights, points, 5, citation)


def kubatko_yeager_maggi_5b():
    data = [
        (
            0.213895020288765,
            [[-0.820754415297359, 0.701020947925133, -0.300763696502910]],
        ),
        (
            0.141917375616806,
            [[0.611831616907812, -0.869995576950389, 0.348546607420888]],
        ),
        (
            0.295568859378071,
            [[-0.951379065092975, -0.087091980055873, 0.150656042323906]],
        ),
        (
            0.256991945593379,
            [[0.200535109198601, -0.783721735474016, -0.844285153176719]],
        ),
        (
            0.122121979248381,
            [[-0.909622841605196, -0.890218158063352, 0.477120081549168]],
        ),
        (
            0.175194917962627,
            [[0.411514133287729, -0.725374126531787, 0.864653509536562]],
        ),
        (
            0.284969106392719,
            [[-0.127534496411879, -0.953467283619037, 0.216019762875977]],
        ),
        (
            0.323336131783334,
            [[-0.555217727817199, -0.530472194607007, 0.873409672725819]],
        ),
        (
            0.159056110329063,
            [[0.706942532529193, -0.782248553944540, -0.390653804976705]],
        ),
        (
            0.748067388709644,
            [[-0.278092963133809, -0.291936530517119, -0.126030507204870]],
        ),
        (
            0.280551223607231,
            [[-0.057824844208300, -0.056757587543798, 0.539907869785112]],
        ),
        (
            0.147734016552639,
            [[-0.043308436222116, 0.012890722780611, -0.776314479909204]],
        ),
        (
            0.259874920383688,
            [[-0.774478920734726, 0.476188541042454, 0.745875967497062]],
        ),
        (
            0.235144061421191,
            [[-0.765638443571458, 0.177195164202219, -0.888355356215127]],
        ),
        (
            0.355576942732463,
            [[-0.732830649614460, -0.737447982744191, -0.651653242952189]],
        ),
    ]
    points, weights = untangle(data)
    weights = weights / 4
    points[:, :2] += 1
    points[:, :2] /= 2
    return WedgeScheme("Kubatko-Yeager-Maggi 5b", weights, points, 5, citation)


def kubatko_yeager_maggi_5c():
    data = [
        (0.711455555931488, _s3(symbolic=False)),
        (0.224710067228267, _s21(-0.025400070899509)),
        (0.185661421316158, _s21_z(-0.108803790659256, 0.871002934865444)),
        (0.250074285747794, _s21_z(-0.798282108034583, 0.570426980705159)),
    ]
    points, weights = untangle(data)
    weights = weights / 4
    points[:, :2] += 1
    points[:, :2] /= 2
    return WedgeScheme("Kubatko-Yeager-Maggi 5c", weights, points, 5, citation)


def kubatko_yeager_maggi_6a():
    data = [
        (
            0.168480079940386,
            _s30(0.513019949700545, -0.930094391938207, -0.582925557762337),
        ),
        (0.000079282874851, _s21(-1.830988812620400)),
        (0.544286440652304, _s3(symbolic=False)),
        (0.026293733850586, _s3_z(1.250521622121900)),
        (0.283472344926041, _s21_z(-0.098283514203544, 0.685008566774710)),
        (0.115195615637235, _s21_z(-0.812603471654584, 0.809574716992997)),
    ]
    points, weights = untangle(data)
    weights = weights / 4
    points[:, :2] += 1
    points[:, :2] /= 2
    return WedgeScheme("Kubatko-Yeager-Maggi 6a", weights, points, 6, citation)


def kubatko_yeager_maggi_6b():
    data = [
        (-0.515987215963885, _s3(symbolic=False)),
        (0.113384887025471, _s21(-0.891966687066689)),
        (0.489402517688430, _s21(-0.489005016481638)),
        (0.205362200002623, _s3_z(0.932807703184800)),
        (0.048821553028563, _s21_z(-0.838683160291348, -0.946297575072789)),
        (
            0.166997606970463,
            _s111_z(-0.892665383041055, -0.380071023770412, 0.596750920257972),
        ),
    ]
    points, weights = untangle(data)
    weights = weights / 4
    points[:, :2] += 1
    points[:, :2] /= 2
    return WedgeScheme("Kubatko-Yeager-Maggi 6b", weights, points, 6, citation)


def kubatko_yeager_maggi_6c():
    data = [
        (0.108764249640922, _s21(-0.895512822481133)),
        (
            0.162544166564880,
            _s30(-0.603390269052889, -0.458729487713671, +0.062119756766560),
        ),
        (0.201100563750029, _s3_z(0.936241512371697)),
        (0.047097659849389, _s21_z(-0.841699897299232, 0.948681147283254)),
        (
            0.167804597090964,
            _s111_z(-0.890337410253393, -0.382973596286234, 0.600638052820557),
        ),
    ]
    points, weights = untangle(data)
    weights = weights / 4
    points[:, :2] += 1
    points[:, :2] /= 2
    return WedgeScheme("Kubatko-Yeager-Maggi 6c", weights, points, 6, citation)


def kubatko_yeager_maggi_7a():
    data = [
        (0.101999439969640, _s21(-0.052693741802220)),
        (
            0.013773382049005,
            _s30(-1.203867696672760, -0.769101467805088, +0.972969164477851),
        ),
        (
            0.183161577533988,
            _s30(-0.806342417251714, -0.550525003554855, +0.356867420806569),
        ),
        (0.018944865817845, _s3_z(1.291674052437540)),
        (0.376139984367254, _s3_z(0.561030375657598)),
        (0.147104614209618, _s21_z(-0.059715871789826, 0.774596669241324)),
        (0.139932422827537, _s21_z(-0.797426985353099, 0.774596669241551)),
    ]
    points, weights = untangle(data)
    weights = weights / 4
    points[:, :2] += 1
    points[:, :2] /= 2
    return WedgeScheme("Kubatko-Yeager-Maggi 7a", weights, points, 7, citation)


def kubatko_yeager_maggi_7b():
    data = [
        (-0.879316328492506, _s21(-0.799390499533395)),
        (+0.372687220323677, _s21(-0.611312866165672)),
        (
            +0.323126141949260,
            _s30(-0.876344144151775, -0.612951719548152, +0.489295863699928),
        ),
        (+0.289007666422544, _s3_z(0.734616109970751)),
        (+0.153278562247698, _s21_z(-0.052044650909702, 0.726801565090391)),
        (+0.065992821952079, _s21_z(-0.756988294814865, 0.976659162929848)),
        (+0.281247805794530, _s21_z(-0.848580765301238, 0.305898494016659)),
    ]
    points, weights = untangle(data)
    weights = weights / 4
    points[:, :2] += 1
    points[:, :2] /= 2
    return WedgeScheme("Kubatko-Yeager-Maggi 7b", weights, points, 7, citation)


def kubatko_yeager_maggi_7c():
    data = [
        (0.187125249811092, _s3(symbolic=False)),
        (0.279712056646351, _s21(-0.622563924496121)),
        #
        (0.192663794476979, _s21_z(-0.150946831636914, 0.739705153646415)),
        (0.077939984185063, _s21_z(-0.888439097303094, 0.521191884792341)),
        (
            0.037328649790157,
            _s111_z(-0.879193936849505, -0.569600904418278, 0.967847765724758),
        ),
        (
            0.075181009232977,
            _s111_z(-0.956495962100542, -0.348089160012426, 0.413411329372023),
        ),
    ]
    points, weights = untangle(data)
    weights = weights / 4
    points[:, :2] += 1
    points[:, :2] /= 2
    return WedgeScheme("Kubatko-Yeager-Maggi 7c", weights, points, 7, citation)


def kubatko_yeager_maggi_8a():
    data = [
        (-0.628896123664332, _s3(symbolic=False)),
        (-0.000009664501734, _s21(+0.732570431730499)),
        (+0.290043889959886, _s21(-0.111280133398729)),
        (+0.164125220310641, _s21(-0.744234499888195)),
        #
        (+0.500978176529324, _s3_z(0.324632164542059)),
        (+0.137896989572043, _s21_z(-0.655304484833396, 0.697231953348274)),
        (+0.093150738786246, _s21_z(-0.111390690423267, 0.918085752971442)),
        (+0.026296598245927, _s21_z(-0.860501622328014, 0.955100930524729)),
        (+0.031254499752794, _s21_z(-0.929092752683144, 0.418740152771249)),
        (
            +0.044405706263133,
            _s111_z(-1.027258305900750, -0.401321966766924, 0.577350264603552),
        ),
    ]
    points, weights = untangle(data)
    weights = weights / 4
    points[:, :2] += 1
    points[:, :2] /= 2
    return WedgeScheme("Kubatko-Yeager-Maggi 8a", weights, points, 8, citation)


def kubatko_yeager_maggi_8b():
    data = [
        (0.064622878644877, _s3(symbolic=False)),
        (0.212815083510681, _s21(-0.080724796383744)),
        #
        (0.222859308690085, _s3_z(0.656906854028118)),
        (0.033167391229558, _s3_z(0.222890421390518)),
        (0.083683503199655, _s21_z(-0.082177195702334, 0.875089829009932)),
        (0.160178684391513, _s21_z(-0.655731448496969, 0.398915780473391)),
        (0.035678259898902, _s21_z(-0.896358906478658, 0.076044280208993)),
        (0.029230569799017, _s21_z(-0.901888148396643, 0.838134530826001)),
        (0.046399681341109, _s21_z(-0.668873936739861, 0.962422967861277)),
        (
            0.054487856600218,
            _s111_z(-0.983128918652189, -0.473900476311823, 0.577350269192965),
        ),
    ]
    points, weights = untangle(data)
    weights = weights / 4
    points[:, :2] += 1
    points[:, :2] /= 2
    return WedgeScheme("Kubatko-Yeager-Maggi 8b", weights, points, 8, citation)


def kubatko_yeager_maggi_9():
    data = [
        (0.179697999934032, _s21(-0.670211122327313)),
        (
            0.029779770020782,
            _s30(-0.987687012620047, -0.639473873495245, +0.627160886115292),
        ),
        (0.093251945517294, _s3_z(0.130565599977556)),
        (0.079389858812471, _s21_z(-0.532290571296145, 0.896174462570776)),
        (0.144411166376722, _s21_z(-0.153771400189340, 0.496886101956702)),
        (0.030059746399875, _s21_z(-0.924116817433563, 0.441720100571867)),
        (0.021462670335182, _s21_z(-0.874138544455932, 0.938724295918725)),
        (
            0.020254759898769,
            _s111_z(-0.935121167364029, -0.255783274127814, 0.932336314743883),
        ),
        (
            0.030927308427916,
            _s111_z(-0.939611270417581, -0.094705427266644, 0.251407318247268),
        ),
        (
            0.069133168131076,
            _s111_z(-0.898020111840079, -0.539691298441295, 0.649773968745693),
        ),
    ]
    points, weights = untangle(data)
    weights = weights / 4
    points[:, :2] += 1
    points[:, :2] /= 2
    return WedgeScheme("Kubatko-Yeager-Maggi 9", weights, points, 9, citation)


def _zeta_pm(xi, eta, zeta):
    return [[xi, eta, +zeta], [xi, eta, -zeta]]


def _abz(a, b, z):
    return [[a, b, z], [b, a, z]]


def _abz_pm(a, b, z):
    return [[a, b, z], [a, b, -z], [b, a, z], [b, a, -z]]


def _az(a, z):
    return [[a, a, +z], [a, a, -z]]


def _s3(symbolic):
    fra = frac if symbolic else lambda x, y: x / y
    return [[-fra(1, 3), -fra(1, 3), 0]]


def _s3_z(z):
    symbolic = not isinstance(z, float)
    fra = frac if symbolic else lambda x, y: x / y
    return [[-fra(1, 3), -fra(1, 3), +z], [-fra(1, 3), -fra(1, 3), -z]]


def _s21(a):
    b = -(1 + 2 * a)
    return [[a, b, 0], [b, a, 0], [a, a, 0]]


def _s21_z(a, z):
    b = -(1 + 2 * a)
    return [[a, b, +z], [b, a, +z], [a, a, +z], [a, b, -z], [b, a, -z], [a, a, -z]]


def _s30(a, b, c):
    return [[a, b, 0], [b, a, 0], [a, c, 0], [c, a, 0], [b, c, 0], [c, b, 0]]


def _s111_z(a, b, z):
    c = -(1 + a + b)
    return [
        [b, c, +z],
        [a, b, +z],
        [c, a, +z],
        [c, b, +z],
        [a, c, +z],
        [b, a, +z],
        [b, c, -z],
        [a, b, -z],
        [c, a, -z],
        [c, b, -z],
        [a, c, -z],
        [b, a, -z],
    ]
