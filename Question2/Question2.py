def securitiesBuying(z, security_value):
    no_of_stocks=0
    available = []
    for num, amt in enumerate(security_value):
        for _ in range(num + 1):
            available.append(int(amt))
    available.sort()
    sum = 0
    while sum <= int(z):
        no_of_stocks+=1
        sum += int(available.pop(0))
    return no_of_stocks-1


def main():
    z= input()
    security_value = input().split()
    no_of_stocks_purchased=securitiesBuying(z,security_value)
    print(no_of_stocks_purchased)


if __name__ == '__main__':
    main()