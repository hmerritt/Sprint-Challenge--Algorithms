'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word, position = 1, count = 0):
    if len(word) < 2 or position > len(word) - 1:
        return count

    if word[position - 1] == "t" and word[position] == "h":
        count += 1

    return count_th(word, position + 1, count)

print(count_th("te-th-st-th--sdfsfsasd-th"))
