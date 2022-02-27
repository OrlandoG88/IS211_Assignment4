
# other imports go here
import time
import random


def get_me_random_list(n):
    """Generate list of n elements in random order

    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


def sequential_search(a_list, item):
    pos = 0

    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1
    return found


def ordered_sequential_search(a_list, item):
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos+1

    return found


def binary_search_iterative(a_list, item):
    first = 0

    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
    else:
            first = midpoint + 1
    return found



def binary_search_recursive(a_list, item):
    if len(a_list) == 0:
        return False

    else:
        midpoint = len(a_list) // 2
    if a_list[midpoint] == item:
        return True
    else:
        if item < a_list[midpoint]:
            return binary_search_recursive(a_list[:midpoint], item)
        else:
            return binary_search_recursive(a_list[midpoint + 1:], item)



if __name__ == "__main__":
    """Main entry point"""
    list_sizes = [500, 1000, 5000]
    #the_size = list_sizes



    total_time = 0
    for i in range(100):

        myList500 = get_me_random_list(500)
        sorted_list = sorted(myList500)

        starttime = time.time()
        ordered_sequential_search(sorted_list, -1)
        time_spent = time.time() - starttime
        total_time += time_spent

    avg_time = total_time/100
    print(f"Python ordered_sequential_search took {avg_time:10.7f} seconds to run, on average for a list of {500} random elements")




    total_time = 0
    for i in range(100):
        myList1000 = get_me_random_list(1000)
        sorted_list = sorted(myList1000)

        starttime = time.time()
        ordered_sequential_search(sorted_list, -1)
        time_spent = time.time() - starttime
        total_time += time_spent

    avg_time = total_time / 100
    print(f"Python ordered_sequential_search took {avg_time:10.7f} seconds to run, on average for a list of {1000} random elements")

    total_time = 0
    for i in range(100):
        myList5000 = get_me_random_list(5000)
        sorted_list = sorted(myList5000)

        starttime = time.time()
        ordered_sequential_search(sorted_list, -1)
        time_spent = time.time() - starttime
        total_time += time_spent

    avg_time = total_time / 100
    print(f"Python ordered_sequential_search took {avg_time:10.7f} seconds to run, on average for a list of {5000} random elements")

    total_time = 0
    for i in range(100):
        myList500 = get_me_random_list(500)
        #sorted_list = myList500.sort()

        starttime = time.time()
        sequential_search(myList500, -1)
        time_spent = time.time() - starttime
        total_time += time_spent

    avg_time = total_time / 100
    print(f"Python sequential_search took {avg_time:10.7f} seconds to run, on average for a list of {500} random elements")

    total_time = 0
    for i in range(100):
        myList1000 = get_me_random_list(1000)
        # sorted_list = myList500.sort()

        starttime = time.time()
        sequential_search(myList1000, -1)
        time_spent = time.time() - starttime
        total_time += time_spent

    avg_time = total_time / 100
    print(f"Python sequential_search took {avg_time:10.7f} seconds to run, on average for a list of {1000} random elements")

    total_time = 0
    for i in range(100):
        myList5000 = get_me_random_list(5000)
        # sorted_list = myList500.sort()

        starttime = time.time()
        sequential_search(myList5000, -1)
        time_spent = time.time() - starttime
        total_time += time_spent

    avg_time = total_time / 100
    print(f"Python sequential_search took {avg_time:10.7f} seconds to run, on average for a list of {5000} random elements")

    total_time = 0
    for i in range(100):
        myList500 = get_me_random_list(500)
        sorted_list = sorted(myList500)

        starttime = time.time()
        binary_search_iterative(sorted_list, -1)
        time_spent = time.time() - starttime
        total_time += time_spent

    avg_time = total_time / 100
    print(f"Python binary_search_iterative took {avg_time:10.7f} seconds to run, on average for a list of {500} random elements")

    total_time = 0
    for i in range(100):
        myList1000 = get_me_random_list(1000)
        sorted_list = sorted(myList1000)

        starttime = time.time()
        binary_search_iterative(sorted_list, -1)
        time_spent = time.time() - starttime
        total_time += time_spent

    avg_time = total_time / 100
    print(f"Python binary_search_iterative took {avg_time:10.7f} seconds to run, on average for a list of {1000} random elements")

    total_time = 0
    for i in range(100):
        myList5000 = get_me_random_list(5000)
        sorted_list = sorted(myList5000)

        starttime = time.time()
        binary_search_iterative(sorted_list, -1)
        time_spent = time.time() - starttime
        total_time += time_spent

    avg_time = total_time / 100
    print(f"Python binary_search_iterative took {avg_time:10.7f} seconds to run, on average for a list of {5000} random elements")

    total_time = 0
    for i in range(100):
        myList500 = get_me_random_list(500)
        sorted_list = sorted(myList500)

        starttime = time.time()
        binary_search_recursive(sorted_list, -1)
        time_spent = time.time() - starttime
        total_time += time_spent

    avg_time = total_time / 100
    print(f"Python binary_search_recursive took {avg_time:10.7f} seconds to run, on average for a list of {500} random elements")

    total_time = 0
    for i in range(100):
        myList1000 = get_me_random_list(1000)
        sorted_list = sorted(myList1000)

        starttime = time.time()
        binary_search_recursive(sorted_list, -1)
        time_spent = time.time() - starttime
        total_time += time_spent

    avg_time = total_time / 100
    print(f"Python binary_search_recursive took {avg_time:10.7f} seconds to run, on average for a list of {1000} random element")

    total_time = 0
    for i in range(100):
        myList5000 = get_me_random_list(5000)
        sorted_list = sorted(myList5000)

        starttime = time.time()
        binary_search_recursive(sorted_list, -1)
        time_spent = time.time() - starttime
        total_time += time_spent

    avg_time = total_time / 100
    print(f"Python binary_search_recursive took {avg_time:10.7f} seconds to run, on average for a list of {5000} random element")