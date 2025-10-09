"""Lightweight stub of the Unix-only pwd module for Windows environments."""
import getpass
import os
from collections import namedtuple

_StructPwd = namedtuple("struct_passwd", "pw_name pw_passwd pw_uid pw_gid pw_gecos pw_dir pw_shell")

def getpwuid(uid: int) -> _StructPwd:  # type: ignore[name-defined]
    username = os.environ.get("USERNAME") or getpass.getuser() or "unknown"
    return _StructPwd(username, None, uid, 0, "", "", "")
