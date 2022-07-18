import random
class style():                                                                              #stilusok definiálása
    RED = '\033[31m'
    RESET = '\033[0m'
    UNDERLINE = '\033[4m'
    BLUE = '\033[34m'
    CYAN = '\033[36m'
    GREEN = '\033[92m'
                                                                                             #Történetindító:
print( style.GREEN+"A történet a sötétség földjén játszódik. A zsarnok Árnykirály rettegésben \
tartja a népet. Egy titkos társaság a Fény klánja a király ellen \
szervezkedik. Céljuk, hogy újra a világosság emelkedjen felül a \
királyságban...")

életerő=150
zsakmany=5
ellenfel=50
ellendobas = int(random.randint(1,6))
dobas=0
tuzvarazslat=1
gyogyitas=1
duh=1
csel=5
gyava=False


sereg=200
gomb = ""
nev = ""
kaszt=""
kocka=0
seregmoral=3

while gomb != "m":
    gomb = input (style.BLUE+" (B)elevágsz a kalandba, vagy (m)egfutamodsz?: ")
    if gomb == "B":
        print(style.CYAN+"Üdvözöllek! Remélem siker koronázza utadat!")
        nev = input(style.BLUE+"Kérlek áruld el a neved!: ")
        nev=nev.capitalize()
        break


    elif gomb != "B" and gomb !="m":
        print(style.RED+"Első lecke! Mindig a kérdésre válaszolj!")
    elif gomb == "m":
        print(style.CYAN+"Térj vissza később, ha már elég bátorságot gyűjtöttél!")
        print("\n\n")
        print("++++++" * 50)
        exit()
print(style.CYAN+"Megkezdődött a mozgolódás. Itt az idő hogy vezetőt válasszanak a sereg élére.",nev,"!!! Harsogja a sereg! ")

while gomb != 0:
    gomb = input(style.BLUE + "Milyen fajta hős vagy? (P)aladin, (m)águs, (h)arcos?, vagy (f)eladod?: ")
    if gomb == "P":
        kaszt = "paladin"

        print("\n\t\t",style.CYAN+"A",style.UNDERLINE+style.GREEN+"paladinok",style.RESET+style.CYAN+" védelmezik a gyengéket, igazságot hoznak az igazságtalanság helyébe\n\
        és eltüntetik a gonoszt a világ legsötétebb zugaiból is. \n\
        Ezek a szent harcosok páncélt viselnek, hogy a legkeményebb ellenféllel is szembeszállhassanak. \n\
        A Fény  áldása lehetővé teszi számukra, hogy begyógyítsák a sebeket, \n\
        sőt, néhány esetben még a halottba is életet lehelhetnek.\n")
        gomb = input(style.BLUE+"Biztosan ezt választod? (I)gen (N)em: ")
        while gomb != "0":
            if gomb == "N":
                break
            elif gomb == "I":
                print(style.CYAN+"\n")
                print("Te lettél a sereg vezére", nev, kaszt, "! Ez hatalmas felelősség is!")
                gomb = 0
                break

            elif gomb != "I" and gomb != "N":
                gomb = input(style.RED+"Csak egy kérdésre kell válaszolnod...Biztosan ezt választod? (I)gen (N)em: ")


    elif gomb == "m":
        kaszt= "mágus"
        print("\n\n\t",style.CYAN+"A",style.GREEN+style.UNDERLINE+"mágusokok",style.RESET+style.CYAN+"jártasak a mágia több ágában, legyen az fehér vagy fekete. \n\tRendelkeznek védelmi varázslatokkal, de támadásra is van pár varázsigéjük.\n")
        gomb = input(style.BLUE+"Biztosan ezt választod? (I)gen (N)em: ")
        while gomb != "0":
            if gomb == "N":
                break
            elif gomb == "I":
                print(style.CYAN+"\n")
                print("Te lettél a seregek vezére", nev, kaszt, "! Ez hatalmas felelősség is!")
                gomb = 0
                break

            elif gomb != "I" and gomb != "N":
                gomb = input(style.RED+"Csak egy kérdésre kell válaszolnod...Biztosan ezt választod? (I)gen (N)em: ")

    elif gomb == "h":
        kaszt = "harcos"
        print("\n\n\t\t","A",style.UNDERLINE+style.GREEN+"harcos",style.RESET+style.CYAN+"nem használ a klasszikus értelembe vett mágiát, \n\
        a harc folyamán felgyülemlett dühét fordítja az ellenség ellen.\n\
        Ereje és állóképessége az egyik legnagyobb, ezért képes mindenfajta páncéltípust hordani,\n\
        pajzsot fogni és a pálcák kivételével mindenféle egy- és kétkezes fegyvertípust forgatni.\n\
        Képes komoly sérülések okozására, de akár társai megvédelmezésére is.\n")
        gomb = input(style.BLUE+"Biztosan ezt választod? (I)gen (N)em: ")
        while gomb != "0":
            if gomb == "N":
                break
            elif gomb == "I":
                print(style.CYAN+"\n")
                print("Te lettél a seregek vezére", nev, kaszt, "! Ez hatalmas felelősség is!")
                gomb=0
                break
            elif gomb != "I" and gomb != "N":
                gomb = input(style.RED+"Csak egy kérdésre kell válaszolnod...Biztosan ezt választod? (I)gen (N)em: ")




    elif gomb != "m" and gomb!="h" and gomb!="f" and gomb!="P":
        print("\n")
        print(style.RED+"Talán remeg a kezed az izgalomtól? Próbáld meg újra!")

    else:
        print("\n")
        print(50*"++++++")
        print("\n\n",nev,style.CYAN+"Az utolsó pillanatban kihátráltál a feladat elől. Vezető nélkül az addig összegyűlt sereg szétszéledt, a birodalom a sötétség uralma alatt maradt.")
        print("\n\n")
        print("++++++" * 50)
        exit()
print(style.CYAN+"\n")
print(sereg,"fős sereg gyűlt össze a Fény zászlaja alatt!")
print("\n")
gomb=input(style.BLUE+"Mint megválasztott vezér engedélyezel egy kis esti ünneplést a harcosaidnak a reggeli indulás elött?(I)gen (n)em: ")

while gomb != 0:
    if gomb == "I":
        kocka=random.randint(1,6)
        if kocka == 2 or kocka == 4:
            print("\n\n",style.RED+"Az éjszaka folyamán rajtaütöttek az ünneplő seregen. A váratlan támadásban elesett 20 harcosod.")
            sereg-=20
            break

        elif kocka !=2 and kocka !=4:
            print("\n",style.CYAN+"A harcosaid egy kisebb lakomára gyültek össze, tudván hogy néhányuknak, vagy talán mindnek ez lesz az utolsó.")
            print("De ez nem szegte kedvüket. A szabadságért bármit megtennének.")
            seregmoral+=1
            break

    elif gomb == "n":
            print("\n\n",style.CYAN+"Próbálsz jó döntéseket hozni. Bár előfordulhat hogy nincs olyan. Egyesek feszültek a holnapi harc miatt.")
            seregmoral=seregmoral-2
            break
    else:
        gomb=input(style.RED+"Egyszerű volt a kérdés, legyen a válasz is az!(I)gen vagy (n)em?: ")



print(style.CYAN+"\n\n","A felkelő nap első sugarai  szikráztak a harcosok páncéljain. Mind készen állt a harcra, és akár a halálra is.\n ")
print("Egy folyóhóz értek ahol egy varázslóval találkoztok. Egy helyes válasz a fejtörőre és átjuttat.\n")
print(style.GREEN+"Lába van, de mégse jár,\
víz felett visz, nem madár. \
Nem rab, mégis láncot hord, \
s minden utat összetold. Mi lehet az?")
while gomb != 0:
    gomb=input(style.BLUE+"Jól gondold meg!: ")
    if gomb == "híd" or gomb == "Híd" or gomb ==  "hid" or gomb == "Hid" or gomb == "a híd" or gomb == "a hid":
        print(style.CYAN+"Helyes válasz!")
        print(style.CYAN + "\n")
        print("A varázsló jutalmul egy zsák aranyat adott. A folyóból egy híd emelkedett ki, amin biztonságban átkelhetett a sereg.",sereg,"harcos tart veled.")
        zsakmany+=1
        seregmoral+1
        break
    else:
        if sereg-40 <= 0:
            print(style.RED+"A varázsló elpusztította a megmaradt csapadtodat. Végül veled is végzett.")
            print("\n\n")
            print("++++++" * 50)
            exit()

        elif sereg-40 > 0:
            sereg-=20
            print(style.RED+"\n")
            print("A varázsló dühében elpusztította negyven harcosod! A megmaradt",sereg,"embered élete a válaszodon múlik!")



while gomb != 0:
    print("\n")
    gomb=input(style.BLUE+"Egy sűrű erdőn vezetne át az út. (Á)tkelsz vagy (m)egkerülöd?")
    if gomb == "Á":
        print("\n")
        print(style.CYAN+"Egy démonnal találta szemben magát a sereg.")
        print(style.CYAN+"\n")
        print("Ott állsz",életerő,"életerővel, és a hittel a szívedben hogy győzelemre vezeted a sereget.")
        while dobas != -1:
            ellendobas=random.randint(1,6)
            print(style.CYAN + "\n")
            print("Az ellenfeled", ellendobas, "támadásponttal és", ellenfel, "életerővel rendelkezik!")
            gomb = input(style.BLUE+"Mit teszel: (t)ámadsz, (v)édekezel vagy (m)egpróbálsz elmenekülni?")
            print("\n")
            if gomb == "t":
                dobas = int(random.randint(1, 6))
                print(style.CYAN+"\n")
                print(dobas, "támadásponttal támadtál.")

                if dobas > ellendobas:
                    print("\n")

                    if ellenfel - dobas * 3 <= 0:
                        print(style.CYAN+"\n")
                        print("Sikeres támadás. Bevittél", dobas * 3, "sebzést!")
                        print(style.CYAN + "Véfagyasztó üvöltés kíséretében kilehelte kárhozott lelkét...")
                        print("Zsákmányoltál 5 zsák aranyat. Így ",zsakmany,"zsák arannyal folytatod utad.")
                        print("\n")
                        gomb = 0
                        zsakmany+=5
                        seregmoral+=2
                        életerő=100
                        break



                    elif ellenfel - dobas * 3 > 0:

                        print(style.CYAN + "Sikeres támadás.")
                        print("Bevittél", dobas * 3, "sebzést!")
                        ellenfel = ellenfel - dobas * 3
                        print("Ellenfeled", ellenfel, "életerővel rendelkezik még.")
                        print("\n")
                        ellendobas = int(random.randint(1, 6))


                elif dobas < ellendobas:
                    if életerő - ellendobas * 3 <= 0:
                        print(style.CYAN+"\n\n")
                        print(50*"+++++")
                        print(style.RED + "Ezt elvétetted!")
                        print("Ellenfeledtől", ellendobas * 3, "sebzést kaptál. ")
                        print(style.CYAN + "Ez a harcmező lett végső nyughelyed.")
                        print("\n")
                        print(50*"+++++")
                    elif életerő - ellendobas * 3 > 0:
                        életerő = életerő - ellendobas * 3
                        print(style.RED + "Ezt elvétetted!")
                        print("Ellenfeledtől", ellendobas * 3, "sebzést kaptál. ")
                        print(életerő, "életerőd maradt!")
                        ellendobas = int(random.randint(1, 6))
                        print("\n")


                elif dobas == ellendobas:
                    print("\n")
                    print(style.CYAN + "Kivédte a támadásod!")
                    ellendobas = int(random.randint(1, 6))
            elif gomb == "m":
                sereg=sereg-random.randint(10,30)
                print("\n")
                print(style.RED + "A menekülés közben odaveszett néhány embered, és némi zsákmány.")

                if zsakmany > 0:
                    zsakmany = zsakmany // 2
                    print(style.CYAN+"\n")
                    print(zsakmany,"aranyad, és ",sereg,"harcosod maradt.")
                gomb=0
                break
            elif gomb == "v":
                if csel > 0:
                    print(style.CYAN+"Sikeresen kivédted a támadást!")
                    csel -= 1
                    if csel > 0:
                        print("Még",csel,"alkalommal védheted ki a támadást.")
                elif csel == 0:
                    print("\n")
                    print(style.RED + "Kiismerte a trükkjeid! Kár az energiáért!")
                    print(style.CYAN + "\n")
                    dobas = int(random.randint(1, 6))
                    print(dobas, "támadásponttal támadtál.")

                    if dobas > ellendobas:
                        print("\n")

                        if ellenfel - dobas * 3  <= 0:
                            print(style.RESET + "\n")
                            print("Sikeres támadás.Bevittél", dobas * 3 , "sebzést!")
                            print(style.CYAN + "Véfagyasztó üvöltés kíséretében kilehelte kárhozott lelkét...")
                            print("\n")
                            gomb = 0
                            zsakmany += 50
                            életerő=100
                            seregmoral+=5
                            csel=5
                            break



                        elif ellenfel - dobas * 3  > 0:

                            print(style.CYAN + "Sikeres támadás.")
                            print("Bevittél", dobas * 3, "sebzést!")
                            ellenfel = ellenfel - dobas * 3
                            print("Ellenfeled", ellenfel, "életerővel rendelkezik még.")
                            print("\n")


                    elif dobas < ellendobas:
                        if életerő - ellendobas * 3 <= 0:
                            print(style.RED + "Ezt elvétetted!")
                            print("Ellenfeledtől", ellendobas * 3, "sebzést kaptál. ")
                            print(style.RED + "Ez a harcmező lett végső nyughelyed.")
                            print("\n")
                            exit()
                        elif életerő - ellendobas * 3 > 0:
                            életerő = életerő - ellendobas * 3
                            print(style.RED + "Ezt elvétetted!")
                            print("Ellenfeledtől", ellendobas * 3, "sebzést kaptál. ")
                            print(életerő, "életerőd maradt!")
                            ellendobas = int(random.randint(1, 6))
                            print("\n")


                    elif dobas == ellendobas:
                        print("\n")
                        print(style.CYAN + "Kivédte a támadásod!")



            elif gomb != "m" or gomb != "t" or gomb != "v":
                print("\n")
                print(style.RED+"Talán megsérült a kezed hogy nem tudsz írni?")
                print(style.BLUE+"\n")
                gomb = input("Mit teszel: (t)ámadsz, (v)édekezel vagy (m)egpróbálsz elmenekülni?")



    elif gomb == "m":
        print(style.RED+"A kerülőút veszélyes sziklákon vezetett keresztül.")
        if sereg-70>0:
            sereg-=70
            seregmoral-=3
            print(style.RED+"Odaveszett hetven harcosod.","Így már csak ",sereg,"maradt, de őket is megviselte ez a veszteség.")
            gyava=True
            break
        if sereg-70 <= 0:
            print(50*"+++++")
            print(style.RED+"Odaveszett mindenki! Azóta is kerüli mindenki ezt az útvonalat. Állítólag elátkozott.  ")
            print("\n\n")
            print("++++++" * 50)
            exit()


    elif gomb != "Á" and gomb != "m":
        gomb = input("Egy sűrű erdőn vezetne át az út. (Á)tkelsz vagy (m)egkerülöd?")


print("\n")
print(50*"+++++")
print("\n")
print(style.CYAN+"Rövid időre megpihent a csapat, hogy egyen és erőt gyűjtsön a harcra.")
if seregmoral <= 0:
    seregmoral=1
csel=5
print("\n")
print(style.BLUE+style.CYAN+"Az erdőn átjutva szemetek elé tárult az Árnyerőd.")
print("Három hatalmas kapu zárta el a külvilágtól. Kémeid jelentése alapján az egyik bejárat mögött maga az Árnykirály tartózkodik egy kisebb, testőrökből álló sereggel, készen arra hogy elmeneküljön amíg tart a harc.")
print("Nem fogja önként kockáztatni az életét, ezt meghagyja csatlósainak. Akikből bőven akad, így reménytelen lenne a harc. Egyetlen esély a győzelemre, ha sarokba szorítod, s legyőzöd. Akkor a csatlósai kiket a félelem láncai kötnek urukhoz, leteszik a fegyvert.")
print("De van egy gond a kémek jelentésével...A három információból ",style.RED+"csak egy lehet igaz,a másik kettőnek abban az esetben hamisnak kell lennie!",style.CYAN+"Ezt neked kell megfejtened",nev,kaszt,"! S nem hibázhatsz...most nem!\n")
print(style.GREEN+"Első jelentés: Az első kapu mögött vár az Árnykirály a kitörésre.")
print("Második: Az Árnykirály nem a második kapu mögött lesz.")
print("Harmadik: Nem az első kapun át fog menekülni. \n")


while gomb != "":
    gomb=input(style.BLUE+"Jól meggondoltad a választ? Az (E)lső, (m)ásodik, vagy a (h)armadik kaput rohamozzátok meg?")
    if gomb == "E":
        print(50 * "+++++")
        print(style.RED+"Ezt nem jött be. Amint az első kaput elkezdte a sereg ostromolni, a második kapu kitárult, és az Árnykirály hűséges csatlósaivel elmenekült. Az óriási túlerővel szemben esélyed sem volt")
        print("Az utolsó harcosig lemészárolták a sereged.")
        print("Az Árnykirály a harc végére diadalittasan érkezett. Azt rebesgetik aznap az elesett harcosaidból készíttetett vacsorát...")
        print("\n")
        print("++++++" * 50)
        exit()

    elif gomb == "m":
        if kaszt == "mágus":
            print(style.CYAN+"\n")
            print("Sikerült! Miután",kaszt,"képességeddel egy szellemsereget idéztél a két másik kapu megtámadásának látszatához,a második kapu csikorogva kitárult. S ott állt az Árnykirály teljes valójában.")
            print("Nem erre számított...",sereg,"harcosod állta útját. Hatalmas haragra gerjedt mikor észrevette a trükköt, de ekkor már késő volt!")
            print("Muszáj volt megküzdenie veled.")
            break
        elif kaszt == "harcos":
            print(style.CYAN+"\n")
            print("Siker!",kaszt.capitalize(),"képességeid segítségével óriási pusztítást végeztetek a második kapun, olyannyira hogy teljesen megsemmisült. Az Árnykirálynak ideje sem volt másfele menekülni, olyan gyorsan bekerítette sereged.")
            print("Mostmár muszáj volt megküzdenie veled.")
            break
        elif kaszt == "paladin":
            print(style.CYAN + "\n")
            print("Nagyszerű!",kaszt.capitalize(),"képességeiddel felvértezve, három részre osztottad sereged.")
            print("Két kisebb csapat, pajzsukon a Fény áldásával elterelő csapást mért a másik két kapura. Így mágikus védelmükkel hatalmas túlerővel szemben is helytálltak, amig szükség volt rá.")
            print("Ekkor a második kapu csikorogva kitárult. S ott állt az Árnykirály teljes valójában. Vérben forgó szemmel vette tudomásul a cselt. Ott álltál vele szemben a nagyobb  sereggel.")
            print("Muszáj volt megküzdenie veled.")
            break

    elif gomb == "h":
        print(style.RED+"Ezt nem jött be. Amint a harmadik kaput elkezdte a sereg ostromolni, a második kapu kitárult, és az Árnykirály hűséges csatlósaivel elmenekült. Az óriási túlerővel szemben esélyed sem volt")
        print("Az utolsó harcosig lemészárolták a sereged.")
        print("Az Árnykirály már csak akkor jelent meg újra, mikor az utolsó haldokló harcosod is kilehelte lelkét... Azt rebesgetik aznap az elesett harcosaidból készíttetett vacsorát magának...")
        exit()

    elif gomb != "E" or gomb != "m" or gomb != "h":
        print(style.RED+"Ezen múlik a győzelem, nem hibázhatsz!")


print(style.CYAN+"Ott álltál szemtől szemben az Árnykirállyal.")
ellenfel=666
if gyava == True:
    print(style.RED+"Mint ezernyi suttogó hang, úgy hatolt elmédbe sötét ereje.")
    print("Hogy mersz szembeszállni velem",nev,kaszt,"??? Láttam minden lépésedet ezidáig. Te gyáva vagy! S egy gyáva harcos nem győzhet le. A félelem az én fegyverem, aki fél, az már veszített is. A remény ide kevés lesz...")
    print("Innen nem lesz hova menekülnöd mint az erdőben...! Készülj a halálra!")
    while dobas != -1:
        ellendobas = int(random.randint(1, 6))

        print(style.CYAN + "\n")
        print("Esküdt ellenséged", ellendobas, "támadásponttal és", ellenfel, "életerővel rendelkezik!")
        print(style.BLUE+"\n")
        gomb = input("Mit teszel: (t)ámadsz  (s)egítségül hívod a Fényt, vagy (v)édekezel?")
        print("\n")
        if gomb == "t":
            dobas = int(random.randint(1, 6))
            print(style.CYAN+"\n")
            print(dobas, "támadásponttal támadtál.")

            if dobas > ellendobas:
                print("\n")

                if ellenfel - dobas * 4 * seregmoral <= 0:
                    print(style.BLUE + "\n")
                    print("Sikeres támadás. Bevittél", dobas * 4 * seregmoral, "sebzést!")
                    print(style.CYAN + "Véfagyasztó üvöltés kíséretében kilehelte kárhozott lelkét...")
                    dobas = -1
                    zsakmany += 500
                    break



                elif ellenfel - dobas * 4 * seregmoral> 0:

                    print(style.CYAN + "Sikeres támadás.")
                    print("Bevittél", dobas * 4 * seregmoral, "sebzést!")
                    ellenfel = ellenfel - dobas * 4 * seregmoral
                    print("Ellenfeled", ellenfel, "életerővel rendelkezik még.")
                    print("\n")


            elif dobas < ellendobas:
                if életerő - ellendobas * 4  <= 0:
                    print(50 * "+++++")
                    print(style.RED + "Ezt elvétetted!")
                    print("Ellenfeledtől", ellendobas * 4,"sebzést kaptál. ")
                    print(style.RED + "Ez a harcmező lett végső nyughelyed.")
                    print("\n")
                    exit()
                elif életerő - ellendobas * 4 > 0:
                    életerő = életerő - ellendobas * 4
                    print(style.RED + "Ezt elvétetted!")
                    print("Ellenfeledtől", ellendobas * 4, "sebzést kaptál. ")
                    print(életerő, "életerőd maradt!")
                    ellendobas = int(random.randint(1, 6))
                    print("\n")


            elif dobas == ellendobas:
                print("\n")
                print(style.CYAN + "Kivédte a támadásod!")

        elif gomb == "s":
            if kaszt == "mágus":
                if tuzvarazslat == 1:
                    while gomb != -1:
                        print(style.CYAN+"Ez a varázslat egy hatalmas tűzgömböt idéz meg ami lángra borítja az ellenfeled.")
                        print(style.CYAN+"\n")
                        gomb=input("Aktiválod a tűzmágiát? (I)gen (n)em: ")
                        if gomb == "I":
                            if ellenfel-300 > 0:
                                ellenfel-=300
                                print(style.CYAN+"\n")
                                print("300 sebzést vittél be ellenfelednek!",ellenfel,"életereje maradt.")
                                tuzvarazslat-=1
                                break


                            elif ellenfel-300 <= 0:
                                print(style.CYAN+"Egy hatalmas tűzgömböt idéztél ami lángra borította az Árnykirályt. Őrjítő sikolyok közt emésztették fel a lágok. Csak a páncélja maradt hátra.")
                                dobas = -1
                                break

                        elif gomb == "n":
                            print(style.CYAN + "\n")
                            print("Esküdt ellenséged", ellendobas, "támadásponttal és", ellenfel, "életerővel rendelkezik!")
                            dobas = int(random.randint(1, 6))
                            print(dobas, "támadásponttal támadtál.")

                            if dobas > ellendobas:
                                print("\n")

                                if ellenfel - dobas * 4 * seregmoral <= 0:
                                    print(style.CYAN + "\n")
                                    print("Sikeres támadás.Bevittél", dobas * 4 * seregmoral, "sebzést!")
                                    print(style.CYAN + "Véfagyasztó üvöltés kíséretében kilehelte kárhozott lelkét...")
                                    dobas = -1
                                    zsakmany += 500
                                    break



                                elif ellenfel - dobas * 4 * seregmoral > 0:

                                    print(style.CYAN + "Sikeres támadás.")
                                    print("Bevittél", dobas * 4 * seregmoral, "sebzést!")
                                    ellenfel = ellenfel - dobas * 4 * seregmoral
                                    print("Ellenfeled", ellenfel, "életerővel rendelkezik még.")
                                    print("\n")


                            elif dobas < ellendobas:
                                if életerő - ellendobas * 4 <= 0:
                                    print(style.RED + "Ezt elvétetted!")
                                    print("Ellenfeledtől", ellendobas * 4, "sebzést kaptál. ")
                                    print(style.RED + "Ez a harcmező lett végső nyughelyed.")
                                    print("\n")
                                    print("++++++" * 50)
                                    exit()
                                elif életerő - ellendobas * 4 > 0:
                                    életerő = életerő - ellendobas * 4
                                    print(style.RED + "Ezt elvétetted!")
                                    print("Ellenfeledtől", ellendobas * 4, "sebzést kaptál. ")
                                    print(életerő, "életerőd maradt!")
                                    ellendobas = int(random.randint(1, 6))
                                    print("\n")


                            elif dobas == ellendobas:
                                print("\n")
                                print(style.CYAN + "Kivédte a támadásod!")

                            print("\n")
                            break



                        elif gomb != "I" or gomb != "n":
                            print(style.BLUE+"\n")
                            gomb = input("Aktiválod a tűzmágiát? (I)gen (nem): ")

                elif tuzvarazslat == 0:
                    print(style.RED+"Nincs több manád egy újabb varázslathoz!")
                    print(style.CYAN + "\n")
                    print("Esküdt ellenséged", ellendobas, "támadásponttal és", ellenfel, "életerővel rendelkezik!")
                    dobas = int(random.randint(1, 6))
                    print(dobas, "támadásponttal támadtál.")

                    if dobas > ellendobas:
                        print("\n")

                        if ellenfel - dobas * 4 * seregmoral <= 0:
                            print(style.CYAN + "\n")
                            print("Sikeres támadás.Bevittél", dobas * 4 * seregmoral, "sebzést!")
                            print(style.CYAN + "Véfagyasztó üvöltés kíséretében kilehelte kárhozott lelkét...")
                            dobas = -1
                            zsakmany += 500
                            break



                        elif ellenfel - dobas * 4 * seregmoral > 0:

                            print(style.CYAN + "Sikeres támadás.")
                            print("Bevittél", dobas * 4 * seregmoral, "sebzést!")
                            ellenfel = ellenfel - dobas * 4 * seregmoral
                            print("Ellenfeled", ellenfel, "életerővel rendelkezik még.")
                            print("\n")


                    elif dobas < ellendobas:
                        if életerő - ellendobas * 4 <= 0:
                            print(style.RED + "Ezt elvétetted!")
                            print("Ellenfeledtől", ellendobas * 4, "sebzést kaptál. ")
                            print(style.RED + "Ez a harcmező lett végső nyughelyed.")
                            print("\n")
                            print("++++++" * 50)
                            exit()
                        elif életerő - ellendobas * 4 > 0:
                            életerő = életerő - ellendobas * 4
                            print(style.RED + "Ezt elvétetted!")
                            print("Ellenfeledtől", ellendobas * 4, "sebzést kaptál. ")
                            print(életerő, "életerőd maradt!")
                            ellendobas = int(random.randint(1, 6))
                            print("\n")


                    elif dobas == ellendobas:
                        print("\n")
                        print(style.CYAN + "Kivédte a támadásod!")

                    print("\n")







            elif kaszt == "paladin":
                if gyogyitas == 1:
                    while gomb != -1:
                        print(style.CYAN+"\n")
                        print("Ennek a varázslatnak a segítségével életerőt tudsz elvenni és a magad gyógyítására használni.")
                        print(style.BLUE+"\n")
                        gomb=input("Aktiválod az életerő elszívást? (I)gen (n)em: ")
                        print("\n")
                        if gomb == "I":

                            if ellenfel-200 > 0:
                                ellenfel-=200
                                print(style.CYAN+"\n")
                                print("200 sebzést vittél be ellenfelednek!",ellenfel,"életereje maradt.")
                                if életerő < 100:
                                    életerő=120
                                    print(style.CYAN+"\n")
                                    print(életerő,"életerőd van")
                                    print("Életerőd is visszatöltődött, sőt...úgylátszik egy kicsit túl is teng.")
                                    gyogyitas -= 1
                                    break



                            elif ellenfel-200 <= 0:
                                print(style.CYAN+"Felemésztetted a varázslatoddal az Árnykirály életerejének utolsó cseppjeit is. Úgy porlatd el mint egy ősrégi pergamen. Csak a páncélja maradt hátra.")
                                dobas = -1
                                break

                        elif gomb == "n":
                            print(style.CYAN + "\n")
                            print("Esküdt ellenséged", ellendobas, "támadásponttal és", ellenfel, "életerővel rendelkezik!")
                            dobas = int(random.randint(1, 6))
                            print(dobas, "támadásponttal támadtál.")

                            if dobas > ellendobas:
                                print("\n")

                                if ellenfel - dobas * 4 * seregmoral <= 0:
                                    print(style.CYAN + "\n")
                                    print("Sikeres támadás.Bevittél", dobas * 4 * seregmoral, "sebzést!")
                                    print(style.CYAN + "Véfagyasztó üvöltés kíséretében kilehelte kárhozott lelkét...")
                                    dobas = -1
                                    zsakmany += 500
                                    break



                                elif ellenfel - dobas * 4 * seregmoral > 0:

                                    print(style.CYAN + "Sikeres támadás.")
                                    print("Bevittél", dobas * 4 * seregmoral, "sebzést!")
                                    ellenfel = ellenfel - dobas * 4 * seregmoral
                                    print("Ellenfeled", ellenfel, "életerővel rendelkezik még.")
                                    print("\n")


                            elif dobas < ellendobas:
                                if életerő - ellendobas *4 <= 0:
                                    print(style.RED + "Ezt elvétetted!")
                                    print("Ellenfeledtől", ellendobas * 4, "sebzést kaptál. ")
                                    print(style.RED + "Ez a harcmező lett végső nyughelyed.")
                                    print("\n")
                                    print("++++++" * 50)
                                    exit()
                                elif életerő - ellendobas * 4 > 0:
                                    életerő = életerő - ellendobas * 4
                                    print(style.RED + "Ezt elvétetted!")
                                    print("Ellenfeledtől", ellendobas * 4, "sebzést kaptál. ")
                                    print(életerő, "életerőd maradt!")
                                    ellendobas = int(random.randint(1, 6))
                                    print("\n")


                            elif dobas == ellendobas:
                                print("\n")
                                print(style.CYAN + "Kivédte a támadásod!")

                            print("\n")
                            break
                        elif gomb != "I" or gomb != "n":
                            print(style.BLUE+"\n")
                            gomb = input("Aktiválod az életerő elszívást? (I)gen (nem): ")

                elif gyogyitast == 0:
                    print(style.RED+"Nincs több erőd egy újabb varázslathoz!")
                    print(style.BLUE + "\n")
                    print("Esküdt ellenséged", ellendobas, "támadásponttal és", ellenfel, "életerővel rendelkezik!")
                    dobas = int(random.randint(1, 6))
                    print(dobas, "támadásponttal támadtál.")

                    if dobas > ellendobas:
                        print("\n")

                        if ellenfel - dobas * 4 * seregmoral <= 0:
                            print(style.CYAN + "\n")
                            print("Sikeres támadás.Bevittél", dobas * 4 * seregmoral, "sebzést!")
                            print(style.CYAN + "Véfagyasztó üvöltés kíséretében kilehelte kárhozott lelkét...")
                            dobas = -1
                            zsakmany += 500
                            break



                        elif ellenfel - dobas * 4 * seregmoral > 0:

                            print(style.CYAN+ "Sikeres támadás.")
                            print("Bevittél", dobas * 4 * seregmoral, "sebzést!")
                            ellenfel = ellenfel - dobas * 4 * seregmoral
                            print("Ellenfeled", ellenfel, "életerővel rendelkezik még.")
                            print("\n")


                    elif dobas < ellendobas:
                        if életerő - ellendobas * 4 <= 0:
                            print(style.RED + "Ezt elvétetted!")
                            print("Ellenfeledtől", ellendobas * 4, "sebzést kaptál. ")
                            print(style.RED + "Ez a harcmező lett végső nyughelyed.")
                            print("\n")
                            exit()
                        elif életerő - ellendobas * 4  > 0:
                            életerő = életerő - ellendobas * 4
                            print(style.RED + "Ezt elvétetted!")
                            print("Ellenfeledtől", ellendobas * 4, "sebzést kaptál. ")
                            print(életerő, "életerőd maradt!")
                            ellendobas = int(random.randint(1, 6))
                            print("\n")


                    elif dobas == ellendobas:
                        print("\n")
                        print(style.CYAN+"Kivédte a támadásod!")

                    print("\n")




            elif kaszt == "harcos":
                if duh == 1:
                    print(style.CYAN+"Ennek a képességnek a birtokában a harcban felgyülemlett dühödet fordítod a javadra, hatalmas pusztítást okozva az ellenfélen.",style.RED+" De akár az életed árán is...")

                    while gomb != -1:
                        gomb = input(style.BLUE + "Aktiválod a gyilkos düh képességed? Csak óvatosan, itt valaki biztosan meghal. (I)gen (n)em: ")
                        if gomb == "I":

                            print("\n")

                            if ellenfel - 400 > 0:
                                ellenfel -= 400
                                print(style.CYAN+"400 sebzést vittél be ellenfelednek!")
                                print(ellenfel,"életereje maradt.")
                                duh -= 1
                                kocka=random.randint(1,6)
                                if kocka == 2 or kocka == 6:
                                    if életerő-20 > 0:
                                        életerő-=20
                                        print(style.RED+"Te sem úsztad meg sérülés nélkül. Az árnykirály pengéje mélyen a húsodba vágott.")
                                        print("20 életerőt veszítettél, így",életerő,"életpontod maradt.")
                                        break
                                    elif életerő-20 <= 0:
                                        print(50*"+++++")
                                        print(style.RED+"Mindent feltettél a győzelem oltárára, de ez sem volt elég. Legalább nyugodt lelkiismerettel távozhatsz a túlvilágra.")
                                        exit()
                                elif ellenfel-400 <= 0:
                                    break
                            elif ellenfel - 400 <= 0:
                                print(style.CYAN + "Támadásod elsöprő volt. Hét részre hasítottad az Árnykirály testét.")
                                dobas = -1
                                break

                        elif gomb == "n":
                            print(style.CYAN + "\n")
                            print("Esküdt ellenséged", ellendobas, "támadásponttal és", ellenfel, "életerővel rendelkezik!")
                            dobas = int(random.randint(1, 6))
                            print(dobas, "támadásponttal támadtál.")

                            if dobas > ellendobas:
                                print("\n")

                                if ellenfel - dobas * 4 * seregmoral <= 0:
                                    print(style.CYAN + "\n")
                                    print("Sikeres támadás.Bevittél", dobas * 4 * seregmoral, "sebzést!")
                                    print(style.CYAN + "Véfagyasztó üvöltés kíséretében kilehelte kárhozott lelkét...")
                                    dobas = -1
                                    zsakmany += 500
                                    break



                                elif ellenfel - dobas * 4 * seregmoral > 0:

                                    print(style.CYAN + "Sikeres támadás.")
                                    print("Bevittél", dobas * 4 * seregmoral, "sebzést!")
                                    ellenfel = ellenfel - dobas * 4 * seregmoral
                                    print("Ellenfeled", ellenfel, "életerővel rendelkezik még.")
                                    print("\n")


                            elif dobas < ellendobas:
                                if életerő - ellendobas * 4 <= 0:
                                    print(style.RED + "Ezt elvétetted!")
                                    print("Ellenfeledtől", ellendobas * 4, "sebzést kaptál. ")
                                    print(style.RED + "Ez a harcmező lett végső nyughelyed.")
                                    if gyava == True:
                                        print("Az Árnykirály gúnyos mosollyal az arcán csak ennyit mormogott : Ahogy mondtam....egy gyáva sem győzhet ellenem... ")
                                    print("\n")
                                    print("++++++" * 50)
                                    exit()
                                elif életerő - ellendobas * 4 > 0:
                                    életerő = életerő - ellendobas * 4
                                    print(style.RED + "Ezt elvétetted!")
                                    print("Ellenfeledtől", ellendobas * 4, "sebzést kaptál. ")
                                    print(életerő, "életerőd maradt!")
                                    ellendobas = int(random.randint(1, 6))
                                    print("\n")


                            elif dobas == ellendobas:
                                print("\n")
                                print(style.CYAN+ "Kivédte a támadásod!")

                            print("\n")
                            break

                        elif gomb != "I" or gomb != "n":
                            gomb = input(style.BLUE+"Aktiválod az életerő elszívást? (I)gen (nem): ")

                elif duh == 0:
                    print(style.RED+"Nincs több erőd egy újabb aktiváláshoz!")
                    print(style.CYAN + "\n")
                    print("Esküdt ellenséged", ellendobas, "támadásponttal és", ellenfel, "életerővel rendelkezik!")
                    dobas = int(random.randint(1, 6))
                    print(dobas, "támadásponttal támadtál.")

                    if dobas > ellendobas:
                        print("\n")

                        if ellenfel - dobas * 3 * seregmoral <= 0:
                            print(style.CYAN + "\n")
                            print("Sikeres támadás.Bevittél", dobas * 3 * seregmoral, "sebzést!")
                            print(style.CYAN + "Véfagyasztó üvöltés kíséretében kilehelte kárhozott lelkét...")
                            dobas = -1
                            zsakmany += 500
                            break



                        elif ellenfel - dobas * 4 * seregmoral > 0:

                            print(style.CYAN + "Sikeres támadás.")
                            print("Bevittél", dobas * 4 * seregmoral, "sebzést!")
                            ellenfel = ellenfel - dobas * 4 * seregmoral
                            print("Ellenfeled", ellenfel, "életerővel rendelkezik még.")
                            print("\n")


                    elif dobas < ellendobas:
                        if életerő - ellendobas * 4 <= 0:
                            print(style.RED + "Ezt elvétetted!")
                            print("Ellenfeledtől", ellendobas * 4, "sebzést kaptál. ")
                            print(style.RED + "Ez a harcmező lett végső nyughelyed.")
                            print("\n")
                            print("++++++" * 50)
                            exit()
                        elif életerő - ellendobas * 4 > 0:
                            életerő = életerő - ellendobas * 4
                            print(style.RED + "Ezt elvétetted!")
                            print("Ellenfeledtől", ellendobas * 4, "sebzést kaptál. ")
                            print(életerő, "életerőd maradt!")
                            ellendobas = int(random.randint(1, 6))
                            print("\n")


                    elif dobas == ellendobas:
                        print("\n")
                        print(style.CYAN +"Kivédte a támadásod!")

                    print("\n")


        elif gomb == "v":
            if csel > 0:
                print(style.CYAN+"Sikeresen kivédted a támadást!")
                csel-=1
                if csel > 0:
                    print("Még", csel, "alkalommal védheted ki a támadást.")
            elif csel == 0:
                print("\n")
                print(style.RED+"Kiismerte a trükkjeid! Kár az energiáért!")
                print(style.CYAN+"\n")
                dobas = int(random.randint(1, 6))
                print(dobas, "támadásponttal támadtál.")

                if dobas > ellendobas:
                    print("\n")

                    if ellenfel - dobas * 4 * seregmoral <= 0:
                        print(style.CYAN + "\n")
                        print("Sikeres támadás.Bevittél", dobas * 4 * seregmoral, "sebzést!")
                        print(style.CYAN + "Véfagyasztó üvöltés kíséretében kilehelte kárhozott lelkét...")
                        dobas = -1
                        zsakmany += 500
                        break



                    elif ellenfel - dobas * 4 * seregmoral > 0:

                        print(style.CYAN + "Sikeres támadás.")
                        print("Bevittél", dobas * 4 * seregmoral, "sebzést!")
                        ellenfel = ellenfel - dobas * 4 * seregmoral
                        print("Ellenfeled", ellenfel, "életerővel rendelkezik még.")
                        print("\n")


                elif dobas < ellendobas:
                    if életerő - ellendobas * 4 <= 0:
                        print(style.RED + "Ezt elvétetted!")
                        print("Ellenfeledtől", ellendobas * 4, "sebzést kaptál. ")
                        print(style.RED + "Ez a harcmező lett végső nyughelyed.")
                        print("\n")
                        exit()
                    elif életerő - ellendobas * 4 > 0:
                        életerő = életerő - ellendobas * 4
                        print(style.RED + "Ezt elvétetted!")
                        print("Ellenfeledtől", ellendobas * 4, "sebzést kaptál. ")
                        print(életerő, "életerőd maradt!")
                        ellendobas = int(random.randint(1, 6))
                        print("\n")


                elif dobas == ellendobas:
                    print("\n")
                    print(style.CYAN + "Kivédte a támadásod!")



        elif gomb != "t" or gomb != "s" or gomb != "v":
            print("\n")
            print(style.RED+"Talán megsérült a kezed hogy nem tudsz írni?")
else:
    print(style.RED+"Egy bátor harcos, aki nem futamodik meg?! Na lássuk mire lesz elég a bátorságod ellenem! ")
    while dobas != -1:
        ellendobas = int(random.randint(1, 6))

        print(style.CYAN + "\n")
        print("Esküdt ellenséged", ellendobas, "támadásponttal és", ellenfel, "életerővel rendelkezik!")
        print(style.BLUE+"\n")
        gomb = input("Mit teszel: (t)ámadsz  (s)egítségül hívod a Fényt, vagy (v)édekezel?")
        print("\n")
        if gomb == "t":
            dobas = int(random.randint(1, 6))
            print(style.CYAN+"\n")
            print(dobas, "támadásponttal támadtál.")

            if dobas > ellendobas:
                print("\n")

                if ellenfel - dobas * 3 * seregmoral <= 0:
                    print(style.BLUE + "\n")
                    print("Sikeres támadás. Bevittél", dobas * 3 * seregmoral, "sebzést!")
                    print(style.CYAN + "Véfagyasztó üvöltés kíséretében kilehelte kárhozott lelkét...")
                    dobas = -1
                    zsakmany += 500
                    break



                elif ellenfel - dobas * 4 * seregmoral> 0:

                    print(style.CYAN + "Sikeres támadás.")
                    print("Bevittél", dobas * 4 * seregmoral, "sebzést!")
                    ellenfel = ellenfel - dobas * 4 * seregmoral
                    print("Ellenfeled", ellenfel, "életerővel rendelkezik még.")
                    print("\n")


            elif dobas < ellendobas:
                if életerő - ellendobas * 4  <= 0:
                    print(50 * "+++++")
                    print(style.RED + "Ezt elvétetted!")
                    print("Ellenfeledtől", ellendobas * 4,"sebzést kaptál. ")
                    print(style.RED + "Ez a harcmező lett végső nyughelyed.")
                    print("\n")
                    exit()
                elif életerő - ellendobas * 4 > 0:
                    életerő = életerő - ellendobas * 4
                    print(style.RED + "Ezt elvétetted!")
                    print("Ellenfeledtől", ellendobas * 4, "sebzést kaptál. ")
                    print(életerő, "életerőd maradt!")
                    ellendobas = int(random.randint(1, 6))
                    print("\n")


            elif dobas == ellendobas:
                print("\n")
                print(style.CYAN + "Kivédte a támadásod!")

        elif gomb == "s":
            if kaszt == "mágus":
                if tuzvarazslat == 1:
                    while gomb != -1:
                        print(style.CYAN+"Ez a varázslat egy hatalmas tűzgömböt idéz meg ami lángra borítja az ellenfeled.")
                        print(style.CYAN+"\n")
                        gomb=input("Aktiválod a tűzmágiát? (I)gen (n)em: ")
                        if gomb == "I":
                            if ellenfel-300 > 0:
                                ellenfel-=300
                                print(style.CYAN+"\n")
                                print("300 sebzést vittél be ellenfelednek!",ellenfel,"életereje maradt.")
                                tuzvarazslat-=1
                                break


                            elif ellenfel-300 <= 0:
                                print(style.CYAN+"Egy hatalmas tűzgömböt idéztél ami lángra borította az Árnykirályt. Őrjítő sikolyok közt emésztették fel a lágok. Csak a páncélja maradt hátra.")
                                dobas = -1
                                break

                        elif gomb == "n":
                            print(style.CYAN + "\n")
                            print("Esküdt ellenséged", ellendobas, "támadásponttal és", ellenfel, "életerővel rendelkezik!")
                            dobas = int(random.randint(1, 6))
                            print(dobas, "támadásponttal támadtál.")

                            if dobas > ellendobas:
                                print("\n")

                                if ellenfel - dobas * 4 * seregmoral <= 0:
                                    print(style.CYAN + "\n")
                                    print("Sikeres támadás.Bevittél", dobas * 4 * seregmoral, "sebzést!")
                                    print(style.CYAN + "Véfagyasztó üvöltés kíséretében kilehelte kárhozott lelkét...")
                                    dobas = -1
                                    zsakmany += 500
                                    break



                                elif ellenfel - dobas * 4 * seregmoral > 0:

                                    print(style.CYAN + "Sikeres támadás.")
                                    print("Bevittél", dobas * 4 * seregmoral, "sebzést!")
                                    ellenfel = ellenfel - dobas * 4 * seregmoral
                                    print("Ellenfeled", ellenfel, "életerővel rendelkezik még.")
                                    print("\n")


                            elif dobas < ellendobas:
                                if életerő - ellendobas * 4 <= 0:
                                    print(style.RED + "Ezt elvétetted!")
                                    print("Ellenfeledtől", ellendobas * 4, "sebzést kaptál. ")
                                    print(style.RED + "Ez a harcmező lett végső nyughelyed.")
                                    print("\n")
                                    print("++++++" * 50)
                                    exit()
                                elif életerő - ellendobas * 4 > 0:
                                    életerő = életerő - ellendobas * 4
                                    print(style.RED + "Ezt elvétetted!")
                                    print("Ellenfeledtől", ellendobas * 4, "sebzést kaptál. ")
                                    print(életerő, "életerőd maradt!")
                                    ellendobas = int(random.randint(1, 6))
                                    print("\n")


                            elif dobas == ellendobas:
                                print("\n")
                                print(style.CYAN + "Kivédte a támadásod!")

                            print("\n")
                            break



                        elif gomb != "I" or gomb != "n":
                            print(style.BLUE+"\n")
                            gomb = input("Aktiválod a tűzmágiát? (I)gen (nem): ")

                elif tuzvarazslat == 0:
                    print(style.RED+"Nincs több manád egy újabb varázslathoz!")
                    print(style.CYAN + "\n")
                    print("Esküdt ellenséged", ellendobas, "támadásponttal és", ellenfel, "életerővel rendelkezik!")
                    dobas = int(random.randint(1, 6))
                    print(dobas, "támadásponttal támadtál.")

                    if dobas > ellendobas:
                        print("\n")

                        if ellenfel - dobas * 4 * seregmoral <= 0:
                            print(style.CYAN + "\n")
                            print("Sikeres támadás.Bevittél", dobas * 4 * seregmoral, "sebzést!")
                            print(style.CYAN + "Véfagyasztó üvöltés kíséretében kilehelte kárhozott lelkét...")
                            dobas = -1
                            zsakmany += 500
                            break



                        elif ellenfel - dobas * 4 * seregmoral > 0:

                            print(style.CYAN + "Sikeres támadás.")
                            print("Bevittél", dobas * 4 * seregmoral, "sebzést!")
                            ellenfel = ellenfel - dobas * 4 * seregmoral
                            print("Ellenfeled", ellenfel, "életerővel rendelkezik még.")
                            print("\n")


                    elif dobas < ellendobas:
                        if életerő - ellendobas * 4 <= 0:
                            print(style.RED + "Ezt elvétetted!")
                            print("Ellenfeledtől", ellendobas * 4, "sebzést kaptál. ")
                            print(style.RED + "Ez a harcmező lett végső nyughelyed.")
                            print("\n")
                            print("++++++" * 50)
                            exit()
                        elif életerő - ellendobas * 4 > 0:
                            életerő = életerő - ellendobas * 4
                            print(style.RED + "Ezt elvétetted!")
                            print("Ellenfeledtől", ellendobas * 4, "sebzést kaptál. ")
                            print(életerő, "életerőd maradt!")
                            ellendobas = int(random.randint(1, 6))
                            print("\n")


                    elif dobas == ellendobas:
                        print("\n")
                        print(style.CYAN + "Kivédte a támadásod!")

                    print("\n")







            elif kaszt == "paladin":
                if gyogyitas == 1:
                    while gomb != -1:
                        print(style.CYAN+"\n")
                        print("Ennek a varázslatnak a segítségével életerőt tudsz elvenni és a magad gyógyítására használni.")
                        print(style.BLUE+"\n")
                        gomb=input("Aktiválod az életerő elszívást? (I)gen (n)em: ")
                        print("\n")
                        if gomb == "I":

                            if ellenfel-200 > 0:
                                ellenfel-=200
                                print(style.CYAN+"\n")
                                print("200 sebzést vittél be ellenfelednek!",ellenfel,"életereje maradt.")
                                if életerő < 100:
                                    életerő=120
                                    print(style.CYAN+"\n")
                                    print(életerő,"életerőd van")
                                    print("Életerőd is visszatöltődött, sőt...úgylátszik egy kicsit túl is teng.")
                                    gyogyitas -= 1
                                    break



                            elif ellenfel-200 <= 0:
                                print(style.CYAN+"Felemésztetted a varázslatoddal az Árnykirály életerejének utolsó cseppjeit is. Úgy porlatd el mint egy ősrégi pergamen. Csak a páncélja maradt hátra.")
                                dobas = -1
                                break

                        elif gomb == "n":
                            print(style.CYAN + "\n")
                            print("Esküdt ellenséged", ellendobas, "támadásponttal és", ellenfel, "életerővel rendelkezik!")
                            dobas = int(random.randint(1, 6))
                            print(dobas, "támadásponttal támadtál.")

                            if dobas > ellendobas:
                                print("\n")

                                if ellenfel - dobas * 4 * seregmoral <= 0:
                                    print(style.CYAN + "\n")
                                    print("Sikeres támadás.Bevittél", dobas * 4 * seregmoral, "sebzést!")
                                    print(style.CYAN + "Véfagyasztó üvöltés kíséretében kilehelte kárhozott lelkét...")
                                    dobas = -1
                                    zsakmany += 500
                                    break



                                elif ellenfel - dobas * 4 * seregmoral > 0:

                                    print(style.CYAN + "Sikeres támadás.")
                                    print("Bevittél", dobas * 4 * seregmoral, "sebzést!")
                                    ellenfel = ellenfel - dobas * 4 * seregmoral
                                    print("Ellenfeled", ellenfel, "életerővel rendelkezik még.")
                                    print("\n")


                            elif dobas < ellendobas:
                                if életerő - ellendobas *4 <= 0:
                                    print(style.RED + "Ezt elvétetted!")
                                    print("Ellenfeledtől", ellendobas * 4, "sebzést kaptál. ")
                                    print(style.RED + "Ez a harcmező lett végső nyughelyed.")
                                    print("\n")
                                    print("++++++" * 50)
                                    exit()
                                elif életerő - ellendobas * 4 > 0:
                                    életerő = életerő - ellendobas * 4
                                    print(style.RED + "Ezt elvétetted!")
                                    print("Ellenfeledtől", ellendobas * 4, "sebzést kaptál. ")
                                    print(életerő, "életerőd maradt!")
                                    ellendobas = int(random.randint(1, 6))
                                    print("\n")


                            elif dobas == ellendobas:
                                print("\n")
                                print(style.CYAN + "Kivédte a támadásod!")

                            print("\n")
                            break
                        elif gomb != "I" or gomb != "n":
                            print(style.BLUE+"\n")
                            gomb = input("Aktiválod az életerő elszívást? (I)gen (nem): ")

                elif gyogyitast == 0:
                    print(style.RED+"Nincs több erőd egy újabb varázslathoz!")
                    print(style.BLUE + "\n")
                    print("Esküdt ellenséged", ellendobas, "támadásponttal és", ellenfel, "életerővel rendelkezik!")
                    dobas = int(random.randint(1, 6))
                    print(dobas, "támadásponttal támadtál.")

                    if dobas > ellendobas:
                        print("\n")

                        if ellenfel - dobas * 4 * seregmoral <= 0:
                            print(style.CYAN + "\n")
                            print("Sikeres támadás.Bevittél", dobas * 4 * seregmoral, "sebzést!")
                            print(style.CYAN + "Véfagyasztó üvöltés kíséretében kilehelte kárhozott lelkét...")
                            dobas = -1
                            zsakmany += 500
                            break



                        elif ellenfel - dobas * 4 * seregmoral > 0:

                            print(style.CYAN+ "Sikeres támadás.")
                            print("Bevittél", dobas * 4 * seregmoral, "sebzést!")
                            ellenfel = ellenfel - dobas * 4 * seregmoral
                            print("Ellenfeled", ellenfel, "életerővel rendelkezik még.")
                            print("\n")


                    elif dobas < ellendobas:
                        if életerő - ellendobas * 4 <= 0:
                            print(style.RED + "Ezt elvétetted!")
                            print("Ellenfeledtől", ellendobas * 4, "sebzést kaptál. ")
                            print(style.RED + "Ez a harcmező lett végső nyughelyed.")
                            print("\n")
                            print("++++++" * 50)
                            exit()
                        elif életerő - ellendobas * 4  > 0:
                            életerő = életerő - ellendobas * 4
                            print(style.RED + "Ezt elvétetted!")
                            print("Ellenfeledtől", ellendobas * 4, "sebzést kaptál. ")
                            print(életerő, "életerőd maradt!")
                            ellendobas = int(random.randint(1, 6))
                            print("\n")


                    elif dobas == ellendobas:
                        print("\n")
                        print(style.CYAN+"Kivédte a támadásod!")

                    print("\n")




            elif kaszt == "harcos":
                if duh == 1:
                    print(style.CYAN+"Ennek a képességnek a birtokában a harcban felgyülemlett dühödet fordítod a javadra, hatalmas pusztítást okozva az ellenfélen.",style.RED+" De akár az életed árán is...")

                    while gomb != -1:
                        gomb = input(style.BLUE + "Aktiválod a gyilkos düh képességed? Csak óvatosan, itt valaki biztosan meghal. (I)gen (n)em: ")
                        if gomb == "I":

                            print("\n")

                            if ellenfel - 400 > 0:
                                ellenfel -= 400
                                print(style.CYAN+"400 sebzést vittél be ellenfelednek!")
                                print(ellenfel,"életereje maradt.")
                                duh -= 1
                                kocka=random.randint(1,6)
                                if kocka == 2 or kocka == 6:
                                    if életerő-20 > 0:
                                        életerő-=20
                                        print(style.RED+"Te sem úsztad meg sérülés nélkül. Az árnykirály pengéje mélyen a húsodba vágott.")
                                        print("20 életerőt veszítettél, így",életerő,"életpontod maradt.")
                                        break
                                    elif életerő-20 <= 0:
                                        print(50*"+++++")
                                        print(style.RED+"Mindent feltettél a győzelem oltárára, de ez sem volt elég. Legalább nyugodt lelkiismerettel távozhatsz a túlvilágra.")
                                        print("\n\n")
                                        print("++++++" * 50)
                                        exit()
                                elif ellenfel-400 <= 0:
                                    break
                            elif ellenfel - 400 <= 0:
                                print(style.CYAN + "Támadásod elsöprő volt. Hét részre hasítottad az Árnykirály testét.")
                                dobas = -1
                                break

                        elif gomb == "n":
                            print(style.CYAN + "\n")
                            print("Esküdt ellenséged", ellendobas, "támadásponttal és", ellenfel, "életerővel rendelkezik!")
                            dobas = int(random.randint(1, 6))
                            print(dobas, "támadásponttal támadtál.")

                            if dobas > ellendobas:
                                print("\n")

                                if ellenfel - dobas * 4 * seregmoral <= 0:
                                    print(style.CYAN + "\n")
                                    print("Sikeres támadás.Bevittél", dobas * 4 * seregmoral, "sebzést!")
                                    print(style.CYAN + "Véfagyasztó üvöltés kíséretében kilehelte kárhozott lelkét...")
                                    dobas = -1
                                    zsakmany += 500
                                    break



                                elif ellenfel - dobas * 4 * seregmoral > 0:

                                    print(style.CYAN + "Sikeres támadás.")
                                    print("Bevittél", dobas * 4 * seregmoral, "sebzést!")
                                    ellenfel = ellenfel - dobas * 4 * seregmoral
                                    print("Ellenfeled", ellenfel, "életerővel rendelkezik még.")
                                    print("\n")


                            elif dobas < ellendobas:
                                if életerő - ellendobas * 4 <= 0:
                                    print(style.RED + "Ezt elvétetted!")
                                    print("Ellenfeledtől", ellendobas * 4, "sebzést kaptál. ")
                                    print(style.RED + "Ez a harcmező lett végső nyughelyed.")
                                    if gyava == True:
                                        print("Az Árnykirály gúnyos mosollyal az arcán csak ennyit mormogott : Ahogy mondtam....egy gyáva sem győzhet ellenem. ")
                                    print("\n")
                                    exit()
                                elif életerő - ellendobas * 4 > 0:
                                    életerő = életerő - ellendobas * 4
                                    print(style.RED + "Ezt elvétetted!")
                                    print("Ellenfeledtől", ellendobas * 4, "sebzést kaptál. ")
                                    print(életerő, "életerőd maradt!")
                                    ellendobas = int(random.randint(1, 6))
                                    print("\n")


                            elif dobas == ellendobas:
                                print("\n")
                                print(style.CYAN+ "Kivédte a támadásod!")

                            print("\n")
                            break

                        elif gomb != "I" or gomb != "n":
                            gomb = input(style.BLUE+"Aktiválod az életerő elszívást? (I)gen (nem): ")

                elif duh == 0:
                    print(style.RED+"Nincs több erőd egy újabb aktiváláshoz!")
                    print(style.CYAN + "\n")
                    print("Esküdt ellenséged", ellendobas, "támadásponttal és", ellenfel, "életerővel rendelkezik!")
                    dobas = int(random.randint(1, 6))
                    print(dobas, "támadásponttal támadtál.")

                    if dobas > ellendobas:
                        print("\n")

                        if ellenfel - dobas * 4 * seregmoral <= 0:
                            print(style.CYAN + "\n")
                            print("Sikeres támadás.Bevittél", dobas * 4 * seregmoral, "sebzést!")
                            print(style.CYAN + "Véfagyasztó üvöltés kíséretében kilehelte kárhozott lelkét...")
                            dobas = -1
                            zsakmany += 500
                            break



                        elif ellenfel - dobas * 4 * seregmoral > 0:

                            print(style.CYAN + "Sikeres támadás.")
                            print("Bevittél", dobas * 4 * seregmoral, "sebzést!")
                            ellenfel = ellenfel - dobas * 4 * seregmoral
                            print("Ellenfeled", ellenfel, "életerővel rendelkezik még.")
                            print("\n")


                    elif dobas < ellendobas:
                        if életerő - ellendobas * 4 <= 0:
                            print(style.RED + "Ezt elvétetted!")
                            print("Ellenfeledtől", ellendobas * 4, "sebzést kaptál. ")
                            print(style.RED + "Ez a harcmező lett végső nyughelyed.")
                            print("\n")
                            print("++++++" * 50)
                            exit()
                        elif életerő - ellendobas * 4 > 0:
                            életerő = életerő - ellendobas * 4
                            print(style.RED + "Ezt elvétetted!")
                            print("Ellenfeledtől", ellendobas * 4, "sebzést kaptál. ")
                            print(életerő, "életerőd maradt!")
                            ellendobas = int(random.randint(1, 6))
                            print("\n")


                    elif dobas == ellendobas:
                        print("\n")
                        print(style.CYAN +"Kivédte a támadásod!")

                    print("\n")


        elif gomb == "v":
            if csel > 0:
                print(style.CYAN+"Sikeresen kivédted a támadást!")
                csel-=1
                if csel > 0:
                    print("Még", csel, "alkalommal védheted ki a támadást.")
            elif csel == 0:
                print("\n")
                print(style.RED+"Kiismerte a trükkjeid! Kár az energiáért!")
                print(style.CYAN+"\n")
                dobas = int(random.randint(1, 6))
                print(dobas, "támadásponttal támadtál.")

                if dobas > ellendobas:
                    print("\n")

                    if ellenfel - dobas * 4 * seregmoral <= 0:
                        print(style.CYAN + "\n")
                        print("Sikeres támadás.Bevittél", dobas * 4 * seregmoral, "sebzést!")
                        print(style.CYAN + "Véfagyasztó üvöltés kíséretében kilehelte kárhozott lelkét...")
                        dobas = -1
                        zsakmany += 500
                        break



                    elif ellenfel - dobas * 4 * seregmoral > 0:

                        print(style.CYAN + "Sikeres támadás.")
                        print("Bevittél", dobas * 4 * seregmoral, "sebzést!")
                        ellenfel = ellenfel - dobas * 4 * seregmoral
                        print("Ellenfeled", ellenfel, "életerővel rendelkezik még.")
                        print("\n")


                elif dobas < ellendobas:
                    if életerő - ellendobas * 4 <= 0:
                        print(style.RED + "Ezt elvétetted!")
                        print("Ellenfeledtől", ellendobas * 4, "sebzést kaptál. ")
                        print(style.RED + "Ez a harcmező lett végső nyughelyed.")
                        print("\n")
                        print("++++++" * 50)
                        exit()
                    elif életerő - ellendobas * 4 > 0:
                        életerő = életerő - ellendobas * 4
                        print(style.RED + "Ezt elvétetted!")
                        print("Ellenfeledtől", ellendobas * 4, "sebzést kaptál. ")
                        print(életerő, "életerőd maradt!")
                        ellendobas = int(random.randint(1, 6))
                        print("\n")


                elif dobas == ellendobas:
                    print("\n")
                    print(style.CYAN + "Kivédte a támadásod!")



        elif gomb != "t" or gomb != "s" or gomb != "v":
            print("\n")
            print(style.RED+"Talán megsérült a kezed hogy nem tudsz írni?")


print(style.CYAN+"\n\n\n")

sereg+=200
print("Ahogy legyőzted az Árnykirályt, sok harcosa aki eddig csak egy bűbáj hatása miatt szolgálta, átállt az oldaladra. Az így megnőtt létszámmal megsemmisítő csapást mértél a hű csatlósokra.")
print("++++++"*50)
print("\n\n\n")
print("Eljött ez a nap is végre. Újra a fény vette át a sötétség helyét.")
print(sereg,"harcosoddal és",zsakmany," zsák arannyal indultál haza.")
print("A város főterén ünneplő tömeg várta a megfáradt de győztes sereget.")
print("Ahogy végignéztél a sok boldog arcon, belül érezted: ezért megérte.")
print("\n\n")
print("++++++"*50)



