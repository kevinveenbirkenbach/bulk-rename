#!/usr/bin/env python3

import argparse
import os

def rename_files(search, replace, recursive=False):
    if recursive:
        # Walk through directories recursively
        for root, _, files in os.walk('.'):
            for filename in files:
                if search in filename:
                    newname = filename.replace(search, replace)
                    oldpath = os.path.join(root, filename)
                    newpath = os.path.join(root, newname)
                    print(f"Renaming: '{oldpath}' -> '{newpath}'")
                    os.rename(oldpath, newpath)
    else:
        # Rename files in the current directory only
        for filename in os.listdir('.'):
            if os.path.isfile(filename) and search in filename:
                newname = filename.replace(search, replace)
                print(f"Renaming: '{filename}' -> '{newname}'")
                os.rename(filename, newname)

def main():
    parser = argparse.ArgumentParser(
        description='Rename files by replacing a search string with a replacement string in file names.'
    )
    parser.add_argument('search_string', type=str, help='The string to search for in file names.')
    parser.add_argument('replacement_string', type=str, help='The string to replace the search string with.')
    parser.add_argument('-r', '--recursive', action='store_true',
                        help='Perform renaming recursively in subdirectories.')
    
    args = parser.parse_args()

    rename_files(args.search_string, args.replacement_string, recursive=args.recursive)

if __name__ == '__main__':
    main()
