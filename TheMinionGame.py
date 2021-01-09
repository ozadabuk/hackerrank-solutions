def findSubCount(st:str, sub:str):
    start = 0
    count = 0
    while True:
        start = st.find(sub, start) + 1
        if start > 0:
            count += 1
        else:
            return count

def minion_game(s):
    # your code goes here
    vowels = "AEIOU"
    p1Score = 0
    p2Score = 0

    for i in range(len(s)):
        if s[i] in vowels:
            p1Score += (len(s) - i)
        else:
            p2Score += (len(s) - i)

    if p1Score > p2Score:
        print("Kevin " + str(p1Score))
    elif p1Score == p2Score:
        print("draw")
    else:
        print("Stuart " + str(p2Score))

if __name__ == "__main__":

    f = open("input.txt", "r")
    data = f.read()
    data = data.rstrip("\n")
    #data = "BANANA"
    print(data)
    result = minion_game(data)
    print(result)