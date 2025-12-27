import tarfile

def tar_compress(source, output):
    with tarfile.open(output, "w:gz") as tar:
        tar.add(source, arcname=".")

def tar_extract(archive, output):
    with tarfile.open(archive, "r:gz") as tar:
        tar.extractall(output)
