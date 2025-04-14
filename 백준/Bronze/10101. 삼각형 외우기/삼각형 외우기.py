angle_A = int(input())
angle_B = int(input())
angle_C = int(input())

angle_sum = angle_A + angle_B + angle_C

if angle_sum != 180:
    print("Error")
elif angle_A == angle_B == angle_B:
    print("Equilateral")
elif angle_A != angle_B != angle_C != angle_A:
    print("Scalene")
else:
    print("Isosceles")
