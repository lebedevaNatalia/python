def num_gens(max_num):
    for num in range(1, max_num + 1, 2):
        yield num
        if max_num > num:
            print('StopIteration')

add_to_15 = num_gens(15)
print(add_to_15)