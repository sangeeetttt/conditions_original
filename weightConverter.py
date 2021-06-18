'''
input weight of a person in either kg or lbs. if provides weight in kg, then convert to lbs
and viseversa.
'''

weight = int(input('Enter the weight: '))
unit = input('(Kg) or (Lbs) : ').lower()

if unit.lower() == "kg" :
    inlbs = weight* 2.205
    print(inlbs)
elif unit.lower() == "lbs":
    inkgs = weight/2.205
    print(inkgs)
else:
    print(f'invald')