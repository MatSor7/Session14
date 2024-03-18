b = 20

def is_prime(num):
    """
    Checks if a number is prime
    :param num: The number to check
    :return: True/False
    """
    if num <= 1:
        return False
    if num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
        return True
