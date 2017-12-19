import advancedPrint as ap 

effectList = ap.effects.__dict__ # Creates array out of class

for effect in effectList: 
    effectString = str(effect).lower() # turns the effect into a string and lowercase
    if(effectString.startswith("_")): # Ignores unnecessary values
        continue
    ap.effect(effectString) # Applies effect
    print(effectString) # Prints effect name
ap.effect(ap.effects.RESET) # Resets the effect