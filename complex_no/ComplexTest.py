import unittest
import Complex_No

class ComplexTest(unittest.TestCase):
    def test_createComplexNo(self):
        myComplexNo = Complex_No.Complex_No(2,1)
        self.assertEqual(myComplexNo.getReal(),2)
        self.assertEqual(myComplexNo.getImaginary(),1)

    def test_adding_of_two_complex_no(self):
        firstNo = Complex_No.Complex_No(1,2)
        secondNo = Complex_No.Complex_No(2,2)
        result = firstNo.add(secondNo)
        self.assertEqual(result.getReal(),3)
        self.assertEqual(result.getImaginary(),4)

suite = unittest.TestLoader().loadTestsFromTestCase(ComplexTest)
unittest.TextTestRunner(verbosity=2).run(suite)
