def sum_of_intervals(intervals):
    #print(list(range(intervals[0], intervals[1])))
    concat = []
    for i in range(len(intervals)):
        concat += list(range(intervals[i][0], intervals[i][1]))
    return len(set(concat))