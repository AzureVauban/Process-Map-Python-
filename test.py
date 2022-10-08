"""unit testing code, test out Mode A and Mode B for the script
   re-add to gitignore when pulling and merging modifications into master
"""
import random
import unittest

from main import (Node, findlocalendpoints, reversearithmetic,
                  tentative_formatoutput)


class Issue12_single_unique_endpoint(unittest.TestCase): #pylint:disable=C0103
    """test new formatting and endpoint search methods from main.py module wih only one endpoint

    Args:
        unittest (class): Unit testing framework for python
    """
    #? Tritanium Bar Mock Tree: https://frackinuniverse.miraheze.org/wiki/Tritanium_Bar
    desiredamount       : int = random.randint(1, 100)
    # it should take 6696 pixels to make one tritanium bar
    tritaniumbar        : Node = Node('Tritanium Bar')
    lead                : Node = Node('Lead', tritaniumbar)
    pixels              : Node = Node('Pixels', lead, 0, 1, 200)
    irradiumbar         : Node = Node('Irradium Bar', tritaniumbar)
    irradiumore         : Node = Node('Irradium Ore', irradiumbar, 0, 1, 2)
    pixels2             : Node = Node('Pixels', irradiumore, 0, 1, 600)
    triangliumpyramid   : Node = Node('Trianglium Pyramid', tritaniumbar)
    triangliumore       : Node = Node('Trianglium Ore', triangliumpyramid, 0, 1, 2)
    pixels3             : Node = Node('Pixels', triangliumore, 0, 1, 810)
    prisilitestar       : Node = Node('Prisilite Star', tritaniumbar)
    prismshard          : Node = Node('Prism Shard', prisilitestar, 0, 1, 2)
    # buy prism shards from geologist NPC ingame
    pixels4             : Node = Node('Pixels', prismshard, 0, 1, 1838)
    reversearithmetic(tritaniumbar, desiredamount)
    roots: dict = findlocalendpoints(tritaniumbar, {})

    def test_endpointsdict(self):
        """test to see if the length of the endpoints dictionary
        is 4 elements
        """
        self.assertEqual(len(self.roots), 4)

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
        """test to see if the total sum of the endpoint node's % compostion correctly
        rounds towards 1 (100%)
        """
        tentative_formatoutput(self.roots)
        #! temp : list = list(tentative_formatoutput(self.roots).items()) save this for later, creates a list of the the instancekey and the node tuple
        totalofpixels: int = 0
        endpointnodes: dict = tentative_formatoutput(self.roots)
        floatpercents: dict = {}
        #! totalpercent: float = 0.00 only used for testing, remove later
        # find total amount of an item
        for nodeinstance in endpointnodes.items():
            totalofpixels += nodeinstance[1].amountonhand
        # find the % composition of the total
        for nodeinstance in endpointnodes.items():
            if isinstance(nodeinstance[1], Node):
                floatpercents.update(
                    {nodeinstance[1].instancekey: nodeinstance[1].amountonhand/totalofpixels})
            else:
                raise TypeError('not an instance of', Node)
        # check to see if the total of the % rounds to 1.00
        #! for floatnum in floatpercents.items():
        #!     totalpercent += floatnum[1]
        # print % into debug console
        print('total # of pixels',totalofpixels,end='x\n')
        for floatnum in floatpercents.items():
            print(round(floatnum[1]*100,2),'%')
        # ? use debug console to see output
        # desired output Pixels : 147312x (2.99 % used in Lead, 17.92 % used in Irradium Ore, 24.19 % used in Trianglium Ore, 54.9 % used in Prism Shard)
        self.assertEqual(len(endpointnodes), 1)
class Issue12_multiple_unique_endpoint(unittest.TestCase): #pylint:disable=C0103
    """test new formatting and endpoint search methods from main.py module wih only one endpoint
    """
    pass
    