# Calculate Simple interest with P = Principal amount, N = Period (years), R = Rate of interest

P=float(input('Please enter the Principal amount in INR : '))
N=float(input('Please enter the number of years : '))
R=float(input('Please enter the rate of interest in p.a.% : '))

#Calculate simple interest
I=P*N*R/100

#Calculate amount
A=P+I 

#Display above results

print(f'Simple Interest for given values is : {I:.2f} INR')
print(f'Total Amount is : {A:.2f} INR')