from django import template

register = template.Library()
# decorator method
@register.filter(name='cut')
def cut(value,arg):
    """
    this cuts out values of all arg from the strings

    """
    return value.replace(arg,'')

#give name to the filter 'cut' is the name given to the filter cut is the original function
# register.filter('cut',cut)    
