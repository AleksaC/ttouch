#!/usr/bin/env python

import argparse
import os
import shutil
import sys
from typing import Optional
from typing import Sequence


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")

    args = parser.parse_args(argv)
    template_dir = os.path.expanduser(
        os.environ.setdefault("TTOUCH_TEMPLATE_DIR", "~/.templates")
    )

    filename = os.path.basename(args.filename)
    template = os.path.join(template_dir, filename)

    if os.path.exists(template):
        shutil.copyfile(template, args.filename)
    else:
        with open(args.filename, "w"):
            pass

    return 0


if __name__ == "__main__":
    sys.exit(main())
