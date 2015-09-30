__author__ = 'TJ. September 2015'


import random, time

def sequential_search(list,object):
    """This will perform a sequential list and will return more than 1 value"""

    start = time.time()
    count=0
    found=False

    while count<len(list) and not found:
        if list[count]==object:
            found=False
        else:
            count+=1
        end=time.time()
        timeaccounted=end-start
        return (found,timeaccounted)

def ordered_sequential_search(list,object):
    start=time.time()
    count=0
    found=False
    stop=False

    while count<len(list) and not found and not stop:
        if list[count]==object:
            found=True
        else:
            if list[count]>object:
                stop=True
    else:
        count+=1
    end=time.time()
    timeaccounted=end-start
    return (found,timeaccounted)

def binary_search_iteractive(list,object):
    start=time.time()
    first=0
    last=len(list)-1
    found=False

    while first <= last and not found:
        point=(first+last)//2
        if list[point]==object:
            found=True
        else:
            if object < list[point]:
                last=point-1
            else:
                first=point+1
    end=time.time()
    timeaccounted=end-start

    return (found,timeaccounted)


def binary_search_recursive(list,object):
    start=time.time()
    if len(list)==0:
        return False
    else:
        point=len(list)//2
        if list[point]==object:
            return True
        else:
            if object<list[point]:
                end=time.time()
                timeaccounted=end-start
                return (binary_search_recursive(list[:point],object),timeaccounted)

def main():

    seqtime500 = 0.0
    seqtime1000 = 0.0
    seqtime10000 = 0.0

    orseqtime500 = 0.0
    orseqtime1000 = 0.0
    orseqtime10000 = 0.0

    biit_time500 = 0.0
    biit_time1000 = 0.0
    biit_time10000 = 0.0

    bire_time500 = 0.0
    bire_time1000 = 0.0
    bire_time10000 = 0.0

    for i in xrange(100):
        lst500 = [int(100*random.random()) for i in xrange(500)]
        lst1000 = [int(100*random.random()) for i in xrange(1000)]
        lst10000 = [int(100*random.random()) for i in xrange(10000)]

        seq500 = sequential_search(lst500, -1)
        seqtime500 += seq500[1]
        seqavg500 = seqtime500 / 100

        seq1000 = sequential_search(lst1000, -1)
        seqtime1000 += seq1000[1]
        seqavg1000 = seqtime1000 / 100

        seq10000 = sequential_search(lst10000, -1)
        seqtime10000 += seq10000[1]
        seqavg10000 = seqtime10000 / 100

        lst500.sort()
        lst1000.sort()
        lst10000.sort()

        orseq500 = ordered_sequential_search(lst500, -1)
        orseqtime500 += orseq500[1]
        orseqavg500 = orseqtime500 / 100

        orseq1000 = ordered_sequential_search(lst1000, -1)
        orseqtime1000 += orseq1000[1]
        orseqavg1000 = orseqtime1000 / 100

        orseq10000 = ordered_sequential_search(lst10000, -1)
        orseqtime10000 += orseq10000[1]
        orseqavg10000 = orseqtime10000 / 100

        biit500 = binary_search_iteractive(lst500, -1)
        biit_time500 += biit500[1]
        biitavg500 = biit_time500 / 100

        biit1000 = binary_search_iteractive(lst1000, -1)
        biit_time1000 += biit1000[1]
        biitavg1000 = biit_time1000 / 100

        biit10000 = binary_search_iteractive(lst10000, -1)
        biit_time10000 += biit10000[1]
        biitavg10000 = biit_time10000 / 100

        bire500 = binary_search_recursive(lst500, -1)
        bire_time500 += bire500[1]
        bireavg500 = bire_time500 / 100

        bire1000 = binary_search_recursive(lst1000, -1)
        bire_time1000 += bire1000[1]
        bireavg1000 = bire_time1000 / 100

        bire10000 = binary_search_recursive(lst10000, -1)
        bire_time10000 += bire10000[1]
        bireavg10000 = bire_time10000 / 100

    print "Sequential Search took {:.7f}".format(seqavg500),"seconds to run, on average over 500 items"
    print "Sequential Search took {:.7f}".format(seqavg1000),"seconds to run, on average over 1,000 items"
    print "Sequential Search took {:.7f}".format(seqavg10000),"seconds to run, on average over 10,000 items"

    print "Ordered Sequential Search took {:.7f}".format(orseqavg500),"seconds to run, on average over 500 items"
    print "Ordered Sequential Search took {:.7f}".format(orseqavg1000),"seconds to run, on average over 1,000 items"
    print "Ordered Sequential Search took {:.7f}".format(orseqavg10000),"seconds to run, on average over 10,000 items"

    print "Binary Iterative Search took {:.7f}".format(biitavg500),"seconds to run, on average over 500 items"
    print "Binary Iterative Search took {:.7f}".format(biitavg1000),"seconds to run, on average over 1,000 items"
    print "Binary Iterative Search took {:.7f}".format(biitavg10000),"seconds to run, on average over 10,000 items"

    print "Binary Recursive Search took {:.7f}".format(bireavg500),"seconds to run, on average over 500 items"
    print "Binary Recursive Search took {:.7f}".format(bireavg1000),"seconds to run, on average over 1,000 items"
    print "Binary Recursive Search took {:.7f}".format(bireavg10000),"seconds to run, on average over 10,000 items"

if __name__ == "__main__":
    main()
