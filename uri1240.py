n = int(input())
for i in range (n):
    ent = input().split()
    if (ent[0])[-len(ent[1]):] == ent[1]:
        print("encaixa")
    else:
        print("nao encaixa")
