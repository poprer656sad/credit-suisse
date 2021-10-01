def totalPairs(n, values):
    extras = 0
    if n < 2:
        return 0
    if n == 2:
        return 1
    for i in range(n-1):
        for j in range(i+2, n):
            if values[i] == max(values[i:j]) and values[j] == max(values[i+1:j+1]):
                extras += 1
    if values[-3] == max(values[-3:-2]) and values[-1] == max(values[-2:-1]):
        extras += 1
    return n + extras-1

if __name__ == "__main__":
    n = int(input())
    values = list(map(int, input().split()))
    answer = totalPairs(n, values)
    print(answer)