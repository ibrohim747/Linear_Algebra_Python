def Vector_Components(cor_a, cor_b):
    delta_x = cor_b[0] - cor_a[0]
    delta_y = cor_b[1] - cor_a[0]
    return delta_x, delta_y

v1 = (1,1)
v2 = (5,4)

print(Vector_Components(v1, v2))
