from typing import List

def multiples_of_3_or_5(number):
    sum: int = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
            # print(i)
    return sum

numbers: List[int] = [10, 49, 1_000, 8_456, 19_564]

for number in numbers:
    answer: int = multiples_of_3_or_5(number)
    print(f"Sum of all multiples of 3 and 5 below {number} is {answer}")
