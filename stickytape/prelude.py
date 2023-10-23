
global __stickytape_zipfile
global __stickytape_bytesio
global __stickytape_os

from zipfile import ZipFile as __stickytape_zipfile
from io import BytesIO as __stickytape_bytesio
import os as __stickytape os

def __stickytape_extract_archive(archive_data, hash):
    from zipfile import ZipFile
    from io import BytesIO 
    import os
    dir_path = Path(__stickytape_os.environ.get("XDG_CACHE_HOME", Path.home() / ".cache")) / "mn2" / "dependencies"
    dir_path.mkdir(parents=True, exists_ok=True)
    hash_file = dir_path / "hash.txt"
    if not hash_file.exists() or hash_file.read_text(encoding="utf-8").strip() != hash:
        buffer = __stickytape_bytesio(archive_data)
        archive = __stickytape_zipfile(buffer)
        archive.extractall(dir_path)
        hash_file.write_text(hash)

    
    import sys
    sys.path.insert(0, __stickytape_working_dir)

