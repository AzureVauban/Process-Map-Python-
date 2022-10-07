"""unit testing code, test out Mode A and Mode B for the script
   readd to gitignore when pulling and merging modifications into master
"""
import random
import unittest

from numpy import roots

from main import Node, findlocalendpoints, reversearithmetic,tentative_formatoutput


class Issue12(unittest.TestCase):
    """test new formatting and endpoint search methods from main.py module

    Args:
        unittest (class): Unit testing framework for python
    """
    tritaniumbar : Node = Node('Tritanium Bar')
    lead : Node = Node('Lead',tritaniumbar)
    pixels : Node = Node('Pixels',lead,0,1,200)
    irradiumbar : Node = Node('Irradium Bar',tritaniumbar)
    irradiumore : Node = Node('Irradium Ore',irradiumbar,0,1,2)
    pixels2 : Node = Node('Pixels',irradiumore,0,1,600)
    triangliumpyramid : Node = Node('Trianglium Pyramid',tritaniumbar)
    triangliumore : Node = Node('Trianglium Ore',triangliumpyramid,0,1,2)
    pixels3 : Node = Node('Pixels',triangliumore,0,1,810)
    prisilitestar : Node = Node('Prisilite Star',tritaniumbar)
    prismshard : Node = Node('Prism Shard',prisilitestar,0,1,2)
    pixels4 : Node = Node('Pixels',prismshard,0,1,1838) #? buy from geologist NPC ingame
    desiredamount : int = random.randint(1,100)
    reversearithmetic(tritaniumbar,desiredamount)
    roots : dict = findlocalendpoints(tritaniumbar,{})
    def test_endpointsdict(self):
        """test to see if the length of the endpoints dictionary
        is 4 elements
        """
        self.assertEqual(len(self.roots),4)

    def test_endpoints(self):
        """test to see if the item name of each endpoint is Pixels
        """
        iscalledpixels: bool = True
        for instance in self.roots.items():
            if not isinstance(instance[1], Node):
                raise TypeError('endpoint is not an instance of', Node)
            else:
                iscalledpixels = instance[1].ingredient == 'Pixels'
                if not iscalledpixels:
                    break
        self.assertTrue(iscalledpixels)
    def test_temptest(self):
        """tentative description
        """
        tentative_formatoutputs(self.roots)
        print('hello world from VS Code')
        self.assertEqual(1,1*1)