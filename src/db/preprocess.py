def get_averages_per_station(lists_from_query, omitted_values=None):
    if omitted_values is None:
        omitted_values = []
    averages = []
    for arr in lists_from_query:
        row_counts = 0
        sum_of_values = 0
        for l in arr:
            if l not in omitted_values:
                row_counts += 1
                sum_of_values += l[0]
        if row_counts != 0:
            averages.append(sum_of_values / row_counts)
        else:
            averages.append(0)
    return averages


def get_sum_per_station(lists_from_query):
    sum_of_values = []
    for arr in lists_from_query:
        sum_tmp = 0
        for l in arr:
            sum_tmp += l[0]
        sum_of_values.append(sum_tmp)
    return sum_of_values
