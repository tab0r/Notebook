def remove_smallest(numbers):
    #raise NotImplementedError("TODO: remove_smallest")
    lowest = min(numbers)
    numbers.remove(lowest)
    return numbers

Test.describe("remove_smallest")

Test.it("works for the examples")
Test.assert_equals(remove_smallest([1, 2, 3, 4, 5]), [2, 3, 4, 5], "Wrong result for [1, 2, 3, 4, 5]")
Test.assert_equals(remove_smallest([5, 3, 2, 1, 4]), [5, 3, 2, 4], "Wrong result for [5, 3, 2, 1, 4]")
Test.assert_equals(remove_smallest([1, 2, 3, 1, 1]), [2, 3, 1, 1], "Wrong result for [1, 2, 3, 1, 1]")
Test.assert_equals(remove_smallest([]), [], "Wrong result for []")

from numpy.random import randint

def randlist():
    return list(randint(400, size=randint(1, 10)))


Test.it("returns [] if list has only one element")
for i in xrange(10):
    x = randint(1, 400)
    Test.assert_equals(remove_smallest([x]), [], "Wrong result for [{}]".format(x))

Test.it("returns a list that misses only one element")
for i in xrange(10):
    arr = randlist()
    Test.assert_equals(len(remove_smallest(arr[:])), len(arr) - 1, "Wrong sized result for {}".format(arr))
