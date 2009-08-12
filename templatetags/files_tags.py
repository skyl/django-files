from django import template

register = template.Library()

from django.contrib.contenttypes.models import ContentType

@register.inclusion_tag('files/tags/add.html')
def add_file_to(model_instance, css_id):
    ''' Tag instance with an file with dialog widget

    {% add_file_to myModel 'css_id' %}
    This is a javascript bit that requires jQuery.
    On pinax you may put it in extra_body.
    '''

    ContentType.objects.get_for_model(model_instance)
    obj_id = model_instance.id

    app_label = model_instance._meta.app_label
    model_name = model_instance._meta.module_name

    return locals()

@register.inclusion_tag('files/tags/add_link.html')
def file_link_add_to(model_instance, css_id):
    ''' Produce the link for add_file_to javascript

    {% file_link_add_to myModel 'css_id' %}
    '''

    app_label = model_instance._meta.app_label
    model_name = model_instance._meta.module_name

    return locals()

@register.inclusion_tag('files/tags/link_to_files_for.html')
def link_to_files_for(model_instance, css_class):
    ''' Produce the link to the files detail page

    {% link_to_files_for myModel 'css_class' %}
    '''

    app_label = model_instance._meta.app_label
    model_name = model_instance._meta.module_name

    return locals()

@register.inclusion_tag('files/tags/add_url.html')
def files_add_url(model_instance):
    ''' Produce the url to add files to a model

    {% files_add_url myModel %} might return something like:
    /files/add/auth/user/1/
    '''

    app_label = model_instance._meta.app_label
    model_name = model_instance._meta.module_name

    return locals()

@register.inclusion_tag('files/tags/show_file.html')
def show_file(file, user, truncate):
    ''' Show the file summary, suitable for a list display

    {% show_file file_instance user 50 %} to truncate at 50
    {% show_file file_instance user 0 %} to not truncate the description
    Add an extra argument
    '''

    if file.owner == user:
        is_owner = True

    else:
        is_owner = False

    return locals()

