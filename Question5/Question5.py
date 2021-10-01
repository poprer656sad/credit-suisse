def sol(n):
   return "B" if max(map(len, n.split("1"))) % 2 == 0 else "A"

# do not edit below code
def main():
	n=input()
	print(sol(n))

if __name__ == '__main__':
    main()
