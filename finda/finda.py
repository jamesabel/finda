
import glob
import os
import copy

class Finda:
    def __init__(self, patterns, paths, verbose):
        self.patterns = patterns
        self.paths = paths
        self.verbose = verbose
        self.matches = []

    def run(self):
        if self.verbose:
            print("strings :", self.patterns)
            print("paths :", self.paths)
        for path in self.paths:
            for expanded_path in glob.glob(path):
                if self.verbose:
                    print("searching :", expanded_path)
                for root, dirs, files in os.walk(expanded_path):
                    for name in files:
                        file_path = os.path.join(root, name)
                        self.remove_patterns = copy.copy(self.patterns)
                        for pattern in self.patterns:
                            if pattern.lower() in file_path.lower():
                                self.remove(pattern)
                        self.search_in_file(file_path)
                        if len(self.remove_patterns) == 0:
                            self.append(file_path)

    def search_in_file(self, file_path):
        try:
            if '.txt' in file_path:
                #print(file_path)
                for pattern in self.patterns:
                    with open(file_path) as f:
                        for line in f.readlines():
                            if pattern.lower() in line.lower():
                                self.remove(pattern)
        except:
            if self.verbose:
                print("could not read ", file_path)

    def append(self, file_path):
        if file_path not in self.matches:
            self.matches.append(file_path)

    def remove(self, pattern):
        if pattern in self.remove_patterns:
            self.remove_patterns.remove(pattern)

    def get_matches(self):
        self.matches.sort()
        return self.matches

    def print(self):
        for match in self.matches:
            try:
                print(match)
            except:
                if self.verbose:
                    print("error printing match")
