n = input()
n = int(n) if n.isdigit() else 0

b = [int(d) for d in str(n)]

if sum(b) % 9 == 0 and any(d % 2 == 0 for d in b):
    print(f"YES")
else:
    print(f"NO")