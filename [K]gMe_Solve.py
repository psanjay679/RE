import sys
import binascii
username = raw_input()

# username = 'name'

ans = "142{}42CA1618CA427087"

if len(username) < 4:
    print 'length must be atleast of 4 characters'
    sys.exit(0)

char = hex(ord(username[0]) + ord(username[-1]))[2:] + hex(ord(username[1]) + ord(username[-2]))[2:]

ans = ans.format(char).upper()
print ans

# print ans == "142d3ce42ca1618ca427087".upper()
