def divisors(num):
    divisors = []
    for i in range(1,num+1):
        if num % i == 0:
            divisors.append(i)

    return divisors

def run():
    try:
        num = int(input('Type a number: '))
        if(num <= 0):
            raise ValueError
        print(divisors(num))
        print('fin')
    except ValueError as ve:
        print("It should be a positive integer number")

if __name__ == '__main__':
    run()