lst=[1,2,3,4,5,6,7,8,9,10]
even_sum=0
odd_sum=0
for ele in lst:
    if ele%2==0:
        even_sum+=ele
    else:
        odd_sum+=ele

print(f"Sum of all even numbers is {even_sum}\nSum of all odd numbers is {odd_sum}")
        