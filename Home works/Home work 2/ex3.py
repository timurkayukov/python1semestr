def is_palindrome(s):
    return s == s[::-1]


def is_mirror(s):
    mirror_chars = {'A': 'A', 'H': 'H', 'I': 'I', 'M': 'M', 'O': 'O',
                    'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X',
                    'Y': 'Y', '0': '0', '1': '1', '8': '8','E':'3','3':'E','J':'L','L':'J','S':'2','2':'S','5':'Z','Z':'5'}

    mirrored = ""
    for char in reversed(s):
        if char in mirror_chars:
            mirrored += mirror_chars[char]
        else:
            return False

    return mirrored == s


def check_string(s):
    is_plain_palindrome = is_palindrome(s)
    is_mirror_string = is_mirror(s)

    if is_plain_palindrome and is_mirror_string:
        return "is a mirrored palindrome"
    elif is_plain_palindrome:
        return "is a regular palindrome"
    elif is_mirror_string:
        return "is a mirrored string"
    else:
        return "is not a palindrome"



s= input()
result = check_string(s)
print(s,result)
