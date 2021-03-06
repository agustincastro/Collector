from django import template

register = template.Library()


@register.filter(name='addcss')
def addcss(field, css):
    return field.as_widget(attrs={"class": css})


@register.filter(name='placeholder')
def placeholder(value, token):
    # value.field.widget.attrs["placeholder"] = token
    return value.as_widget(attrs={"placeholder":token})
# def placeholder(field, args=None):
#     if args == None:
#         return field
#     return field.field.widget.attrs.update({ "placeholder": args })
