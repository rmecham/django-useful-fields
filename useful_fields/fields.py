# coding: utf-8
from __future__ import unicode_literals

import uuid

import bleach
import pytz
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.encoding import smart_text
from markdown import markdown
from markdown.extensions.smarty import SmartyExtension


class TimeZoneField(models.CharField):
    description = 'A pytz timezone object'
    CHOICES = [(tz, tz) for tz in pytz.all_timezones]
    MAX_LENGTH = 63

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = kwargs.get('choices', self.CHOICES)
        kwargs['max_length'] = kwargs.get('max_length', self.MAX_LENGTH)
        super(TimeZoneField, self).__init__(*args, **kwargs)

    def get_internal_type(self):
        return 'CharField'

    def to_python(self, value):
        "Convert to pytz timezone object"
        return self._get_python_and_db_repr(value)[0]

    def get_prep_value(self, value):
        "Convert to string describing a valid pytz timezone object"
        return self._get_python_and_db_repr(value)[1]

    def _get_python_and_db_repr(self, value):
        "Returns a tuple of (python representation, db representation)"
        if value is None or value == '':
            return (None, None)
        if value is pytz.UTC or isinstance(value, pytz.tzinfo.BaseTzInfo):
            return (value, smart_text(value))
        if isinstance(value, str):
            try:
                return (pytz.timezone(value), value)
            except pytz.UnknownTimeZoneError:
                pass
        raise ValidationError("Invalid timezone “{}”".format(value))


smarty_extension = SmartyExtension(substitutions={
    'left-double-quote': '“',
    'right-double-quote': '”',
    'left-single-quote': '‘',
    'right-single-quote': '’',
    'ellipsis': '…',
    'ndash': '–',
    'mdash': '—',
})


class MarkdownMixin(object):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('blank', True)
        kwargs.setdefault('editable', False)
        populate_from = kwargs.pop('populate_from', None)
        if populate_from is None:
            raise ValueError("missing 'populate_from' argument")
        else:
            self._populate_from = populate_from
        self._allow_html = kwargs.pop('allow_html', False)
        self._extensions = kwargs.pop('extensions', [])
        super(MarkdownMixin, self).__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(MarkdownMixin, self).deconstruct()
        kwargs['populate_from'] = self._populate_from
        if self._allow_html:
            kwargs['allow_html'] = self._allow_html
        if self._extensions:
            kwargs['extensions'] = self._extensions
        return name, path, args, kwargs

    def render(self, model_instance):
        value = getattr(model_instance, self._populate_from)
        extensions = list(self._extensions)
        # Everyone gets smarty, no matter what.
        extensions.append(smarty_extension)
        if not self._allow_html:
            value = bleach.clean(value)
        html = markdown(value, extensions=extensions)
        return html


class MarkdownCharField(MarkdownMixin, models.CharField):
    def pre_save(self, model_instance, add):
        """
        Since CharFields are one-liners, we really don’t want the <p> tags that
        Markdown automatically adds. Here, we get rid of them.
        """
        return self.render(model_instance)[3:-4]


class MarkdownTextField(MarkdownMixin, models.TextField):
    def pre_save(self, model_instance, add):
        return self.render(model_instance)


class UUIDPrimaryKeyField(models.UUIDField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('primary_key', True)
        kwargs.setdefault('default', uuid.uuid4)
        kwargs.setdefault('editable', False)
        super(UUIDPrimaryKeyField, self).__init__(*args, **kwargs)
