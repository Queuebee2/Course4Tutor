""" our data is scuffed.
this script takes a dictionary (stored in a pickle file) of result lists
the list contains everything NCBIWWW qblast yields, along with some annotation.

since the dictionary contains multiple lists of just headers (for the csv file),
these are skipped.

prints acession codes along with all found E-values, ordered by E-value.
"""

import pickle
import collections

website_1 = "https://www.ncbi.nlm.nih.gov/nuccore/KT021004"

def main():
    with open('pickled_data_list.dat', 'rb') as picklefile:

        result_list_of_lists = pickle.load(picklefile)

        print('got',len(set([str(l) for l in result_list_of_lists])),'results')



        
        dicc = dict()
        acessions = []
        
        for result_list in result_list_of_lists:

            e_val = result_list[5]
            if type(e_val) == float:

                acession =  result_list[1].split("|")[3]
                acessions.append(acession)
                if acession == 'KT021004.1':
                    print(result_list)
                if acession not in dicc.keys():
                    dicc[acession] = [e_val]
                else:
                    dicc[acession].append(e_val)
                
            else:
                pass
            

        print(len(acessions),'acession codes')
        print(len(set(acessions)),'authentic ones')
        new = []
        for i in acessions:
            if i in new:
                print(i,'already exists')
            new.append(i)
        
        sorted_by_e_val = sorted(dicc.items(), key=lambda kv: kv[1])


        for i in sorted_by_e_val:
            print(i)

            
bigassBoy="""FEATURES             Location/Qualifiers
     source          1..60284
                     /organism="Thermobifida phage P1312"
                     /mol_type="genomic DNA"
                     /isolation_source="compost"
                     /host="Thermobifida fusca NTU22"
                     /db_xref="taxon:1661715"
                     /country="Taiwan"
                     /collection_date="01-Dec-2013"
     gene            243..980
                     /locus_tag="P1312_001"
     CDS             243..980
                     /locus_tag="P1312_001"
                     /codon_start=1
                     /transl_table=11
                     /product="head morphogenesis protein"
                     /protein_id="ALA06374.1"
                     /translation="MTTPLPEPVPDTTTPELDALETETRTLIDRHLDDARDVAATTVA
                     SPVEVTRRNSRLMDRLRQARAAIIDTAMGAVRRAVPLGARDAAREAPPPAGTEVRYVP
                     DDVDVHRATGDIDLRNDVSFIISSQGLRVEINPPGRRREEALEVVEQTLARIHNVTTT
                     GIHRAYNRGRQWYAALFAYDLKWFTRVDERTCSRCRPMHGRVIASKERFSLREPDWEG
                     FDGLPPLHFRCRCYTEVVRRRLFGGEG"
     gene            987..1475
                     /locus_tag="P1312_002"
     CDS             987..1475
                     /locus_tag="P1312_002"
                     /note="similar to WP_030728966 Streptomyces"
                     /codon_start=1
                     /transl_table=11
                     /product="hypothetical protein"
                     /protein_id="ALA06375.1"
                     /translation="MTLSHRSKHSGRYERTLASAERDAQAARLRAQHWTYQQIADELG
                     YPNRSEAYRAVQRALKAAIREPGEELLALELERLDRLARAAEEVLEAHHVKVAGGEIV
                     YDEAGQPLEDTKPVLEAIDRLLKIQERRARLLGLDAPVKQQITGKVATYRVEGVDLDA
                     LR"
     gene            1462..2805
                     /locus_tag="P1312_003"
     CDS             1462..2805
                     /locus_tag="P1312_003"
                     /codon_start=1
                     /transl_table=11
                     /product="terminase large subunit"
                     /protein_id="ALA06376.1"
                     /translation="MRSAELVHTYRPRGTAVQVMEAREDEVLVCGPAGTGKSRVCLEK
                     LHLVALLNPGMRGLIVRKTSVSLGSTTLVTWREQVIKEALATGTVHFYGGSPQEAASY
                     RYDNGSVIVVGGMDKATKIMSSEYDLVFADEATELTLNDWEAITSRLRHGRLSFQQLL
                     AACNPDAPTHWLKQRCDRGLTRLINSRHEDNPVYYNSDGTLTERGRDYIGKLDRLTGV
                     RHARLRLGLWAAAEGMVYDQFQEAVHVVDPFSIPEHWPRYLSVDFGFTNPFVAQWWAE
                     DEDGRLYLYREIYRTRRTVDQHARDILDQVTTPDGRWLEPRPAAVVCDHDAEGRAVLE
                     RELGVETTPAHKSVLDGIQAVQARLRVAEDGKPRLFFVRGALVERDPELEGARRPTCT
                     VEEIPGYIWSRSRDGREKDQPVKADDHGMDAMRYMVAHRDLAEQREVIAVAGFNW"
     gene            complement(2795..5101)
                     /locus_tag="P1312_004"
     CDS             complement(2795..5101)
                     /locus_tag="P1312_004"
                     /experiment="LC tandem mass spectrometry"
                     /codon_start=1
                     /transl_table=11
                     /product="portal protein"
                     /protein_id="ALA06377.1"
                     /translation="METTPSSSPPPPARRGDSLENLSPAAAPEQPLFVAVVGRTPSER
                     LFLARLRLGRRLPPTVETEQGDQLISVSLQLLPGLPLEASRLVQREPLGCCHLSDELL
                     AFSPRGFLGQPLAGLPHLGELSRQLLDLRNDRILALGGGLTAGLRALALGALGELGAE
                     GFQFFEQPLVFGVVGLGALFVFAHLRLVQLRFGPPIDVLAVATSGGAAVSGFSSVLAV
                     VVGVLGVGARFGFLGGLYVVALGFGLVGLCCVVGHVLPFRDAMCAFAAQKSPVNSVTT
                     IPAVSLSIRDDSSKSTVNRLTIASENQQGCGRTTMLNPTEAAEKASELYEIRNRERKR
                     LDTIRLYLQGRPELTYLPPDTPRELQALAKMARVPLMKLIVNATTQQMFVDGYQSADT
                     EAADTIWREIWQSNRWDKKQIPLHKSTAAYGVAYGAILPAADDDAPPVIRPLSARKMT
                     AAYGDDDEWPEYALEQRKDGTWWLYDDTGVYELRRLDKPVRRPGKTTIVFEQVGFTEH
                     EQDVCPVVRYLADEDLDDPVQGDVEPNMTLQDQINLCTLHLLVAQHYGAHGRKILIGK
                     MMEAVEKQLKASASTLLTITAKPEDFKVEELSQTQLDGFIAARESAARFAAAISQTPT
                     HELLGTLSNLAAASLVEVRESTARKVAERKVMIGESHEQLLGQAGTLLGIPVDPAARV
                     RWKRLIDARAVQFVELLGLLAEKLGVPEEALWQETPFSDATVAEWRAMAAEQQPTSVT
                     PVETPTLVPLTDVTDPTEDDDTTEMTTS"
     gene            4301..5080
                     /locus_tag="P1312_005"
     CDS             4301..5080
                     /locus_tag="P1312_005"
                     /note="similar to WP_040692134 Nocardiopsis lucentensis"
                     /codon_start=1
                     /transl_table=11
                     /product="hypothetical protein"
                     /protein_id="ALA06378.1"
                     /translation="MCRKGTHSIPEWEHMTDNTTETNETEPERDDVEPTEEPETGTDT
                     EHADDNSEDAAETADSSTPTSGDGEDVDWRAKAELYKAQMRKNEQRAKANYAENQRLL
                     KELETLRTQLAEGTKGKSAKTSGEPTTEGEDPIVAQIKQLSAELAEVRETSKRLAEET
                     ARAKRQQLIAEVAASKGLTLDQARRLQGETREELEADADELVALFGLNRRREPAPKPK
                     PREKKPLRGGATNDSDEERLFGGRSRREILEAVTSTGRRRR"
     gene            complement(5085..5774)
                     /locus_tag="P1312_006"
     CDS             complement(5085..5774)
                     /locus_tag="P1312_006"
                     /codon_start=1
                     /transl_table=11
                     /product="hypothetical protein"
                     /protein_id="ALA06379.1"
                     /translation="MVGQRLDAGQPRAFDHDEPAVLAEDALPQRLRGDLTLKISEGDT
                     IRRGEPGRELRRHGQPPVLHWVLSLVQQRVGVGNDVVEIAAVGGDILVDRQRVHHARE
                     LPLGSGDHGPHLVANHLAAKINDVQRPLVLGHPRTVVNVVDAEIDGHLVDLGVVKARA
                     PRLDLRLAGHGHAQRGLPTRGRRHITGGHLRHGLGQRQLSRQQVHGERRNRLTGNKRH
                     WLLPVTRGDHA"
     gene            5121..6005
                     /locus_tag="P1312_007"
     CDS             5121..6005
                     /locus_tag="P1312_007"
                     /codon_start=1
                     /transl_table=11
                     /product="capsid protein"
                     /protein_id="ALA06380.1"
                     /translation="MAFVTSESISTLAVDLLSAELSLTQTVSQVPSGDVAPPTGGETT
                     LRVPVPREAKIQPRGASLDYTEIDEVPVDFSIDHIYDGARVTEHQRSLDIVDFGRQVV
                     RNQVRAVVAGAERQLASVMNALPIDEDVTPDGSDFDNVIADANALLDEAENPMENRWL
                     AVSPQFAARLTSPDGVTLTDFQGEVATEALRQGILGEYRGFIVVKSPRLTGIKALAYH
                     SSAFAFGTLTPPMIPGTIDSAVITEEGLSVRHVFMVDPATASTLSLLSIYAGAELVDA
                     DRVVVLGVQVENPLPDGS"
     gene            6036..6461
                     /locus_tag="P1312_008"
     CDS             6036..6461
                     /locus_tag="P1312_008"
                     /codon_start=1
                     /transl_table=11
                     /product="hypothetical protein"
                     /protein_id="ALA06381.1"
                     /translation="MAESLMTVEQYEARLGRTLTGAERAQAEALLADASDVVRRIAQG
                     RLDEATSEDVPGPIRMVIFSMVTRAVRNPAGVNSERIADYQYSGARPLYPTDEEQDLI
                     RDEMDIPSVRTITLVGDMPQRLLDDAAATPYVGYYLGDD"
     gene            complement(6363..6644)
                     /locus_tag="P1312_009"
     CDS             complement(6363..6644)
                     /locus_tag="P1312_009"
                     /codon_start=1
                     /transl_table=11
                     /product="hypothetical protein"
                     /protein_id="ALA06382.1"
                     /translation="MGTHRLERRNRSNRRRRAAASCSATAFSSRDPHTLCGGAISSGV
                     AYSTTLPVMVFSNRTGKLIVSQVVADVGGGRSIIQQPLRHVPYERDRAH"
     gene            complement(6376..6954)
                     /locus_tag="P1312_010"
     CDS             complement(6376..6954)
                     /locus_tag="P1312_010"
                     /codon_start=1
                     /transl_table=11
                     /product="hypothetical protein"
                     /protein_id="ALA06383.1"
                     /translation="MGLVVGVHHIRWQTAARRNFEPLLFGPRADLRCRCLRLLHAFLN
                     WLRLLRAGSRRLARRGPFSELHLKLTLILGAQLRLNLASLPFPTLMLQLPQGLTCHWL
                     ICGHPPLRAAQPVQQAPPCGRLMLRNRLLLTRPPHLVWRGDLLRCCVLHDPAGHGVLK
                     SDRQANRLPGSSRRRGWPQHHPATVAACPLRA"
     gene            6487..6963
                     /locus_tag="P1312_011"
     CDS             6487..6963
                     /locus_tag="P1312_011"
                     /note="similar to WP_040692137 Nocardiopsis lucentensis"
                     /codon_start=1
                     /transl_table=11
                     /product="hypothetical protein"
                     /protein_id="ALA06384.1"
                     /translation="MTGRVVEYATPEEIAPPHKVWGSREEKAVAEHEAAARRRLLDRL
                     RRSKRWVPTDKPVTRKTLRQLEHERRERERRQIEAKLRAEYERQLEMELAKRSPASES
                     AATSSEQPEPVEESVKQPKASTAQIRAWAKEQGLEVPARGSLPSDVVDAYHKAHAE"
     gene            6978..7340
                     /locus_tag="P1312_012"
     CDS             6978..7340
                     /locus_tag="P1312_012"
                     /codon_start=1
                     /transl_table=11
                     /product="head-tail adaptor"
                     /protein_id="ALA06385.1"
                     /translation="MLGHLWNRTLAHYRTETVRNDMGGLDEQRIRLGVIAVRVPQPTA
                     LERVMARSQVGPQQGQAELTQPVYCDPGEDVRRGDELVDETTGEVFRVVAAIRPSVAV
                     YLRLDTEVLQAEPAGEVS"
     gene            7340..7732
                     /locus_tag="P1312_013"
     CDS             7340..7732
                     /locus_tag="P1312_013"
                     /codon_start=1
                     /transl_table=11
                     /product="tail protein"
                     /protein_id="ALA06386.1"
                     /translation="MAGRMVVEIRGVDSLRDRLRMMRSHVREGTEAAAREAGRMGEAT
                     MKGLAPVDTGRLRDSIRHEVQGPTVRFGPGDEIDYAAFVEFGTSKMAAQPYVRPTVEA
                     MRRIWPDLVAEHVNRALQQKKRGRRWWR"
     gene            complement(7696..8508)
                     /locus_tag="P1312_014"
     CDS             complement(7696..8508)
                     /locus_tag="P1312_014"
                     /experiment="LC tandem mass spectrometry"
                     /codon_start=1
                     /transl_table=11
                     /product="hypothetical protein"
                     /protein_id="ALA06388.1"
                     /translation="MQRRVIADLERDLTTVGEATHPLAETIRRLVGGDLDGVPLLFGT
                     GNVGGLTDQVKGLRAAAVSALEPGPEPRVASHFRGPPLTMCCVDVPGMADPPRPWDPG
                     RALPPVISRRRLNPHLRGRGKLFSVESKADRDVSDQRVRVTHRPRIHQPDGPQPVTLQ
                     FDVVLPVVKQRGELGCDLQSLSEPSTALGPHVQGVHHATPKPAVHVIRSLGSLPHCHK
                     RVRLVLRHVVPHRHRQILVAPLHHGLLHSSERRGRGRGNPGHRHHLRPRFFC"
     gene            7720..8157
                     /locus_tag="P1312_015"
     CDS             7720..8157
                     /locus_tag="P1312_015"
                     /note="similar to WP_026128262 of Nocardiopsis
                     lucentensis"
                     /codon_start=1
                     /transl_table=11
                     /product="tail protein"
                     /protein_id="ALA06387.1"
                     /translation="MVAVTRITPTAATALAAVQKAVVQRCNEYLSVPVWDYVPEDQPH
                     PFVTVGEATETADNVHGRFGRRVVHTLHVWTKGRGGFAEALQIAAELTTLFDHRENDI
                     ELEGHRLWSVRLVDARPMRDPDPLIRHIPISFAFHTEQLPPPS"
     gene            8703..9098
                     /locus_tag="P1312_017"
     CDS             8703..9098
                     /locus_tag="P1312_017"
                     /note="similar to WP_040692145 of Nocardiopsis
                     lucentensis"
                     /codon_start=1
                     /transl_table=11
                     /product="hypothetical protein"
                     /protein_id="ALA06389.1"
                     /translation="MALLGRDQILGASDFETRDVECPEWGGTVRVRPLTAVQRSLIES
                     TMLEANQTKRFDKVGKVAIQCVAWCVVDEQGERVFTEADVKALGEKSSAPILRLRDAI
                     FELSGMSKGAVEEEVEDFTETPTGSSSSV"
     gene            9119..9406
                     /locus_tag="P1312_018"
     CDS             9119..9406
                     /locus_tag="P1312_018"
                     /codon_start=1
                     /transl_table=11
                     /product="tail protein"
                     /protein_id="ALA06390.1"
                     /translation="MHEMLERMPARELTAWAAYEQVAGPLGQPRDDILVGILAERITS
                     MLQSGKKRRRWRVDDFVPKWGRRKRTAQTPQEQRNLLLELTRRFGGTIRKR"
     gene            9418..14391
                     /locus_tag="P1312_020"
     CDS             9418..14391
                     /locus_tag="P1312_020"
                     /codon_start=1
                     /transl_table=11
                     /product="tail tape measure protein"
                     /protein_id="ALA06391.1"
                     /translation="MATLEELTVVLDADTRPWMRELDRATRATQREFTRFAEVASRSG
                     RRGGTSFITGFAEQAARTQRVVQRSVERPLQEAQRVAVASGGRAGSSFVSGFTRPVQT
                     MTLKVSQALDPTMTATVKRLGEGGVQAGQKWVDEVGRTVRDARPRFAAAAAQAGAGFS
                     SGLQQAAQSASRPLSAQLGDAGRRGGQGFTSGLSGGLAGVAGAFAPVAAAAVGMSSVV
                     GGAVLRVAGDFDHAMAAVRAVTGATGEEFARLESLAKEMGATTMFSATEAAQAMEFLG
                     MAGWDTTQIMAGLPDVLNLAAAGGLGLAEAADIASNIMAGMSMEASEVGRAADALATA
                     AANANVDVRMLGETASYAAGTAASAGWSIEQLALATGLFGNVGIQGSMAGTALNHILN
                     QLQNSSSKAADLFAQLGIEIRDSSGAVRDFDELLIDLMDSEVTSTQLIEAFGQEHGPK
                     LVSVLQQGEGAVRKLAEAMDNTSGEADRMASIRMDSFVGALDQAKSAAEGFFIAIADL
                     GILDTARGIVDAFSAAVSAATTWLEKHADTIRPVIRFVSLLVASIAAVVGVFLAAKAA
                     IAGVGAVFAVVTSPIGLVIGAIGLLIAGLVKLWQKSETFRDIVTAVWDYIADAVGAVV
                     DWFKDTVWPVLVEGWEEIKKAAGPHIKRIVAWLKTLRDGADSLGERWGWLWDAITAPI
                     RTARTIITTWASNVVQAFKGWVDVIAGLLEGDWERAWEGAKEVLAAVWDTMVEVAKAG
                     LKLLWTSLKTWFLELPRAIGEWLVEVAPVIWDKATNEWIPAFVDWVVEMGRKFTSKLG
                     EWLDDFSTWLTEDVPDEIEKNLPEWTAEFVKWAGGLWGEVRRKLTEFATRFGRWIVSQ
                     AQALPGRLSTWSEKVRQWAGGLWGRVKGKINEFGTRFAGWAEEFAESLPARLQGWTNR
                     IVEWIEGFAESLPGHLEKWTDRFVRWIEEFAESLPERLETLTQKFVDWATGAPEETAT
                     AFEDADGPGKIEEQIENDWAPRLIAAFGRALLNLALEIPGMVVKIGWALLSSFGRILL
                     DLALMAAEKFRHLLGVAARLWEQIKQKIIEKASELVDGVKDKINELYDNTVGRVTDLY
                     NEVVGNSIWPDMVDAIIGETGRLSKGVGDKFSGMGRGTTGETSSMAQTVTRQVQQLRA
                     AVVAAVAAMQASVARLIGLLARGFTSAFAQLGAQALRSFRGMAAGLVAETSNLVRVLN
                     RAFSQFGSNTVRGFTNTVRGVASAWAKLRQAAAAPVRYVISPVYNKGLRPVWNRVAAR
                     VSGLSPMSAMSVPSGLAEGGVVPGYQPSKRDDLIMGMRSGEGVLVPEVVKGLGAGFID
                     FWNRIGNRGGVSAVRRVSQETNKAGLGQAPMEGLSKYAGSVPGLARGGIVGRAQQFTS
                     TSWRHIEGRIEAKAKPALDEMHTGLGKLFGRGDTFNGIAHAAMGTIKPRVLAAFRRAD
                     EAFRALMGGGLDSWGDLATASERIRRTARFLTAQRGKPYIWGGVGPGGYDCSGLTSAA
                     ENVFRGLYPYRRRHTTHSFLGAPPPGWVRGLRAPLSVGVTHAGVGHMAGTLAGVNFES
                     RGSRGVVLGRAARGTRSFPHQFGFAPSLGDALPAKSYDQGGWLMPGYTLAYNGTGRPE
                     PVNAEPIRIILDIEGGDDELRRRIRRMVRIEGGGDVQVAFGSGRGRR"
     gene            14388..16361
                     /locus_tag="P1312_021"
     CDS             14388..16361
                     /locus_tag="P1312_021"
                     /codon_start=1
                     /transl_table=11
                     /product="tail protein"
                     /protein_id="ALA06392.1"
                     /translation="MITLVGATSAGGFTGTVTVNLPAGVQDGDRMFMLASANDFPTIT
                     ARPPGWAVMTEDIIGTDVATYVWTRVADGEPASYTVTWEGSHWHFLNLVVFRGVDSVR
                     SYAVNSTDSAATIDLPVLDAQPGDVLLAYGFHWGEVDKTWTPAGLTTITNLSRAIISA
                     YQVQAGGPTPAYTLVTDTVGHMAATAILLTPKTVPTTQPRFPLTIRTELKLGGEWVDI
                     SGDVRDTDPVTISRGRADESATADASTCRLLLNNRHGKYSPRNPNSPYYGMLGRNIPL
                     RVAVMVGDTRIGRFAGEVSEWPLRWDLSGNDVWLPIEASGPLRRLSQGHGPARSALRR

                     FIVARNPVAYWPLTDGASALVASPDVGLYDMGIVVDAPPGTLGVTQSRLDWREGQLAP
                     WLEDVARTRRAVGRIAGQVESSSADWALDMVRAGVGGVDRLVAVARRGDTGPSQEWQV
                     RFDAGALDIRVFVRTVLDDASPSAWTQVSTALVEPRFFTDQLRHVRLEVRDAGVESDW
                     WLYIDGELMDTGTTNGLGRPLPVVSAQYWWDHSSVQDAEHVALGHITVWDASEEAAYP
                     NPLEMVQAMYGHRGERAGVRIHRIAREEGIPLEVVGDLEATPPMGPQYAETPLEVMRE
                     AERVDDGMLYESRDEVALVYRTNRSRYNQELSG"
     gene            16358..19648
                     /locus_tag="P1312_022"
     CDS             16358..19648
                     /locus_tag="P1312_022"
                     /codon_start=1
                     /transl_table=11
                     /product="phosphodiesterase"
                     /protein_id="ALA06393.1"
                     /translation="MSVEWVWAGAGTETSVWVRGKVTGSSTRLVVSEAEDLSNPVFFG
                     PVSPTSEGVVSIEATGLEPDTRYWYALEDDSVIDTAFMGTFRTHPPAGEPASFIVGAA
                     GDAGLTGTGDDSHITNAVSNHPVFDVMRARALAEDWLQFIHLGDLHYRDISINDPDAY
                     RQAYHDVLTFNGTLGADARQGRFYRAVPISYVWDDHDYGPNNSDRTHVGRAAAATVYR
                     EIVPHYPLPAGSGDAPIYQSWQIGRVLFVASDVRWARDPNLLPDNDPSTPKTMLGEQQ
                     KRWLERILRNSSAQALVWVMPSQWLSDQGDVRNVGISYSGADYSNDSWWRFRGERAEL
                     VDLLGDLGWLDRMVMLQADKHALSMSSGPNNPWGGFPLFMFASLDASYSEHPEGQYDI
                     GQSPGRGRYGTLRVVDSGHTIALHGTGYIGDTVWRSYTAYAHVEPRVLALDYARGQTF
                     DPLEPTDDDQNLVNDFTAQRTDGSEIRYEKTDGPLSVQEPPQGVGRYSGSGEFNVHSN
                     DDLPSIAGWQVHKGTVDEARIPNLHINLTNPRMEELRTSVAGVEPGDKITIANPPAWL
                     PPEPIEVIAEGYEEELSTHEWHIEYNASPARIVEVATVAPQVVLNRNHSMEVTPYGWQ
                     RPGGASLWISRDYAYQGEFSLKLVPDGTTETTRIIARPEDAPRVYAGVEYEFSAWVLS
                     PTGYAMDLSVQWLDVNNTQIAFVIVVTSTPIPAGVWTRLVGRAVAPEGAYRARPSINQ
                     RNTPSSSDVMYVDEVIFSEVGVSPGADAPNRADTSGSILQVPVDESDTEFIVATVQDE
                     HSGARWINSRGLTETHAYEFPFNLRLGGEVVQVTACEPAGWDDFRSPRPSDSWGTSPS
                     GHAWVDTTVPDTRLGTSTRDLYGFVQLLDNPQTVRLQTLDVGFPVQDCEILWTVRVDA
                     TASGTALLPSLVLRYQSATNYYRCRLHLNTDGTCSLSVARGTTQIGAAVNLPMLTYTG
                     STAFEDRIWVRTRLIGNRVLARAWKQVDLTGEGGLDAGLDLRYQEPQHWQIDREITTD
                     PIPAGQVGFAASAFTGNTNTSPELRFQLVEIVTPQRITVVRSVNGVVKSHEAGTRVGL
                     NRPAIIGL"
     gene            19670..20212
                     /locus_tag="P1312_023"
     CDS             19670..20212
                     /locus_tag="P1312_023"
                     /note="similar to WP_040692409 Nocardiopsis lucentensis"
                     /codon_start=1
                     /transl_table=11
                     /product="hypothetical protein"
                     /protein_id="ALA06394.1"
                     /translation="MPFPQWFAGQTITADRLNAARMKMVAQSENQEVVNSTALVPTEI
                     IIPLESGATYWYQLVLTYTASNTGGGMGGGGIRWAWDVPTGTSMPRQTASYALVDNQA
                     ISLIAGGRILLRSPAATTEMRAEGSGPDNFHAALEYGSIQVGGLSGEAVLQFAQWNAH
                     STPTTLRGATRTRVFYTRVQ"
     gene            20237..20497
                     /locus_tag="P1312_024"
     CDS             20237..20497
                     /locus_tag="P1312_024"
                     /codon_start=1
                     /transl_table=11
                     /product="hypothetical protein"
                     /protein_id="ALA06395.1"
                     /translation="MAVPEGAYRVRYNVSTVDDAPWLTWIFESDLPGGAAKQVVDEAL
                     QMAAEHVINWLNAEYPSARVVASRMYTGRLEGDPWPQDEEGE"
     gene            20494..21270
                     /locus_tag="P1312_025"
     CDS             20494..21270
                     /locus_tag="P1312_025"
                     /codon_start=1
                     /transl_table=11
                     /product="O-methyltransferase"
                     /protein_id="ALA06396.1"
                     /translation="MSTVINAGLVTRWWPRRLRHPGLVELAVCQRLRALAAQVPADEA
                     IVELGAYQGRTTGWLLLGASEGQGAHVTTVDPWTLYKPRQDTPEELSVLYGRAETYAV
                     FKQHMDAIGATPDRLTVKRGYAHTIGRKWVGGPVGLLWHDAEHSADAVARDLEAWLPH
                     LSEGAVVVLHDAGNPEYGVVEGALRVLGDGWQFEDEDGHLHDEPQVIRWRKNPQRRGM
                     LVARRCLVEETSPQEEAVEEPSGVVGDVEDGGLPRVEESA"
     gene            21428..22423
                     /locus_tag="P1312_027"
     CDS             21428..22423
                     /locus_tag="P1312_027"
                     /codon_start=1
                     /transl_table=11
                     /product="glycosyl/glycerophosphate transferase"
                     /protein_id="ALA06397.1"
                     /translation="MIRFCMNSTSWDEARDEMIVGGQLYRYFQPVWDALAEMGVPYTV
                     GRQPEMGAVNVYPNTRPTYVHGSYRRDRVSVGVSHGLADKGYRQGYRFHHHVLLPGPA
                     FAEVLLRDGFPLRKLHVAGYPKLDPLFRGEVDGAGFWSGDGRIKVLYAPTHGGGSERW
                     RNGNPDAPGARATSWWHRDQVAGLLDEEKFEVVLAPHPRHSPGHQATFAQYVDADVVI
                     ADGGSTIYEAWCLGKPVVLPAWLTRRRNETRDQGRNLEARVYKEGLGYQADEPEQLAG
                     LVERAAGEGMRQSEIEFAAQVIPPELRGRGGCEWARFLAELEEGHLSKRWRYQVA"
     gene            22494..23063
                     /locus_tag="P1312_028"
     CDS             22494..23063
                     /locus_tag="P1312_028"
                     /note="similar to WP_045936534 Streptomyces sp. NRRL
                     S-104"
                     /codon_start=1
                     /transl_table=11
                     /product="hypothetical protein"
                     /protein_id="ALA06398.1"
                     /translation="MEDLMHPPYQQPPHSSPVRQQGMSAGAKVALAGCGGCGALIGLV
                     LMAGCVAAIVAPADPAPPAAESSASGSASPEESVSPSPEPSETPEDEVSFEELGFPPA
                     LEGEERAAYLADVRDLDRGFVFPDEDSVVARGQDVCVTLRDEGEQAAIDYIEAIWLHE
                     DYDFGRRPTTREEAEQLLGIVHEHVCPDW"
     gene            complement(23068..23346)
                     /locus_tag="P1312_029"
     CDS             complement(23068..23346)
                     /locus_tag="P1312_029"
                     /note="similar to WP_017602347 Nocardiopsis lucentensis"
                     /codon_start=1
                     /transl_table=11
                     /product="hypothetical protein"
                     /protein_id="ALA06399.1"
                     /translation="MGNSLERLLRARHLVDHADPRIDHALTRMRTRPASPDEAYWQAA
                     LRVAKQDERRELARRHPVAYTIGYMLGCLTLLAAPALLGAAITWWILT"
     gene            23167..23517
                     /locus_tag="P1312_030"
     CDS             23167..23517
                     /locus_tag="P1312_030"
                     /codon_start=1
                     /transl_table=11
                     /product="hypothetical protein"
                     /protein_id="ALA06400.1"
                     /translation="MSPGEFAALVLLGDAEGGLPVRLVGRRGAGAHAGERVVDAWVGV
                     VDEVSGAQEAFQAVPHDNRVGPAPPGAGPLRSGGDLITGRVRVRRGRTGRTPPGPSRR
                     RRGRPTSSGRVGCR"
     gene            complement(23530..23850)
                     /locus_tag="P1312_032"
     CDS             complement(23530..23850)
                     /locus_tag="P1312_032"
                     /codon_start=1
                     /transl_table=11
                     /product="hypothetical protein"
                     /protein_id="ALA06401.1"
                     /translation="MPHQIPADATPVRTRTKRTIGYVAPVPVPAGEDPWTGELIPPTV
                     RYAAWLADGTPAGGWDSYRYTVITYGHDRYATEAQAKNAVRRIHQRRTEYAAYSRNHH
                     TEVQ"
     gene            23822..24076
                     /locus_tag="P1312_033"
     CDS             23822..24076
                     /locus_tag="P1312_033"
                     /codon_start=1
                     /transl_table=11
                     /product="hypothetical protein"
                     /protein_id="ALA06402.1"
                     /translation="MASAGIWWGMVSPFRGLGAWGEEDGHTRVGVAVVVGVVVGVFAV
                     PPVVGVGVEVGVLPVVQEVIVHGGPFCVPFCGVWLAGEVG"
     gene            24099..24554
                     /locus_tag="P1312_035"
     CDS             24099..24554
                     /locus_tag="P1312_035"
                     /codon_start=1
                     /transl_table=11
                     /product="hypothetical protein"
                     /protein_id="ALA06403.1"
                     /translation="MASFVFGWGLGGEAERDRGADQLVGGRLVGGLDDLDGDAVVADV
                     AAGQAGGAGAAGAGGLVDLAVGADGVVDAGAGGGDYAAVLDELGGFGDLVGLVLGGDL
                     AGGGADLGVAGGAVAGAQCAGRAQRAVAAGAAGGGLGGVVHGPPPTLSP"
     gene            complement(24126..24608)
                     /locus_tag="P1312_036"
     CDS             complement(24126..24608)
                     /locus_tag="P1312_036"
                     /note="similar to WP_031096358 Streptomyces"
                     /codon_start=1
                     /transl_table=11
                     /product="hypothetical protein"
                     /protein_id="ALA06404.1"
                     /translation="MTQLYVDKVLSFWLTLSTSRRQGWRRAMNNTTKTTARCARCNRP
                     LRSARALRTGYGPACYTKVRAAAREVAAQHKPHQVAKATELIEDSGVVPTTRTGVYYT
                     VGTNGEIYKTARTGCTCPAGLTGRYVCYHRIAVEIVEATYQPAAYQLIRTPIALGLAA
                     "
     gene            24655..24882
                     /locus_tag="P1312_038"
     CDS             24655..24882
                     /locus_tag="P1312_038"
                     /codon_start=1
                     /transl_table=11
                     /product="transcriptional regulator"
                     /protein_id="ALA06405.1"
                     /translation="MPDPNADYWTLRDIADHWGVSYHTVRTYRARGRGELPEPDAVFG
                     RSPAWRPATIIRFQRPGQGARTDLRKNTTSE"
     gene            25042..25404
                     /locus_tag="P1312_039"
     CDS             25042..25404
                     /locus_tag="P1312_039"
                     /note="involved in exopolysaccharide biosynthesis"
                     /codon_start=1
                     /transl_table=11
                     /product="hypothetical protein"
                     /protein_id="ALA06406.1"
                     /translation="MLRPGGSMTNQELQQQYEAVRQVWEQILDRYREAFRKVSEAFRP
                     LVEWAQTPEGQAALAEVGRRFSLPTCRCLCQVAHAHREDGQGLCVGEATTRVVFPAPW
                     GWQPVPMCAPCTEATCAV"
     gene            25530..25973
                     /locus_tag="P1312_040"
     CDS             25530..25973
                     /locus_tag="P1312_040"
                     /codon_start=1
                     /transl_table=11
                     /product="sensory protein kinase CreC"
                     /protein_id="ALA06407.1"
                     /translation="MYKRDMPHRGESPKWILERPMHPPDATALGLWIVGASAVAAALV
                     TLWRALRALFRVARKIGHFFDDWFGEAPRPGVPGRPGFPERLGKVETAVKGLREEIGE
                     VKEQVAEIVHELHPNAGGSLRDAVNRIEARTINLPRPAPRRDGDG"
     gene            25970..26845
                     /locus_tag="P1312_041"
     CDS             25970..26845
                     /locus_tag="P1312_041"
                     /codon_start=1
                     /transl_table=11
                     /product="N-acetylmuramoyl-L-alanine amidase"
                     /protein_id="ALA06408.1"
                     /translation="MMPRPDRYVSRSDLGWGRSPAASANPKLGLVIHYDGSNQNLAAK
                     THAACISYWKNTRAFHTGPARGWVDIGYSWGVCPHSYVFEGRGLYKTQAAQPGGNTTY
                     YSVTLMCGPTDTITDVQINAVRQLRAWLMETAGVAGTVKGHRDFVSTSCPGDALYRMV
                     RDGVFSKPATWGGTSSSWEELMLGLKKGDRGEAVEALQELIRLAGHGAALGPAGVDGV
                     YGDGTAEGLRLCRADVGSRALPGYGDKVTGHAFAQLIAAVAKHQATKVSGGSTGGVPR
                     HLEVESLTAKRLTVG"
     gene            27063..27344
                     /locus_tag="P1312_042"
     CDS             27063..27344
                     /locus_tag="P1312_042"
                     /note="Similar to Thermobifida fusca Tfu_2915"
                     /codon_start=1
                     /transl_table=11
                     /product="hypothetical protein"
                     /protein_id="ALA06409.1"
                     /translation="MTTTEPAQNETVPDIGASIIRTLVPLLVGALVALGSRYLAVDLP
                     VDALEEVVTVVVAGVYYAVARVLEEWVSPVWGRVLLGLGIGGTPRYTQH"
     gene            complement(27490..28350)
                     /locus_tag="P1312_044"
     CDS             complement(27490..28350)
                     /locus_tag="P1312_044"
                     /note="helix-turn-helix family protein; similar to
                     WP_018223844 of Salinispora pacifica"
                     /codon_start=1
                     /transl_table=11
                     /product="transcriptional regulator"
                     /protein_id="ALA06410.1"
                     /translation="MKEKTMLTAAEFKTLREYLGIPGEWIARRFGVSDRSVRHWDSGK
                     YPAPERISRWLRWLAEDTEATVAWIAERLENSPERLLVTYRNDAELYACAADDPYRGL
                     YPDDDLPAAWHRRMAARVAGRVPGLRLVYPGQTAADIPAAVSSLLDVTADCDDRADPE
                     AWIEAWGSVAASHGFETERAGEEAYNGAPVLEDAEGELYVLSWWEGRVYASRITTWVR
                     EAEEGLEAVELRDNGREVWVYAYASSSSGSMSLVDARVVVGSEATPGEREERVRDYVR
                     GLEAGGYERG"
     gene            complement(28406..28819)
                     /locus_tag="P1312_045"
     CDS             complement(28406..28819)
                     /locus_tag="P1312_045"
                     /codon_start=1
                     /transl_table=11
                     /product="hypothetical protein"
                     /protein_id="ALA06411.1"
                     /translation="MVVLVGERPQTPAPGNSPRARPEGPAMRTTANEAYGLGLIDETD
                     YTVSVALTDDVADNGRSTVEVLRREQIGEVDGEAVYALGGKITGWTIPVPTDADDVID
                     QALTAAEDVLDEHGWKPAGPWEIADSNAHAPVTRG"
     gene            complement(28905..29336)
                     /locus_tag="P1312_046"
     CDS             complement(28905..29336)
                     /locus_tag="P1312_046"
                     /codon_start=1
                     /transl_table=11
                     /product="hypothetical protein"
                     /protein_id="ALA06412.1"
                     /translation="MTPSQSFAWSAEAGLTATEHVCTRKVRLSSVGGMAADDPQQMRE
                     RLDRIRCSFYQWRISYELHRPEGGRWVAWRIDPLEEWEAEAGLTCVVSAWDHDTFLAR
                     LGAEQRRQDELRVRRRQEEEEGKSRSPLSPMRRRGEGSRGG"
     gene            complement(29333..30751)
                     /locus_tag="P1312_047"
     CDS             complement(29333..30751)
                     /locus_tag="P1312_047"
                     /note="similar to ADJ28745 Nitrosococcus watsonii C-113"
                     /codon_start=1
                     /transl_table=11
                     /product="hypothetical protein"
                     /protein_id="ALA06413.1"
                     /translation="MRPQRPHHPNRTVKPPTIVVGGFLLGGLLTSSPRLKPGDSNPRG
                     LGFLLHRQPPAGLTPFGSYAGSTGVLPLRQPGGEDIACGVHVAVMGRAAGALPGTDVQ
                     RHLLLQGAARRAQLGGREPAVHDQQFPVIPGALVLQHRAEFPPARVRDGAGQGVVAEH
                     VADGQVLDHDRLVLTDEPSGQLVQEVAAAIGDPGVDAGDLQSGLFAVFRALLLAGQGS
                     LRLGELAPVAAFVPGVGDLLPGGEGHQSADTSVHPYRGLHRGKRADLLLHEDGHEPPP
                     GRVPAHGDRGRLRTLRKGPRPHDAQRLAHLRQEQPPVLPAERAAGVFGRRPGLLLALE
                     RGVLGPLGEEVRERRLKVPQCLLERNRRHLVQEREFGGSLPLGERGRGLHVGDPAALL
                     GVGAGPLLQRLVVDEADAAERPKQFFGLLEGRVEAVLVRPLHKLRHVSHFTRRSVKND
                     LRWEDGASSPGLKPGVSAPELR"
     gene            29438..30544
                     /locus_tag="P1312_049"
     CDS             29438..30544
                     /locus_tag="P1312_049"
                     /experiment="LC tandem mass spectrometry"
                     /note="IS605 orfB"
                     /codon_start=1
                     /transl_table=11
                     /product="transposase"
                     /protein_id="ALA06414.1"
                     /translation="MAQLVKRAYKYRFYPTLEQAEELLRTFGCVRFVYNKALEERTRA
                     YTQEGRRVSYVETSAALTQWKRTPELAFLNEVSSVPLQQALRHLQAAFANFFAKRAKY
                     PTFKSKKKSRASAEYTRSAFRWKDGRLFLAKMREPLRIVWSRPLPEGAQPSTVTVSRD
                     AAGRWFVSILVEEKIRPLPPVESSVGVDAGISALVTLSTGEKITNPGHERRDRRKLAK
                     AQRALARKQKGSKNREKARLKVARIYARITDRRRDFLHKLTTRLVRENQTVVIEDLTV
                     RNMLRNHSLARAISDASWREFRSMLEYKCAWYDRELLVVDRWFPSSKLCSACGTLQEK
                     MPLNVRTWQCACGAAHDRDVNAARNILAAGLAER"
     gene            30724..31998
                     /locus_tag="P1312_050"
     CDS             30724..31998
                     /locus_tag="P1312_050"
                     /experiment="LC tandem mass spectrometry"
                     /codon_start=1
                     /transl_table=11
                     /product="hypothetical protein"
                     /protein_id="ALA06415.1"
                     /translation="MGGAAAGAAPFYSTSGPRLGGLFPAGATALTACDRRGDIVHGDF
                     PISAARAAGRGVVLDIRLVGGLQPLQGRKCGPGLRPELGGDELHLFQCGELPHPIPER
                     VHAASANLGGDLQQLQPGAAVLVFGDRGFRDPDDRVSGRGTRGRRRHSRESAGPHGAA
                     VDPLHVSGDDQVRPVGALRHGARDDVNRVRLRGRENTVGVSQLLHDQGDSVDIPGRGG
                     RGGDARRGLFRLDHDLVTVRSDERDGVRREVNKSHGVLSCCVVGVLGVVDQVVRLVEF
                     LGELGGKDVVQFAAVGVVQQGGGVGEDRRAAGLGGGLGEDFDLAVDIDGEDGQVGELG
                     FGELTDVRGGDEVHDPVPSGRALGLFPGAGVWGRSPDLVTPSLASGSGSVKWGLENFL
                     PTLHRCPPVRLQTRSTTANPDRTGPSTHAALW"
     gene            complement(30778..31767)
                     /locus_tag="P1312_051"
     CDS             complement(30778..31767)
                     /locus_tag="P1312_051"
                     /experiment="LC tandem mass spectrometry"
                     /note="similar to WP_037974524 Synergistes jonesii"
                     /codon_start=1
                     /transl_table=11
                     /product="hypothetical protein"
                     /protein_id="ALA06416.1"
                     /translation="MNFVTPAHVRQLAEAEFSDLPVLAIDVDGEIEVFPQSTAEARGA
                     TILTDAAALLDYTDGGELDDVLAAQFAQELNQAHDLVDDTEDTDDTTGENPMRLVNLT
                     PHPVTLVTANGDEVVIQPEETPARIPTTTTPAGDVNGIPLVVEQLGDANSVLPTPQPD
                     TVYIVARPVAERANRPDLVVPTNVERVNGRPVRARALARVAASSPRATAADAIIRVAE
                     TAVTEDKDRRTGLELLEVAAEVRRGSVNAFRDGVRQLTALEQMQFISAQLRAETRAAL
                     AALQGLESAYKADVQNNPPSCRPCGGYGEIPVDDVTSPIACGECGGTGREQAA"
     gene            complement(31952..33166)
                     /locus_tag="P1312_052"
     CDS             complement(31952..33166)
                     /locus_tag="P1312_052"
                     /note="Helix-turn-helix XRE-family like proteins"
                     /codon_start=1
                     /transl_table=11
                     /product="transcriptional regulator"
                     /protein_id="ALA06417.1"
                     /translation="MQHIGDRIREYRMLHGFTQEGLAEKAGMHPNTIKKLEQGGTARM
                     DTLHRIARALNTTTGSLISSRPRLLEHGDDGKLDLLDLRRTISPPITVDGDPLCDDTE
                     PPDLPALKDALVRLDAAYHGDRYTDLAEILPGLIRSAHTAVAHHTHTPREAEARRLRS
                     VALQIAARYLTQVRAYDLAHLALADATRDAAASDDEMVSVSCVVGQAWVLIRQGRFDE
                     AERLAALTADRVEPRLSTATVDHLSSWGYLLLRVSAAAARNNRPDVSAEALGLARVAA
                     ARIGRDRYHELRSWGAFGPLTVELRSIEAELVADRPDRVLEMAGRLPLESRLTSSDSW
                     HRHRLDVAEAYARMRRDSEAIRVLAELRREAPTWLRHQRMARETLERVVRRRKRALTT
                     EQRVLMGLFGRG"
     gene            complement(33456..34868)
                     /locus_tag="P1312_053"
     CDS             complement(33456..34868)
                     /locus_tag="P1312_053"
                     /codon_start=1
                     /transl_table=11
                     /product="replicative DNA helicase"
                     /protein_id="ALA06418.1"
                     /translation="MLPPHSTERNTTIMTLTPIAPARTEPPHDLAAEQAVLGAILTAP
                     DRRRAHELLGEVLELAPPATWYRPAHALLLDHLTALADADQPLDAITLHDRLAKTGDH
                     TRTGGAPYLHTLVEQAAVGATVGHYARIIAEKAVLRRLIQAGARIAQFGQQATPGADV
                     DDLVERARDEVDSIVRTGSAHDPEVTTLADGLAGFLDRLERGDAVGDVVPVPYADLAD
                     KLVGGGFAPGQLVVIAGRPGHGKTTVALDIMRHAAKRGKRVLFHSLEMTRDELDIKLA
                     AAETGIATTQLTPGPNGADLTDDQWRRLADYVGRAADMDITIDEAADCSLARIKARVN
                     AMERQGRLPHLVVVDYIQLMDTEPAERRDLRIAALSRGLKILAKTKKIVVVALAQARR
                     ESADRENGVPRLSDLAESSALEKDPNIVLTVATPHVDDLEHERSGETIINVAKNRGGP
                     LGEVSLACQFHYSRCANLHR"
     gene            34798..35892
                     /locus_tag="P1312_054"
     CDS             34798..35892
                     /locus_tag="P1312_054"
                     /codon_start=1
                     /transl_table=11
                     /product="hypothetical protein"
                     /protein_id="ALA06419.1"
                     /translation="MRAGAMGVSVIMVVFLSVEWGGSTCLAAGCRPFFVSRVLGVAGA
                     EVSEVGPLIGAYAFELGEKRLNVAGCRGDGAHAAGEGFAAVDAAAWALAGGLCADVGE
                     VVPEGVGVAAVEPLVDAGDRGAALGGLVADVGDDGAGFVLGGGMVGEAVEDDADGAGF
                     RGFRTLGARRALSLVNHGARGAPLLVRRTPLLTLGVVLLFLLAAPRSRRRRSFRARGK
                     KRKTFVLFDLRIVPPRFSGVRTPGFWGTYPAFPGYGATCGFPGLSGARLLLPLPPLVD
                     RRAHLLGCPAHGLRVAGDLLERGQEVSEPVRLRSAGRRVEPDGVGVPRLHAADGGGAF
                     ADDVGLDEFVEVGGDGFALGEAEDDGEQVE"
     gene            complement(34912..36066)
                     /locus_tag="P1312_055"
     CDS             complement(34912..36066)
                     /locus_tag="P1312_055"
                     /note="similar to WP_037974524 Synergistes jonesii"
                     /codon_start=1
                     /transl_table=11
                     /product="hypothetical protein"
                     /protein_id="ALA06420.1"
                     /translation="MSTDVIELEALDQPTFTQVGHWLIFRHDISPTARHLYTVLAAFV
                     HQGRRNTGDTEVWPSLNLLAVILGLSKGESVTPYLDELIQADVIRKRSTTIGGMKARN
                     TYAIRFNPPPGTPEANGLGDLLAPLKEIASDPKAMSRAAKEVRATINERREREKQARA
                     GQSGKTAGRAVPRKSGVRTPESRGTYPRKPGWNNTKVEQDEGLPLLPARAEAAAPPRP
                     RRSEEEEKNNTKGQKGCSSDQQRCTTCTMVDQRKCTTCTKGAETPETRAIRVVLDRLA
                     DHSPTEDEARAVITHIRNQATQRGTTIARIDKWLDGRDPDTLRHDLAHIRAQTTRQGP
                     GCGIHRRKTLPCRMCAIAAATGDVEPLLAELKRVGPDERPDLADLCAGHS"
     gene            complement(36525..37130)
                     /locus_tag="P1312_056"
     CDS             complement(36525..37130)
                     /locus_tag="P1312_056"
                     /note="similar to WP_040271854 Streptomonospora alba"
                     /codon_start=1
                     /transl_table=11
                     /product="hypothetical protein"
                     /protein_id="ALA06421.1"
                     /translation="MRIEKIVNCTGMPLLIPQGAGDEHGYVEYPAAQVPARVLTEEVT
                     VAGLDVRIVRDLGVEGLPDPQEGVYYLVTSRVALAAPDRTDLLVPSDVYEWGDGRQVV
                     GALLRPEPTPRGWGRGLPDLSEVVVTLGNHGAPWMTQVIAERARDGEEWSVYTDNSAV
                     NSVLGRHRGLPLGEALAKLGEMMQVAQQQGRVFEEKHKNLL"
     gene            complement(37840..38460)
                     /locus_tag="P1312_060"
     CDS             complement(37840..38460)
                     /locus_tag="P1312_060"
                     /note="similar to WP_017541564 Nocardiopsis halophila"
                     /codon_start=1
                     /transl_table=11
                     /product="hypothetical protein"
                     /protein_id="ALA06422.1"
                     /translation="MTTITAADAAARAGRTVDTIRHWCRMGAVRATKRAGRWAIDVAS
                     LDYRISLDTQEPTMPTLVCEHTTDPDNPCRDCQRKFRPIMFKRYVAALTEGLELPPLT
                     GTPKQIAWAEQLRARSLAGNWEDVERGLTDEGRVLNVVWEAGWWAPEPDEEEFGIEYP
                     NWQQKLIPHEELARLRTLAEARAWIARVVAERTDAAWWIDPYRYGY"
     gene            38523..40232
                     /locus_tag="P1312_061"
     CDS             38523..40232
                     /locus_tag="P1312_061"
                     /codon_start=1
                     /transl_table=11
                     /product="hypothetical protein"
                     /protein_id="ALA06423.1"
                     /translation="MVGRNPPARRLHRTQTPRHLPHIIRPRTRKKSRNLTSNGTHNPP
                     KRNQKKRGRSTSFPPFHGHDLAATPMLTLLQHQVQQHTSHPQHHDRQHADKHHDPLRR
                     NRAALRIQHVIGSLTERTQGQREPSTAPSKPTAPASHQTSHRHIQRGSRIRLNPDGQG
                     DRQVNRGPPTIGNETRQQVHLAEPNHAPQSDPSAPHGGERRQADREDRDDEPPRLAVR
                     SVAGPRVRIPGPLRLDYRTGFTQPRPDRFTGGLHWTGLVHLVSDYPTGPVHQTSRLTR
                     TGPVHQTSRLTRTTRPVHHTRRGPRTGPVRYTRPGSRPDQTTRLSPSLDPVHRTSIRS
                     AHAGLRHHTGPVHHAIHLGLVCRTTSPPLNPGIRLAPVQRRDQPFYPDQSSLGCLDTD
                     SIILVRTGGLLTPSRPVRPDCSTRPDHRTRLVCSTRPDHRTRRGGRPDRLRPGLLDRS
                     TRLDCLTGPPQTRRGRPVHPVSLPGRSTRLLTRLFTGPVHGTRPDRLRPGLLDRCLRP
                     VRLKLGQQPDRLRPLLPLPIQPKQPRRPRSAPTELGHQLVAARLYTQPPLKRGDLLQR
                     HVI"
     gene            complement(38715..40349)
                     /locus_tag="P1312_062"
     CDS             complement(38715..40349)
                     /locus_tag="P1312_062"
                     /note="similar to WP_013475335 Micromonospora sp. L5"
                     /codon_start=1
                     /transl_table=11
                     /product="hypothetical protein"
                     /protein_id="ALA06424.1"
                     /translation="MSHRHIVTEKERVARGDQTGGPPPTERGNTIMASTTVPMSDDVA
                     LEEIAAFEGRLGVEPGRNQLMSEFGWGGSRASRLLRLYRERKQRPEAVRLLPELEADR
                     SEAAVQQSGSEAVRSGAVDRSGEQSGEQSGGPARKTDGVDRSASSGLGRSSEAVQSGG
                     PVQQSGSEAVRSASSSGPVVRSGGADQSGPVVRSGGAVRSDGAARGEQSTSPDQDDAV
                     GVEAAQAGLVRVEGLVPSLDRREPDPWVEGWTGGPADQSEVDGVVDRSGVVAQASMSG
                     PNTGPVDRVEARTESGGLVRSTARAGVADRSGPGASSGVVDRSGGPGEAAGLVDRSGP
                     GEAAGLVDRSGGVVRDEVDQSGPVEAAGEPVRSGLGEAGPVVEAQRAGDADPRSGDGP
                     DRKPWGLIIAILAISLSAFTAVWGGWVGLGRMVGFGKVNLLPGFVADGGWATIDLAIT
                     LPIGIEAYAASALYVAVAGLVRGGSRWFAGSSAGLSLALGAFGQAAYHVLDAQGRTVA
                     PEWIVVFVSVLPVVVLGMAGVLLHLVLEERKHRRRR"
     gene            complement(40484..42526)
                     /locus_tag="P1312_063"
     CDS             complement(40484..42526)
                     /locus_tag="P1312_063"
                     /codon_start=1
                     /transl_table=11
                     /product="DNA segregation ATPase FtsK/SpoIII"
                     /protein_id="ALA06425.1"
                     /translation="MRRPAGTRPAGTSKEEWRAMAKKVDWGLKSSGPVVNGLQAALGL
                     GAVTAVADYAAIHPIWALGAAAVGAGGTLLVRGMQSPNRVIADLARWAGAGGWSFSLL
                     SGLADWSVGSVATLAGGAVLASCLGPAIDRREQAAAAALASGGISSGGLMLGSTAREC
                     AQWQQALVRVYGQVLRGVVVENVREWPNRYGKDVDVLLPANGVTSDTLRRGLPGLATV
                     MDLPRGCPIELVEPEGSRRRVVLRVATVNRLDADIPYPVDGAGVESILDGIPFGEHAD
                     ASIASAPIREDSWLIVGKRGSGKTTLLHGLTATIGSCRDALVWHIDLNGGSLTQPWIE
                     PWLRGEVARPPVDWAAPTVDEAILMMRAAVRMAKHRKVAYRGLKRKHNVSLLPISPEL
                     PAVEIIIDEGAEALAAAGRGKVAELANLLAEIQRIARDAAINEVISALRGTSDLIPAA
                     MTSQTGVSICMRVEQDKELAAVFGWHSGVDYRDLRRKGSGFVGTDRGIQQFQAWNILP
                     AQIEEIGMRISRQRPDLDAATARAGGEEYATRYERMRELFEDPDALIDPADSDSSAVL
                     ARAAAPVESGRWTVTAGWDDPGVRREQVRVALAPAREDEDIVERIIALMDERGEDRIP
                     REVAARELTGGDDEELRRRVAEAGGPAPRSIRYQGLPARGWYRRDLEAVREVVSQT"
     gene            complement(42486..44174)
                     /locus_tag="P1312_064"
     CDS             complement(42486..44174)
                     /locus_tag="P1312_064"
                     /note="similar to WP_017602419 Nocardiopsis lucentensis"
                     /codon_start=1
                     /transl_table=11
                     /product="hypothetical protein"
                     /protein_id="ALA06426.1"
                     /translation="MDGPGLGLVVGAALHRRARRALRGVDCSRLGSRRRGRPRPGRAV
                     LQGGQVTAEAVEAEAAPPTPGPPVITVTAEPVDDDQSTADAPKEKQEKEEEAPFPAGQ
                     VLLGAGSALTLGSVALASAVGPWGLLLAPGAVAVGGGVFLATRSRKRSKRGRSSERAF
                     GGARSGAGARPVGRVGGARLGGGGRRSSGGGRGGVSPTHGGGRPAAARSVGLGARPAP
                     TSRTAPWARGGTPRPGAGGRAVVAPPLRLRPAAGAGGRVLGGGAGVRPGGGASRRVGR
                     GSGMGPAPRNRWGASQQPSAHPRGGLRRAVRAAGRRVADWADDRSGRRLSTGWRAAKD
                     QPGFRAAHKAARDTLRSKKRRGPATEVAALLVAVASWLRSLWARRQDSGGAKEKDKKS
                     KKTAAASTASAVSEPGAVSPAGDADVEETPPRETTPPSSGEEDSPEHTSTTHTTRGGR
                     VSTFPLLEIAVEMQGAAAKYSPETMWQVIADAERLPGVIDSVASSIRIYLERLVSEQY
                     PVDTAVIDQLGEVYRSLKTAAAQAEEVGPMIRNIHQHDVDRREAPRGDETRWNV"
     gene            complement(44577..45035)
                     /locus_tag="P1312_067"
     CDS             complement(44577..45035)
                     /locus_tag="P1312_067"
                     /codon_start=1
                     /transl_table=11
                     /product="ABC-ATPase"
                     /protein_id="ALA06427.1"
                     /translation="MGHYPNGGRPDRHPLSDLRPKVGGLMSPMPRCTVVSFGYGHGPA
                     PESDVIIDLRELLHRPLPTALRTMDGHDTCIKHWVENTPGAWAVINGVVDMVRGILAE
                     APHRNVQVAVGCTGGRHRSVVVAEKIGRGLEQSGYLVEVDHRDMHRALVA"
     gene            45020..46795
                     /locus_tag="P1312_068"
     CDS             45020..46795
                     /locus_tag="P1312_068"
                     /codon_start=1
                     /transl_table=11
                     /product="intergrase/recombinase"
                     /protein_id="ALA06428.1"
                     /translation="MDSDPRVARVGAAVRCYGYAFHSPSCSFQDRVRSRLVVASPVRD
                     RHTHSGVSSYQHATILLHRHTRDGTISDVKNTDLIEDQRTRVALYVRVSLDRREKASV
                     EEQLADLRLTVDRLGWDIVAELADNDVPASRYSKADRPNWMRLLQIIRRGEVDAVGFW
                     ELSRSTRRRTEWAEFAELAIDCRLRILVGSSVYRAENPHEMHILDMMATQGVLEVDQL
                     SERIHRSQRANAERGRPAGVPGYGYRRRYDPATGRLIGQEPDPDEAKVIRMIARWLRA
                     GRSLSWIAEELNRRRIPTDKGRVAGEKYVDSRGRERVSLGWVPANLRRVMSRPELKGI
                     RTYKGKEVAQGQWEPILSVEEWAEVQAALNRTKQRSAATGQRYVRDAAARWLLSGIAI
                     CDVCGGDIRAVPRSRRGRPAGDDPSRWRYRCNGVYKGAPMGHVTRRADWLDEAVEALL
                     IRELSRPDVVEAFAVQEDPGVIERARAEILKIEEELRQLEEDVAVGLVTPRIASARER
                     ALQRRLEQLRKEATPRLVDPLVGQLVGASDVWAWWQEWELDQRRAALRAVTREIRVLP
                     ARVPGRNTRPPVEEMVRIVFGPVGG"
     gene            complement(46846..47265)
                     /locus_tag="P1312_069"
     CDS             complement(46846..47265)
                     /locus_tag="P1312_069"
                     /codon_start=1
                     /transl_table=11
                     /product="hypothetical protein"
                     /protein_id="ALA06429.1"
                     /translation="MKTVAAPLTYGDCFFHAHKHHKNTPKQVTCLYPPKRRCCTRSMA
                     TSSRGRDALATQQARAAVHVTIHTRAEGAPVEVSRIVGAATTLHIREGTTCREISHAI
                     GEHLNAGEIASLTRIFADHGLVLNRTPEREILRTDFT"
     gene            complement(47286..47870)
                     /locus_tag="P1312_070"
     CDS             complement(47286..47870)
                     /locus_tag="P1312_070"
                     /note="similar to WP_036322164 Microbispora sp. ATCC
                     PTA-5024"
                     /codon_start=1
                     /transl_table=11
                     /product="hypothetical protein"
                     /protein_id="ALA06430.1"
                     /translation="MPCLPRQARGRVLPTVASPRDEIPMHASERWQRLAELLAARRAR
                     LNPEWADRTRFCADTDLSYRSLSDLENGRRDNYSPAWLAKVERAYQLKPGAIKRYVNN
                     EVDTLETDDSGAPSEPLSSTQRPAEDSPSPQQDDWAEGVSWWPSRRDPALRVYRMRWL
                     DANGRRHEYITEADREVSPSVIVEYLERRKSEAM"
     gene            47971..48198
                     /locus_tag="P1312_071"
     CDS             47971..48198
                     /locus_tag="P1312_071"
                     /note="Helix-turn-helix XRE-family like proteins"
                     /codon_start=1
                     /transl_table=11
                     /product="transcriptional regulator"
                     /protein_id="ALA06431.1"
                     /translation="MAGMNTVTVRGDTIRALREQRGWTLEDLARRTQRSRAYLSRVEN
                     GQRTPSRITMHRIANALEVPIDDLVTPREKA"
     gene            48520..48948
                     /locus_tag="P1312_072"
     CDS             48520..48948
                     /locus_tag="P1312_072"
                     /codon_start=1
                     /transl_table=11
                     /product="hypothetical protein"
                     /protein_id="ALA06432.1"
                     /translation="MTIVHHDQHTTTIVDLPTRDETLDPTGRVAPEITYTVEPRRWHG
                     YTVWEWHLNDPTMSTCRVRGVQPTEARATQRAAEAARIHEQLHAITRLSSRRWTYEID
                     GVEMTYKCGIRALISRGVPEIHAHDWLAGIGYKAEEEGWW"
     gene            complement(48866..49402)
                     /locus_tag="P1312_073"
     CDS             complement(48866..49402)
                     /locus_tag="P1312_073"
                     /codon_start=1
                     /transl_table=11
                     /product="hypothetical protein"
                     /protein_id="ALA06433.1"
                     /translation="MGCVLSGVSARGGDESVEEASCPLGVQLHQPFDEGPVDPVELAV
                     FLAQPPGLFAVEHVAGDQRRLNGGDEGEDEEGAGHHGGGGDGAHADHRNGANGDAAFA
                     HLFSLKVKPGRGRCPRLGRVSAQRVRGSGPRGLRGRGGSSTGFRCSLRLVTTSPPPPP
                     CSRSPPASHGRGFPAHPC"
     gene            49094..49405
                     /locus_tag="P1312_074"
     CDS             49094..49405
                     /locus_tag="P1312_074"
                     /codon_start=1
                     /transl_table=11
                     /product="hypothetical protein"
                     /protein_id="ALA06434.1"
                     /translation="MSEGSITVGTVAMIGVGAVAAATMMAGALLILALVAAVEAPLIA
                     RYVLYRKEARRLREENRQLDRVNRALIERLVELDAEGTRRLLNALVPPTGRHTRKDTP
                     Q"
     gene            49402..50229
                     /locus_tag="P1312_075"
     CDS             49402..50229
                     /locus_tag="P1312_075"
                     /codon_start=1
                     /transl_table=11
                     /product="hypothetical protein"
                     /protein_id="ALA06435.1"
                     /translation="MTVSMNNFRVDQATTYNSTALPAPSSRDLACAEVYATHSTTSGD
                     RWGIVARLADTRWVYATYEDERWHLYIDDNPYDALRHISQQTRYALRPVDLHNWHHAT
                     CEIVEHAEEETRRLQKRIADLEEGVTIPITPLANVPASCITITTAGTADEATPTVEDA
                     KAARTIAVGATRLGYPLHVATITTVSYRWWAIVERQPYTVKDVMAAVFTEGFPARWRV
                     VAARDAFAVVRRIGMDLLSLRPMDPPAWNHILCHAVISASRQMDAPLASEEASHGVA"
     gene            50446..51360
                     /locus_tag="P1312_077"
     CDS             50446..51360
                     /locus_tag="P1312_077"
                     /codon_start=1
                     /transl_table=11
                     /product="exodeoxyribonuclease VIII"
                     /protein_id="ALA06436.1"
                     /translation="MGCRTPQRGPLMTATTEQAEERTVIRRPGLYDLPEHIYHADPVP
                     GGSLSSTGARRLLECPARFRYEQAHPPAPRPHFDFGTAAHKLVLGVGPELAVLDYPDW
                     RTKAAREAARKARERGAIPLKRGDYEQIQAMAEALKSHPVAGPIFTESAGRAEQSLFW
                     QDSDTRVVCRARIDHLPHPTQQGRLILADYKTCATADPNKLPRVIVDHGYHLQAAWYI
                     DGVRALGLAEDVAFLFVFQEKQAPYLVTVVELDHEALTIGSYLAREARQRYATCRRTG
                     NWPGYADDAPVVVSLPSYYTQQYEGASL"
     gene            51357..52118
                     /locus_tag="P1312_078"
     CDS             51357..52118
                     /locus_tag="P1312_078"
                     /note="similar to WP_045740910 Actinoplanes rectilineatus"
                     /codon_start=1
                     /transl_table=11
                     /product="hypothetical protein"
                     /protein_id="ALA06437.1"
                     /translation="MTIQPHETTQPEPLHEEGTLTPHQQAPAGTDNPLITWALAARQA
                     HAIAESLARTSFVPRSLQGRPADITAAILTGQELGMQPMAALRSLDIIQGTPSLRAHA
                     MRALVQRAGHQIQLVESTPELCRMRGRRKGDEEWQTVVWTIERAQKLGLTSKEQWKRQ
                     PQSMLVARATSEICRLIASDVLFAVPYSTEELQDKPVEEAPPRVTVEEIHARGQQADP
                     HEEQPDEFEPSEEDQVDWADQQWGEQTPEAATSQG"
     gene            52187..52939
                     /locus_tag="P1312_079"
     CDS             52187..52939
                     /locus_tag="P1312_079"
                     /note="DnaQ-like exonuclease"
                     /codon_start=1
                     /transl_table=11
                     /product="DNA polymerase III subunit epsilon"
                     /protein_id="ALA06438.1"
                     /translation="MTNQQQATGWHNGPLASFDTETTGTNPNEARIVTAACWLITPGH
                     DKKHREWLVNPGVEIPAEATQVHGITTEQARKQGQPAAAAVAEIASAVLYAYRNQIPV
                     IVYNARYDITLIHRELVRHGHADLARAWEEFAARGPIVDPFILDKQIDRYRKGSRKLI
                     DVAAHYGVALAEEDAHGSAADALAAARVAWVIANRNPKLAALGPVELHETQVKAAAEQ
                     AHSFADYLRKQGKPVDDVHLEWPLIPTRKEET"
     gene            53097..53723
                     /locus_tag="P1312_081"
     CDS             53097..53723
                     /locus_tag="P1312_081"
                     /codon_start=1
                     /transl_table=11
                     /product="hypothetical protein"
                     /protein_id="ALA06439.1"
                     /translation="MADTIPPNEARQRLADLTGQRVRVTQRTLDGATTVETGILHYDQ
                     DSGTWAIRGAVVTYPDADVYVDPRHLVDVALEQRGSLWGHVHRALCEAGLADTFAESL
                     ADRMLAALSVDDVRVVERVSQSRTQRPHTKEPLPCGATAPLHSGGEATCNRPAGHTTH
                     IADNGARWTDDPRRVELAAGLRRLAKLYGYPAIAAELMRQTVHIGGQP"
     gene            53720..54208
                     /locus_tag="P1312_082"
     CDS             53720..54208
                     /locus_tag="P1312_082"
                     /codon_start=1
                     /transl_table=11
                     /product="holliday junction resolvase"
                     /protein_id="ALA06440.1"
                     /translation="MTTIITVYGRPAPQGSKKAFRHRATGKIITQEMSKYVRPWRAEV
                     QRAAQAALLTRYDQGRFPLVGPLAVDMIFTLARPKSHYRTGRNAHLLRDSAPARPTGA
                     PDLSKLARATEDALTEAGVWKDDAAVVEYRRLAKVYPGSDPDALDQPGVLIRIHLLET
                     TP"
     gene            54205..54645
                     /locus_tag="P1312_083"
     CDS             54205..54645
                     /locus_tag="P1312_083"
                     /codon_start=1
                     /transl_table=11
                     /product="WhiB family transcriptional regulator"
                     /protein_id="ALA06441.1"
                     /translation="MTHLQPENDWHPKAACRGHDPDLWFGWEGESINARKAREQVAKR
                     ICATCPVRTQCLTHALTYPEAYGIWGGLNEHELVAERCRRGLKPAPRSDYHRLITCAG
                     CNNTKPHNGRGPDGQPLCAACRFRWVQAGRPATVPPPPTRKEAA"
     gene            54648..55439
                     /locus_tag="P1312_084"
     CDS             54648..55439
                     /locus_tag="P1312_084"
                     /note="similar to WP_017602245 Nocardiopsis lucentensis"
                     /codon_start=1
                     /transl_table=11
                     /product="hypothetical protein"
                     /protein_id="ALA06442.1"
                     /translation="MARNHGTISTYRDGCRCQDCDTYARAYERERGRRRRVGAPTTNL
                     VDATPVRQHLRQLMRAGMSYRDINAMLGIKIHYLLYQPIKRVNPVTARRILEIPIPRS
                     PLPTAKPIPADGSRRRTQALYTLGYSIAWQATHSGVSRNLISRVIHGQSSSIRACHAA
                     KIRELYDAYWDKPAPDTRESRGIRTRARKRGWLPPLAWDDELIDLTEDELEAELERRT
                     ALMTDAELIRCMRAYQAGDRSPLIVAACRTHWRRLSARRRERKAA"
     gene            complement(55343..55657)
                     /locus_tag="P1312_085"
     CDS             complement(55343..55657)
                     /locus_tag="P1312_085"
                     /codon_start=1
                     /transl_table=11
                     /product="hypothetical protein"
                     /protein_id="ALA06443.1"
                     /translation="MARNRGLPGEQPVDGGLRHPSRPGNPRAGPPSPDEGTQVRHHAV
                     CRDAGRLPPALSQENPAAFAIAAGIGQPAHAAFLSLLRALSRRQWVRHAATMSGDRSP
                     AW"
     gene            55382..56044
                     /locus_tag="P1312_086"
     CDS             55382..56044
                     /locus_tag="P1312_086"
                     /note="similar to WP_043984960 Mycobacterium llatzerense"
                     /codon_start=1
                     /transl_table=11
                     /product="hypothetical protein"
                     /protein_id="ALA06444.1"
                     /translation="MPYPLAAAQRPQKRKEGRVSRLTYASRYGKRRRILLAEGRWESS
                     RIPADGVVAHLRALIRAGRSRTWIARATGVPEATIHRLLAGQSTITRHNAYRLLALTR
                     ADRPRGKTWVPATGTKRRLEALACQGWSQVDIARLAGLNANTLSRVVRDSPRQVAAAT
                     ADAVARVYLQLARLCRTDRTGRWVQARARRRGYLPPAAWTPWTIDDPRARPLPVEGWE
                     RG"
     gene            56029..57438
                     /locus_tag="P1312_087"
     CDS             56029..57438
                     /locus_tag="P1312_087"
                     /note="similar to EFE65835 Streptomyces ghanaensis ATCC
                     14672"
                     /codon_start=1
                     /transl_table=11
                     /product="hypothetical protein"
                     /protein_id="ALA06446.1"
                     /translation="MGAWLAVSPPHPGGLGVTSITALIDQLPHRATTPNHPNRDILSI
                     LRHPRHDLPRHATSHRLTKTATPPRGSHPHLQKQTMTISRREPVARNYAQLRSAIWQN
                     ESFKNELDVDAQWLYFVLLSQPNINTAGVLPLQERRWARFAHGMTGPRVTAALERLNA
                     YWYVVVDEDTEEVLVRTFIRHDGLWKQPNVLKSALGHVQSTVSPTLRAVLRYELSRLP
                     IDELPTERAERTRALIERVAGTLPETLPEGFLEPFQEPFQEGSPNPFHQPISDPNPNH
                     RGGDSEPLSPKTTKQQVSEPQQAALEGFPEGFREGFPEGFPEGSGVGVGVGVKGSGSL
                     LVQEREPKTTSSGAAAPHTPPPTAQTLIGEWLDRCPKRPPSRVIGHVAKEIKNLLDDG
                     IHPDDIRRGLAHWMTKGLHPSTLPSVVNEVMNTPSSNVVAFPDARPLTYRQQNTQAMF
                     ADALAEAEQLERAMQEGTA"
     gene            complement(56311..56919)
                     /locus_tag="P1312_088"
     CDS             complement(56311..56919)
                     /locus_tag="P1312_088"
                     /experiment="LC tandem mass spectrometry"
                     /codon_start=1
                     /transl_table=11
                     /product="hypothetical protein"
                     /protein_id="ALA06445.1"
                     /translation="MGFADLLFCGFGGQGFAVTPSVVGVGVGNGLVKRVGRPFLEGFL
                     EGFQKPFGKGFGKGSSNPFDESAGALSALSRQLVDGEPRQLITEHSAQGGRHGGLDVA
                     ERRLEYVRLLPQPVVADESTHENFFGVLVYDHVPVRVEAFQGGGDPGAGHAVGEARPA
                     ALLEGEDARGVDVGLGEQDEVQPLGVDVQFVFETLVLPDGAS"
     gene            57435..58103
                     /locus_tag="P1312_089"
     CDS             57435..58103
                     /locus_tag="P1312_089"
                     /note="similar to WP_030282501 Streptomyces sp. NRRL
                     B-5680"
                     /codon_start=1
                     /transl_table=11
                     /product="hypothetical protein"
                     /protein_id="ALA06447.1"
                     /translation="MTPTEAVAFVEKMKAAAPHISFEWDTPKAWAAALADIDWDEAHA
                     ALLNAIRKTPWITPAVIQDEVRAMRAEKLKHYVVPPPPNPDDVAGYLHALRAAPRAAL
                     RAAATSPLSLESGLDPVTKTRREHLRAGSPRMVDPATTKPDTDRRSHTARQALAEARR
                     KCAAASARLRTNSEGLSETEKQAREQAARLRTQPRPPRKGDPKTLSVAEIQTVLKEAR
                     RGQS"
     gene            58214..58504
                     /locus_tag="P1312_090"
     CDS             58214..58504
                     /locus_tag="P1312_090"
                     /codon_start=1
                     /transl_table=11
                     /product="hypothetical protein"
                     /protein_id="ALA06448.1"
                     /translation="MKHRPEQQRRRSVVPPRGSRPWPAWMRITRTGWECAHPHHPEVS
                     DSVEGLSEHMVVGSALAHLDRWHPGWRIRCRRCGRRQWNDQESSYCYECRPQ"
     gene            58573..58908
                     /locus_tag="P1312_091"
     CDS             58573..58908
                     /locus_tag="P1312_091"
                     /note="similar to WP_037865813 Streptomyces sp. NRRL
                     S-1868"
                     /codon_start=1
                     /transl_table=11
                     /product="hypothetical protein"
                     /protein_id="ALA06449.1"
                     /translation="MPTRIQRRRTRGWRMPSGAVYVGRGSRWGNPYRVARVGGGYVVE
                     GPGWCSSHESRVEAHQVAVDRYRVWAVHQSGFVDQARARLAGCDLACWCAPGVPCHAD
                     VLLVVANTE"
     gene            complement(59571..59867)
                     /locus_tag="P1312_093"
     CDS             complement(59571..59867)
                     /locus_tag="P1312_093"
                     /codon_start=1
                     /transl_table=11
                     /product="hypothetical protein"
                     /protein_id="ALA06450.1"
                     /translation="MDPQAPLSPLATRCPRCHPVAVAENTITEPTETPTTVPDHHAGE
                     DKPASGTGEMWDLPAPPEHERGRDAATDAARPQPRLSQTSGPNWRRSDGKRPAE""".split("\n")

for item in bigassBoy:
    if 'product=' in item:
        print(item)
