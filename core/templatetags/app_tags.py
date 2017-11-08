from __future__ import unicode_literals
from django import template
from django.utils import six
import re
import unicodedata
from unidecode import unidecode

register = template.Library()

# Extra characters outside of alphanumerics that we'll allow.
SLUG_OK = '-_~'


def smart_text(s, encoding='utf-8', errors='strict'):
    if isinstance(s, six.text_type):
        return s

    if not isinstance(s, six.string_types):
        if six.PY3:
            if isinstance(s, bytes):
                s = six.text_type(s, encoding, errors)
            else:
                s = six.text_type(s)
        elif hasattr(s, '__unicode__'):
            s = six.text_type(s)
        else:
            s = six.text_type(bytes(s), encoding, errors)
    else:
        s = six.text_type(s)
    return s


@register.filter(name="uni_slugify")
def slugify(s, ok=SLUG_OK, lower=True, only_ascii=True, spaces=False, space_replacement='-'):
    """
    Creates a unicode slug for given string with several options.
    L and N signify letter/number.
    :param s: Your unicode string.
    :param ok: Extra characters outside of alphanumerics to be allowed.
               Default is '-_~'
    :param lower: Lower the output string.
                  Default is True
    :param spaces: True allows spaces, False replaces a space with the "space_replacement" param
    :param only_ascii: True to replace non-ASCII unicode characters with
                       their ASCII representations.
    :param space_replacement: Char used to replace spaces if "spaces" is False.
                              Default is dash ("-") or first char in ok if dash not allowed
    :type s: String
    :type ok: String
    :type lower: Bool
    :type spaces: Bool
    :type only_ascii: Bool
    :type space_replacement: String
    :return: unicode string
    """

    if only_ascii and ok != SLUG_OK and hasattr(ok, 'decode'):
        try:
            ok.decode('ascii')
        except UnicodeEncodeError:
            raise ValueError(('You can not use "only_ascii=True" with '
                              'a non ascii available chars in "ok" ("%s" given)') % ok)

    rv = []
    for c in unicodedata.normalize('NFKC', smart_text(s)):
        cat = unicodedata.category(c)[0]
        if cat in 'LN' or c in ok:
            rv.append(c)
        elif cat == 'Z':  # space
            rv.append(' ')
    new = ''.join(rv).strip()

    if only_ascii:
        new = unidecode(new)
    if not spaces:
        if space_replacement and space_replacement not in ok:
            space_replacement = ok[0] if ok else ''
        new = re.sub('[%s\s]+' % space_replacement, space_replacement, new)
    if lower:
        new = new.lower()

    return new


@register.filter
def partition(data, n):
    try:
        n = int(n)
    except (ValueError, TypeError):
        return [data]

    res = []
    for i in range(0, len(data), n):
        res.append(data[i:i+n])
    return res
