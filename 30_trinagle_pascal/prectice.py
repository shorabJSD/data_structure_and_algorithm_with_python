def generate_pascal_training(runRows):
    triangle = []
    for row_num in range(runRows):
        row = [1]
        if row_num >0:
            for j in range(1, row_num):
                value = triangle()
