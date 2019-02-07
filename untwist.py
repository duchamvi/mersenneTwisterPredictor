def reverseRightShiftXor(number, shift):
    stateWord = 0   # word in the mersenne twister

    shiftmask = (0xffffffff << (32 - shift)) & 0xffffffff   # position of bits to copy
    stateWord ^= shiftmask & number
    
    step = 0
    while (step * shift < 32):
        step += 1
        stepmask = stateWord & shiftmask    # copy of the bits
        stepmask = stepmask >> shift
        shiftmask = shiftmask >> shift

        stateWord ^= (shiftmask & number)^stepmask # XOR of copied bits
    return stateWord


def reverseLeftShiftXor(number, shift, mask):
    stateWord = 0   # word in the mersenne twister

    shiftmask = (0xffffffff << (shift)) ^ 0xffffffff   # position of bits to copy
    stateWord ^= shiftmask & number
    
    step = 0
    while (step * shift < 32):
        step += 1
        stepmask = stateWord & shiftmask    # copy of the bits
        stepmask = (stepmask << shift) & mask
        shiftmask = (shiftmask << shift) & 0xffffffff

        stateWord ^= (shiftmask & number)^stepmask # XOR of copied bits
    return stateWord

def reverseWord(number):
    number = reverseRightShiftXor(number, 18)
    number = reverseLeftShiftXor(number, 15, 0xEFC60000)
    number = reverseLeftShiftXor(number, 7, 0x9D2C5680)
    number = reverseRightShiftXor(number, 11)
    return number

def reverseState(numbers):
    return [reverseWord(w) for w in numbers]
