
global __stickytape_contextlib
global __stickytape_zipfile
global __stickytape_bytesio

import contextlib as __stickytape_contextlib
from zipfile import ZipFile as __stickytape_zipfile
from io import BytesIO as __stickytape_bytesio

@__stickytape_contextlib.contextmanager
def __stickytape_temporary_dir():
    import tempfile
    import shutil
    dir_path = tempfile.mkdtemp()
    try:
        yield dir_path
    finally:
        shutil.rmtree(dir_path)

global __stickytape_working_dir
with __stickytape_temporary_dir() as __stickytape_working_dir:
    def __stickytape_extract_archive(archive):
        buffer = __stickytape_bytesio(archive)
        archive = __stickytape_zipfile(buffer)
        archive.extractall(__stickytape_working_dir)
    
    import sys as __stickytape_sys
    __stickytape_sys.path.insert(0, __stickytape_working_dir)

