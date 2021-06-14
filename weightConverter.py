'''
input weight of a person in either kg or lbs. if provides weight in kg, then convert to lbs
and viseversa.
'''

weight = int(input('the weight: '))
unit = str(input('the unit of measurement you entered(kg or lbs): '))

if unit = kg:
    inlbs= weight* 2.205
    print(inlbs)
elif unit = lbs:
    inkgs= weight/2.205
    print(inkgs)