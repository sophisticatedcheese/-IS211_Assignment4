__author__ = 'TJ September 2015'


import time, random
"""some functions were copied from the text. Others were from an example shown to me at a different college.
My biggest issue was the gap_insertion_sort function. I couldnt understand why I kept getting an error. Spent
two days trying to figure it out but couldnt. Assignment is late."""
def insertion_sort(a_list):
    start=time.time()
    for index in range(1,len(a_list)):
        current_value=a_list[index]
        position=index

        while position>0 and a_list[position-1]>current_value:
            a_list[position]=a_list[position-1]
            position-=1
            a_list[position]=current_value
    end=time.time()
    timeaccounted=end-start
    return (timeaccounted,a_list)

def shell_sort(a_list):
    start=time.time()
    list_count=len(a_list)//2
    while list_count>0:
        for start_position in range(list_count):
            gap_insertion_sort(a_list,start_position,list_count)
            list_count=list_count // 2
    end=time.time()
    timeaccounted=end-start
    return (timeaccounted,a_list)

def gap_insertion_sort(a_list, start, gap):

    for t in range(start+gap,len(a_list),gap):
        current_value=a_list[t]
        position=t

        while position>= gap and a_list[position-gap]> current_value:
            a_list[position]=a_list[position-gap]
            position=position-gap
            a_list[position]=current_value

def python_sort(a_list):
    start=time.time()
    a_list=a_list.sort()
    end=time.time()
    timeaccounted=end-start
    return (timeaccounted,a_list)


def rand_list(length):
    randlist = []
    for item in range(length):
        randlist.append(random.randint(1,length))
    return randlist


def main():

    tests = [500,1000,10000]
    for test in tests:
        counter = 100
        results = [0,0,0]
        while counter > 0:
            randlist = rand_list(test)
            results[0] += insertion_sort(randlist)[0]
            results[1] += shell_sort(randlist)[0]
            results[2] += python_sort(randlist)[0]
            counter -= 1
        print "For list of {}: ".format(test)
        print "Insertion Sort took %10.7f seconds to run, on average" % \
              (results[0] / 100)
        print "Shell Sort " + \
                "took %10.7f seconds to run, on average" % \
              (results[1] / 100)
        print "Python Sort " + \
                "took %10.7f seconds to run, on average" % \
              (results[2] / 100)

if __name__ == "__main__":
    main()




