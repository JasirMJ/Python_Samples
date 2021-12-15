# import sys
# from functools import lru_cache

# sys.setrecursionlimit(3333)  # estimated by trial and error

# @lru_cache()
# def solution(n):
#     n = int(n)

#     if n <= 2:
#         return n - 1

#     if n % 2 == 0:
#         return solution(n // 2) + 1

#     return min(solution(n + 1), solution(n - 1)) + 1

# print(solution("4"))
# print(solution("15"))
# print(solution(str(10**309 - 1)))

def stepCount(n):
    count = 0
    reminder_list = []
    while n > 1:

        print(f"{n} % 2 = {n%2}")
        
        if n % 2 == 0:             # bitmask: *0
            n = n // 2
        elif n == 3 or n % 4 == 1: # bitmask: 01
            n = n - 1
        else:                      # bitmask: 11
            n = n + 1
        count += 1
    return count

# print(stepCount(10**309))
print(stepCount(3))