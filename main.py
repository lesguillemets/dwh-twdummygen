import json
import argparse
from pathlib import Path

import polars as pl


def main(f: Path):
    with f.open("r") as fp:
        js = json.load(fp)
    print(len(js))
    data_to_use = js[:1000]
    df = pl.DataFrame()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=Path)
    args = parser.parse_args()
    main(args.file)
