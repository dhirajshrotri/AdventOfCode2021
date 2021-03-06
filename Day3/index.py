def part2():
    line_cnt = 1
    with open("input.txt", 'r') as infile:
        line = infile.readline().rstrip()
        col_num = [[int(i)] for i in line]
        for line in infile:
            line_cnt += 1
            line = line.rstrip()
            for i in range(0, len(line)):
                col_num[i] += [int(line[i])] 
    freq_num = [str(int(sum(col)>(line_cnt//2))) for col in col_num]
    l_freq_num = ['0' if i == '1' else '1' for i in freq_num]
    
    # O2
    filter_num = [[i, 1] for i in range(line_cnt)]    
    for i in range(len(freq_num)):
        s = [col_num[i][j[0]] if j[1] == 1 else None for j in filter_num ]
        filter_num = [[index, int(digit == int(freq_num[i]))] for index, digit in enumerate(s)]
        if len([j for j in filter_num if j[1] == 1]) == 1:
            break
    _index = [j[0] for j in filter_num if j[1] == 1]
    print(_index)
    o2gen = int(''.join([str(col_num[i][_index[0]]) for i in range(len(freq_num))]), 2)
    print(f"O2: {o2gen}")

    # CO2
    filter_num = [[i, 1] for i in range(line_cnt)]    
    for i in range(len(l_freq_num)):
        s = [col_num[i][j[0]] if j[1] == 1 else None for j in filter_num ]
        filter_num = [[index, int(digit == int(l_freq_num[i]))] for index, digit in enumerate(s)]
        if len([j for j in filter_num if j[1] == 1]) == 1:
            break
    _index = [j[0] for j in filter_num if j[1] == 1]
    print(_index)
    co2gen = int(''.join([str(col_num[i][_index[0]]) for i in range(len(l_freq_num))]), 2)
    print(f"CO2: {co2gen}")
    print(co2gen*o2gen)

part2()