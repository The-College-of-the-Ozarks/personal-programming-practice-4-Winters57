# convert.py
#
# User inputs speed in mph
# Program outputs speed in kph, ft/s, m/s depending on user choice.
#
# Three functions are defined, each with 1 parameter and returning a value:
#   mph -> kph
#   mph -> ft/s
#   mph -> m/s

def mph_to_kph(mph):
    return 1.609*mph

def mph_to_ms(mph):
    return mph_to_kph(mph)*1000/3600

def mph_to_fts(mph):
    return mph*5280/3600

mph = input("Input speed in mph: ")
mph = float(mph)

sel = input("------------------------\nPlease choose which unit you wish to convert mph to. \n kph: \n m/s: \n ft/s:\n------------------------\nunit: ")

if sel == "kph":
    
    print("Speed in kph is", mph_to_kph(mph))

elif sel == "m/s":

    print("Speed in m/s is", mph_to_ms(mph))
    
elif sel == "ft/s":

    print("Speed in ft/s is", mph_to_fts(mph))
    
else:
    print("Incorrect conversion unit input, run again")
