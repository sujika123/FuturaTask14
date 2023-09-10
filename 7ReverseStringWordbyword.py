#python program to reverse a string word by word
#Method 1
def reverse_word(s, start, end):
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1


def reverse_string(s):
    s = list(s)
    start, end = 0, len(s) - 1
    reverse_word(s, start, end)

    start = end = 0
    while end < len(s):
        if s[end] == ' ':
            reverse_word(s, start, end - 1)
            start = end + 1
        end += 1
    reverse_word(s, start, end - 1)
    return ''.join(s)


s = "i am omkhar"
print(reverse_string(s))

print("________________________________")
# method 2

# Python code
# To reverse words in a given string

# input string
string = "hello how are you"
# reversing words in a given string
s = string.split()[::-1]
l = []
for i in s:
	# appending reversed words to l
	l.append(i)
# printing reverse words
print(" ".join(l))

