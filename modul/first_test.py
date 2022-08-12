def spam(number):
    return 'bulochka' * number


def my_sum(list_of_numbers):
    count = 0
    for i in list_of_numbers:
        count += i
    return count


def shortener(string):
    new_list = []
    for word in string.split():
        if len(word) > 6:
            new_word = word[:6] + '*'
            new_list.append(new_word)
        else:
            new_list.append(word)
    
    new_str = ''
    for i in new_list:
        new_str += (i + ' ')

    return new_str[:-1]


def compare_ends(words):
    count = 0
    for i in words:
        if len(i) >= 2:
            if i[0] == i[-1]:
                count += 1
    return count