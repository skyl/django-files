--------------
django-files
--------------

An app for tagging arbitrary models with "files".
A file is a simple model with a filefield, title, description, owner, content-object.

The idea is to have templatetags for tagging objects with 
(google gears drag and drop?)

Likewise, an overview of files for various model_instances will be obtainable.


Requirements
============

    * jQuery 1.3+

This app is being built for pinax-0.7+.
Your mileage may vary out of the box in other environments.
For quick integration you will need a current copy django-uni_form, for instance.

Install
=======

    * Check out the code onto your path as files::

        git clone git://github.com/skyl/django-files.git files

    * Add 'files' to INSTALLED_APPS

    * add (r'^files/', include('files.urls')), to your urlpatterns

    * syncdb

For Pinax you can take the additional steps, 
add to the right_tabs block in site_base.html::

    <li id="tab_files"><a href="{% url files_all %}">{% trans "Files" %}</a></li>

In site_tabs.css you can add rules for
``body.files #tab_files a`` and ``body.files #tab_files``. 

Pinax Usage
===========

In the template with the object(s) you want to tag add::

    {% load files_tags %}

Where you would like the link to add an file to a model instance::

    {% file_link_add_to myModelInstance 'css_id' %}

To make this link a jQuery dialog widget, in extra_body::

    <script type="text/javascript" src="{{MEDIA_URL}}files/js/jquery-ui.js"></script>
    {% add_file_to myModelinstance 'css_id' %}
 
Note that you can choose 'css_id' for these tags but they must match.

Add css for the widget to extra_head::

    {% include 'files/widgetCSS.html' %}
  
To add a link to all of the files for a model instance::
    
    {% link_to_files_for myModelInstance 'css_class' %}


