# This is the main code

# import China
from China import is_prime  # Easier to use, but risk of overwriting the definition.
from China import is_prime as china_prime  # Solution to the one above.
import China as prc


a = 10
is_prime = 7
# print(China.b)
# print(China.is_prime(12))
# print(China.is_prime(2))
# print(China.is_prime(17))
# print(is_prime(11))
print(china_prime(11), is_prime)
print(prc.is_prime(25))
