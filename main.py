import mersenneTwister

def test(n):
    rng = mersenneTwister.Mt()
    
    for i in range(n):
        print(rng.getRandomNumber())

if __name__ == "__main__":
    test(10)