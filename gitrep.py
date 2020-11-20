#!/usr/bin/python
import argparse, os, subprocess, sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("name", help="name of the new repository")
    args = parser.parse_args()

    try:
        os.mkdir(args.name)
    except FileExistsError:
        print("A package with this name already exists")
        exit(-1)

    os.chdir(args.name)
    os.open("README.md", os.O_CREAT, mode=0o644)

    subprocess.run(["git", "init", "-b", "main"], stdout=sys.stdout)
    subprocess.run(["git", "add", "."], stdout=sys.stdout)
    subprocess.run(["git", "commit", "-m", "'First commit'"], stdout=sys.stdout)
    subprocess.run(["hub", "create", args.name], stdout=sys.stdout)
    subprocess.run(["git", "push", "-u"], stdout=sys.stdout)

if __name__ == "__main__":
    main()
