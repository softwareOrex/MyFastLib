import argparse
from myfastlib.archive.zip_archiver import zip_compress, zip_extract
from myfastlib.archive.tar_archiver import tar_compress, tar_extract
from myfastlib.speed.timer import timer
import runpy
import time


def run_script(path):
    start = time.perf_counter()
    runpy.run_path(path)
    end = time.perf_counter()
    print(f"[MyFastLib] Script executed in {end - start:.6f}s")


def main():
    parser = argparse.ArgumentParser(
        prog="myfast",
        description="MyFastLib CLI – speed & archive toolkit"
    )

    sub = parser.add_subparsers(dest="command")

    # ZIP
    zip_cmd = sub.add_parser("zip")
    zip_cmd.add_argument("source")
    zip_cmd.add_argument("output")

    unzip_cmd = sub.add_parser("unzip")
    unzip_cmd.add_argument("archive")
    unzip_cmd.add_argument("output")

    # TAR
    tar_cmd = sub.add_parser("tar")
    tar_cmd.add_argument("source")
    tar_cmd.add_argument("output")

    untar_cmd = sub.add_parser("untar")
    untar_cmd.add_argument("archive")
    untar_cmd.add_argument("output")

    # BENCH
    bench_cmd = sub.add_parser("bench")
    bench_cmd.add_argument("script")

    args = parser.parse_args()

    if args.command == "zip":
        zip_compress(args.source, args.output)

    elif args.command == "unzip":
        zip_extract(args.archive, args.output)

    elif args.command == "tar":
        tar_compress(args.source, args.output)

    elif args.command == "untar":
        tar_extract(args.archive, args.output)

    elif args.command == "bench":
        run_script(args.script)

    else:
        parser.print_help()
