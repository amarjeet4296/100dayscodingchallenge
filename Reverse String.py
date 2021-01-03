A = "Vaibhav Sharma"
print(A[::-1])



s = "AMARJEET KRISHNAN"
output = ''
i = len(s)-1
while i >= 0:
    output = output + s[i]
    i = i - 1
print(output)


def reverse(string):
    reversed_string = ''
    for i in string:
        reversed_string = i + reversed_string
    print(reversed_string)

string = "MADHUR GUPTA"
print(string)
reverse(string)
