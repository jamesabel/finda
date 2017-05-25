
import glob
import os
import copy
import time


class Finda:
    def __init__(self, includes, excludes, paths, case, verbose):
        self.includes = includes
        self.includes.sort()
        self.excludes = excludes
        self.excludes.sort()
        self.paths = paths
        self.case = case
        self.verbose = verbose
        self.matches = []
        self.remove_includes = None
        self.remove_excludes = None

    def run(self):
        if self.verbose:
            print("strings :", self.includes)
            print("excludes :", self.excludes)
            print("paths :", self.paths)
            print("case :", self.case)
        for path in self.paths:
            for expanded_path in glob.glob(path):
                if self.verbose:
                    print("searching :", expanded_path)
                for root, dirs, files in os.walk(expanded_path):
                    for name in files:
                        file_path = os.path.join(root, name)
                        self.remove_includes = copy.copy(self.includes)
                        self.remove_excludes = copy.copy(self.excludes)
                        for include in self.includes:
                            self.remove(include, file_path, self.remove_includes)
                        for exclude in self.excludes:
                            self.remove(exclude, file_path, self.remove_excludes)
                        self.search_in_file(file_path)
                        # we 'hit' all the matches but none of the excludes
                        if (len(self.remove_includes) == 0) and (self.remove_excludes == self.excludes):
                            self.append(file_path)
        self.matches.sort(key=lambda k: k['mtime'], reverse=True)

    def search_in_file(self, file_path):
        try:
            if file_path.endswith('.txt'):
                #print(file_path)
                for include in self.includes:
                    with open(file_path) as f:
                        for line in f.readlines():
                            self.remove(include, line, self.remove_includes)
                for exclude in self.excludes:
                    with open(file_path) as f:
                        for line in f.readlines():
                            self.remove(exclude, line, self.remove_excludes)
        except UnicodeDecodeError:
            if self.verbose:
                print("UnicodeDecodeError : %s" % file_path)

    def append(self, file_path):
        if file_path not in self.matches:
            mtime = 0
            try:
                mtime = os.path.getmtime(file_path)
            except:
                raise
            self.matches.append({'path': file_path, 'mtime': mtime})

    def remove(self, s, s2, l):
        orig_s = s
        if not self.case:
            s = s.lower()
            s2 = s2.lower()
        if s in s2:
            if orig_s in l:
                l.remove(orig_s)

    def get_paths(self):
        return [m['path'] for m in self.matches]

    def print(self):
        for match in self.matches:
            try:
                print("%s , %s" % (match['path'], time.strftime("%c", time.localtime(match['mtime']))))
            except:
                if self.verbose:
                    print("error printing match")
