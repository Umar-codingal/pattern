rows=int(input("Enter the number of rows you want: "))
number=1

for i in range(1, rows +1):
    for j in range(1, i+1  ):
        print(number, end=" ")
        number+=1
    print()