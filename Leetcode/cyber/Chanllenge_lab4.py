"""
RSA Public-Key: (2072 bit)
Modulus:
    00:8d:a5:69:19:b5:26:d4:52:25:ac:ed:4b:e6:45:
    22:ce:f0:4a:63:91:0b:9f:6f:fe:a6:b1:12:55:41:
    01:3b:e4:5d:48:b6:fb:26:71:b7:54:0e:6a:4e:0b:
    55:e3:a9:e4:c4:5a:8d:5f:54:a0:69:9c:65:32:d4:
    a1:28:7f:ac:b0:08:b1:c5:6e:35:d6:01:dc:2a:9e:
    2e:66:51:89:ea:a3:5d:22:d7:be:a2:52:c1:ec:f2:
    70:31:ab:65:7d:5b:35:e8:2c:de:70:f8:25:9d:2e:
    14:e9:86:f3:62:e3:e8:6e:7b:d8:e4:81:2a:52:f2:
    e8:cc:2f:69:b8:b0:c9:59:77:8f:db:24:0a:8e:17:
    cb:95:72:45:70:12:d8:3b:6c:72:72:90:e5:0b:8e:
    7d:a2:8f:eb:df:ab:f5:23:da:03:b9:4b:94:32:2a:
    f4:21:f9:ca:02:ad:e6:04:da:ab:92:cd:9c:28:24:
    44:36:f1:15:fd:be:d7:6d:2c:85:00:7a:ca:7f:ce:
    49:89:3a:f8:0e:79:55:63:2e:c7:b8:9f:56:fa:b0:
    18:76:e0:fe:88:29:9a:37:34:0d:43:9c:b2:e0:1b:
    3c:07:e6:0c:88:47:42:1b:fe:04:9d:59:95:40:6b:
    26:f4:a0:8b:20:d1:49:b3:c6:1a:ae:a3:53:1d:62:
    f8:f8:d1:e2:87
Exponent: 65537 (0x10001)
Modulus=8DA56919B526D45225ACED4BE64522CEF04A63910B9F6FFEA6B1125541013BE45D48B6FB2671B7540E6A4E0B55E3A9E4C45A8D5F54A0699C6532D4A1287FACB008B1C56E35D601DC2A9E2E665189EAA35D22D7BEA252C1ECF27031AB657D5B35E82CDE70F8259D2E14E986F362E3E86E7BD8E4812A52F2E8CC2F69B8B0C959778FDB240A8E17CB9572457012D83B6C727290E50B8E7DA28FEBDFABF523DA03B94B94322AF421F9CA02ADE604DAAB92CD9C28244436F115FDBED76D2C85007ACA7FCE49893AF80E7955632EC7B89F56FAB01876E0FE88299A37340D439CB2E01B3C07E60C8847421BFE049D5995406B26F4A08B20D149B3C61AAEA3531D62F8F8D1E287
"""

"""
299996217561787292756826251240073744022587364427659002955601969311597453693948323421942282716737653493469667806494795328718748694431287426493332498123774403296361258944222401796946976412532226598881087042326060698386611304550152758781853605660146138394024484376984580234460609993575374222942038026173435262460884234328411077658271473762471945787635582916630508147146325427058379173689622281755189370552117476758492729644576568772220182957835384550972772092654842082706142246481708409910183742375894996805693099913395071166112170527842473265346582564838421321907545834628201837626578791668861148755559537560386588395858682503
"""

import math
from functools import reduce

def isPrime(x):
    if x < 2:
        return False
    for n in range(2, x - 1):
        if x % n == 0:
            return False
    return True


def gcd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a



# inverse gcd: a⋅λ+b⋅μ=gcd(a,b)
# a^−1=λ mod b
#https://en.wikipedia.org/wiki/Euler%27s_factorization_method




def Euclidean(num1, num2):
    # e = 65537

    while num1 > 0:
        if num2 == 0:
            return lst_divisor
        factor = num1 // num2
        new_num = num1 - factor * num2
        reminder = num1 % num2
        print(num1, "=", num2, "x", factor, "+", reminder)
        reminder_lst.append(reminder)
        lst_divisor.append(new_num)
        num1 = num2
        num2 = new_num
    return lst_divisor


def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if len(factors) > 0:
            return factors
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors





def main():


    modulus = 299996217561787292756826251240073744022587364427659002955601969311597453693948323421942282716737653493469667806494795328718748694431287426493332498123774403296361258944222401796946976412532226598881087042326060698386611304550152758781853605660146138394024484376984580234460609993575374222942038026173435262460884234328411077658271473762471945787635582916630508147146325427058379173689622281755189370552117476758492729644576568772220182957835384550972772092654842082706142246481708409910183742375894996805693099913395071166112170527842473265346582564838421321907545834628201837626578791668861148755559537560386588395858682503

    '''
        p = prime_factors(modulus)[0]
        print(p)
        q = modulus // p
        print(q)
    '''
    print()
    # phi = (p-1) * (q - 1)
    phi = 299996187678051674930465818678877682223264556087385307553103024409835066893974572236830684788116780702301190696911268637395498255433806315365432731296304835157207752689999757367539595599887938629973055609311443848462860778055715083627060499660541439441478722185737579281000011402789583084858987991698323680321735393529720885513282759669704910825321362468547836277339434853381498045179952561003065854814857940303165168544493615997129828620900289373024881121773613134958404926420947386910433482888785819893341826347844926731707232824545037606839381106714623115131470586079963587914951747525465655253695540399024876938051993768

    global reminder_lst
    global lst_divisor
    lst_divisor = []
    reminder_lst = []

    p = 10038779
    q = 29883735617826360432561196061799322808340273695402498944901762386799973751185111597928620872791168477109583526691323250438997481111127899766827469568139153506254222644429407380812644287968908031433014616849923750526494437675154793105999604698952545762191247000953460598590785791138083050034475111582139148840798690192144988714092767034962314220448082671869806890573676881128509669720752123515737259536455327561100082952775090354336935095177947890970881228947747737320060761022999750259487109176912351273565550144434404937703297435658507201458123798206776075248548238249711627044143395493501863997161361711457796649957


    e = 65537
    v = 4866
    lst1 = Euclidean(e, phi)
    print(lst1)
    print("gcd is", lst1[-2])
    print()
    print(4866 * 1064 - 65537 * 79)
    A =  4577508700093865677868468478552232818457734655040439866840151737336696322596007938062936734792815977269346944426984278154256347642305969381653611414869536828924237494697648005974328937850190558462747083469054791163203393168068649520531310552215411743617784185814693673512672404943613273187039199104297170763412048057276361223633714690475684129962026984276787711938896117511962678260829036437479070674807481885090333224659255321377692427497448607245142150567978594304872132176037160488127828293769715121127635173228022746413586719327174536625713430683653861408539765111005441016753158483382908208396715449273309381540992
    test = 4866 * phi - e * 4866 * A - e * 79
    print("test: ", test)
    u = (4866 * A -  79)
    print("u is: ", u)
    d = 277722030343394924541957851062242517328649219255958527161058846055954702588222397610216434636614938156908548465329563139896886867806345468354306258151549668947662413040801002170468510988308911372493328301151023234662713066899893035060155142513461245897034584337563279865687347480333960897530855248856813647386972367683014111799081103985850231848926139163056987271044766345568287652762758469698292696911244733450315607073301679603305977268697704450170019417109829295070897131252350563975203470411302386113934753594917368047658719848299006311618659553007963425517516089049811111927430878345324423911637123022860953487473526617

    exponent1 = d % (p-1)
    exponent2 = d % (q-1)
    print()
    print("e1:", exponent1)
    print()
    print("e2:", exponent2)
    # coefficient INTEGER, -- (inverse of q) mod p

    print()
    print()
    lst2 = Euclidean(p, q)
    print(lst2)
    #coefficient =
    print()

    #print("Coe: ", coefficient)


    print()







main()

