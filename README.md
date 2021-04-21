# Ansible Collection - moreati.pathlib

A bare mniimum wrapper arounf the pathlib module.

```
$ ansible-playbook playbooks/demo.yml
PLAY [Demonstrate pathlib filter plugins] ***************************************************************

TASK [Gathering Facts] **********************************************************************************
ok: [localhost]

TASK [Show components of path] **************************************************************************
ok: [localhost] => {
    "msg": {
        "path": "/foo/bar/pkg-1.2.3.tar.gz",
        "path.anchor": "/",
        "path.as_uri()": "file:///foo/bar/pkg-1.2.3.tar.gz",
        "path.is_absolute()": true,
        "path.name": "pkg-1.2.3.tar.gz",
        "path.parent": "/foo/bar",
        "path.parents": "[PosixPath('/foo/bar'), PosixPath('/foo'), PosixPath('/')]",
        "path.parts": [
            "/",
            "foo",
            "bar",
            "pkg-1.2.3.tar.gz"
        ],
        "path.stem": "pkg-1.2.3.tar",
        "path.suffix": ".gz",
        "path.suffixes": [
            ".2",
            ".3",
            ".tar",
            ".gz"
        ]
    }
}
```