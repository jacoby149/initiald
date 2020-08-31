#Strategy
#Get all py files that arent init.py
#group python files by shared directory
#make the correct init file for each shared directory

import os
import glob
import psutil


sys_string = '/'
if psutil.WINDOWS:
    sys_string = '\\'


def get_files():
    paths = []
    for filename in glob.iglob('**', recursive=True):
        paths.append(filename)
    return paths


def filter_py(files):
    def f(s):
        def is_long_enough(s):
            return len(s) > 3

        def is_py(s):
            return s[-3:] == ".py"

        def is_init(s): 
            # print(s)
            return '__init__.py' in s
        return is_long_enough(s) and is_py(s) and not is_init(s)
    return list(filter(f, files))


def in_folder(dir, file):
    if dir in file:
        print(dir, ', ', file)
        file = file[len(dir) + 1:-3]
        print(file)
        if sys_string in file:
            return False
        else:
            return True
    return False


def write_init(init, d):
    with open(d + sys_string + "__init__.py", 'w+') as f:
        for line in init:
            f.write(line)


def make_inits(dir_set,pys):
    for d in dir_set:
        init = []
        for p in pys:
            if in_folder(d, p):
                raw_p = p[len(d) + 1:-3]
                imp_str = 'from .' + raw_p + ' import *\n'
                init.append(imp_str)
                print('appending', imp_str)
        write_init(init, d)


def get_all_dirs(dir_set):
    lastlength = 0
    while len(dir_set) != lastlength:
        dir_new = set(dir_set)
        lastlength = len(dir_set)
        for d in dir_set:
            parent = sys_string.join(d.split(sys_string)[:-1])
            if parent not in dir_set and parent != '':
                dir_new.add(parent)
        dir_set = dir_new
    return dir_set


def make_empty_inits(dir_set):
    for d in dir_set:
        with open(d + sys_string + "__init__.py", 'w+') as f:
            f.write('# intentionally left blank')


def get_package_structure():
    # get all the files
    files = get_files()
    # get all of the non __init__ python files
    pys = filter_py(files)
    # split by backslash
    split_pys = [d.split(sys_string) for d in pys]
    # get all the directories
    dir_set = set([sys_string.join(d[:-1]) for d in split_pys])
    dir_set.remove('')
    return dir_set, pys


def delete_inits(dir_set):
    for d in dir_set:
        file_name = d + sys_string + '__init__.py'
        os.remove(file_name)


def create_inits():
    dir_set, pys = get_package_structure()
    make_empty_inits(get_all_dirs(dir_set))
    make_inits(dir_set, pys)


def cleanup_inits():
    dir_set, pys = get_package_structure()
    delete_inits(get_all_dirs(dir_set))


create_inits()
