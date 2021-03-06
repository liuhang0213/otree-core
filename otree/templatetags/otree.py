from .otree_tags import (
    template, FormFieldNode, NextButtonNode,
    c, abs_value, safe_json,
)

# renaming otree_tags to otree and removing internal tags
# this code is duplicated in otree_tags. I duplicate it rather than importing
# register, because PyCharm's autocomplete doesn't detect the import and
# flags all the template tags in yellow.

register = template.Library()
register.tag('formfield', FormFieldNode.parse)
register.tag('next_button', NextButtonNode.parse)
register.filter(name='c', filter_func=c)
register.filter(name='abs', filter_func=abs_value)
register.filter(name='json', filter_func=safe_json)
