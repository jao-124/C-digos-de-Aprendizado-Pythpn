import math
import time

print('Parâmetro K da velocidade de vento NBR 5422:\n')
'''
Pontos retirados do gráfico da norma
X = [10.0399 10.1487 10.2585 10.3701 10.4840 10.5002 10.5988 10.7115 10.8193 10.9228 11.0005 11.0271 11.1406 11.2629
     11.3896 11.5007 11.5157 11.6365 11.7534 11.8751 12.0010 12.0049 12.1381 12.2715 12.3999 12.5012    12.5280
     12.6570    12.7893    12.9274    13.0014    13.0693    13.2090    13.3482    13.4836    13.5017    13.6258
     13.7805    13.9387    14.0019    14.0972    14.2568    14.4265    14.5022    14.6101    14.7986    14.9865
     15.0024    15.1757    15.3687    15.5103    15.5624    15.7650    15.9778    16.0181    16.2016    16.4374
     16.5260    16.6862    16.9460    17.0339    17.2103    17.4779    17.5417    17.7586    18.0496    18.0729
     18.4190    18.5575    18.7806    19.0654    19.1578    19.5732    19.5841    20.0811    20.1232    20.5966
     20.7176    21.1120    21.2938    21.6275    21.9448    22.1429    22.6584    22.7319    23.1739    23.4853
     23.6893    24.1807    24.2048    24.7203    25.0497    25.2357    25.7522    25.9931    26.2687    26.7852
     26.9614    27.3017    27.8182    28.1267    28.3347    28.8512    29.3677    29.8720    29.8842    30.4007
     30.9177    31.4347    31.9518    32.4688    32.8880    32.9858    33.5028    34.0199    34.5369    35.0539
     35.5710];
Y = [0.994885605338418    0.984966634890372    0.975042897998093    0.965123927550048    0.955200190657769
     0.953794089609152    0.945276453765491    0.935357483317445    0.925433746425167    0.915510009532889
     0.908093422306959    0.905591039084843    0.895400381315539    0.885209723546235    0.87501906577693
     0.866048617731173    0.864828408007626    0.854637750238322    0.844447092469018    0.834256434699714
     0.824370829361297    0.82406577693041    0.813875119161106    0.803684461391802    0.793884652049571
     0.786134413727359    0.78408484270734    0.774289799809342    0.764489990467112    0.754690181124881
     0.749575786463298    0.74489037178265    0.735095328884652    0.725100095328885    0.715495710200191
     0.714237368922784    0.705700667302193    0.69534795042898    0.685    0.680881792183031    0.67465204957102
     0.66430409914204    0.653951382268827    0.649618684461392    0.643603431839848    0.633255481410868
     0.622907530981888    0.622035271687321    0.612554814108675    0.602206863679695    0.594842707340324
     0.592192564346997    0.582178265014299    0.572163965681602    0.570319351763584    0.562154432793136
     0.552140133460439    0.548508102955195    0.542125834127741    0.532111534795043    0.528779790276454
     0.522097235462345    0.512082936129647    0.509747378455672    0.502068636796949    0.492578646329838
     0.491863679694948    0.481658722592946    0.477726406101049    0.471448999046711    0.463665395614871
     0.461244041944709    0.451272640610105    0.451034318398475    0.441539561487131    0.440829361296473
     0.432778836987607    0.430619637750238    0.423555767397521    0.420414680648236    0.414966634890372
     0.410204957102002    0.407459485224023    0.400905624404194    0.4    0.394380362249762    0.39
     0.386954242135367    0.38    0.379690181124881    0.373565300285987    0.37    0.368036224976168
     0.362559580552908    0.36    0.35708770257388    0.351754051477598    0.35    0.346768350810296
     0.342354623450906    0.34    0.338522402287893    0.335200190657769    0.33234509056244    0.33
     0.329947569113441    0.327983794089609    0.326334604385129    0.324795042897998    0.323145853193518
     0.321339370829361    0.32    0.319623450905624    0.318288846520496    0.317621544327931    0.317597712106768
     0.317607244995234    0.317011439466158];
'''

# Equação obtida via ajuste de curva exponencial:

# Coeficientes
tp = 1
a = 3.393
b = -0.1529
c = 0.2667
d = 0.003546

print('-------------------------------------------------------------------------------------------------------------\n')

x = float(input('Entre com a velocidade de vento desejada:\n'))

if 10 < int(x) < 34:
    f_x = a * math.exp(b * x) + c * math.exp(d * x)
    print(f'k = {f_x}\n')
else:
    if x <= 10:
        print(f'k = 1.000\n')
    else:
        if x >= 34:
            print(f'k = 0.320\n')
time.sleep(5)