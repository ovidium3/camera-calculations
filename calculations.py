import numpy as np
import math
from sympy import symbols, Eq, solve

camPos = np.array([0, 0, 0])
point = np.array([-10, 0, 1])

converted_point = [point[1], point[2], -point[0]]

# temporary guessed values
nearDistance = 0.1
farDistance = 1000000
fovRadians = math.radians(120)
# 1536 by 2048 resolution

# constant values
camForward = np.array([0, 0, 1])
camUp = np.array([0, 1, 0])
camRight = np.array([1, 0, 0])
viewRatio = 4/3

nearCenter = camPos + camForward * nearDistance
farCenter = camPos + camForward * farDistance

nearHeight = 2 * math.tan(fovRadians/ 2) * nearDistance
farHeight = 2 * math.tan(fovRadians / 2) * farDistance
nearWidth = nearHeight * viewRatio
farWidth = farHeight * viewRatio

farTopLeft = farCenter + camUp * (farHeight*0.5) - camRight * (farWidth*0.5)
farTopRight = farCenter + camUp * (farHeight*0.5) + camRight * (farWidth*0.5)
farBottomLeft = farCenter - camUp * (farHeight*0.5) - camRight * (farWidth*0.5)
farBottomRight = farCenter - camUp * (farHeight*0.5) + camRight * (farWidth*0.5)

camX = 2048
camY = 1536
nearTopLeft = nearCenter + camY * (nearHeight*0.5) - camX * (nearWidth*0.5)
nearTopRight = nearCenter + camY * (nearHeight*0.5) + camX * (nearWidth*0.5)
nearBottomLeft = nearCenter - camY * (nearHeight*0.5) - camX * (nearWidth*0.5)
nearBottomRight = nearCenter - camY * (nearHeight*0.5) + camX * (nearWidth*0.5)

A = farTopLeft
B = farTopRight
C = farBottomLeft

AB = B - A
AC = C - A

normal_vector = np.cross(AB, AC)

x, y, z = symbols("x, y, z")
equation = Eq((normal_vector[0]*(x - A[0]) + normal_vector[1]*(y - A[1]) + normal_vector[2]*(z - A[2])), 0)
z_value = solve((equation), (z))
print(z_value)

t = symbols("t")
line_vector = camPos + t*point
print(line_vector)

line_equation = Eq((line_vector[2]), z_value)
print(line_equation)

reconverted_point = [-converted_point[2], converted_point[0], converted_point[1]]
