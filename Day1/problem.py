# unserscore = int(input("Enter a score: "))
# print("Your score is: ", unserscore)



age =6
day ="wednesday"

price = 12 if age < 10 else 20
print(price)


#loops
 #1
 #Counting positve no
numbers = [1,2,-3,4,5,-6,7,8,9,10,-5]
count = 0
for number in numbers:
        if number > 0:
            count += 1
print(count)

#2
#even
n =10
sum_even = 0
for i in range(2,n+1):
    if i % 2 == 0:
        sum_even += i
print(sum_even)

#3
#multiplication table but skip 5
number = 10
for i in range(1,11):
    if i == 5:
        continue
    print(number , "x", i, "=", number * i)


#4
#reverse string  using for loop
string = "hello"
reverse = ""
for i in string:
    reverse = i + reverse
print(reverse)


#5
#prime number
num =29
is_prime = True

if num > 1:
    for i in range(2,num):
        if num % i == 0:
            is_prime = False
            break
if is_prime:    
    print(num, "is a prime number")


    
