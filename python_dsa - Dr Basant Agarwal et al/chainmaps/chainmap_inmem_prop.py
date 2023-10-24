from collections import ChainMap

defaults = {
    'theme':'Default',
    'language':'eng',
    'showIndex':True,
    'showFooter':True
}

cm = ChainMap(defaults) #creates a chainMap with defaults
print(cm.maps)

print()
cm2 = cm.new_child({'theme':'bluesky'}) #creates a new chainMap with a child
                                        # that ovverrides the parent
print(cm2.maps)

print()
print(cm2['theme']) # returns the overriden theme 'bluesky'
print(cm2.pop('theme')) # returns the child theme value 'bluesky'
print(cm2['theme']) # returns 'Default' theme

print()
print(cm2.maps)
print(cm2.parents)