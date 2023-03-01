from interface import *
from apriori import *
from fpGrowth import *
import csv
import tracemalloc
import time


def runApr(dps,a,b):
    with open('AprOutput.txt', 'a') as f:
        data = interface(dps)
        data = apr(data,a,b,)
        for line in data:
            f.write("\nRule: for min support = ")
            f.write(str(a))
            f.write(" / min confidence = ")
            f.write(str(b))
            f.write("\n")
            f.write(str(line))


def runFP(dps,c,d):
    with open('fpOutput.txt', 'a') as f:
        data = interface(dps)
        data = fpGrowth(data,c,d)
        for line in data:
            f.write("\nRule for occurrences: ")
            f.write(str(c))
            f.write(" / minimal probability = ")
            f.write(str(d))
            f.write("\n")
            f.write(str(line))


def main2(dps,a,b,c,d):
    with open('output.txt', 'a') as f:
        data = interface(dps)
        f.write("\n------Starting Fp Growth \n")
        #data, patterns that occur x times, certain minimum probability
        f.write("Rules for Occurrences = "), f.write(str(a)), f.write(" / Minimal Probability = "),
        f.write(str(b)), f.write("\n"), f.write(str(fpGrowth(data, a, b))), f.write("\n")
        f.write("\n------Starting Apriori----------\n")
        #data, support, confidence
        f.write("\nRules for Min_Support= "), f.write(str(c)), f.write(" / Min_Confidence = "),
        f.write(str(d)), f.write("\n"), f.write(str(apr(data, c, d))), f.write("\n")


def runFP2(a,b,c):
    with open('fp2Output.txt', 'a') as f:
        data = fpGrowth(a,b,c)
        for line in data:
            f.write("\nRule for occurrences: ")
            f.write(str(b))
            f.write(" / minimal probability = ")
            f.write(str(c))
            f.write("\n")
            f.write(str(line))


def runapr2(a,b,c):
    with open('apr2Output.txt', 'a') as f:
        data = apriori(a,b,c)
        for line in data:
            f.write("\nRule: for min support = ")
            f.write(str(b))
            f.write(" / min confidence = ")
            f.write(str(c))
            f.write("\n")
            f.write(str(line))


def numMF():
    with open('adult.data', 'r') as f:
        data=interface((0,9))
        count = 0
        total = 32561
        for line in data:
            for entry in line:
                if 'Female' in entry:
                    count = count + 1
        print("female count: ", count)
        count2 = total-count
        print('\nmale count: ', count2)


def Test1():
    tic=time.perf_counter()
    runApr([3, 7, 14], 0.2, 1)
    runApr([3, 7, 14],0.4, 0.8)
    runApr([3, 7, 14],0.3, 0.8)
    runApr([3, 7, 14],0.3, 0.8)
    runApr([3, 7, 14], 0.5, 1)
    runApr([3, 7, 14], 0.6, 0.8)
    runApr([3, 7, 14], 0.7, 0.8)
    runApr([3, 7, 14], 0.8, 1)
    runApr([3, 7, 14], 0.7, 0.8)
    runApr([3, 7, 14], 0.6, 0.8)
    runApr([3, 7, 14], 0.5, 0.8)
    runApr([3, 7, 14], 0.4, 0.8)
    runApr([3, 7, 14], 0.3, 0.8)
    runApr([3, 7, 14], 0.2, 0.8)
    runApr([3, 7, 14], 0.8, 0.6)
    runApr([3, 7, 14], 0.7, 0.6)
    runApr([3, 7, 14], 0.6, 0.6)
    runApr([3, 7, 14], 0.5, 0.6)
    runApr([3, 7, 14], 0.4, 0.6)
    runApr([3, 7, 14],0.3, 0.6)
    runApr([0,3,7,9,14],0.2, 0.8)
    runApr([0,3,7,9,14], 0.4, 0.8)
    runApr([0,3,7,9,14],0.6, 0.8)
    runApr([0,3,7,9,14], 0.8, 0.8)
    runApr([0,3,7,9,14], 0.2, 0.8)
    runApr([0,3,7,9,14],0.4,  0.8)
    runApr([0,3,7,9,14],0.6, 0.8)
    runApr([0,3,7,9,14],0.7, 0.8)
    runApr([0,3,7,9,14],0.8, 0.8)
    runApr([0,3,7,9,14],0.2, 0.6)
    runApr([0,3,7,9,14],0.3, 0.6)
    runApr([0,3,7,9,14],0.4, 0.6)
    runApr([0,3,7,9,14],0.5, 0.6)
    runApr([0,3,7,9,14],0.6, 0.6)
    runApr([0,3,7,9,14], 0.7, 0.6)
    runApr([0,6,7,14], 0.2, 0.8)
    runApr([0,6,7,14], 0.4, 0.8)
    runApr([0,6,7,14], 0.6, 0.8)
    runApr([0,6,7,14], 0.8, 0.8)
    runApr([0,6,7,14], 0.2, 0.8)
    runApr([0,6,7,14], 0.4, 0.8)
    runApr([0,6,7,14], 0.6, 0.8)
    runApr([0,6,7,14], 0.8, 0.8)
    runApr([0,6,7,14], 0.4, 0.6)
    runApr([0,6,7,14], 0.6, 0.6)
    runApr([0,6,7,14], 0.8, 0.6)
    runApr([0,6,7,14], 0.2, 0.4)
    runApr([0,6,7,14],0.4, 0.4)
    runApr([0,6,7,14],0.4, 0.4)
    toc=time.perf_counter()
    print("Time to Run Apriori = ", {toc-tic}, " seconds")


def Test2():
    tic = time.perf_counter()
    runFP([3,7,14],250, 0.8)
    runFP([3, 7, 14], 350, 0.8)
    runFP([3, 7, 14], 450, 0.8)
    runFP([3, 7, 14], 650, 0.8)
    runFP([3, 7, 14], 850, 0.8)
    runFP([3, 7, 14], 1000, 0.8)
    runFP([3, 7, 14], 2000, 0.8)
    runFP([3, 7, 14], 5000, 0.8)
    runFP([3, 7, 14], 250, 0.9)
    runFP([3, 7, 14], 350, 0.9)
    runFP([3, 7, 14], 450, 0.9)
    runFP([3, 7, 14], 650, 0.9)
    runFP([3, 7, 14], 850, 0.9)
    runFP([3, 7, 14], 1000, 0.9)
    runFP([3, 7, 14], 2000, 0.9)
    runFP([3, 7, 14], 5000, 0.9)
    runFP([0,3,7,9,14], 250, 0.8)
    runFP([0,3,7,9,14], 350, 0.8)
    runFP([0,3,7,9,14], 450, 0.8)
    runFP([0,3,7,9,14], 650, 0.8)
    runFP([0,3,7,9,14], 850, 0.8)
    runFP([0,3,7,9,14], 1000, 0.8)
    runFP([0,3,7,9,14], 20000, 0.8)
    runFP([0,3,7,9,14], 5000, 0.8)
    runFP([0,3,7,9,14], 250, 0.9)
    runFP([0,3,7,9,14], 450, 0.9)
    runFP([0,3,7,9,14], 650, 0.9)
    runFP([0,3,7,9,14], 850, 0.9)
    runFP([0,3,7,9,14], 950, 0.9)
    runFP([0,3,7,9,14], 1000, 0.9)
    runFP([0,3,7,9,14], 2000, 0.9)
    runFP([0,3,7,9,14], 5000, 0.9)
    runFP([0,6,7,14], 250, 0.8)
    runFP([0,6,7,14], 450, 0.8)
    runFP([0,6,7,14], 650, 0.8)
    runFP([0,6,7,14], 750, 0.8)
    runFP([0,6,7,14], 850, 0.8)
    runFP([0,6,7,14], 950, 0.8)
    runFP([0,6,7,14], 1000, 0.8)
    runFP([0,6,7,14], 2000, 0.8)
    runFP([0,6,7,14],5000, 0.8)
    runFP([0,6,7,14], 250, 0.9)
    runFP([0,6,7,14], 450, 0.9)
    runFP([0,6,7,14], 650, 0.9)
    runFP([0,6,7,14], 850, 0.9)
    runFP([0,6,7,14], 9850, 0.9)
    runFP([0,6,7,14], 1050, 0.9)
    runFP([0,6,7,14],2000, 0.9)
    runFP([0,6,7,14],5000, 0.9)
    toc = time.perf_counter()
    print("Time to Run Fp Growth = ", {toc-tic}, " seconds")


def Test3():
    tic = time.perf_counter()
    data = interface((1,3,7,8,9,11))
    runFP2(data, 250, 0.8)
    runFP2(data, 350, 0.8)
    runFP2(data, 450, 0.8)
    runFP2(data, 550, 0.8)
    runFP2(data, 650, 0.8)
    runFP2(data, 750, 0.8)
    runFP2(data, 850, 0.8)
    runFP2(data, 950, 0.8)
    runFP2(data, 250, 0.9)
    runFP2(data, 350, 0.9)
    runFP2(data, 450, 0.9)
    runFP2(data, 550, 0.9)
    runFP2(data, 650, 0.9)
    runFP2(data, 750, 0.9)
    runFP2(data, 950, 0.9)
    runFP2(data, 950, 0.95)
    runFP2(data, 250, .95)
    runFP2(data, 350, .95)
    runFP2(data, 450, 0.95)
    runFP2(data, 550, 0.95)
    runFP2(data, 650, 0.95)
    runFP2(data, 750, 0.95)
    toc = time.perf_counter()
    print("Time to Run Fp Growth = ", {toc - tic}, " seconds")


def Test4():
    tic = time.perf_counter()
    data = interface((1,3,7,8,9,11))
    runapr2(data, 0.2, 0.8)
    runapr2(data, 0.3, 0.8)
    runapr2(data, 0.4, 0.8)
    runapr2(data, 0.5, 0.8)
    runapr2(data, 0.6, 0.8)
    runapr2(data, 0.7, 0.8)
    runapr2(data, 0.8, 0.8)
    runapr2(data, 0.2, 0.6)
    runapr2(data, 0.3, 0.6)
    runapr2(data, 0.4, 0.6)
    runapr2(data, 0.5, 0.6)
    runapr2(data, 0.6, 0.6)
    runapr2(data, 0.7, 0.6)
    runapr2(data, 0.8, 0.6)
    runapr2(data, 0.2, 0.4)
    runapr2(data, 0.3, 0.4)
    runapr2(data, 0.4, 0.4)
    runapr2(data, 0.5, 0.4)
    runapr2(data, 0.6, 0.4)
    runapr2(data, 0.7, 0.4)
    runapr2(data, 0.8, 0.4)
    runapr2(data, 0.9, 0.4)
    toc = time.perf_counter()
    print("Time to Run Apriori = ", {toc - tic}, " seconds")


def main():
    tracemalloc.start()
    #Test1()
    Test3()
    snap = tracemalloc.take_snapshot()
    top_stats = snap.statistics('lineno')
    print("[Top 10 Memory Usages: ]")
    for stat in top_stats[:10]:
        print(stat)
    tracemalloc.stop()
    tracemalloc.start()
    #Test2()
    Test4()
    snap2 = tracemalloc.take_snapshot()
    top_stats2 = snap2.statistics('lineno')
    print("[Top 10 Memory Usages: ]")
    for stats in top_stats2[:10]:
        print(stats)
    tracemalloc.stop()


#main()
numMF()