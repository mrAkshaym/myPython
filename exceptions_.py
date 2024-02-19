

acronyms = {'LOL': 'Laugh Out Loud',
            'IDK': "I Don't Know",
            'BFF': 'Best Friends Forever',
            'IMHO': 'In My Humble Opinion',
            'TBT': 'Throwback Thursday',
            'YOLO': 'You Only Live Once',
            'SMH': 'Shaking My Head',
            'LMAO': 'Laughing My'}

#definition = acronyms.get('WDYD')
'''
try:
    definition = acronyms['WDYD']
    print(definition)
except:
    print("The key does not exist in the dictionary.")
'''

try:
    raise Exception("Testing exception handling")
except:
    print("The user exception has been caught.")
finally:
    print("This will always execute.")
