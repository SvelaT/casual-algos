import math
import time

def testCPU(print_result = False):
    start = time.time()
    for i in range(10**8):
        math.sqrt(i)
    result = time.time() - start
    if print_result:
        print(f"CPU test took {result} seconds")
        print(f"It managed to compute aproximately {(10**8)//result} square root operations per second")
    return result
    
def testRAM(print_result = False):
    start = time.time()
    for _ in range(10**8):
        var = """
        aaaaaaa aaaaaaa aaaaaaa aaaaaaa aaaaaaa aaaaaaa aaaaaaa aaaaaaa 
        aaaaaaa aaaaaaa aaaaaaa aaaaaaa aaaaaaa aaaaaaa aaaaaaa aaaaaaa 
        aaaaaaa aaaaaaa aaaaaaa aaaaaaa aaaaaaa aaaaaaa aaaaaaa aaaaaaa 
        aaaaaaa aaaaaaa aaaaaaa aaaaaaa aaaaaaa aaaaaaa aaaaaaa aaaaaaa 
        """
        del var
    result = time.time() - start
    if print_result:
        print(f"RAM test took {result} seconds")
    return result