name = input()
corrected_name = ""
for char in name:
    if not len(corrected_name):
        corrected_name += char
    elif char != corrected_name[-1]:
        corrected_name += char

print(corrected_name)
