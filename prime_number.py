# print prime number between 1 to 1000


def print_prime():
    prime_palin = []
    for number in range(1, 1000):
        count = 0
        for i in range(2, (number // 2 + 1)):
            if number % i == 0:
                count = count + 1
                break
        if count == 0 and number != 1:
            print(" %d" % number, end='  ')
            prime_palin.append(check_prime_to_be_palindrome(number))

    return prime_palin


def check_prime_to_be_palindrome(num):
    temp = num
    rev = 0
    while num > 0:
        x = num % 10
        rev = rev * 10 + x
        num = num // 10
    if temp == rev:
        return temp
    else:
        return


print("the prime numbers between 1 and 1000 are: ")
palin_list = print_prime()
print("the prime number which are palindrome also : ", palin_list)

