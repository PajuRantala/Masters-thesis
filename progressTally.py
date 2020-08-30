# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 14:04:21 2018

@author: rantala2
"""
import os


class ProgressTally():
    '''
    Updates the tally CSV based on the files in updateDir.
    Files have format subj_id,tag[,value]. One line per file.
    '''

    def __init__(self, fname):

        self.tally = {}
        self.updateDir = './updates/'
        try:

            if isinstance(fname, basestring):
                dbfile = open(fname)
            else:
                dbfile = fname

            header = dbfile.readline()

            if len(header) > 1:
                self.header = header.rstrip().split(',')
            else:
                self.header = ['subj_id']

            for line in dbfile:
                l = line.rstrip().split(',')
                self.tally[l[0]] = l[1:]
        except IOError as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)
        finally:
            dbfile.close()

    def updateTally(self, remove=False):
        for f in os.listdir(self.updateDir):
            with open(os.path.join(self.updateDir, f)) as newFile:
                parts = newFile.readline().rstrip().split(',')
                if parts[1] not in self.header:
                    self.__addHeader__(parts[1])

                if parts[0] in self.tally.keys():
                    self.__updateLine__(parts)
                else:
                    self.__createLine__(parts)
            if remove:
                os.remove(os.path.join(self.updateDir, f))

    def __updateLine__(self, parts):
        idx = self.header.index(parts[1]) - 1
        if len(parts) > 2:
            newItem = parts[2]
        else:
            newItem = '1'

        self.tally[parts[0]][idx] = newItem

    def __createLine__(self, parts):
        idx = self.header.index(parts[1]) - 1
        if len(parts) > 2:
            newItem = parts[2]
        else:
            newItem = '1'
        newLine = [0] * (len(self.header) - 1)
        newLine[idx] = newItem

        self.tally[parts[0]] = newLine

    def __addHeader__(self, headerNew):
        print 'Added ', headerNew
        self.header.append(headerNew)
        for key in self.tally.keys():
            self.tally[key].append('0')

    def save(self, fname):
        with open(fname, 'w') as f:

            h = ','.join(self.header)
            f.write(h + '\n')

            for key in sorted(self.tally):
                f.write(key + ',')
                f.write(','.join(self.tally[key]) + '\n')

if __name__ == '__main__':
    pt = ProgressTally('progress.csv')
    pt.updateTally()
    pt.save('progress.csv')
