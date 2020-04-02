from django import template

from {{cookiecutter.project_slug}}.base.models import People

register = template.Library()


# People (Directors) snippets
@register.inclusion_tag("base/include/people.html", takes_context=True)
def directors(context):
    return {
        "directors": (People.published.all()).filter(position__iregex=r"Director|CEO"),
        "request": context["request"],
    }


# People (Staff) snippets
@register.inclusion_tag("base/include/people.html", takes_context=True)
def staff(context):
    return {
        "staff": (People.published.all()).exclude(position__iregex=r"Director|CEO"),
        "request": context["request"],
    }
