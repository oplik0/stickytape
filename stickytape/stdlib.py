import sys


def is_stdlib_module(module_name):
    return any([module in _stdlib_modules for module in module_name.split('/')])


_stdlib_modules = set([
    "string",
    "re",
    "struct",
    "difflib",
    "StringIO",
    "cStringIO",
    "textwrap",
    "codecs",
    "unicodedata",
    "stringprep",
    "fpformat",

    "datetime",
    "calendar",
    "collections",
    "heapq",
    "bisect",
    "array",
    "sets",
    "sched",
    "mutex",
    "Queue",
    "weakref",
    "UserDict",
    "UserList",
    "UserString",
    "types",
    "new",
    "copy",
    "pprint",
    "repr",

    "numbers",
    "math",
    "cmath",
    "decimal",
    "fractions",
    "random",
    "itertools",
    "functools",
    "operator",

    "os.path",
    "fileinput",
    "stat",
    "statvfs",
    "filecmp",
    "tempfile",
    "glob",
    "fnmatch",
    "linecache",
    "shutil",
    "dircache",
    "macpath",

    "pickle",
    "cPickle",
    "copy_reg",
    "shelve",
    "marshal",
    "anydbm",
    "whichdb",
    "dbm",
    "gdbm",
    "dbhash",
    "bsddb",
    "dumbdbm",
    "sqlite3",

    "zlib",
    "gzip",
    "bz2",
    "zipfile",
    "tarfile",

    "csv",
    "ConfigParser",
    "robotparser",
    "netrc",
    "xdrlib",
    "plistlib",

    "hashlib",
    "hmac",
    "md5",
    "sha",

    "os",
    "io",
    "time",
    "argparse",
    "optparse",
    "getopt",
    "logging",
    "logging.config",
    "logging.handlers",
    "getpass",
    "curses",
    "curses.textpad",
    "curses.ascii",
    "curses.panel",
    "platform",
    "errno",
    "ctypes",

    "select",
    "threading",
    "thread",
    "dummy_threading",
    "dummy_thread",
    "multiprocessing",
    "mmap",
    "readline",
    "rlcompleter",

    "subprocess",
    "socket",
    "ssl",
    "signal",
    "popen2",
    "asyncore",
    "asynchat",

    "email",
    "json",
    "mailcap",
    "mailbox",
    "mhlib",
    "mimetools",
    "mimetypes",
    "MimeWriter",
    "mimify",
    "multifile",
    "rfc822",
    "base64",
    "binhex",
    "binascii",
    "quopri",
    "uu",

    "HTMLParser",
    "sgmllib",
    "htmllib",
    "htmlentitydefs",
    "xml",
    "xml.etree",
    "xml.etree.ElementTree",
    "xml.dom",
    "xml.dom.minidom",
    "xml.dom.pulldom",
    "xml.sax",
    "xml.sax.handler",
    "xml.sax.saxutils",
    "xml.sax.xmlreader",
    "xml.parsers",
    "xml.parsers.expat",

    "webbrowser",
    "cgi",
    "cgitb",
    "wsgiref",
    "urllib",
    "urllib2",
    "httplib",
    "ftplib",
    "poplib",
    "imaplib",
    "nntplib",
    "smtplib",
    "smtpd",
    "telnetlib",
    "uuid",
    "urlparse",
    "SocketServer",
    "BaseHTTPServer",
    "SimpleHTTPServer",
    "CGIHTTPServer",
    "cookielib",
    "Cookie",
    "xmlrpclib",
    "SimpleXMLRPCServer",
    "DocXMLRPCServer",

    "audioop",
    "imageop",
    "aifc",
    "sunau",
    "wave",
    "chunk",
    "colorsys",
    "imghdr",
    "sndhdr",
    "ossaudiodev",

    "gettext",
    "locale",

    "cmd",
    "shlex",

    "Tkinter",
    "ttk",
    "Tix",
    "ScrolledText",
    "turtle",

    "pydoc",
    "doctest",
    "unittest",
    "test",
    "test.test_support",

    "bdb",
    "pdb",
    "hotshot",
    "timeit",
    "trace",

    "sys",
    "sysconfig",
    "__builtin__",
    "future_builtins",
    "__main__",
    "warnings",
    "contextlib",
    "abc",
    "atexit",
    "traceback",
    "__future__",
    "gc",
    "inspect",
    "site",
    "user",
    "fpectl",
    "distutils",

    "code",
    "codeop",

    "rexec",
    "Bastion",

    "imp",
    "importlib",
    "imputil",
    "zipimport",
    "pkgutil",
    "modulefinder",
    "runpy",

    "parser",
    "ast",
    "symtable",
    "symbol",
    "token",
    "keyword",
    "tokenize",
    "tabnanny",
    "pyclbr",
    "py_compile",
    "compileall",
    "dis",
    "pickletools",

    "formatter",

    "msilib",
    "msvcrt",
    "_winreg",
    "winsound",

    "posix",
    "pwd",
    "spwd",
    "grp",
    "crypt",
    "dl",
    "termios",
    "tty",
    "pty",
    "fcntl",
    "pipes",
    "posixfile",
    "resource",
    "nis",
    "syslog",
    "commands",

    "ic",
    "MacOS",
    "macostools",
    "findertools",
    "EasyDialogs",
    "FrameWork",
    "autoGIL",
    "ColorPicker",

    "gensuitemodule",
    "aetools",
    "aepack",
    "aetypes",
    "MiniAEFrame",

    "al",
    "AL",
    "cd",
    "fl",
    "FL",
    "flp",
    "fm",
    "gl",
    "DEVICE",
    "GL",
    "imgfile",
    "jpeg",

    "sunaudiodev",
    "SUNAUDIODEV",
])


if sys.version_info[0] >= 3:
    _stdlib_modules.add("asyncio")
