
# Yihan Xiao 2018/09/27
# This is the file for unit test for Bionic Ant
# The main function is in this module. Simply run it to see the result of all test cases.
# The first test case is required in document. The rest are arbitrary cases to prove the 
# functionality of the program, including basic navigation, bouandary limit check and invalid command.


import unittest
from BioAnt import BioAnt
from Stamp import Stamp

class BioAntUnitTest(unittest.TestCase):
    '''Tests for BioAnt within Stamp'''

    def test_case1(self):
        '''Case1: basic test case with two cases from doc'''
        input_lines =  '''  
                        5 5
                        1 2 N
                        LMLMLMLMM  
                        3 3 E
                        MMRMMRMRRM
                   '''
        stamp_env = Stamp(input_lines)
        output = stamp_env.AntsNavigate()
        self.assertEqual(output, '1 3 N 5 1 E')

    def test_case2(self):
        '''Case2: simple case with one ant'''

        input_lines =  '''  
                        4 4
                        1 1 E
                        LRLRLRMM
                   '''
        stamp_env = Stamp(input_lines)
        output = stamp_env.AntsNavigate()
        self.assertEqual(output, '3 1 E')

    def test_case3(self):
        '''Case3: two ants keep rotating without moving'''

        input_lines =  '''  
                        8 8
                        1 1 E
                        LLLLRRRRLLLL
                        4 4 W
                        RRRRLLLLRRRR
                   '''
        stamp_env = Stamp(input_lines)
        output = stamp_env.AntsNavigate()
        self.assertEqual(output, '1 1 E 4 4 W')

    def test_case4(self):
        '''Case4: two ants navigate'''

        input_lines =  '''  
                        7 7
                        0 3 N
                        RMMRMMRMM
                        3 0 S
                        RRMMMLMMLM
                   '''
        stamp_env = Stamp(input_lines)
        output = stamp_env.AntsNavigate()
        self.assertEqual(output, '0 1 W 1 2 S')

    def test_case5(self):
        '''Case5: three ants navigate'''

        input_lines =  '''  
                        10 10
                        0 0 N
                        MRMLMRMLMRMLMRM
                        8 8 W
                        MMMMMMMMRMM
                        4 4 E
                        MMRMRM
                   '''
        stamp_env = Stamp(input_lines)
        output = stamp_env.AntsNavigate()
        self.assertEqual(output, '4 4 E 0 10 N 5 3 W')

    def test_case6(self):
        '''Case6: ant should be limited within the range of stamp'''

        input_lines =  '''  
                        5 5
                        2 2 N
                        MMMMR
                   '''
        stamp_env = Stamp(input_lines)
        output = stamp_env.AntsNavigate()
        self.assertEqual(output, '2 5 E')

    def test_case7(self):
        '''Case7: invalid command will be discarded'''

        input_lines =  '''  
                        5 5
                        1 1 N
                        MMKRR
                   '''
        stamp_env = Stamp(input_lines)
        output = stamp_env.AntsNavigate()
        self.assertEqual(output, '1 3 S')

    def test_case8(self):
        '''Case8: Mixed cases with 4 ants'''

        input_lines =  '''  
                        6 6
                        0 0 N
                        MMMRMMML
                        1 0 E
                        LMMM
                        5 5 E
                        MMRMM
                        0 2 W
                        RRMMLMMR     
                   '''
        stamp_env = Stamp(input_lines)
        output = stamp_env.AntsNavigate()
        self.assertEqual(output, '3 3 N 1 3 N 6 3 S 2 4 E')

if __name__ == '__main__':
    try:
        unittest.main()
    except:
        print()


   
