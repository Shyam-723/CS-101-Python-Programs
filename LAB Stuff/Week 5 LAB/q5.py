weight_start = int(input("Input your starting weight (pounds): "))
i=1

while(i <= 6):
    print(f'Your expected weight after {i} month of this diet : {weight_start - (4*i)} pounds')
    i = i+1
