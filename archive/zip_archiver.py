import zipfile
from pathlib import Path

def zip_compress(source, output):
    source = Path(source)
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as z:
        if source.is_file():
            z.write(source, source.name)
        else:
            for file in source.rglob("*"):
                z.write(file, file.relative_to(source))

def zip_extract(archive, output):
    with zipfile.ZipFile(archive, "r") as z:
        z.extractall(output)
