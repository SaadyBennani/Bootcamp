# peaks_valleys.py


def peaks(data):
    """
    returns the indices of peaks
    """

    peaks_list = []
    for i in range(1, len(data)-1):
        left = data[i-1]
        middle = data[i]
        right = data[i+1]
        if middle > right and middle > left:
            peaks_list.append(i)
    return peaks_list


def valleys(data):
    """
    returns the indices of peaks_valleys
    """

    valleys_list = []
    for i in range(1, len(data)-1):
        left = data[i-1]
        middle = data[i]
        right = data[i+1]
        if middle < right and middle < left:
            valleys_list.append(i)
    return valleys_list


def peaks_and_valleys(data):
    """
    returns the indices of peaks and valleys in one list
    """

    p = peaks(data)
    v = valleys(data)
    return sorted(p+v)


def draw(data):
    """
    draws an image representing the data
    """
    image = []
    peak = max(data)
    while peak > 0:
        row = ['x' if data >= peak else ' ' for data in data]
        image.append(''.join(row))
        peak -= 1
    return '\n'.join(image)


data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

print(data)
print(peaks(data))
print(valleys(data))
print(peaks_and_valleys(data))
print(draw(data))
