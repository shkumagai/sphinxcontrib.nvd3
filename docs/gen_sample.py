#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import os
import random
import time


cwd = os.path.abspath(os.path.dirname(__file__))


def gen_cumulativeline_sample():
    start_time = int(time.mktime(datetime.datetime(2012, 6, 1).timetuple()) * 1000)
    nb_element = 50

    xdata = list(range(nb_element))
    xdata = [start_time + x * 1000000000 for x in xdata]
    ydata1 = [i + random.randint(1, 10) for i in range(nb_element)]
    ydata2 = [x * 2 for x in ydata1]

    with open(os.path.join(cwd, 'cumulativeline-sample.csv'), 'w') as fp:
        fp.write("xdata,ydata1,ydata2\n")

        for n in range(len(xdata)):
            line = ",".join([str(xdata[n]),
                             str(ydata1[n]),
                             str(ydata2[n])])
            fp.write("%s\n" % line)


def gen_discretebar_sample():
    xdata = ["A", "B", "C", "D", "E", "F", "G"]
    ydata = [3, 12, -10, 5, 25, -7, 2]

    with open(os.path.join(cwd, 'discretebar-sample.csv'), 'w') as fp:
        fp.write("xdata,ydata\n")

        for n in range(len(xdata)):
            line = ",".join([str(xdata[n]),
                             str(ydata[n])])
            fp.write("%s\n" % line)


def gen_line_sample():
    xdata = list(range(0, 24))
    ydata1 = [i + random.randint(1, 10) for i in range(0, 24)]
    ydata2 = [i * random.randint(1, 10) for i in range(0, 24)]

    with open(os.path.join(cwd, 'line-sample.csv'), 'w') as fp:
        fp.write("xdata,ydata1,ydata2\n")

        for n in range(len(xdata)):
            line = ",".join([str(xdata[n]),
                             str(ydata1[n]),
                             str(ydata2[n])])
            fp.write("%s\n" % line)


def gen_multivar_sample():
    nb_element = 10

    xdata = list(range(nb_element))
    ydata1 = [random.randint(1, 10) for i in range(nb_element)]
    ydata2 = [x * 2 for x in ydata1]

    with open(os.path.join(cwd, 'multibar-sample.csv'), 'w') as fp:
        fp.write("xdata,ydata1,ydata2\n")

        for n in range(len(xdata)):
            line = ",".join([str(xdata[n]),
                             str(ydata1[n]),
                             str(ydata2[n])])
            fp.write("%s\n" % line)


def gen_pie_sample():
    xdata = ["Orange", "Banana", "pear", "Kiwi", "Apple", "Strawberry", "Pineapple"]
    ydata = [3, 4, 0, 1, 5, 7, 3]

    with open(os.path.join(cwd, 'pie-sample.csv'), 'w') as fp:
        fp.write("xdata,ydata\n")

        for n in range(len(xdata)):
            line = ",".join([str(xdata[n]),
                             str(ydata[n])])
            fp.write("%s\n" % line)


def gen_scatter_sample():
    nb_element = 50
    xdata = [i + random.randint(1, 10) for i in range(nb_element)]
    ydata1 = [i * random.randint(1, 10) for i in range(nb_element)]
    ydata2 = [x * 2 for x in ydata1]
    ydata3 = [x * 5 for x in ydata1]

    with open(os.path.join(cwd, 'scatter-sample.csv'), 'w') as fp:
        fp.write("xdata,ydata1,ydata2,ydata3\n")

        for n in range(len(xdata)):
            line = ','.join([str(xdata[n]),
                             str(ydata1[n]),
                             str(ydata2[n]),
                             str(ydata3[n])])
            fp.write("%s\n" % line)


def gen_stackedarea_sample():
    xdata = [100, 101, 102, 103, 104, 105, 106]
    ydata1 = [6, 11, 12, 7, 11, 10, 11]
    ydata2 = [8, 20, 16, 12, 20, 28, 28]

    with open(os.path.join(cwd, 'stackedarea-sample.csv'), 'w') as fp:
        fp.write("xdata,ydata1,ydata2\n")

        for n in range(len(xdata)):
            line = ','.join([str(xdata[n]),
                             str(ydata1[n]),
                             str(ydata2[n])])
            fp.write("%s\n" % line)


def main():
    gen_cumulativeline_sample()
    gen_line_sample()
    gen_scatter_sample()


if __name__ == "__main__":
    main()
