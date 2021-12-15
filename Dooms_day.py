# Solar Doomsday
# ==============
# Who would've guessed? Doomsday devices take a LOT of power. 
# Commander Lambda wants to supplement the LAMBCHOP's quantum antimatter reactor core with solar arrays, 
# and you've been tasked with setting up the solar panels.
# Due to the nature of the space station's outer paneling, 
# all of its solar panels must be squares. 
# Fortunately, you have one very large and flat area of solar material, a pair of industrial-strength scissors, and 
# enough MegaCorp Solar Tape(TM) to piece together any excess panel material into more squares. 
# For example, 
# if you had a total area of 12 square yards of solar material, you would be able to make one 3x3 square panel (with a total area of 9). 
# That would leave 3 square yards, so you can turn those into three 1x1 square solar panels.
# Write a function solution(area) that takes as its input a single unit of measure representing the 
# total area of solar panels you have (between 1 and 1000000 inclusive) and returns a list of the areas of the 
# largest squares you could make out of those panels, starting with the largest squares first. 
# So, following the example above, solution(12) would return [9, 1, 1, 1].

# -- Python cases --
# Input:
# solution.solution(15324)
# Output:
# 15129,169,25,1
# Input:
# solution.solution(12)
# Output:
# 9,1,1,1


#solar Doomsday
#==============
import math
# def solution(area):
#     print(f"solution({area})")
#     bal_area = area
#     print("Output")
#     # lst = []
#     while bal_area > 0:
#         sqr_rt = int(math.sqrt(bal_area))
#         bal_area -= sqr_rt**2
#         # lst.append(sqr_rt**2) 
#         print(sqr_rt**2) if bal_area == 0 else print(sqr_rt**2, end=",") 
#     # print("out :", lst)


def solution(area):
    area_ = area
    lst = []
    while area_ > 0:
        root_area = int(area_**(1/2))
        # print(f"Root of area {root_area} ,")
        area_ = area_ - root_area**2
        # print("Area ", area_)
        lst.append(root_area**2)
    return lst

print("-- Python cases --")
print("Input:")
print(solution(15324))
print("Input:")
print(solution(12))
print("Input:")
print(solution(11))