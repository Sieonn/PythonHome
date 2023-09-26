import untitest
import myinfomation

class Mytest(untitest.TestCase):
    def test_sum(self):
        self.assertEqual(myfunction.sum(2, 5),7)
        
        
    def test_multiple(self):
        self.assertEqual()