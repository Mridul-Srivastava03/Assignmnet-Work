def master_yoda(s):
    words = s.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)

s = input("Enter your message for master yoda: ")
print(master_yoda(s))