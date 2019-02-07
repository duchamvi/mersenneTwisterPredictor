import mersenneTwister
import untwist

def hprint(n):
    print(hex(n))

def testMt(n):
    rng = mersenneTwister.Mt()
    
    for i in range(n):
        print(rng.getRandomNumber())


def testUntwist():
    testWord = 0x1234abcd
    testWord ^= testWord >> 18
    result = untwist.reverseRightShiftXor(testWord, 18)
    hprint(result)


def getNumbers(rng, n):
    values = []
    for i in range(n):
        values.append(rng.getRandomNumber())
    return values

if __name__ == "__main__":
    #testMT(10)
    mt = mersenneTwister.Mt()
    values = getNumbers(mt, 624)
    testUntwist()