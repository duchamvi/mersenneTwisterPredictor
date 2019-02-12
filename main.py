import mersenneTwister
import untwist
import random

def hprint(n):
    print(hex(n))

def extract(y):
    y = y^(y>>11)
    y = y^((y<<7)&0x9D2C5680)
    y = y^((y<<15)&0xEFC60000)
    y = y^(y>>18)
    return y   

def computeNextstate(old1, old2, old3):
    return old1 ^ old2 ^ old3 # to change

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
        print(hex(mtref.getRandomNumber()), "==", hex(mthack.getRandomNumber()), " !!!")

def testUntwistPyrand(n):
    values = [random.getrandbits(32) for _ in range(624)]
    state = untwist.reverseState(values)
    mthack = mersenneTwister.Mt()
    mthack.reinitState(state)

    for i in range(n):
        print("Python random", hex(random.getrandbits(32)), "==", hex(mthack.getRandomNumber()), " !!!")


def getNumbers(rng, n):
    values = []
    for i in range(n):
        values.append(rng.getRandomNumber())
    return values


def testTrunc():
    ref = extract(0) & 0x000000ff
    hprint(ref)
    for i in range (32):  
        state  = 1 * (2**i) 
        number = extract(state) & 0xffffffff
        if number !=0:
            print("{} : {}".format(i, hex(number))) 



def createState_OutputTable():
    # so : state-output (find wich bit of output give which bit of state)
    soMask = extract(0x00000000)    
    print("So Mask", hex(soMask))
    sotable = [[] for _ in range (32)] 

    for i in range (32):
        state  = 0x1 << i
        word = extract(state)
        print("So state", hex(state)," ->", hex(word))

        # register bits of state
        for bit in range(32):
            ref = 0x1 << bit
            if ref & word != 0x0:
                sotable[bit].append(i)

    for (i, l) in enumerate(sotable):
        print("o{} : {}".format(i, l))
    return sotable    

def applytable(input, table):  
    # sotable for state to output
    result = 0    
    for i in range (32):
        ref = 0x1 << i
        for inputbit in table[i]:
            if input & (0x1 << inputbit) != 0x0:
                result ^= ref         
    return result    


def test_bruteforce2k(nbUnknownBits = 8):
    output1 = 0x12345678 & 0x00ffffff
    output2 = 0x12345678 & 0x00ffffff

    extensions = []
    for i in range(2**(nbUnknownBits)):
        extensions.append(i << 32 - nbUnknownBits)

    for ex1 in extensions:
        state1 = untwist.reverseWord(output1^ex1)
        for ex2 in extensions:
            state2 = untwist.reverseWord(output2^ex2)
            nextstate = computeNextstate(state1, state2, 0x12345678)
            word = extract(nextstate)
            #hprint(word)
    print("done")


if __name__ == "__main__":
    # testMT(10)
    # testUntwist(10)
    testUntwistPyrand(10)

    #sotable = createState_OutputTable()
    #state = 0x12345a78
    #word = extract(state)
    #tableword = applytable(state, sotable)   
    #print("Test state", hex(state)," ->", hex(word) , " sotable -> ", hex(tableword))

    test_bruteforce2k()

