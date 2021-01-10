
from argparse import ArgumentParser
from urllib.parse import urlparse

class fingerprint():

    def __init__(self, inputfile, outputfile, mode):
        self.inputfile = inputfile
        self.outputfile = outputfile
        self.mode = mode

    def checkduplicate(self, word):
        flag = 0
        try:
            t = open(self.outputfile, 'r').read()
            for line in t.split("\n"):
                if word.lower() == line.lower():
                    flag = 1
                if flag > 0:
                    return 0
            return 1
        except OSError:
            print('cannot open {}'.format(self.outputfile))

    def argumentextract(self):
        try:
            f = open(self.inputfile, 'r').read()
            for url in f.split("\n"):
                parse_object = urlparse(url)
                for argumentin in parse_object.query.split('&'):
                    if self.checkduplicate(argumentin) == 1:
                        try:
                            t = open(self.outputfile, 'a')
                            print('The argumnet :{}'.format(argumentin))
                            t.write('{}\n'.format(argumentin))
                            t.close()
                        except OSError:
                            print('cannot open :{}'.format(self.outputfile))
        except OSError:
            print('cannot open :{}'.format(self.inputfile))

    def urlextract(self):
        try:
            f = open(self.inputfile, 'r').read()
            for url in f.split("\n"):
                parse_object = urlparse(url)
                for domainin in parse_object.netloc.split('.'):
                    if (domainin != 'com') and self.checkduplicate(domainin) == 1 and domainin != 'www' and domainin != '\n':
                        try:
                            t = open(self.outputfile, 'a')
                            print('The domain :{}'.format(domainin))
                            t.write('{}\n'.format(domainin))
                            t.close()
                        except OSError:
                            print('cannot open :{}'.format(self.outputfile))
        except OSError:
            print('cannot open :{}'.format(self.inputfile))

    def directories(self):
        try:
            f = open(self.inputfile, 'r').read()
            for url in f.split("\n"):
                parse_object = urlparse(url)
                for directoryin in parse_object.path.split('/'):
                    if self.checkduplicate(directoryin) == 1:
                        try:
                            t = open(self.outputfile, 'a')
                            if '&' in directoryin:
                                if self.checkduplicate(directoryin.split('&')[0]) == 1:
                                    t.write('{}\n'.format(directoryin.split('&')[0]))
                                    t.close()
                                continue
                            if '=' in directoryin:
                                if self.checkduplicate(directoryin.split('=')[0]) == 1:
                                    t.write('{}\n'.format(directoryin.split('=')[0]))
                                    t.close()
                                continue
                            print('The Directory/file :{}'.format(directoryin))
                            t.write('{}\n'.format(directoryin))
                            t.close()
                        except OSError:
                            print('cannot open :{}'.format(self.outputfile))
        except OSError:
            print('cannot open :{}'.format(self.inputfile))


    def modeselect(self):
        if self.mode == 'u':
            self.urlextract()
        elif self.mode == 'a':
            self.argumentextract()
        elif self.mode == 'd':
            self.directories()


if __name__ == "__main__": # getting some parameters from the user
    parser = ArgumentParser(description='Fingerprints urls to domains/arguments/directories')
    parser.add_argument(
        '-i', '--input', default=True, dest='inputfile', required=True, help='Input file')
    parser.add_argument(
        '-o', '--output', default=True, dest='outputfile', required=True, help='Url Output file name')
    parser.add_argument(
        '-m', '--mode', default=True, dest='mode', required=True, help='u/a/d/all - url/arguments/directories/everything')
    args = parser.parse_args()
    a = fingerprint(args.inputfile, args.outputfile, args.mode)
    a.modeselect()
