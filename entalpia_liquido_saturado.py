import matplotlib.pyplot as plt
import numpy
from scipy.optimize import minimize
def dados_R444B(dados):
    if dados == 'tmp':
        return [-40,-39,-38,-37,-36,-35,-34,-33,-32,-31,-30,-29,-28,-27,-26,-25,-24,-23,-22,-21,-20,-19,-18,-17,-16,-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70]
    elif dados == 'pvap':
        return [0.080804,0.084994,0.089355,0.093892,0.09861,0.10351,0.10861,0.1139,0.11939,0.12509,0.131,0.13713,0.14348,0.15006,0.15687,0.16393,0.17123,0.17878,0.18659,0.19466,0.20301,0.21162,0.22052,0.22971,0.2392,0.24898,0.25907,0.26948,0.2802,0.29125,0.30264,0.31436,0.32644,0.33887,0.35165,0.36481,0.37834,0.39225,0.40656,0.42125,0.43636,0.45187,0.4678,0.48416,0.50095,0.51819,0.53587,0.554,0.57261,0.59168,0.61124,0.63128,0.65182,0.67287,0.69442,0.7165,0.73911,0.76225,0.78594,0.81019,0.835,0.86038,0.88634,0.9129,0.94005,0.96781,0.99619,1.0252,1.0548,1.0851,1.1161,1.1477,1.1799,1.2129,1.2466,1.2809,1.316,1.3518,1.3883,1.4256,1.4637,1.5025,1.542,1.5824,1.6236,1.6656,1.7084,1.7521,1.7966,1.8419,1.8882,1.9353,1.9833,2.0323,2.0821,2.1329,2.1847,2.2374,2.2912,2.3459,2.4016,2.4584,2.5162,2.5751,2.6351,2.6962,2.7584,2.8217,2.8863,2.952,3.0189]
    elif dados == 'pliq':
        return [0.12981,0.13581,0.14203,0.14846,0.15513,0.16202,0.16915,0.17652,0.18414,0.19202,0.20015,0.20855,0.21722,0.22616,0.23539,0.2449,0.25471,0.26482,0.27523,0.28596,0.297,0.30837,0.32007,0.3321,0.34448,0.35721,0.37029,0.38373,0.39754,0.41173,0.4263,0.44125,0.4566,0.47235,0.4885,0.50507,0.52206,0.53948,0.55733,0.57562,0.59436,0.61355,0.6332,0.65332,0.67391,0.69499,0.71655,0.73861,0.76117,0.78424,0.80782,0.83193,0.85657,0.88174,0.90746,0.93373,0.96056,0.98795,1.0159,1.0445,1.0736,1.1033,1.1337,1.1646,1.1961,1.2283,1.2611,1.2946,1.3286,1.3634,1.3988,1.4348,1.4716,1.509,1.5471,1.5859,1.6254,1.6656,1.7065,1.7482,1.7906,1.8337,1.8776,1.9222,1.9676,2.0137,2.0607,2.1084,2.1569,2.2062,2.2563,2.3072,2.3589,2.4114,2.4648,2.519,2.5741,2.63,2.6868,2.7444,2.803,2.8623,2.9226,2.9838,3.0458,3.1088,3.1727,3.2374,3.3031,3.3697,3.4372]
    elif dados == 'dliq':
        return [1248.7,1245.9,1243.2,1240.4,1237.6,1234.8,1231.9,1229.1,1226.3,1223.4,1220.6,1217.7,1214.9,1212.0,1209.1,1206.2,1203.3,1200.4,1197.4,1194.5,1191.6,1188.6,1185.6,1182.6,1179.6,1176.6,1173.6,1170.6,1167.5,1164.5,1161.4,1158.3,1155.2,1152.1,1149.0,1145.8,1142.7,1139.5,1136.3,1133.1,1129.9,1126.6,1123.4,1120.1,1116.8,1113.5,1110.2,1106.9,1103.5,1100.1,1096.7,1093.3,1089.9,1086.4,1082.9,1079.4,1075.9,1072.3,1068.7,1065.1,1061.5,1057.9,1054.2,1050.5,1046.8,1043.0,1039.2,1035.4,1031.5,1027.7,1023.8,1019.8,1015.8,1011.8,1007.8,1003.7,999.57,995.41,991.20,986.96,982.67,978.34,973.96,969.54,965.07,960.55,955.97,951.34,946.66,941.92,937.12,932.25,927.33,922.33,917.26,912.13,906.91,901.62,896.25,890.79,885.23,879.59,873.84,867.99,862.03,855.96,849.76,843.44,836.98,830.37,823.61]
    elif dados == 'dvap':
        return [0.3187962255,0.3040252949,0.2900652647,0.2768779245,0.2644033738,0.2526145607,0.2414525787,0.2308828962,0.2208675678,0.2113762709,0.202375893,0.193839772,0.1857320629,0.1780341469,0.1707212975,0.1637679735,0.157158573,0.1508682468,0.1448813422,0.1391807819,0.1337488464,0.1285727143,0.1236384318,0.1189315192,0.1144400449,0.1101527819,0.106058035,0.1021460893,0.09840582562,0.09483167378,0.09141603437,0.08814455707,0.08501232679,0.08202099738,0.07915149596,0.07640003056,0.07376263185,0.07123521869,0.06881365263,0.06648494116,0.0642549637,0.06211180124,0.06005645307,0.05807875479,0.05617977528,0.0543537341,0.05259835893,0.05090872066,0.04928536225,0.04772130756,0.04621712807,0.04476876931,0.04337265788,0.04202916824,0.04073319756,0.0394835551,0.03827897719,0.03711676936,0.03599712023,0.03491498202,0.03387074922,0.0328633869,0.03188978889,0.03094921234,0.03004085556,0.02916217083,0.02831337241,0.02749292057,0.02669870511,0.02593092003,0.02518764798,0.0244684235,0.02377216755,0.02309788885,0.02244517765,0.02181262951,0.02119946577,0.02060538625,0.02002964387,0.01947116321,0.01892935564,0.01840400471,0.01789420943,0.01739947454,0.01691932864,0.01645278052,0.016,0.01556008527,0.0151327139,0.01471713663,0.01431331854,0.0139207907,0.01353894477,0.01316759718,0.01280622895,0.01245438581,0.01211210969,0.01177870175,0.01145396651,0.01113759383,0.01082919117,0.01052864317,0.01023562407,0.009950248756,0.009671179884,0.009398496241,0.009133254178,0.008873114463,0.008619946556,0.008371703642,0.008129420372]
    elif dados == 'eliq':
        return [141.29,142.71,144.14,145.56,146.99,148.42,149.86,151.29,152.73,154.16,155.61,157.05,158.49,159.94,161.39,162.84,164.29,165.75,167.21,168.67,170.13,171.60,173.07,174.54,176.02,177.49,178.97,180.45,181.94,183.43,184.92,186.41,187.91,189.41,190.91,192.42,193.93,195.44,196.96,198.48,200.00,201.53,203.06,204.59,206.13,207.67,209.22,210.77,212.32,213.88,215.44,217.00,218.57,220.15,221.73,223.31,224.90,226.49,228.09,229.69,231.30,232.91,234.53,236.15,237.78,239.41,241.05,242.70,244.35,246.01,247.67,249.34,251.02,252.70,254.39,256.09,257.79,259.50,261.22,262.94,264.67,266.42,268.16,269.92,271.69,273.46,275.25,277.04,278.84,280.66,282.48,284.32,286.16,288.02,289.89,291.77,293.66,295.57,297.49,299.42,301.37,303.33,305.32,307.31,309.33,311.36,313.42,315.49,317.59,319.71,321.85]
    elif dados == 'evap':
        return [422.82,423.45,424.09,424.72,425.34,425.97,426.59,427.22,427.84,428.46,429.07,429.68,430.30,430.90,431.51,432.12,432.72,433.32,433.91,434.51,435.10,435.69,436.27,436.85,437.43,438.01,438.59,439.16,439.72,440.29,440.85,441.41,441.96,442.51,443.06,443.60,444.14,444.68,445.21,445.74,446.27,446.79,447.30,447.82,448.32,448.83,449.33,449.82,450.31,450.80,451.28,451.76,452.23,452.69,453.15,453.61,454.06,454.50,454.94,455.38,455.80,456.22,456.64,457.05,457.45,457.85,458.24,458.62,458.99,459.36,459.72,460.08,460.42,460.76,461.09,461.41,461.72,462.03,462.32,462.61,462.88,463.15,463.41,463.65,463.89,464.11,464.33,464.53,464.72,464.90,465.06,465.21,465.35,465.48,465.59,465.68,465.76,465.83,465.87,465.90,465.91,465.90,465.88,465.83,465.76,465.67,465.55,465.41,465.24,465.04,464.82]

def dados_R454C(dados):
    if dados == 'tmp':
        return [-40, -39, -38, -37, -36, -35, -34, -33, -32, -31, -30, -29, -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70]
    elif dados == 'pvap':
        return [0.091068,0.095526,0.10015,0.10496,0.10995,0.11512,0.12048,0.12603,0.13179,0.13775,0.14392,0.15030,0.15691,0.16374,0.17080,0.17809,0.18563,0.19341,0.20145,0.20974,0.21830,0.22712,0.23622,0.24560,0.25526,0.26522,0.27547,0.28603,0.29689,0.30807,0.31958,0.33141,0.34357,0.35608,0.36893,0.38214,0.39570,0.40964,0.42394,0.43862,0.45369,0.46916,0.48502,0.50129,0.51797,0.53507,0.55260,0.57057,0.58897,0.60783,0.62714,0.64692,0.66717,0.68790,0.70911,0.73082,0.75303,0.77575,0.79899,0.82276,0.84705,0.87190,0.89729,0.92324,0.94976,0.97686,1.0045,1.0328,1.0617,1.0912,1.1213,1.1521,1.1835,1.2155,1.2482,1.2816,1.3156,1.3504,1.3858,1.4220,1.4589,1.4965,1.5349,1.5740,1.6139,1.6546,1.6961,1.7383,1.7815,1.8254,1.8702,1.9159,1.9624,2.0099,2.0582,2.1075,2.1577,2.2089,2.2611,2.3142,2.3684,2.4237,2.4800,2.5374,2.5959,2.6555,2.7164,2.7784,2.8417,2.9063,2.9722]
    elif dados == 'pliq':
        return [0.13082,0.13677,0.14293,0.14931,0.15590,0.16271,0.16976,0.17704,0.18455,0.19231,0.20032,0.20859,0.21711,0.22590,0.23496,0.24429,0.25391,0.26381,0.27401,0.28450,0.29530,0.30640,0.31782,0.32956,0.34163,0.35403,0.36676,0.37984,0.39326,0.40705,0.42119,0.43570,0.45058,0.46583,0.48148,0.49751,0.51394,0.53077,0.54801,0.56567,0.58374,0.60224,0.62118,0.64055,0.66037,0.68064,0.70136,0.72255,0.74421,0.76635,0.78897,0.81208,0.83568,0.85978,0.88439,0.90952,0.93517,0.96134,0.98805,1.0153,1.0431,1.0714,1.1003,1.1298,1.1599,1.1905,1.2217,1.2535,1.2859,1.3189,1.3525,1.3868,1.4216,1.4571,1.4933,1.5301,1.5675,1.6056,1.6444,1.6838,1.7239,1.7647,1.8062,1.8484,1.8913,1.9349,1.9793,2.0244,2.0702,2.1167,2.1640,2.2121,2.2609,2.3104,2.3608,2.4119,2.4639,2.5166,2.5701,2.6244,2.6796,2.7355,2.7923,2.8499,2.9084,2.9677,3.0278,3.0888,3.1506,3.2132,3.2768]
    elif dados == 'dliq':
        return [1261.1,1258.2,1255.3,1252.4,1249.6,1246.6,1243.7,1240.8,1237.9,1234.9,1231.9,1229.0,1226.0,1223.0,1220.0,1216.9,1213.9,1210.8,1207.8,1204.7,1201.6,1198.5,1195.4,1192.2,1189.1,1185.9,1182.7,1179.5,1176.3,1173.1,1169.8,1166.5,1163.3,1160.0,1156.6,1153.3,1149.9,1146.6,1143.2,1139.7,1136.3,1132.9,1129.4,1125.9,1122.4,1118.8,1115.2,1111.7,1108.0,1104.4,1100.7,1097.1,1093.3,1089.6,1085.8,1082.0,1078.2,1074.4,1070.5,1066.6,1062.6,1058.7,1054.7,1050.6,1046.6,1042.4,1038.3,1034.1,1029.9,1025.6,1021.4,1017.0,1012.6,1008.2,1003.7,999.22,994.65,990.04,985.37,980.64,975.86,971.02,966.12,961.16,956.13,951.02,945.85,940.60,935.27,929.86,924.35,918.76,913.07,907.28,901.38,895.36,889.23,882.97,876.58,870.05,863.37,856.53,849.52,842.33,834.95,827.35,819.54,811.48,803.16,794.56,785.64]
    elif dados == 'dvap':
        return [0.2250984806,0.2152203857,0.2058629776,0.1969899929,0.1885796183,0.1805966915,0.1730223545,0.1658264792,0.1589926227,0.1524948152,0.1463164826,0.1404376036,0.1348435814,0.129516902,0.1244415685,0.1196072099,0.1149967226,0.1105998938,0.106404486,0.1024002621,0.09858044164,0.09492168961,0.09143275121,0.08809796494,0.08490405841,0.08185315544,0.07893282816,0.0761324705,0.07345919342,0.07089181908,0.06843221789,0.0660763843,0.06381213707,0.06164468006,0.05956280898,0.05756720972,0.05564830273,0.05380393845,0.05203455094,0.05033219247,0.04869734599,0.04712313275,0.04561003421,0.04415205969,0.042749658,0.04140101018,0.04010105466,0.03884702043,0.03764068205,0.03647771212,0.03535567812,0.03427357165,0.03322921513,0.03222272346,0.03125,0.03031129702,0.02940484592,0.02852985649,0.02768395991,0.02686583203,0.0260756193,0.02531132935,0.02457243955,0.02385723829,0.02316530764,0.02249566958,0.02184741764,0.0212192586,0.02061133211,0.02002202423,0.01945109023,0.01889787588,0.01836142632,0.0178412132,0.01733673133,0.0168469288,0.01637197119,0.01591064581,0.01546312046,0.0150283284,0.01460578974,0.01419547164,0.01379671914,0.01340913967,0.01303220257,0.01266560276,0.01230890426,0.01196186557,0.01162412238,0.01129522325,0.0109749004,0.01066291332,0.01035882987,0.01006248805,0.00977326036,0.009491268033,0.009216589862,0.008947745168,0.008685833406,0.008429570935,0.008179290038,0.007934618742,0.007695267411,0.007460459564,0.007231180852,0.00700623555,0.006785641582,0.006569007423,0.006356470887,0.006147415012,0.005941417622]
    elif dados == 'eliq':
        return [146.22,147.51,148.80,150.09,151.39,152.69,153.99,155.29,156.59,157.90,159.21,160.53,161.84,163.16,164.48,165.81,167.14,168.47,169.80,171.14,172.48,173.82,175.17,176.52,177.87,179.23,180.59,181.95,183.32,184.69,186.06,187.44,188.82,190.21,191.59,192.98,194.38,195.78,197.18,198.59,200.00,201.41,202.83,204.26,205.68,207.11,208.55,209.99,211.43,212.88,214.34,215.79,217.26,218.72,220.19,221.67,223.15,224.64,226.13,227.63,229.13,230.63,232.15,233.66,235.19,236.72,238.25,239.79,241.34,242.89,244.45,246.01,247.59,249.16,250.75,252.34,253.94,255.55,257.17,258.79,260.42,262.06,263.71,265.37,267.04,268.71,270.40,272.10,273.81,275.52,277.26,279.00,280.75,282.52,284.31,286.10,287.91,289.74,291.59,293.45,295.33,297.23,299.15,301.09,303.05,305.04,307.06,309.11,311.19,313.30,315.45]
    elif dados == 'evap':
        return [365.02,365.65,366.28,366.91,367.54,368.17,368.80,369.43,370.05,370.67,371.30,371.92,372.54,373.16,373.78,374.39,375.01,375.62,376.23,376.84,377.45,378.06,378.66,379.26,379.86,380.46,381.06,381.65,382.24,382.84,383.42,384.01,384.59,385.17,385.75,386.32,386.90,387.47,388.03,388.60,389.16,389.71,390.27,390.82,391.37,391.91,392.45,392.99,393.52,394.05,394.57,395.09,395.61,396.12,396.63,397.13,397.63,398.12,398.61,399.09,399.57,400.04,400.51,400.97,401.42,401.87,402.31,402.74,403.17,403.59,404.01,404.41,404.81,405.20,405.59,405.96,406.33,406.68,407.03,407.37,407.70,408.01,408.32,408.62,408.90,409.17,409.43,409.68,409.92,410.13,410.34,410.53,410.70,410.86,411.00,411.12,411.22,411.30,411.36,411.40,411.41,411.40,411.36,411.29,411.19,411.06,410.89,410.68,410.44,410.14,409.80]



def modelo_polinomial_entalpia_liquido(T, a4, a5, a6, a7):
    return a4 + a5*T + a6*T**2 + a7*T**3

def erro_pl(a):
    y_data = numpy.array(dados_R444B('eliq'))
    x_data = numpy.array(dados_R444B('tmp'))
    y_calculado = modelo_polinomial_entalpia_liquido(x_data,a[0],a[1],a[2],a[3])
    erro = abs((y_calculado - y_data)*100/y_data)
    return max(erro)

res = minimize(erro_pl, [199.9974,1.3992,0.0019,0.000020], method='Nelder-Mead')


def max_desvio_abs(calculada,real):
    desvio = []
    for i in range(0,len(calculada)):
        desvio.append(abs((calculada[i] - real[i])*100/real[i]))
    return max(desvio)

def mean_desvio_abs(calculada,real):
    desvio = []
    for i in range(0,len(calculada)):
        desvio.append(abs((calculada[i] - real[i])*100/real[i]))
    return numpy.mean(desvio)

print(res.values())

# Dados R444B:
#--------------------------------------------------------------------
a4B = 1.9994e+02
a5B = 1.5113e+00
a6B = 1.8500e-03
a7B = 2.0309e-05
#--------------------------------------------------------------------

# Dados R454C:
#--------------------------------------------------------------------
a4C = 1.9992e+02
a5C = 1.3949e+00
a6C= 2.0884e-03
a7C = 2.1066e-05
#--------------------------------------------------------------------

dados_obtidos_R444B = []

for T in dados_R444B('tmp'):
    dado = a4B + a5B*T + a6B*T**2 + a7B*T**3
    dados_obtidos_R444B.append(dado)

dados_obtidos_R454C = []
for T in dados_R454C('tmp'):
    dado = a4C + a5C*T + a6C*T**2 + a7C*T**3
    dados_obtidos_R454C.append(dado)

#--------------------------------------------------------------------

erro_444B = []
erro_454C = []

for i in range(0, len(dados_obtidos_R444B)):
    erro444B = ((dados_obtidos_R444B[i] - dados_R444B('eliq')[i])/ dados_R444B('eliq')[i])*100
    erro454C = ((dados_obtidos_R454C[i] - dados_R454C('eliq')[i]) / dados_R454C('eliq')[i]) * 100

    erro_444B.append(erro444B)
    erro_454C.append(erro454C)

#____________________________________________________________________

#plt.scatter(dados_R444B('tmp'),dados_R444B('eliq'),s=10)
#plt.plot(dados_R444B('tmp'), dados_obtidos_R444B,linewidth=1.5, color='orange')
#plt.legend(["REFPROP", "Entalpia calculada"])
#plt.grid()
#plt.ylabel("Entalpia [kj/kg]")
#plt.xlabel("Temperatura [ºC]")


#print("Média do erro: "+ str(mean_desvio_abs(dados_obtidos_R454C, dados_R454C('pvap'))))
#print("Erro máximo: "+ str(max_desvio_abs(dados_obtidos_R454C, dados_R454C('pvap'))))

erro_abs_R444B = []
erro_abs_R454C = []



for i in range(0, len(erro_454C)):
    erro_abs_R454C.append(abs(erro_454C[i]))
    erro_abs_R444B.append(abs((erro_444B[i])))

print("Média do erro:")
print("R444B: {}".format(numpy.mean(erro_abs_R444B)))
print("R454C: {}".format(numpy.mean(erro_abs_R454C)))
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
print("Erro mínimo:")
print("R444B: {}".format(min(erro_444B)))
print("R454C: {}".format(min(erro_454C)))
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
print("Erro máximo:")
print("R444B: {}".format(max(erro_444B)))
print("R454C: {}".format(max(erro_454C)))

plt.plot(dados_R444B('tmp'), erro_444B, linewidth=3)
plt.plot(dados_R454C('tmp'), erro_454C, linewidth=3)
plt.legend(["Erro 444B", "Erro 454C"])
plt.ylabel("Erro [%]")
plt.xlabel("Temperatura [ºC]")
plt.grid()



plt.show()