limit = 10
sum_of_evens = 0

for num in range(1, limit + 1):
    if num % 2 == 0:
        sum_of_evens += num

print("Sum of even numbers:", sum_of_evens)