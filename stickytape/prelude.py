
global __stickytape_extract_archive
def __stickytape_extract_archive(archive_data, hash):
    from zipfile import ZipFile, ZIP_DEFLATED
    from io import BytesIO 
    from pathlib import Path
    import os

    dir_path = Path(os.environ.get("XDG_CACHE_HOME", Path.home() / ".cache")) / "mn2" / "dependencies"
    dir_path.mkdir(parents=True, exist_ok=True)
    hash_file = dir_path / "hash.txt"
    if not hash_file.exists() or hash_file.read_text(encoding="utf-8").strip() != hash:
        buffer = BytesIO(archive_data)
        archive = ZipFile(buffer, mode="r", compression=ZIP_DEFLATED)
        archive.extractall(dir_path)
        hash_file.write_text(hash)

    
    import sys
    sys.path.insert(0, str(dir_path.absolute()))

