is_female = False
is_tall = True

if is_female and is_tall:
    print("You are a female or tall")
elif is_female and not(is_tall):
    print("You are a short female")
elif not(is_female) and is_tall:
    print("You are not a female and is tall")
else:
    print("You either not female or not tall or both")
