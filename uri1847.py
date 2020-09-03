temps = input().split()
a,b,c = [int(i) for i in temps]
if(a>b):
    if(c>=b):
        print(":)")
    elif(b>c):
        if((b-c)<(a-b)):
            print(':)')
        else:
            print(':(')
elif(b>a):
    if(c<=b):
        print(":(")
    elif(c>b):
        if((b-a)>(c-b)):
            print(":(")
        else:
            print(':)')
else:
    if(c>b):
        print(':)')
    else:
        print(':(')

        
