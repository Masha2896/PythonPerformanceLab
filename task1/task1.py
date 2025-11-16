from itertools import cycle, islice

result_overall = {}

for iteration in range(2):
    while True:
        try:
            list_num_arr = int(input("Длина массива: "))
            chunk_size = int(input("Интервал: "))

            if list_num_arr <= 0 or chunk_size <= 0:
                print("Числа должны быть положительными")
                continue
            elif list_num_arr < chunk_size:
                print("Интервал не может быть больше длины массива")
                continue

            break

        except ValueError:
            print("Введите целое число")


    list_num_arr = list(range(1, list_num_arr + 1))

    pool = cycle(list_num_arr)
    result = []

    while True:
        chunk = list(islice(pool, chunk_size))

        result.append(chunk)
        if chunk[-1] == list_num_arr[0]:
            break

        last_element = chunk[-1]
        next_start_index = (list_num_arr.index(last_element)) % len(list_num_arr)

        pool = cycle(list_num_arr)

        for _ in range(next_start_index):
            next(pool)

    result_overall[iteration + 1] = [chunk[0] for chunk in result]

if 1 in result_overall and 2 in result_overall:
    combined_list = result_overall[1] + result_overall[2]
    res = ''.join(map(str, combined_list))
    print(res)
