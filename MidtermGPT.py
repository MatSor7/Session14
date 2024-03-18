import re


def count_bob_patterns(text):
    pattern = r'b\w*Bob'
    matches = re.findall(pattern, text)
    return len(matches)


# Test the function
text = "Bob is a bbbbBob, bbobs, babobob. Bob"
print("Number of 'b...Bob' patterns:", count_bob_patterns(text))

