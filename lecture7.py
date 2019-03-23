import unittest


class DistanceTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.something = "Set up coment"
        print(cls.something)

    def testzero(self):
        self.assertEqual(5 + 5, 10)

    def testone(self):
        self.assertEqual(5 + 1, 5)


test10 = DistanceTest("testzero")
test20 = DistanceTest("testone")
suite1 = unittest.TestSuite([test10, test20])

from HtmlTestRunner import HTMLTestRunner

unittest.main(verbosity=2, testRunner=HTMLTestRunner(output=r"D:\Noise"))

# print(test10.run())
# print(test20.run())


# suite1 = unittest.TestSuite([test10])
# suite1.addTest(test20)
# result = unittest.TestResult()
# suite1.run(result)
# print(result)

# suite1 = unittest.TestLoader().loadTestsFromTestCase(DistanceTest)
# result1 = unittest.TestResult()
# print(result1)
