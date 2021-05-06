# Simple Application of Assertion



#============================================================================================================#
podBayDoorStatus = 'open'
# if podBayDoorStatus != 'open', throw AssertionError
assert podBayDoorStatus == 'open','The pod bay doors need to be "open"'# assert ..., exception message

podBayDoorStatus = 'I\'m sorry, Dave. I\'m afraid I can\'t do that.'
assert podBayDoorStatus == 'open','The pod bay doors need to be "open"'# throw AssertionError

#============================================================================================================#
# Exercise 1
market_2nd = {'ns':'green','ew':'red'}
mission_16th = {'ns':'red','ew':'green'}

def switchLights(spotlight):
    for key in spotlight.keys():
        if spotlight[key] == 'green':
            spotlight[key] = 'yellow'
        elif spotlight[key] == 'yellow':
            spotlight[key] = 'red'
        elif spotlight[key] == 'red':
            spotlight[key] = 'green'
    assert 'red' in spotlight.values(),'Neither light is red! '+ str(spotlight)

switchLights(market_2nd)

#============================================================================================================#

