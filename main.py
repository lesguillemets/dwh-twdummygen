import json
import argparse
from pathlib import Path
from datetime import datetime
from random import randint

import polars as pl


def main(f: Path):
    with f.open("r") as fp:
        js = json.load(fp)
    print(len(js))
    print(js[0])
    data_to_use = [tw for tw in js if "in_reply_to_status_id_str" not in tw["tweet"]][
        :1000
    ]
    # df = pl.DataFrame()
    tweets = (tw["tweet"]["full_text"] for tw in data_to_use)
    times = [
        datetime.strptime(tw["tweet"]["created_at"], "%a %b %d %H:%M:%S %z %Y")
        for tw in data_to_use
    ]

    df = pl.DataFrame(
        {
            "記事": tweets,
            "記載日": (t.strftime("%Y-%m-%d") for t in times),
            "記載時刻": (t.strftime("%H:%M:%S") for t in times),
            "オーナー": "M",
            "患者ID": "99999",
            "オーナー職種": "job",
            "記事データ種別": "S",
            "シーケンスID": (randint(0, 100000) for _ in range(len(times))),
        }
    )

    df.write_csv("data/Dummy.csv")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=Path)
    args = parser.parse_args()
    main(args.file)
