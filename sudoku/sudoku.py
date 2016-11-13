import logging


def clear_if_value_single(row, col):
    if len(ori[row * 9 + col]) == 1:
        logging.debug('value at cell[%d, %d] is single' % (row, col))
        el = ori[row * 9 + col][0]
        for i in (set(get_row_list(row)) | set(get_colum_list(col)) | set(get_block_list(row, col))) - set([row * 9 + col]):
            if len(ori[i]) > 1:
                if el in ori[i]:
                    ori[i].remove(el)
                    if len(ori[i]) == 1:
                        clear_if_value_single(i // 9, i % 9)
    else:
        logging.debug('value at cell[%d, %d] is not single' % (row, col))


def clear_if_value_single_all():
    for i in range(9):
        for j in range(9):
            clear_if_value_single(i, j)


def set_if_value_single_in_block():
    block_list = []
    for i in range(9):
        block_list.append(get_row_list(i))
    for i in range(9):
        block_list.append(get_colum_list(i))
    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            block_list.append(get_block_list(i, j))
    logging.debug(block_list)
    test = []
    for block in block_list:
        test.clear()
        logging.debug('For block: %s' % block)
        for i in block:
            if len(ori[i]) > 1:
                test += ori[i]
        for v in set(test):
            if test.count(v) == 1:
                # print(v)
                for i in block:
                    if len(ori[i]) > 1 and v in ori[i]:
                        ori[i] = [v]
                        clear_if_value_single(i // 9, i % 9)


def get_row_list(row):
    row_list = []
    for i in range(9):
        row_list.append(row * 9 + i)
    return row_list


def get_colum_list(col):
    col_list = []
    for i in range(9):
        col_list.append(i * 9 + col)
    return col_list


def get_block_list(row, col):
    get_block_list = []
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            get_block_list.append((start_row + i) * 9 + start_col + j)
    return get_block_list


def print_grid():
    print('Grid is:')
    for i in range(81):
        s = ''.join(str(x) for x in ori[i])
        print('|{0:^9}'.format(s), end='')
        if i % 9 == 8:
            print('|')


def count_numbers():
    numbers = []
    for i in range(81):
        numbers += ori[i]
    return len(numbers)

# set log level
# logging.basicConfig(level=logging.DEBUG)

# init table
ori = [[1, 2, 3, 4, 5, 6, 7, 8, 9] for i in range(81)]

# read data
ori[1] = [8]
ori[7] = [7]
ori[10] = [3]
ori[11] = [7]
ori[13] = [2]
ori[17] = [1]
ori[21] = [9]
ori[29] = [4]
ori[32] = [1]
ori[33] = [2]
ori[36] = [7]
ori[45] = [1]
ori[48] = [2]
ori[50] = [4]
ori[51] = [9]
ori[52] = [6]
ori[58] = [7]
ori[65] = [5]
ori[66] = [4]
ori[68] = [6]
ori[70] = [9]
ori[72] = [3]
ori[73] = [4]
ori[75] = [1]
ori[76] = [9]
ori[79] = [8]
# print(ori)

num_count = 0

# deal
clear_if_value_single_all()
logging.debug(ori)

while num_count != count_numbers():
    num_count = count_numbers()
    set_if_value_single_in_block()
    print_grid()

num_to_be_checked = []
cell_to_be_checked = []
for i in get_colum_list(2):
    if len(ori[i]) > 1:
        num_to_be_checked += ori[i]
        cell_to_be_checked.append(i)
print(num_to_be_checked)
print(cell_to_be_checked)
for v in set(num_to_be_checked):
    print('checking %d: ' % v)
    for i in cell_to_be_checked:
        if v in ori[i]:
            print(i, i // 9 //3)

# print(get_block_list(3, 3))
# print(list(set(get_row_list(1)) | set(get_colum_list(0)) | set(get_block_list(1,0)) - set([1 * 9 + 0])))
