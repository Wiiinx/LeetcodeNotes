def checkInclusion(s1, s2):
    if len(s1) > len(s2):
        return False

    # initializing 2 hash maps, 存储每个字母的数字
    s1Count, s2Count = [0] * 26, [0] * 26

    # 当前window下hash map的数字
    for i in range(len(s1)):
        s1Count[ord(s1[i]) - ord('a')] += 1
        s2Count[ord(s2[i]) - ord('a')] += 1

    # 这里是O(26)用来遍历每个字母来对比上面window下 match的的数量
    matches = 0
    for i in range(26):
        matches += (1 if s1Count[i] == s2Count[i] else 0)

    #这里开始sliding window，移动到下一格
    l = 0
    for r in range(len(s1), len(s2)):
        if matches == 26:
            return True

        # ——————Right——————
        # 先移动右边
        index = ord(s2[r]) - ord('a')  # 当前r所在字母对应hash map字母表的index
        s2Count[index] += 1  # 这个位置的字母数量+1
        if s1Count[index] == s2Count[index]:  # 移动r之后，s2位置上的字母数量 == s1 hash map的数量， matches +=1
            matches += 1
        elif s1Count[index] + 1 == s2Count[index]:  # 移动r一格之后，s2这格字母的数量更多，match减少
            matches -= 1

        # ——————Left——————
        index = ord(s2[l]) - ord('a')
        #print(l, s2[l], ord(s2[l]) - ord('a'), "s2count", s2Count[index], "s1Count", s1Count[index])
        s2Count[index] -= 1  # 查看当前l所在字母
        if s1Count[index] == s2Count[index]: # check if Hash Map matches
            matches += 1
        elif s1Count[index] - 1 == s2Count[index]:
            matches -= 1
        l += 1
    return matches == 26



def main():
    print(checkInclusion("ab", "eidbaooo"))
    print(checkInclusion("ab", "eidboaoo"))
    #print(checkInclusion("abcd", "dabcweadf"))
    #print(checkInclusion("a", "a"))
    #print(checkInclusion("adc", "dcda"))
    print(checkInclusion("paoolrbebsqumnolusfdaavvkdmyulelajnilqxsujdycieizlwvuwcnwfemijpyixbjamphkufjfvfvjvdjbdkthlxrtyahuifdjqlvpvccajaosgffminewnhyzymgvwbsgirfwnjszjswffrolsuupwkiwjjtbcgqbyarskbyxdigcusygjpvdcubzmmpfzzwhuwibivbxjklpptfryfbamafxuzpzagivenlctomtcymlmkbzozyncdwvabqjvvzuwivzfjcqhrixwinyxqsnckkhjmfsomdkujzecihamydgkyntwztemhawvxpahtiwrjwysrzmrhwxkbazynwmgtyclyjqsrfkddjdmvxhtwnvxrlxfxnpyevsafmqmbvbnueqxegkcuwzwdmqqpdlegyrjhgytgfxtzagazguoadzycnwwhdlkogbzrwiwjxxvlpvxfbtrxtqahcfrbzixqyftlddwmwtorfvjzenksaukrevkddgnafwqtgsizisktrrmqvkeagjngtngqiithdxxefqpcdwmglvvjerwcwitdzlsozczimmbwxwvpccjyemhyyekruqejgrnhpfnxiodwmworpenustqtaswegjordqwqmdsmgbpxytptvnwtjmxwhfsnszscafeiyyuikthfnzcoassldzlkdgclyezsquhksisjvmcsxlwdpplwrwxthuipsjjfhtfqhcrnfcomnkbthyvhaelbtsyhrmjharxzhymxxbcwtxansrcwqsgzzdxzcqbphtccnjhikhhovezgbkgcwkavkrbydyctgizqferucmghsihyxgbpmehtwpwcwunitcrgdmcnodipruqegudtkluswpnvbdqyukspwvgchexiaxuebqfvitnmukebchkzmtnwcuymbnmyqgmzefnelwqnhleaadekwjehlkydpuwybendymsluptckrvbglxmamohiyszwkslittmdbfmxkmqomxfuskubytbgfvnlebmzxcsreqnjuctcjriszjpojywsitudelqljtufsbxmnykadnryjz","pwjurfxfwxotemsiyitndgrtvzksgniyqolgwfhofhmnwmxbmphratrwdskjwutemrzivnndkxfmzzpenueyiztqcydbeftbuobqwyazibaettbqbueeaiayutaoqvmckemxhrecvptegifgemdsjkepzsedvkfixtvikviadomqsrwowftrnqdumlabwtbfsxkoytkgznmkfzbtntumlbjhxeaoxbuoshxsjnosnsrtzrtcqdifbiyvmrbwteajksskklrpkmbylwwprapfdhujoigcrqhtgtwolwjmoudnzlnmpnchwslpibwvffbcbbefpvfygnpluzyjrqipupidoxtgglbvnxmtzjaglglpkryudoskkyspuxmxrkmcxkueluiuvxsdwkorxgjikyoniicljvddfgfuhujplkakjnvskuozvmmavmyzdgzbohjrnfvsslyarxscfxscijsyhcqxnceqfavyzofvysilqdnpjypgtpjatklrnzhkygyfoaupibuqtuxbfsfcawiiulgohigutukhywypthyymvcabnsdsjtrdrtmifarhrcimzrpcbdfjtpwqsndlpiuletacqcccpnziupvclsinkdffnojfrvgypdajujzkdixugrbhqmwyjztfvvokmgdrbfmrdprmzoslldcssvkofxqsdrwapobietvmoonfipeejlgtuvpcbcfnsmupwjsgliheexediefcfrglliqoxjjsdjtpehqmkxkvkkflhwbvohryjpfgebcvkjqtcetxzhtfysomusfzsztqweekxbdcruwjgpdrwokseyaqznhihjulevycglkuacfgzlargjoquxoupfrhdegpqzrshmbierjjvzsdwsibinlrslimfgrsaacxijthbzmxnyuslffnfxziudxcdwfwnkmdeucbyydkhqkestxzvdraxjjcuzdgayabmxsltqdnsikxaasugkcovnvwfxiuozaphegpkhtmtqxxmwhrtblrtxvrtidkcluorcrksklgmismylsrwwtlhlnqnqlfmmefzltunpqozqpnxhtqvpovckbiaaejtwejjuuzmtargntaqehigzibxfczkwcthqijyhcdtupeqbtnnorrgmktlsgjortvsgjhrgzccgvlfjeqjfywufbqwnerpzxlnczxwjttiiokqfigqhgqaatzwynivuhpukuzgsijrfpganfroohnruzlijwinapnemwsxveqfremhwqwqwhxlmvfsnuglnkkqynvflxgdqayxpklerojawlidelttqlfvfmjoiwhylwrillyjjoxrfkayddfeytomjphsgzzbgxhbgdwonzrqrcbnrztgvoodyxrzbinqgeaptvyfkdizuzbxdiulvfqlsllkxkvmprritvhkdoghouifwpprblaeauyxyhlipccqjnorphmrelbsashkmmhnperidnmmizijbtfqkhgboniuphozbdgmlfieqjjpywvqggmsliocmvdkhxszrvqyjoxdvspqlljtbztjybmpwebavgmldxxohjfrmxpljszfjploblpsenjxqxdvmmwljoxmagpgxunlnoibvupfluyclemsywizdmrzchiujcqnlmcjkutxbzeibruvvknviojcflxfhyjhjkwerwgfowucgtyrimxiehdgwrifbpdaaqffgzssxiemrcyxpezijuyptdynatoivsqbkqbgutgmikqywkhcwhknunsnfsdkkhwwxvttohjwydlzihsjtwbzbtbemhssndaubxegtvinucugvvascicyfgqnhsidgcrrctjwrjjqbgcsfioebytsmalmnnnpznxcjlyvfykwsqbewxfgiazugkqdoggrjukpplsnaovwsliyiojnyhmiloyjkkwtrdcsyjxllfhvizydwlqlojidvzjylhzfvksneyduudibadamaoifenrvdduvljircjtlnohxxckjnfeiaagyqxyoyezloucybulpjrlhdwkdkagbukvjrkxjddpsahymtcfaivfaeioyynxykdacbloejpnnhtcxepzzuhzrnjrmpwvngrivioukkolckoskxjmjyzaqysaqbjevvqibbimxhehlkuyknwqkhfabgdnuwgzofmyetruzxszdcypmqouxyqyuvfvijircklyfifwbypgwbwvwrvxxmoyzdlpecfsbinlthrdnckqagstfgyzhduluvscnmmwzapxaraxcvkndddlfrcnzpkyhksxerhgaulwetciqaefwmmzdsqfldtouxlqqgrqsvksyrnspqmkiewwhrjkoahzpacgylikhnoswnsyzuvxzdrlxgcfflogzezkofstastmpvftshxvizunhsuakqqjscycfrqejprsogqzlkuskvnbgbjisbasgdjlmgpiklkhbfoaqjfrjmmtzfggyrsyymtfkuuqtrbvtnnzcaiuqjlgosortmyjqqzmadqgjijrofedppddtfdyijinvxehpbanizoqtowugvzflscmcfqelycotzwpwhxzmdsaxrwhgvlaookontbwunqfiuxarlztainztyooiuazebwmukvgcpvnkllkjoazejdmocpeuurhfarzjdybgxusmocaiaqxicgdorwdrvrrmjczfajbbmjnmvohjfsprufofokpaoolrbebsqumnolusfdaavvkdmyelelajniwqxsujdycieizlwviwcnwfcmijpyixbjamphkufkmvfvjvdjbdkthlxrtyahuifdjqlvpvccajaosgffminewnhyzymgvwbsgirfwnjszjswffkolsuupwkiwjjtbcgqbyarskbyxdigcusygjpvdcubzmmpfzzwhuwibivbxjklpptfryfbamafxuzpzagivenlctomtcymlmkbzozyncdwvabqjvvbuwivzfjcqhrixwinyxqsnckkhimfsomdkujtecihamydgkyntwztemhawvxpahtiwrjwysrzmrhwxkfazynwmgtyclyjqsrfkddjdmvxhzwnvxrlxfxnpyevsafmqmbvbnueqxegkcuwzidmqqpdlegyrjhgytgfxtzagazguoydzycnwwhdlkogbzrwiwjxxvlgvxfbtrxtqahcfrbzixqyftlddwmwtorfvjzenksaukrevkddgnafwqtgswzisktrrmqvkeagjngtnjqiithdxxefqpcdwmglvvjerwcwitdzlsozczimmbwxwvpccjyemhyyekruqejgrnhpfnxjodwmworpenustqoaswegjordqlqmdsmgbpxytptvnwtjmxwhfsnszscafeiyyuikthfnzcoassldzlkdgclyezsquhksisjvmcsxlwdpplwrwxthuupsjjfhtfqhcrnfcomnkbthyvhaelbtsyhrhjharxzhymxxbcwtxansrcwqsgzzdxzcqbpmtccnjhikhhovezgbkgcwkavkrbydyctgizqferucmghsihyxgbpmehtwpwewunitcrgdmcnodipruqegudtkluswpnvbdqyukspwvgchexiakuebqfvitnmukebchkzmtnwcuymbnmyqgfzefnelwqnhleaadekwjehljydpuwybendymsluptckrvbplxmamohiyszwrslittmdbfmxkmqtmxfusxubatbgfvnlebmzxcsruqnjuctcjriszjpogywsitudelqljtubszxmnykadnryjzhosyorgzvpzolmpbafnvcrrzfaxoqaulbcbnrucuydqbppnpgrdoyugbpiqdafccgordlqbwcgzirbbpaftoqtujqrljdqjrtwaqskcfqjqhvlgzbdmarajevjjrphkdzturmpqomzcewxxrpglsjehpfhmwmgeotxbswzswftewfchvxpqjyzlwwkxmssxpmdrtclakalcsgpwkvntjshydpvjauqilqkeyjojgehwwlattlhlgdgpotxhlrmffspdyxmjfonkzwdjkambqnwicehfzjvrxwsrbkztmtermdjjlaxlremdxnnfavmtclhvhesujoasmqonrjzlznywprupsfdafmuhunpigohenjnmpwdxcolvwuyptjigbihzcotxqjgskupqeomwlosbxqdjxwhmifbxzptjmvnfbpswtbjlmijpprzfelgzxbigrijgxlvmurzdvhxskpczyqrdelsyuqmfdxhzodxlhtsfxapwreaqtmzdhkibnwvsfsdolvwzwwjmgysrqfihakhhbbpfhbtvknsenzyvwyzudvvwgxjavcjyweomjfkucztlevmbbxqwznytbhdaowmecfkcfmiyvcfundeflybuifpvkvezezadmauwjzyfmdkxdvsfqkdkwydqhmmxfblfhnzqanonlmj" ))

main()