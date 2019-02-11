import mersenneTwister
import untwist
import random

def hprint(n):
    print(hex(n))

def testMt(n):
    rng = mersenneTwister.Mt()
    
    for i in range(n):
        print(rng.getRandomNumber())

def twist(y):
    y = y^(y>>11)
    y = y^((y<<7)&0x9D2C5680)
    y = y^((y<<15)&0xEFC60000)
    y = y^(y>>18)
    return y    

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
    ref = twist(0) & 0x000000ff
    hprint(ref)
    for i in range (32):  
        state  = 1 * (2**i) 
        number = twist(state) & 0xffffffff
        if number !=0:
            print("{} : {}".format(i, hex(number))) 



def createState_OutputTable():
    # so : state-output (find wich bit of output give which bit of state)
    soMask = twist(0x00000000)    
    print("So Mask", hex(soMask))
    sotable = [[] for _ in range (32)] 

    for i in range (32):
        state  = 0x1 << i
        word = twist(state)
        print("So state", hex(state)," ->", hex(word))

        # register bits of state
        for bit in range(32):
            ref = 0x1 << bit
            if ref & word != 0x0:
                sotable[bit].append(i)

    for (i, l) in enumerate(sotable):
        print("o{} : {}".format(i, l))
    return sotable    

def tabletwist(state, sotable):
    tableword = 0    
    for i in range (32):
        ref = 0x1 << i
        for statebit in sotable[i]:
            if state & (0x1 << statebit) != 0x0:
                tableword ^= ref         
    return tableword    

if __name__ == "__main__":
    # testMT(10)
    # testUntwist(10)
    #testUntwistPyrand(10)
    sotable = createState_OutputTable()
    
    state = 0x12345a78
    word = twist(state)
    tableword = tabletwist(state, sotable)   

    print("Test state", hex(state)," ->", hex(word) , " sotable -> ", hex(tableword))


