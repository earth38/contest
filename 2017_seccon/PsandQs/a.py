from Crypto.PublicKey import RSA
from Crypto.Util.number import inverse

def gcd(x, y):
    r = modlog(x, y)
    while r != 0:
        x = y
        y = r
        r = modlog(x, y)
    return y

def modlog(x, y):
    r = x % y
    return r

def main():
    u1 = 847796795638781450678718708664542960446354226336422534142899480441478781747168340722544245493739168125415291376063352480076469305992008517388366298914970810765149321160596112226917023146371080685458239747986992197343482255681414590678694753885521068656675164266739274608505094927725285868801825144058835115051061857233824816176186349372737400492228548130718029270482313906040935333159681273527671359469173939861889228505791626525994180917670701909816457560622922219797109618405842358250940062127841301193206255543580550667149741357342408703680375118252445296600962244008043713708516004025217199954286478272550961283413053789743740774140439284662596273452124779590753836094450154459078034659421366584354005421566290862244000178569163732971816333961711759000171156293724203334889496589376907683142167883476184246287660764821622298961378903818077158234683927321823293466245584486980446609569799420950073036635602004293246754252079757527610246223280774592566063422181158810677919909523144033543195999214800559998598003329294711989868113423468536273984117507008756542731210465222475943122324672467669623079721727526348599823126409108190030551584092950358235465140166515452377475799157617227362838246912839086733412861436353117994501342653 
    u2 = 763718912475160487902804749669814117361530270298225094625871588939939773892509348006077810445741086683427253000695920011673348476297973798322806091336777405584801442639626925406721932533140226556519019440300864340670199686368307155860493615065198319490060598587202051942638792919648596288576294804549738135969737494734307362891313864027749187674251692407867312885251279302785352318725391842117065840058358065676707016006124478822206302825992616559261930620693061673348139416033418864269248381876692676529410115745518353146254670349865568255213560376368953292931958006941630719304442332912813624543600126197554727832190226632919876204677667384620275620336951964833888599634720101911051166398907898747710391394105753614253527704990658698844796442515669670816004761855554187277637871343595647487793209271354240148469085627742503649786300484610102224828274384484809539697728008552925590472129497180290668277790132130824141651399551803499770513576176720509094833332201946177880267399933460994496277590932311628302240154240967341858152145815276163397709272690500041597393678630136932574450837982593210399370333578887450410911663220219423601973078501237709613593311133945501455828164291429228495931943107997137587307522565029820756690578833 

    q = gcd(u1, u2)
    #print q
    #print
    #print("p1 = "+str(u1/q))
    p1 = u1/q
    #print
    #print("p2 = "+str(u2/q))
    p2 = u2/q
    e = 65537	

    n = p1*q
    d = inverse(e, (p1-1)*(q-1))

    key = RSA.construct(map(long, (n,e,d)))
    print key.exportKey()


if __name__=="__main__":
    main()