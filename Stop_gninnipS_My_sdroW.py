def spin_words(sentence):
    words = sentence.split()
    ans = []

    for word in words:
        if len(word) < 5:
            ans.append(word)
        else:
            ans.append(word[::-1])

    return " ".join(ans)


def mine(sentence):
    ans = ""
    words = sentence.split()

    for word in words:
        if len(word) < 5:
            ans += word
        else:
            rev = word[::-1]
            ans += rev
        ans += " "
    return ans.rstrip()
