#!/usr/bin/env python3
import subprocess, argparse, os.path

def test(binary_name):
    if not os.path.isfile(binary_name):
        raise IOError("not a file")
    proc = subprocess.run([binary_name], universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    assert proc.returncode == 1
    assert proc.stdout == ""
    assert proc.stderr == ""

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("bin", type=str)
    parser.set_defaults(func=lambda args: test(args.bin))

    args = parser.parse_args()
    args.func(args)
