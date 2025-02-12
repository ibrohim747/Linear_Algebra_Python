def Vector_Components(cor_a, cor_b):
    delta_x = cor_b[0] - cor_a[0]
    delta_y = cor_b[1] - cor_a[1]  # Fixed mistake here
    return delta_x, delta_y

def Vector_Scaling(v1, a):
    res_v = (v1[0] * a, v1[1] * a)
    return res_v

def Vector_Addition(v1, v2):
    res_v = (v1[0] + v2[0], v1[1] + v2[1])
    return res_v

def Vector_Subtraction(v1, v2):
    res_v = (v1[0] - v2[0], v1[1] - v2[1])  # Fixed mistake here
    return res_v

# Test cases
v1 = (3,1)
v2 = (5,4)

print("Vector Components:", Vector_Components(v1, v2))  # (2, 3)
print("Scaled Vector:", Vector_Scaling(v2, 2))   # (10, 8)
print("Vector Addition:", Vector_Addition(v1, v2))  # (8, 5)
print("Vector Subtraction:", Vector_Subtraction(v1, v2))  # (-2, -3)