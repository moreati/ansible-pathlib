# Copyright: 2021, Alex Willmer <alex@moreati.org.uk>
# Licensed under the Apache License, Version 2.0

from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.errors import AnsibleError, AnsibleFilterError
from ansible.module_utils._text import to_native

try:
    import pathlib
    PATH_CLASSES = {
        'Path': pathlib.Path,
        'PosixPath': pathlib.PosixPath,
        'WindowsPath': pathlib.WindowsPath,
        'PurePath': pathlib.PurePath,
        'PurePosixPath': pathlib.PurePosixPath,
        'PureWindowsPath': pathlib.PureWindowsPath,
    }
except ImportError:
    pathlib = None


def path(path, cls='Path'):
    if not pathlib:
        raise AnsibleError("You must install the Python pathlib module to use pathlib filter on Python <= 3.5")

    try:
        cls = PATH_CLASSES[cls]
    except KeyError:
        raise AnsibleError("%s is not a known pathlib class" % to_native(cls))

    try:
        path = cls(path)
    except TypeError as e:
        raise AnsibleFilterError(to_native(e))

    return path




class FilterModule(object):
    def filters(self):
        return {
            'path': path,
        }
