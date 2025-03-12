#!/usr/bin/env python3

import argparse
import os

def rename_files(search, replace, recursive=False, suffix_only=False):
    if recursive:
        for root, _, files in os.walk('.'):
            for filename in files:
                oldpath = os.path.join(root, filename)
                if suffix_only:
                    # Only rename if the file name ends with the search string
                    if filename.endswith(search):
                        newname = filename[:-len(search)] + replace
                        newpath = os.path.join(root, newname)
                        print(f"Renaming: '{oldpath}' -> '{newpath}'")
                        os.rename(oldpath, newpath)
                else:
                    if search in filename:
                        newname = filename.replace(search, replace)
                        newpath = os.path.join(root, newname)
                        print(f"Renaming: '{oldpath}' -> '{newpath}'")
                        os.rename(oldpath, newpath)
    else:
        for filename in os.listdir('.'):
            if os.path.isfile(filename):
                if suffix_only:
                    if filename.endswith(search):
                        newname = filename[:-len(search)] + replace
                        print(f"Renaming: '{filename}' -> '{newname}'")
                        os.rename(filename, newname)
                else:
                    if search in filename:
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
    parser.add_argument('-s', '--suffix-only', action='store_true',
                        help='Only rename the suffix (file extension) if the file name ends with the search string.')
    
    args = parser.parse_args()
    rename_files(args.search_string, args.replacement_string, recursive=args.recursive, suffix_only=args.suffix_only)

if __name__ == '__main__':
    main()
