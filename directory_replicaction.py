# ! /bin/env python

'''
*****************
* search_d_tree *
*****************

  Builds from a listing of file/directory structure for export.
  python 2.6 was used.

  Usage:
  python search_d_tree.py  -s <directory to search> -t <temp archive>
  python search_d_tree.py  -s <directory to search> -o <file name>

  Arguments:

    -s      directory to search
    -t      temp archive (where the structure will reside)
    -o      a file containing output

  Flags:
    -h      help

  Example:
      search_d_tree.py  -s /etc/init.d -t tmp

    Version: 001

'''

import os
import getopt
import sys
import re


def usage():
    print(__doc__)


def pars_cmd(argv):
    file_name = None
    search_string = None
    temp_root = None

    if (len(sys.argv[1:]) != 0):

        try:
            opts, args = getopt.getopt(sys.argv[1:], "s:t:o:h")
        except getopt.GetoptError as err:
            # print help information and exit:
            print(err)  # will print something like "option -a not recognized"
            usage()
            sys.exit(2)

        # checks to see if opts(list) is empty

        if not opts:
            print("There were no options given use -h to see help\n")

        # parses opts and arguments
        for o, a in opts:

            if o in ("-h"):
                # help
                usage()
                exit()

            elif o in ("-o"):
                # output file
                file_name = a
            elif o in ("-s"):
                # a string to scrap directories
                search_string = a
            elif o in ("-t"):
                # a string to scrap directories
                temp_root = a
            else:
                assert False, "parse - unhandled option"
                # ...
                # change options check as needed.

    return (search_string, temp_root, file_name)


def new_filestruct(temp_root):
    new_dir_path = os.path.join('/', temp_root, 'archive')

    if os.path.exists(new_dir_path):
        print("clean-up is requried at " + new_dir_path)
        exit(2)
    else:
        return new_dir_path


def dir_scanning(scan_dir, new_dir_path):
    rootDir = scan_dir
    reg = re.compile(r'\.')

    # build start point
    os.makedirs(new_dir_path)

    for dirName, subdirList, fileList in os.walk(rootDir):
        current_dir_path = new_dir_path + dirName
        os.makedirs(current_dir_path)
        for fname in fileList:
            if not re.match(reg, fname):
                dirName = dirName.replace('./.', ' ')
                os.mknod(os.path.join(current_dir_path, fname))


def main():
    # command line input -> (getopt)
    search_string, temp_root, file_name = pars_cmd(sys.argv)

    if search_string is None:
        usage()
        exit(2)
    elif temp_root is None:
        usage()
        exit(2)

    archive_path = new_filestruct(temp_root)
    dir_structure = dir_scanning(search_string, archive_path)


if __name__ == "__main__":
    main()
