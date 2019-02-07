import mersenneTwister
import untwist

def hprint(n):
    print(hex(n))

def testMt(n):
    rng = mersenneTwister.Mt()
    
    for i in range(n):
        print(rng.getRandomNumber())


def testUntwist():
    shift = 18
    testWord = 0x1234abcd
    testWord ^= testWord >> shift
    result = untwist.reverseRightShiftXor(testWord, shift)
    hprint(result)

    testWord = 0xdeadbeef
    mask = 0xae12ab32
    shift = 16
    testWord ^= (testWord << shift) & mask
    result = untwist.reverseLeftShiftXor(testWord, shift, mask)
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