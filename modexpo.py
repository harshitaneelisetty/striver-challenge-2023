#https://www.codingninjas.com/codestudio/problems/modular-exponentiation_8230803?challengeSlug=striver-sde-challenge

def modularExponentiation(base, power, modulus):
    result = 1
    while power > 0:
        if power & 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        power >>= 1

    return result

  #I iteratively computated the exponentiation by squaring technique
  #I calculated the result of raising a base to a power modulo a given modulus.





  
