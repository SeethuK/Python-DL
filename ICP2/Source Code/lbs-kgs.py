N = int(input("enter the number of students"))
lbs_list = []
kgs_list = []
for weight in range(N):
    x = float(input("enter the weights in lbs"))
    lbs_list.append(x)
    x = x*0.453
    kgs_list.append(round(x,2))
print(lbs_list)
print(kgs_list)