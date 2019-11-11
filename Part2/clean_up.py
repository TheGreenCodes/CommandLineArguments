import os
import shutil
import glob
import argparse


def organize(folder):
    """Organize files according to extension """

    # get into the directory passed
    os.chdir(folder)
    all_files = [x for x in os.listdir('.')]

    file_types = set((os.path.splitext(f)[1] for f in all_files))

    for ftype in file_types:
        new_directory = ftype.replace(".", '')
        os.mkdir(new_directory)

        for fname in glob.glob(f'*.{ftype[1:]}'):
            shutil.move(fname, new_directory)



def main():
    parser = argparse.ArgumentParser(description="sort files according to file extension")

    parser.add_argument("path", help="Path of directory with unsortsed files")
    parser.add_argument("-v","--verbose", help="Descriptive message of directory after sort", action="store_true")


    arguments = parser.parse_args()

    organize(arguments.path)

    if arguments.verbose:
        print("\n The following files were extensions were found and organized successfully...")
        print(os.listdir('.'))
    else:
        print("Done!")
    

main()



