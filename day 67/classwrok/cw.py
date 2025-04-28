#1
average = lambda a, b, c: (a + b + c) / 3

#2
even_or_odd = lambda number: "Even" if number % 2 == 0 else "Odd"

#3
positive_sum = lambda arr: sum(x for x in arr if x > 0)

#4
find_smallest_int = lambda arr: min(arr)

#5
count_by = lambda x, n: [x * i for i in range(1, n + 1)]
