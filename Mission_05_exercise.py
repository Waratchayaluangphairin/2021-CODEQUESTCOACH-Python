is_female = True
is_athlete = True

if is_female and is_athlete:
    print("You are a female and an athlete.")
elif is_female and not(is_athlete):
    print("You are a female but not an athlete.")
elif not(is_female) and is_athlete:
    print("You are not a female but is an athlete.")
else:
    print("You are neither a female nor an athlete.")