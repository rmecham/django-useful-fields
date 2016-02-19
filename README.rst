django-useful-fields
====================

| I found myself copying a few Django database field classes from project to project so I decided to bundle them together
| and release them as an open source package instead. Here are the fields that are currently included:

-  **TimeZoneField**

   | This field stores a reference to a time zone in the database and automatically instantiates the correct pytz time
   | zone object on retrieval. Useful for recording a user’s default time zone.

-  **MarkdownCharField**

   | This field is meant to be used in collaboration with a regular CharField. The regular CharField stores the Markdown-
   | formatted source text and this field will store the rendered HTML version of that same text. Use the ``populate_from``
   | argument to indicated which field on the same model contains the source text. If the ``allow_html`` argument is
   | ``False`` (the default), any HTML tags present in the source text will be removed using the
   | `bleach library <https://github.com/mozilla/bleach>`__. The ``extensions`` argument can be used to enable any desired
   | `extensions <https://pythonhosted.org/Markdown/extensions/index.html>`__ for the
   | `Markdown library <https://pythonhosted.org/Markdown/>`__. One extension is enabled by default:
   | `SmartyPants <https://pythonhosted.org/Markdown/extensions/smarty.html>`__. SmartyPants is configured to use the
   | correct Unicode characters (e.g. “) rather than HTML entities (e.g. ``&ldquo;``). Since CharFields don’t normally
   | contain paragraphs of text, MarkdownCharField strips the ``<p></p>`` tags that Markdown always includes.

-  **MarkdownTextField**

   | This field is meant to be used in collaboration with a regular TextField. The regular TextField stores the Markdown-
   | formatted source text and this field will store the rendered HTML version of that same text. Use the ``populate_from``
   | argument to indicated which field on the same model contains the source text. If the ``allow_html`` argument is
   | ``False`` (the default), any HTML tags present in the source text will be removed using the
   | `bleach library <https://github.com/mozilla/bleach>`__. The ``extensions`` argument can be used to enable any desired
   | `extensions <https://pythonhosted.org/Markdown/extensions/index.html>`__ for the
   | `Markdown library <https://pythonhosted.org/Markdown/>`__. One extension is enabled by default:
   | `SmartyPants <https://pythonhosted.org/Markdown/extensions/smarty.html>`__. SmartyPants is configured to use the
   | correct Unicode characters (e.g. “) rather than HTML entities (e.g. ``&ldquo;``).

-  **UUIDPrimaryKeyField**

   | UUIDs are, in many ways, better primary keys than automatically incrementing integer fields. Unfortunately, the
   | default Django implementation—\ ``UUIDField``—requires some boilerplate (including importing the ``uuid`` module) before
   | it can be used as a primary key. UUIDPrimaryKeyField manages the boilerplate for you. Just add

   ::

       id = UUIDPrimaryKeyField()

   to your model and everything will just work.
