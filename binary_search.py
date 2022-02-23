def binary_search(n, sorted_values):
    low_ind = 0
    high_ind = len(sorted_values)-1

    while low_ind <= high_ind:
        mid_ind = (low_ind + high_ind) // 2
        if sorted_values[mid_ind] == n:
            return mid_ind
        elif sorted_values[mid_ind] < n:
            low_ind = mid_ind + 1
        else:
            high_ind = mid_ind - 1