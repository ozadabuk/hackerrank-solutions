import inspect
def reverse_string(st):
    a = list(st)
    a.reverse()
    return ''.join(a)

def count_substring(string, sub_string):
    count = 0
    s = reverse_string(string)
    k = reverse_string(sub_string)
    n = len(s)
    m = len(sub_string)
    for i in range(0, n):
        if i+m <= n:
            print(s + " " + s[i:i + m])
            if s[i:i+m] == k:
                count += 1
                print(count)
    return count

if __name__ == '__main__':
    string = "AbBaAbBaAbBa"
    sub_string = "Ab"

    count = count_substring(string, sub_string)
    print(count)