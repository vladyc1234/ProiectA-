"""
Observatie pentru cei absenti la laborator: trebuie sa dati enter după fiecare afișare a cozii până vă apare o soluție. Afișarea era ca să vedem progresul algoritmului. Puteți să o dezactivați comentând print-ul cu coada și input()
"""
import cProfile
import time
from copy import deepcopy
import heapq

time2 = time.time()
time1 = time.time()

# timpTimeout = int(input())

def invartitor(stareInitiala, i, j):
    butoane = ['@', '>', '^', '#']
    tempList = []
    result = []

    if i - 1 > -1 and j + 1 < len(stareInitiala[0]):
        tempList.append(stareInitiala[i - 1][j + 1])
    if j + 1 < len(stareInitiala[0]):
        tempList.append(stareInitiala[i][j + 1])
    if i + 1 < len(stareInitiala) and j + 1 < len(stareInitiala[0]):
        tempList.append(stareInitiala[i + 1][j + 1])
    if i + 1 < len(stareInitiala):
        tempList.append(stareInitiala[i + 1][j])
    if i + 1 < len(stareInitiala) and j - 1 > -1:
        tempList.append(stareInitiala[i + 1][j - 1])
    if j - 1 > -1:
        tempList.append(stareInitiala[i][j - 1])
    if i - 1 > -1 and j - 1 > -1:
        tempList.append(stareInitiala[i - 1][j - 1])
    if i - 1 > -1:
        tempList.append(stareInitiala[i - 1][j])


    cTempList = tempList[:]
    x = 0
    dreaptaLim = 0
    cTempList.append('.')
    while cTempList[x] in butoane:
        dreaptaLim += 1
        x += 1
    x = len(cTempList) - 2
    while x > -1 + dreaptaLim:
        if cTempList[x] in butoane:
            dreapta = 1
            while cTempList[x] in butoane and x > -1 + dreaptaLim:
                x -= 1
                dreapta += 1
            while cTempList[(x + dreapta) % len(cTempList)] in butoane:
                dreapta += 1
            cTempList[(x + dreapta) % len(cTempList)] = cTempList[x]
        else:
            cTempList[x + 1] = cTempList[x]
        x -= 1

    cTempList[dreaptaLim] = cTempList[-1]
    cTempList = cTempList[:-1]

    tempNod1 = deepcopy(stareInitiala)

    index = 0
    if i - 1 > -1 and j + 1 < len(stareInitiala[0]):
        tempNod1[i - 1][j + 1] = cTempList[index]
        index += 1
    if j + 1 < len(stareInitiala[0]):
        tempNod1[i][j + 1] = cTempList[index]
        index += 1
    if i + 1 < len(stareInitiala) and j + 1 < len(stareInitiala[0]):
        tempNod1[i + 1][j + 1] = cTempList[index]
        index += 1
    if i + 1 < len(stareInitiala):
        tempNod1[i + 1][j] = cTempList[index]
        index += 1
    if i + 1 < len(stareInitiala) and j - 1 > -1:
        tempNod1[i + 1][j - 1] = cTempList[index]
        index += 1
    if j - 1 > -1 and len(cTempList) > 5:
        tempNod1[i][j - 1] = cTempList[index]
        index += 1
    if i - 1 > -1 and j - 1 > -1:
        tempNod1[i - 1][j - 1] = cTempList[index]
        index += 1
    if i - 1 > -1:
        tempNod1[i - 1][j] = cTempList[index]
        index += 1

    result.append(tempNod1[:])

    cTempList = tempList[:]
    cTempList.insert(0, '.')
    x = 1
    stangaLim = 0
    while cTempList[-x] in butoane:
        stangaLim += 1
        x += 1
    x = 1

    while x < len(cTempList) - stangaLim:
        if cTempList[x] in butoane:
            stanga = 1
            while cTempList[x] in butoane and x < len(cTempList) - stangaLim:
                x += 1
                stanga += 1
            while cTempList[x - stanga] in butoane:
                stanga += 1
            cTempList[x - stanga] = cTempList[x]
        else:
            cTempList[x - 1] = cTempList[x]
        x += 1

    cTempList[-stangaLim - 1] = cTempList[0]
    cTempList = cTempList[1:]

    tempNod2 = deepcopy(tempNod1)

    index = 0
    if i - 1 > -1 and j + 1 < len(stareInitiala[0]):
        tempNod2[i - 1][j + 1] = cTempList[index]
        index += 1
    if j + 1 < len(stareInitiala[0]):
        tempNod2[i][j + 1] = cTempList[index]
        index += 1
    if i + 1 < len(stareInitiala) and j + 1 < len(stareInitiala[0]):
        tempNod2[i + 1][j + 1] = cTempList[index]
        index += 1
    if i + 1 < len(stareInitiala):
        tempNod2[i + 1][j] = cTempList[index]
        index += 1
    if i + 1 < len(stareInitiala) and j - 1 > -1:
        tempNod2[i + 1][j - 1] = cTempList[index]
        index += 1
    if j - 1 > -1 and len(cTempList) > 5:
        tempNod2[i][j - 1] = cTempList[index]
        index += 1
    if i - 1 > -1 and j - 1 > -1:
        tempNod2[i - 1][j - 1] = cTempList[index]
        index += 1
    if i - 1 > -1:
        tempNod2[i - 1][j] = cTempList[index]
        index += 1

    result.append(tempNod2[:])

    count = 0

    for x in tempList:
        if x not in butoane:
            count += 1

    return result, count


def interschimbator(stareInitiala, i, j):
    butoane = ['@', '>', '^', '#']
    tempList = []

    result = []
    if i - 1 > -1 and j + 1 < len(stareInitiala[0]):
        tempList.append(stareInitiala[i - 1][j + 1])
    if j + 1 < len(stareInitiala[0]):
        tempList.append(stareInitiala[i][j + 1])
    if i + 1 < len(stareInitiala) and j + 1 < len(stareInitiala[0]):
        tempList.append(stareInitiala[i + 1][j + 1])
    if i + 1 < len(stareInitiala):
        tempList.append(stareInitiala[i + 1][j])
    if i + 1 < len(stareInitiala) and j - 1 > -1:
        tempList.append(stareInitiala[i + 1][j - 1])
    if j - 1 > -1:
        tempList.append(stareInitiala[i][j - 1])
    if i - 1 > -1 and j - 1 > -1:
        tempList.append(stareInitiala[i - 1][j - 1])
    if i - 1 > -1:
        tempList.append(stareInitiala[i - 1][j])

    if len(tempList) > 4:
        for x in range(0, len(tempList) - 4):
            cTempList = tempList[:]

            if (cTempList[x] and cTempList[x + 4]) not in butoane:
                cTempList[x], cTempList[x + 4] = cTempList[x + 4], cTempList[x]

                tempNod = deepcopy(stareInitiala)

                index = 0
                if i - 1 > -1 and j + 1 < len(stareInitiala[0]):
                    tempNod[i - 1][j + 1] = cTempList[index]
                    index += 1
                    if j + 1 < len(stareInitiala[0]):
                        tempNod[i][j + 1] = cTempList[index]
                        index += 1
                    if i + 1 < len(stareInitiala) and j + 1 < len(stareInitiala[0]):
                        tempNod[i + 1][j + 1] = cTempList[index]
                        index += 1
                    if i + 1 < len(stareInitiala):
                        tempNod[i + 1][j] = cTempList[index]
                        index += 1
                    if i + 1 < len(stareInitiala) and j - 1 > -1:
                        tempNod[i + 1][j - 1] = cTempList[index]
                        index += 1
                    if j - 1 > -1 and len(cTempList) > 5:
                        tempNod[i][j - 1] = cTempList[index]
                        index += 1
                    if i - 1 > -1 and j - 1 > -1:
                        tempNod[i - 1][j - 1] = cTempList[index]
                        index += 1
                    if i - 1 > -1:
                        tempNod[i - 1][j] = cTempList[index]
                        index += 1

            result.append(tempNod[:])

    return result


def urcator(stareInitiala, i, j):
    butoane = ['@', '>', '^', '#']
    tempList = [row[j] for row in stareInitiala]
    result = []

    B = 0
    for x in tempList:
        if x in butoane:
            B += 1
    K = len(stareInitiala) - B - 1

    cTempList = tempList[:]
    cTempList.insert(0, '.')
    x = 1
    stangaLim = 0
    while cTempList[-x] in butoane:
        stangaLim += 1
        x += 1

    while K != 0:
        x = 1
        while x < len(cTempList) - stangaLim:
            if cTempList[x] in butoane:
                stanga = 1
                while cTempList[x] in butoane and x < len(cTempList) - stangaLim:
                    x += 1
                    stanga += 1
                while cTempList[x - stanga] in butoane:
                    stanga += 1
                cTempList[x - stanga] = cTempList[x]
            else:
                cTempList[x - 1] = cTempList[x]
            x += 1

        cTempList[-stangaLim - 1] = cTempList[0]
        cTempList = cTempList[1:]

        K -= 1

        tempNod = deepcopy(stareInitiala)

        for x in range(0, len(tempNod)):
            tempNod[x][j] = cTempList[x]

        result.append(tempNod[:])

        cTempList.insert(0, '.')

    return result


def dreptator(stareInitiala, i, j):
    butoane = ['@', '>', '^', '#']
    tempList = stareInitiala[i]
    result = []

    B = 0
    for x in tempList:
        if x in butoane:
            B += 1
    K = len(stareInitiala[0]) - B - 1

    cTempList = tempList[:]
    x = 0
    dreaptaLim = 0
    while cTempList[x] in butoane:
        dreaptaLim += 1
        x += 1
    cTempList.append('.')

    while K != 0:
        x = len(cTempList) - 2

        while x > -1 + dreaptaLim:
            if cTempList[x] in butoane:
                dreapta = 1
                while cTempList[x] in butoane and x > -1 + dreaptaLim:
                    x -= 1
                    dreapta += 1
                while cTempList[(x + dreapta) % len(cTempList)] in butoane:
                    dreapta += 1
                cTempList[(x + dreapta) % len(cTempList)] = cTempList[x]
            else:
                cTempList[x + 1] = cTempList[x]
            x -= 1

        cTempList[dreaptaLim] = cTempList[-1]
        cTempList = cTempList[:-1]

        K -= 1

        tempNod = deepcopy(stareInitiala)

        tempNod[i] = deepcopy(cTempList[:])

        result.append(tempNod[:])
        cTempList.append('.')

    return result


class NodParcurgere:
    graf = None  # static

    def __init__(self, id, info, parinte, cost=0, h=0, buton ="", activare=0):
        self.id = id  # este indicele din vectorul de noduri
        self.info = info
        self.parinte = parinte  # parintele din arborele de parcurgere
        self.g = cost  # costul de la radacina la nodul curent
        self.h = h
        self.f = self.g + self.h
        self.buton = buton
        self.activare = activare

    def obtineDrum(self):
        l = [self.printInfo()]
        butonL = [(self.buton,self.activare)]
        costL = [self.g]
        nod = self
        while nod.parinte is not None:
            l.insert(0, nod.parinte.printInfo())
            butonL.insert(0, (nod.parinte.buton, nod.parinte.activare))
            costL.insert(0, nod.parinte.g)
            nod = nod.parinte
        return l, butonL, costL

    def afisDrum(self):  # returneaza si lungimea drumului
        l, butonL, costL = self.obtineDrum()
        print(str(1) + ")")
        print(l[0] + "Cost: 0")
        for i in range(1, len(l)):
            if butonL[i][0] == '@' and butonL[i][1] == 1:
                print("Se activeaza invartitorul la dreapta")
            elif butonL[i][0] == '@' and butonL[i][1] == 2:
                print("Se activeaza invartitorul la stanga")
            elif butonL[i][0] == '#' and (butonL[i][1] == 1 or butonL[i][1] == 3):
                print("Se activeaza schimbatorul pe diagonala")
            elif butonL[i][0] == '#' and butonL[i][1] == 2:
                print("Se activeaza schimbatorul pe orizontala")
            elif butonL[i][0] == '#' and butonL[i][1] == 4:
                print("Se activeaza schimbatorul pe verticala")
            elif butonL[i][0] == '^':
                print("Se activeaza urcatorul cu " + str(butonL[i][1]) + " pasi")
            elif butonL[i][0] == '>':
                print("Se activeaza dreptatorul cu " + str(butonL[i][1]) + " pasi")
            print()
            print(str(i+1) + ")")
            print(l[i] + "Cost: " + str(sum(costL[:i+1])))
            print()
        return len(l)

    def contineInDrum(self, infoNodNou):
        nodDrum = self
        while nodDrum is not None:
            if (infoNodNou == nodDrum.info):
                return True
            nodDrum = nodDrum.parinte

        return False

    def printInfo(self):
        sir = ""
        for i in self.info:
            for j in i:
                sir += j + " "
            sir += "\n"
        return sir

    def __repr__(self):
        sir = ""
        sir += self.printInfo() + "("
        sir += "id = {}, ".format(self.id)
        sir += " g:{}".format(self.g)
        sir += " h:{}".format(self.h)

        sir += " f:{})".format(self.f)
        return (sir)


class Graph:  # graful problemei
    def __init__(self, start, scopuri, lista_h=[]):
        self.start = start
        self.scopuri = scopuri
        self.lista_h = lista_h

    def testeaza_scop(self, nodCurent):
        checkCuvinte = [0] * len(self.scopuri)
        for i in range(0, len(nodCurent.info)):
            testLinie = "".join(nodCurent.info[i])
            for j in range(0, len(self.scopuri)):
                if testLinie.find(self.scopuri[j]) > -1:
                    checkCuvinte[j] = 1
        for i in range(0, len(nodCurent.info[0])):
            testColoana = "".join([row[i] for row in nodCurent.info])
            for j in range(0, len(self.scopuri)):
                if testColoana.find(self.scopuri[j]) > -1:
                    checkCuvinte[j] = 1
        if 0 not in checkCuvinte:
            return 1
        else:
            return 0

    # va genera succesorii sub forma de noduri in arborele de parcurgere
    def genereazaSuccesori(self, nodCurent, id):
        listaSuccesori = []
        for i in range(0, len(nodCurent.info)):
            for j in range(0, len(nodCurent.info[0])):
                if nodCurent.info[i][j] == '@':
                    inv = 1
                    list, cost = invartitor(nodCurent.info, i, j)
                    for ls in list:
                        nodNou = NodParcurgere(id, deepcopy(ls), nodCurent, cost=cost, buton='@', activare=inv)
                        nodNou.h = graf.calculeaza_h(nodNou)
                        nodNou.f = nodNou.g + nodNou.h
                        id += 1
                        inv += 1
                        listaSuccesori.append(nodNou)
                elif nodCurent.info[i][j] == '#':
                    schi = 1
                    for ls in interschimbator(nodCurent.info, i, j):
                        nodNou = NodParcurgere(id, deepcopy(ls), nodCurent, cost=2, buton='#', activare=schi)
                        nodNou.h = graf.calculeaza_h(nodNou)
                        nodNou.f = nodNou.g + nodNou.h
                        schi += 1
                        id += 1
                        listaSuccesori.append(nodNou)
                elif nodCurent.info[i][j] == '^':
                    urc = 1
                    for ls in urcator(nodCurent.info, i, j):
                        nodNou = NodParcurgere(id, deepcopy(ls), nodCurent, cost=urc, buton='^', activare=urc)
                        nodNou.h = graf.calculeaza_h(nodNou)
                        nodNou.f = nodNou.g + nodNou.h
                        id += 1
                        urc += 1
                        listaSuccesori.append(nodNou)
                elif nodCurent.info[i][j] == '>':
                    drep = 1
                    for ls in dreptator(nodCurent.info, i, j):
                        nodNou = NodParcurgere(id, deepcopy(ls), nodCurent, cost=drep, buton='>', activare=drep)
                        nodNou.h = graf.calculeaza_h(nodNou)
                        nodNou.f = nodNou.g + nodNou.h
                        id += 1
                        drep += 1
                        listaSuccesori.append(nodNou)
        return listaSuccesori, id

    def calculeaza_h(self, infoNod, tipEuristica="euristica banala"):
        if tipEuristica == "euristica banala":
            if self.testeaza_scop(infoNod):
                return 1
            else:
                return 0
        elif tipEuristica == "euristica neadmisibila":
            if self.testeaza_scop(infoNod):
                return 0
            else:
                return 1

    def __repr__(self):
        sir = ""
        for (k, v) in self.__dict__.items():
            sir += "{} = {}\n".format(k, v)
        return (sir)


#### algoritm BF
# presupunem ca vrem mai multe solutii (un numar fix) prin urmare vom folosi o variabilă numită nrSolutiiCautate
# daca vrem doar o solutie, renuntam la variabila nrSolutiiCautate
# si doar oprim algoritmul la afisarea primei solutii

def breadth_first(gr, nrSolutiiCautate=1):
    global time2
    # in coada vom avea doar noduri de tip NodParcurgere (nodurile din arborele de parcurgere)
    id = 1
    c = [NodParcurgere(id, gr.start, None)]

    while len(c) > 0:
        nodCurent = c.pop(0)

        if gr.testeaza_scop(nodCurent):
            print("Solutie:")
            nodCurent.afisDrum()
            print("\n----------------\n")
            nrSolutiiCautate -= 1
            if nrSolutiiCautate == 0:
                return
        lSuccesori, id = gr.genereazaSuccesori(nodCurent, id)
        c.extend(lSuccesori)
        time2 = time.time()
        if time2 - time1 > 5:
            return


def depth_first(gr, nrSolutiiCautate=1, id=1):
    # vom simula o stiva prin relatia de parinte a nodului curent
    df(NodParcurgere(id, gr.start, None), nrSolutiiCautate, id)


def df(nodCurent, nrSolutiiCautate, id):
    if nrSolutiiCautate <= 0:  # testul acesta s-ar valida doar daca in apelul initial avem df(start,if nrSolutiiCautate=0)
        return nrSolutiiCautate

    if graf.testeaza_scop(nodCurent):
        print("Solutie: ", end="")
        nodCurent.afisDrum()
        print("\n----------------\n")
        input()
        nrSolutiiCautate -= 1
        if nrSolutiiCautate == 0:
            return nrSolutiiCautate
    lSuccesori, id = graf.genereazaSuccesori(nodCurent, id)
    for sc in lSuccesori:
        if nrSolutiiCautate != 0:
            if id < 10000:
                nrSolutiiCautate = df(sc, nrSolutiiCautate, id)
            time2 = time.time()
            if time2 - time1 > 5:
                return

    return nrSolutiiCautate


# df(a)->df(b)->df(c)->df(f)
#############################################


def dfi(nodCurent, adancime, nrSolutiiCautate, id):
    if adancime == 1 and graf.testeaza_scop(nodCurent):
        print("Solutie: ", end="")
        nodCurent.afisDrum()
        print("\n----------------\n")
        nrSolutiiCautate -= 1
        if nrSolutiiCautate == 0:
            return nrSolutiiCautate
    if adancime > 1:
        lSuccesori, id = graf.genereazaSuccesori(nodCurent, id)
        for sc in lSuccesori:
            if nrSolutiiCautate != 0:
                nrSolutiiCautate = dfi(sc, adancime - 1, nrSolutiiCautate, id)
            time2 = time.time()
            if time2 - time1 > 5:
                return
    return nrSolutiiCautate


def depth_first_iterativ(gr, level, nrSolutiiCautate=1, id=1):
    for i in range(1, level + 1):
        if nrSolutiiCautate == 0:
            return
        print("**************\nAdancime maxima: ", i)
        nrSolutiiCautate = dfi(NodParcurgere(id, gr.start, None), i, nrSolutiiCautate, id)


def a_star(gr, nrSolutiiCautate):
    # in coada vom avea doar noduri de tip NodParcurgere (nodurile din arborele de parcurgere)
    id = 1
    c = [NodParcurgere(id, gr.start, None, 0)]
    c[0].h = gr.calculeaza_h(c[0])
    c[0].f = c[0].g + c[0].h
    heapq.heapify(c)
    while len(c) > 0:
        nodCurent = c.pop(0)

        if gr.testeaza_scop(nodCurent):
            print("Solutie: ")
            nodCurent.afisDrum()
            print("\n----------------\n")
            nrSolutiiCautate -= 1
            if nrSolutiiCautate == 0:
                return
        lSuccesori, id = gr.genereazaSuccesori(nodCurent, id)
        for s in lSuccesori:
            time2 = time.time()
            if time2 - time1 > 5:
                return
            c.append(s)


def a_star_opt(gr):
    # in coada vom avea doar noduri de tip NodParcurgere (nodurile din arborele de parcurgere)
    id = 1
    l_open = [NodParcurgere(id, graf.start, None, 0)]
    l_open[0].h = graf.calculeaza_h(l_open[0])
    l_open[0].f = l_open[0].g + l_open[0].h
    heapq.heapify(l_open)
    # l_open contine nodurile candidate pentru expandare (este echivalentul lui c din A* varianta neoptimizata)

    # l_closed contine nodurile expandate
    l_closed = []
    while len(l_open) > 0:

        nodCurent = l_open.pop(0)
        l_closed.append(nodCurent)
        if gr.testeaza_scop(nodCurent):
            print("Solutie: ", end="")
            nodCurent.afisDrum()
            print("\n----------------\n")
            return
        lSuccesori, id = gr.genereazaSuccesori(nodCurent, id)
        for s in lSuccesori:
            gasitC = False
            for nodC in l_open:
                if s.info == nodC.info:
                    gasitC = True
                    if s.f >= nodC.f:
                        lSuccesori.remove(s)
                    else:  # s.f<nodC.f
                        l_open.remove(nodC)
                    break
            if not gasitC:
                for nodC in l_closed:
                    if s.info == nodC.info:
                        if s.f >= nodC.f:
                            lSuccesori.remove(s)
                        else:  # s.f<nodC.f
                            l_closed.remove(nodC)
                        break
            time2 = time.time()
            if time2 - time1 > 5:
                return
        for s in lSuccesori:
            time2 = time.time()
            if time2 - time1 > 5:
                return
            l_open.append(s)


def ida_star(gr, nrSolutiiCautate, id=1):
    nodStart = NodParcurgere(id, gr.start, None, 0)
    nodStart.h = graf.calculeaza_h(nodStart)
    nodStart.f = nodStart.g + nodStart.h
    limita = nodStart.f
    while True:

        nrSolutiiCautate, rez = construieste_drum(gr, nodStart, limita, nrSolutiiCautate, id)
        if rez == "gata":
            break
        if rez == float('inf'):
            print("Nu mai exista solutii!")
            break
        limita = rez
        time2 = time.time()
        if time2 - time1 > 5:
            return


def construieste_drum(gr, nodCurent, limita, nrSolutiiCautate, id):
    global time2
    if nodCurent.f > limita:
        return nrSolutiiCautate, nodCurent.f
    if gr.testeaza_scop(nodCurent) and nodCurent.f == limita:
        print("Solutie: ")
        nodCurent.afisDrum()
        print(limita)
        print("\n----------------\n")
        input()
        nrSolutiiCautate -= 1
        if nrSolutiiCautate == 0:
            return 0, "gata"
    lSuccesori, id = gr.genereazaSuccesori(nodCurent, id)
    minim = float('inf')
    for s in lSuccesori:
        if id < 1000:
            nrSolutiiCautate, rez = construieste_drum(gr, s, limita, nrSolutiiCautate, id)
            if rez == "gata":
                return 0, "gata"
            if rez < minim:
                minim = rez
            time2 = time.time()
        if time2 - time1 > 5:
            return 0, float('inf')
    return nrSolutiiCautate, minim


# construieste_drum(a)->construieste_drum(c)


if __name__ == "__main__":
    ##############################################################################################
    #                                 Initializare problema                                      #
    ##############################################################################################

    # pathInput = input()
    # pathOutput = input()

    # NSOL = int(input())

    fileInput = open("Input/input3" + ".txt", "r")
    # fileOutput = open(pathOutput + ".txt", "w")


    stareInitiala = []
    scopuri = []

    checkCuvinte = 0

    for line in fileInput.readlines():

        if line != "__cuvinte__\n" and checkCuvinte == 0:

            tempList = line.split()
            stareInitiala.append(tempList)
        elif checkCuvinte == 1:
            checkCuvinte = 1
            tempList = line.rstrip("\n")
            scopuri.append(tempList)
        else:
            checkCuvinte = 1

    graf = Graph(stareInitiala, scopuri)

    #breadth_first(graf, nrSolutiiCautate=1)

    #depth_first_iterativ(graf, level=5, nrSolutiiCautate=20)

    #depth_first(graf, nrSolutiiCautate=1)

    #a_star(graf, nrSolutiiCautate=1)

    #a_star_opt(graf)

    ida_star(graf, nrSolutiiCautate=1)




