import mersenneTwister
import untwist

def hprint(n):
    print(hex(n))

def testMt(n):
    rng = mersenneTwister.Mt()
    
    for i in range(n):
        print(rng.getRandomNumber())


def testUntwist(n):
    mtref = mersenneTwister.Mt()
    values = getNumbers(mtref, 624)
    state = untwist.reverseState(values)
    mthack = mersenneTwister.Mt()
    mthack.reinitState(state)

    for i in range(n):
        print(mtref.getRandomNumber(), "==", mthack.getRandomNumber(), " !!!")


def getNumbers(rng, n):
    values = []
    for i in range(n):
        values.append(rng.getRandomNumber())
    return values

if __name__ == "__main__":
    #testMT(10)
    testUntwist(10)