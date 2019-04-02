def find_maxima(x):
    """Find local maxima of x.

    Example:
    >>> x = [1, 2, 3, 2, 4, 3]
    >>> find_maxima(x)
    [2, 4]

    Input arguments:
        x -- 1D list numbers

    Output:
        idx -- list of indices of the local maxima in x
    """

    idx = []
    for i in range(len(x)):
        if i == 0:
            if x[i] > x[i + 1]:
                idx.append(i)
            elif x[i] == x[i+1] and x[i+1] > x[i + 2]:
                idx.append(i, i+1)
        elif i == len(x) - 1:
        # `i` is a local maximum if the signal decreases before and after it
            if x[i-1] < x[i]:
                idx.append(i)
            elif x[i-1] == x[i] and x[i-2] < x[i-1]:
                idx.append(i, i+1)
        else:
            if x[i - 1] < x[i] and x[i+1] < x[i]:
                idx.append(i)
    return idx
