name = str(input("Enter the Legend name in this world"))


def vowels(name):
    final = ""
    letter = ["a","e","i","o","u"]
    for x in name:
        if x in letter:
            pass
        else:
            final += x

    return final

print("ANSWER",vowels(name))

