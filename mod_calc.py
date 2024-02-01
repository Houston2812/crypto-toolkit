if __name__ == "__main__":
	a = int(input("a: "))
	p = int(input("p: "))
	limit = int(input("limit: "))

	power = 1
	prev = a
	
	print(f"{prev}^{power} = {a % p}")

	for _ in range(2, limit + 1):
		power = power * 2
		a = (prev ** power) % p
		
		print(f"{prev}^{power} = {a}")

