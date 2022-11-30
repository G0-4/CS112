# Based on testing harness dated 2017-06-02.

# STUDENTS: TO USE:
# 
# The following command will test all test cases on your file:
# 
#   python3 <thisfile.py> <your_one_file.py>
# 
# 
# You can also limit the tester to only the functions you want tested.
# Just add as many functions as you want tested on to the command line at the end.
# Example: to only run tests associated with func1 and func2, run this command:
# 
#   python3 <thisfile.py> <your_one_file.py> func1 func2
# 
# You really don't need to read the file any further, except that when
# a specific test fails, you'll get a line number - and it's certainly
# worth looking at those areas for details on what's being checked. This would
# all be the indented block of code starting with "class AllTests".


# INSTRUCTOR: TO PREPARE:
#  - add test cases to class AllTests. The test case functions' names must
# be precise - to test a function named foobar, the test must be named "test_foobar_#"
# where # may be any digits at the end, such as "test_foobar_13".
# - any extra-credit tests must be named "test_extra_credit_foobar_#"
# 
# - name all required definitions in REQUIRED_DEFNS, and all extra credit functions
#   in EXTRA_CREDIT_DEFNS. Do not include any unofficial helper functions. If you want
#   to make helper definitions to use while testing, those can also be added there for
#   clarity.
# 
# - to run on either a single file or all .py files in a folder (recursively):
#   python3 <thisfile.py> <your_one_file.py>
#   python3 <thisfile.py> <dir_of_files>
#   python3 <thisfile.py> .                    # current directory
# 
# A work in progress by Mark Snyder, Oct. 2015.
#  Edited by Yutao Zhong, Spring 2016.
#  Edited by Raven Russell, Spring 2017.
#  Edited by Mark Snyder, June 2017.


import unittest
import shutil
import sys
import os
import time


############################################################################
############################################################################
# BEGIN SPECIALIZATION SECTION (the only part you need to modify beyond 
# adding new test cases).

# name all expected definitions; if present, their definition (with correct
# number of arguments) will be used; if not, a decoy complainer function
# will be used, and all tests on that function should fail.
    
REQUIRED_DEFNS = [
                    "sum_divisors", 'negative_product', 'heater',
                    'analyze', 'travel'
                 ]

# for method names in classes that will be tested
SUB_DEFNS = [
                
            ]

# definitions that are used for extra credit
EXTRA_CREDIT_DEFNS = []

# how many points are test cases worth?
weight_required = 1
weight_extra_credit = 0

# don't count extra credit; usually 100% if this is graded entirely by tests.
# it's up to you the instructor to do the math and add this up!
# TODO: auto-calculate this based on all possible tests.
total_points_from_tests = 80

# how many seconds to wait between batch-mode gradings? 
# ideally we could enforce python to wait to open or import
# files when the system is ready but we've got a communication
# gap going on.
DELAY_OF_SHAME = 1


# set it to true when you run batch mode... 
CURRENTLY_GRADING = False



# what temporary file name should be used for the student?
# This can't be changed without hardcoding imports below, sorry.
# That's kind of the whole gimmick here that lets us import from
# the command-line argument without having to qualify the names.
RENAMED_FILE = "student"




# END SPECIALIZATION SECTION
############################################################################
############################################################################


# enter batch mode by giving a directory to work on as the only argument.
BATCH_MODE = len(sys.argv)==2 and (sys.argv[1] in ["."] or os.path.isdir(sys.argv[1]))

# This class contains multiple "unit tests" that each check
# various inputs to specific functions, checking that we get
# the correct behavior (output value) from completing the call.
class AllTests (unittest.TestCase):

    ############################################################################

    '''sum_divisors tests -- x1.5 pts each == 15 pts'''

    def test_sum_divisors_1(self):
        '''sum_divisors(1) should be 1'''
        self.assertEqual(sum_divisors(1), 1)
    
    def test_sum_divisors_2(self):
        '''sum_divisors(5) should be 6'''
        self.assertEqual(sum_divisors(5), 6)

    def test_sum_divisors_3(self):
        '''sum_divisors(10) should be 18'''
        self.assertEqual(sum_divisors(10), 18)
    
    def test_sum_divisors_4(self):
        '''sum_divisors(49) should be 57'''
        self.assertEqual(sum_divisors(49), 57)

    def test_sum_divisors_5(self):
        '''sum_divisors(75) should be 124'''
        self.assertEqual(sum_divisors(75), 124)

    def test_sum_divisors_6(self):
        '''sum_divisors(100) should be 217'''
        self.assertEqual(sum_divisors(100), 217)
    
    def test_sum_divisors_7(self):
        '''sum_divisors(150) should be 372'''
        self.assertEqual(sum_divisors(150), 372)

    def test_sum_divisors_8(self):
        '''sum_divisors(500) should be 1092'''
        self.assertEqual(sum_divisors(500), 1092)
    
    def test_sum_divisors_9(self):
        '''sum_divisors(1234) should be 1854'''
        self.assertEqual(sum_divisors(1234), 1854)

    def test_sum_divisors_10(self):
        '''sum_divisors(4321) should be 4500'''
        self.assertEqual(sum_divisors(4321), 4500)



    ############################################################################

    ''' negative_product tests -- x1.5 pts each == 15 points'''

    def test_negative_product_1(self):
        '''negative_product([1,2,3,4]) should be 1'''
        self.assertEqual(negative_product([1,2,3,4]), 1)

    def test_negative_product_2(self):
        '''negative_product([1,2,3,-4]) should be -4'''
        self.assertEqual(negative_product([1,2,3,-4]), -4)

    def test_negative_product_3(self):
        '''negative_product([1,-2,3,-4]) should be 8'''
        self.assertEqual(negative_product([1,-2,3,-4]), 8)

    def test_negative_product_4(self):
        '''negative_product([1,-2,-3,-4]) should be -24'''
        self.assertEqual(negative_product([1,-2,-3,-4]), -24)

    def test_negative_product_5(self):
        '''negative_product([-1, 3, -1, 2, 4, 4, 3]) should be 1'''
        self.assertEqual(negative_product([-1, 3, -1, 2, 4, 4, 3]), 1)

    def test_negative_product_6(self):
        '''negative_product([-5, -1, -3, -1, 0, -2, -2]) should be 60'''
        self.assertEqual(negative_product([-5, -1, -3, -1, 0, -2, -2]), 60)

    def test_negative_product_7(self):
        '''negative_product([-7, 6, 5, -9, 5, 5, 7, 1, -6, -3]) should be 1134 '''
        self.assertEqual(negative_product([-7, 6, 5, -9, 5, 5, 7, 1, -6, -3]), 1134 )

    def test_negative_product_8(self):
        '''negative_product([4, 0, -8, 10, 2, 5, 4, -7, 3, -10]) should be -560'''
        self.assertEqual(negative_product([4, 0, -8, 10, 2, 5, 4, -7, 3, -10]), -560)

    def test_negative_product_9(self):
        '''negative_product([-61, -32, 24, -48, -24, 69, -78, -56, -83, -20]) should be -815254142976'''
        self.assertEqual(negative_product([-61, -32, 24, -48, -24, 69, -78, -56, -83, 20]), -815254142976)

    def test_negative_product_10(self):
        '''negative_product([-69, 15, 47, -50, -4, 86, 12, -36, -23, -42]) should be 479908800'''
        self.assertEqual(negative_product([-69, 15, 47, -50, -4, 86, 12, -36, -23, -42]), 479908800)

    ############################################################################

    '''heater tests -- 1x each == 15 points'''

    def test_heater_1(self):
        '''heater(10, 50) should be "success, 4 leftover fuel!"'''
        self.assertEqual(heater(10, 50), "success, 4 leftover fuel!")

    def test_heater_2(self):
        '''heater(5, 55) should be "success, no leftover fuel!"'''
        self.assertEqual(heater(5, 55), "success, no leftover fuel!")
    
    def test_heater_3(self):
        '''heater(5, 50) should be "failure, highest temp is 75"'''
        self.assertEqual(heater(5, 50), "failure, highest temp is 75")

    def test_heater_4(self):
        '''heater(1, 90) should be "success, 1 leftover fuel!"'''
        self.assertEqual(heater(1, 90), "success, 1 leftover fuel!")

    def test_heater_5(self):
        '''heater(0, 80) should be "success, no leftover fuel!"'''
        self.assertEqual(heater(0, 80), "success, no leftover fuel!")

    def test_heater_6(self):
        '''heater(1, 10) should be "failure, highest temp is 15"'''
        self.assertEqual(heater(1, 10), "failure, highest temp is 15")

    def test_heater_7(self):
        '''heater(100, 10) should be "success, 1 leftover fuel!"'''
        self.assertEqual(heater(100, 10), "success, 86 leftover fuel!")

    def test_heater_8(self):
        '''heater(7, 100) should be "success, 7 leftover fuel!"'''
        self.assertEqual(heater(7, 100), "success, 7 leftover fuel!")

    def test_heater_9(self):
        '''heater(8, 40) should be "success, no leftover fuel!"'''
        self.assertEqual(heater(8, 40), "success, no leftover fuel!")

    def test_heater_10(self):
        '''heater(50, -100) should be "success, 14 leftover fuel!"'''
        self.assertEqual(heater(50, -100), "success, 14 leftover fuel!")

    def test_heater_11(self):
        '''heater(25, -100) should be "failure, highest temp is 25"'''
        self.assertEqual(heater(25, -100), "failure, highest temp is 25")

    def test_heater_12(self):
        '''heater(25, -100) should be "failure, highest temp is 20"'''
        self.assertEqual(heater(4, 0), "failure, highest temp is 20")
    
    def test_heater_13(self):
        '''heater(-10, 50) should be "failure, highest temp is 50"'''
        self.assertEqual(heater(-10, 50), "failure, highest temp is 50")

    def test_heater_14(self):
        '''heater(2, 65) should be "failure, highest temp is 75"'''
        self.assertEqual(heater(2, 65), "failure, highest temp is 75")

    def test_heater_15(self):
        '''heater(0, 79) should be "failure, highest temp is 79"'''
        self.assertEqual(heater(0, 79), "failure, highest temp is 79")

    ############################################################################

    ''' analyze tests 1 pt each == 25 points'''

    def test_analyze_1(self):
        '''analyze("w", "wbfs") should be 19.05'''
        self.assertEqual(analyze("w", "wbfs"), 19.05)

    def test_analyze_2(self):
        '''analyze("f", "wbfs") should be 14.29'''
        self.assertEqual(analyze("f", "wbfs"), 14.29)

    def test_analyze_3(self):
        '''analyze("b", "wwbbwwff") should be 15.38'''
        self.assertEqual(analyze("b", "wwbbwwff"), 15.38)

    def test_analyze_4(self):
        '''analyze("w", "wwbbwwff") should be 61.54'''
        self.assertEqual(analyze("w", "wwbbwwff"), 61.54)

    def test_analyze_5(self):
        '''analyze("w", "bbbbb") should be 0'''
        self.assertEqual(analyze("w", "bbbbb"), 0)

    def test_analyze_6(self):
        '''analyze("f", "sssssss") should be 0'''
        self.assertEqual(analyze("f", "sssssss"), 0)

    def test_analyze_7(self):
        '''analyze("b", "ffff") should be 0'''
        self.assertEqual(analyze("b", "ffff"), 0)
    
    def test_analyze_8(self):
        '''analyze("s", "wwwwwwwww") should be 0'''
        self.assertEqual(analyze("s", "wwwwwwwww"), 0)

    def test_analyze_9(self):
        '''analyze("s", "wbfs") should be 57.14'''
        self.assertEqual(analyze("s", "wbfs"), 57.14)

    def test_analyze_10(self):
        '''analyze("b", "wbfs") should be 9.52'''
        self.assertEqual(analyze("b", "wbfs"), 9.52)

    def test_analyze_11(self):
        '''analyze("b", "bbbbb") should be 100'''
        self.assertEqual(analyze("b", "bbbbb"), 100)
    
    def test_analyze_12(self):
        '''analyze("w", "www") should be 100'''
        self.assertEqual(analyze("w", "www"), 100)
    
    def test_analyze_13(self):
        '''analyze("w", "bbbwwwwwsss") should be 32.26'''
        self.assertEqual(analyze("w", "bbbwwwwwsss"), 32.26)
    
    def test_analyze_14(self):
        '''analyze("b", "bbbwwwwwsss") should be 9.68'''
        self.assertEqual(analyze("b", "bbbwwwwwsss"), 9.68)

    def test_analyze_15(self):
        '''analyze("s", "bbbwwwwwsss") should be 58.06'''
        self.assertEqual(analyze("s", "bbbwwwwwsss"), 58.06)

    def test_analyze_16(self):
        '''analyze("s", "sssffbbbwwwwwwwwbbffsss") should be 57.14'''
        self.assertEqual(analyze("s", "sssffbbbwwwwwwwwbbffsss"), 57.14)

    def test_analyze_17(self):
        '''analyze("b", "sssffbbbwwwwwwwwbbffsss") should be 7.94'''
        self.assertEqual(analyze("b", "sssffbbbwwwwwwwwbbffsss"), 7.94)

    def test_analyze_18(self):
        '''analyze("w", "sssffbbbwwwwwwwwbbffsss") should be 25.4'''
        self.assertEqual(analyze("w", "sssffbbbwwwwwwwwbbffsss"), 25.4)

    def test_analyze_19(self):
        '''analyze("f", "sssffbbbwwwwwwwwbbffsss") should be 9.52'''
        self.assertEqual(analyze("f", "sssffbbbwwwwwwwwbbffsss"), 9.52)

    def test_analyze_20(self):
        '''analyze("b", "ffffwwwwwwwwbbbbwwwwwwwwffffssss") should be 5.56'''
        self.assertEqual(analyze("b", "ffffwwwwwwwwbbbbwwwwwwwwffffssss"), 5.56)

    def test_analyze_21(self):
        '''analyze("f", "ffffwwwwwwwwbbbbwwwwwwwwffffssss") should be 16.67'''
        self.assertEqual(analyze("f", "ffffwwwwwwwwbbbbwwwwwwwwffffssss"), 16.67)

    def test_analyze_22(self):
        '''analyze("w", "ffffwwwwwwwwbbbbwwwwwwwwffffssss") should be 44.44'''
        self.assertEqual(analyze("w", "ffffwwwwwwwwbbbbwwwwwwwwffffssss"), 44.44)

    def test_analyze_23(self):
        '''analyze("s", "ffffwwwwwwwwbbbbwwwwwwwwffffssss") should be 33.33'''
        self.assertEqual(analyze("s", "ffffwwwwwwwwbbbbwwwwwwwwffffssss"), 33.33)

    def test_analyze_24(self):
        '''analyze("s", "ffffssswwswwsswwwwwsssssssffffssss") should be 77.27'''
        self.assertEqual(analyze("s", "ffffssswwswwsswwwwwsssssssffffssss"), 77.27)

    def test_analyze_25(self):
        '''analyze("f", "ffffsssfsfsbbbsswwffwbbbbwfwssbbbbssfffbbsssffffssfffss") should be 17.87'''
        self.assertEqual(analyze("f", "ffffsssfsfsbbbsswwffwbbbbwfwssbbbbssfffbbsssffffssfffss"), 17.87)

    ############################################################################

    ''' travel tests -- 1x each == 20 points'''

    def test_travel_1(self):
        '''travel(10, -1, 0) should be 10'''
        self.assertEqual(travel(10, -1, 0), 10)

    def test_travel_2(self):
        '''travel(10, 10, -1) should be 22'''
        self.assertEqual(travel(10, 10, -1), 22)

    def test_travel_3(self):
        '''travel(900, -50, 10) should be 13'''
        self.assertEqual(travel(900, -50, 10), 13)

    def test_travel_4(self):
        '''travel(500, 75, 25) should be 5'''
        self.assertEqual(travel(500, 75, 25), 5)

    def test_travel_5(self):
        '''travel(0, 1, 0) should be 999, already on the end!'''
        self.assertEqual(travel(0,1,0), 0)

    def test_travel_6(self):
        '''travel(0, -1, 0) should be 0, already on the end!'''
        self.assertEqual(travel(0,-1,0), 0)

    def test_travel_7(self):
        '''travel(1000, -1, 0) should be 0, already on the end!'''
        self.assertEqual(travel(1000,-1,0), 0)

    def test_travel_8(self):
        '''travel(1000, 1, 0) should be 0, already on the end!'''
        self.assertEqual(travel(1000,1,0), 0)

    def test_travel_9(self):
        '''travel(800, 5, 5) should be 9'''
        self.assertEqual(travel(800, 5, 5), 9)

    def test_travel_10(self):
        '''travel(300, 25, -5) should be 18'''
        self.assertEqual(travel(300, 25, -5), 18)

    def test_travel_11(self):
        '''travel(100, 50, 1) should be 16'''
        self.assertEqual(travel(100, 50, 1), 16)

    def test_travel_12(self):
        '''travel(999, -50, 10) should be 12'''
        self.assertEqual(travel(999, -50, 10), 12)

    def test_travel_13(self):
        '''travel(1, 100, 50) should be 5'''
        self.assertEqual(travel(1, 100, 50), 5)

    def test_travel_14(self):
        '''travel(873, -18, 2) should be 25'''
        self.assertEqual(travel(873, -18, 2), 25)

    def test_travel_15(self):
        '''travel(904, -5, -5) should be 19'''
        self.assertEqual(travel(904, -5, -5), 19)

    def test_travel_16(self):
        '''travel(777, 7, 7) should be 8'''
        self.assertEqual(travel(777, 7, 7), 8)

    def test_travel_17(self):
        '''travel(888,-8,-8) should be 15'''
        self.assertEqual(travel(888,-8,-8), 15)

    def test_travel_18(self):
        '''travel(123,45,-6) should be 10'''
        self.assertEqual(travel(123,45,-6), 19)

    def test_travel_19(self):
        '''travel(222,22,2) should be 20'''
        self.assertEqual(travel(222,22,2), 20)

    def test_travel_20(self):
        '''travel(500, -5, -15) should be 9'''
        self.assertEqual(travel(500, -5, -15), 9)

    ############################################################################

# This class digs through AllTests, counts and builds all the tests,
# so that we have an entire test suite that can be run as a group.
class TheTestSuite (unittest.TestSuite):
    # constructor.
    def __init__(self,wants):
        self.num_req = 0
        self.num_ec = 0
        # find all methods that begin with "test".
        fs = []
        for w in wants:
            for func in AllTests.__dict__:
                # append regular tests
                # drop any digits from the end of str(func).
                dropnum = str(func)
                while dropnum[-1] in "1234567890":
                    dropnum = dropnum[:-1]
                
                if dropnum==("test_"+w+"_") and (not (dropnum==("test_extra_credit_"+w+"_"))):
                    fs.append(AllTests(str(func)))
                if dropnum==("test_extra_credit_"+w+"_") and not BATCH_MODE:
                    fs.append(AllTests(str(func)))
        
#       print("TTS ====> ",list(map(lambda f: (f,id(f)),fs)))
        # call parent class's constructor.
        unittest.TestSuite.__init__(self,fs)

class TheExtraCreditTestSuite (unittest.TestSuite):
        # constructor.
        def __init__(self,wants):
            # find all methods that begin with "test_extra_credit_".
            fs = []
            for w in wants:
                for func in AllTests.__dict__:
                    if str(func).startswith("test_extra_credit_"+w):
                        fs.append(AllTests(str(func)))
        
#           print("TTS ====> ",list(map(lambda f: (f,id(f)),fs)))
            # call parent class's constructor.
            unittest.TestSuite.__init__(self,fs)

# all (non-directory) file names, regardless of folder depth,
# under the given directory 'dir'.
def files_list(dir):
    this_file = __file__
    if dir==".":
        dir = os.getcwd()
    info = os.walk(dir)
    filenames = []
    for (dirpath,dirnames,filez) in info:
#       print(dirpath,dirnames,filez)
        if dirpath==".":
            continue
        for file in filez:
            if file==this_file:
                continue
            filenames.append(os.path.join(dirpath,file))
#       print(dirpath,dirnames,filez,"\n")
    return filenames

def main():
    if len(sys.argv)<2:
        raise Exception("needed student's file name as command-line argument:"\
            +"\n\t\"python3 testerX.py gmason76_2xx_Px.py\"")
    
    if BATCH_MODE:
        print("BATCH MODE.\n")
        run_all()
        return
        
    else:
        want_all = len(sys.argv) <=2
        wants = []
        # remove batch_mode signifiers from want-candidates.
        want_candidates = sys.argv[2:]
        for i in range(len(want_candidates)-1,-1,-1):
            if want_candidates[i] in ['.'] or os.path.isdir(want_candidates[i]):
                del want_candidates[i]
    
        # set wants and extra_credits to either be the lists of things they want, or all of them when unspecified.
        wants = []
        extra_credits = []
        if not want_all:
            for w in want_candidates:
                if w in REQUIRED_DEFNS:
                    wants.append(w)
                elif w in SUB_DEFNS:
                    wants.append(w)
                elif w in EXTRA_CREDIT_DEFNS:
                    extra_credits.append(w)
                else:
                    raise Exception("asked to limit testing to unknown function '%s'."%w)
        else:
            wants = REQUIRED_DEFNS + SUB_DEFNS
            extra_credits = EXTRA_CREDIT_DEFNS
        
        # now that we have parsed the function names to test, run this one file.    
        run_one(wants,extra_credits)    
        return
    return # should be unreachable! 

# only used for non-batch mode, since it does the printing.
# it nicely prints less info when no extra credit was attempted.
def run_one(wants, extra_credits):
    
    has_reqs = len(wants)>0
    has_ec   = len(extra_credits)>0
    
    # make sure they exist.
    passed1 = 0
    passed2 = 0
    tried1 = 0
    tried2 = 0
    
    # only run tests if needed.
    if has_reqs:
        print("\nRunning required definitions:")
        (tag, passed1,tried1) = run_file(sys.argv[1],wants,False)
    if has_ec:
        print("\nRunning extra credit definitions:")
        (tag, passed2,tried2) = run_file(sys.argv[1],extra_credits,True)
    
    # print output based on what we ran.
    if has_reqs and not has_ec:
        print("\n%d/%d Required test cases passed (worth %.1f each)" % (passed1,tried1,weight_required) )
        print("\nScore based on test cases: %.2f/%d (%.2f*%.1f) " % (
                                                                passed1*weight_required, 
                                                                total_points_from_tests,
                                                                passed1,
                                                                weight_required
                                                             ))
    elif has_ec and not has_reqs:
        print("%d/%d Extra credit test cases passed (worth %d each)" % (passed2, tried2, weight_extra_credit))
    else: # has both, we assume.
        print("\n%d / %d Required test cases passed (worth %d each)" % (passed1,tried1,weight_required) )
        print("%d / %d Extra credit test cases passed (worth %d each)" % (passed2, tried2, weight_extra_credit))
        print("\nScore based on test cases: %.2f / %d ( %d * %d + %d * %d) " % (
                                                                passed1*weight_required+passed2*weight_extra_credit, 
                                                                total_points_from_tests,
                                                                passed1,
                                                                weight_required,
                                                                passed2,
                                                                weight_extra_credit
                                                             ))
    if CURRENTLY_GRADING:
        print("( %d %d %d %d )\n%s" % (passed1,tried1,passed2,tried2,tag))

# only used for batch mode.
def run_all():
        filenames = files_list(sys.argv[1])
        #print(filenames)
        
        wants = REQUIRED_DEFNS + SUB_DEFNS
        extra_credits = EXTRA_CREDIT_DEFNS
        
        results = []
        for filename in filenames:
            print(" Batching on : " +filename)
            # I'd like to use subprocess here, but I can't get it to give me the output when there's an error code returned... TODO for sure.
            lines = os.popen("python3 tester1p.py \""+filename+"\"").readlines()
            
            # delay of shame...
            time.sleep(DELAY_OF_SHAME)
            
            name = os.path.basename(lines[-1])
            stuff =lines[-2].split(" ")[1:-1]
            print("STUFF: ",stuff, "LINES: ", lines)
            (passed_req, tried_req, passed_ec, tried_ec) = stuff
            results.append((lines[-1],int(passed_req), int(tried_req), int(passed_ec), int(tried_ec)))
            continue
        
        print("\n\n\nGRAND RESULTS:\n")
        
            
        for (tag_req, passed_req, tried_req, passed_ec, tried_ec) in results:
            name = os.path.basename(tag_req).strip()
            earned   = passed_req*weight_required + passed_ec*weight_extra_credit
            possible = tried_req *weight_required # + tried_ec *weight_extra_credit
            print("%10s : %3d / %3d = %5.2d %% (%d/%d*%d + %d/%d*%d)" % (
                                                            name,
                                                            earned,
                                                            possible, 
                                                            (earned/possible)*100,
                                                            passed_req,tried_req,weight_required,
                                                            passed_ec,tried_ec,weight_extra_credit
                                                          ))
# only used for batch mode.
def run_all_orig():
        filenames = files_list(sys.argv[1])
        #print(filenames)
        
        wants = REQUIRED_DEFNS + SUB_DEFNS
        extra_credits = EXTRA_CREDIT_DEFNS
        
        results = []
        for filename in filenames:
            # wipe out all definitions between users.
            for fn in REQUIRED_DEFNS+EXTRA_CREDIT_DEFNS :
                globals()[fn] = decoy(fn)
                fn = decoy(fn)
            try:
                name = os.path.basename(filename)
                print("\n\n\nRUNNING: "+name)
                (tag_req, passed_req, tried_req) = run_file(filename,wants,False)
                (tag_ec,  passed_ec,  tried_ec ) = run_file(filename,extra_credits,True)
                results.append((tag_req,passed_req,tried_req,tag_ec,passed_ec,tried_ec))
                print(" ###### ", results)
            except SyntaxError as e:
                tag = filename+"_SYNTAX_ERROR"
                results.append((tag,0,len(wants),tag,0,len(extra_credits)))
            except NameError as e:
                tag =filename+"_Name_ERROR"
                results.append((tag,0,len(wants),tag,0,len(extra_credits)))
            except ValueError as e:
                tag = filename+"_VALUE_ERROR"
                results.append((tag,0,len(wants),tag,0,len(extra_credits)))
            except TypeError as e:
                tag = filename+"_TYPE_ERROR"
                results.append((tag,0,len(wants),tag,0,len(extra_credits)))
            except ImportError as e:
                tag = filename+"_IMPORT_ERROR_TRY_AGAIN"
                results.append((tag,0,len(wants),tag,0,len(extra_credits)))
            except Exception as e:
                tag = filename+str(e.__reduce__()[0])
                results.append((tag,0,len(wants),tag,0,len(extra_credits)))
        
#           try:
#               print("\n |||||||||| scrupe: "+str(scruples))
#           except Exception as e:
#               print("NO SCRUPE.",e)
#           scruples = None
        
        print("\n\n\nGRAND RESULTS:\n")
        for (tag_req, passed_req, tried_req, tag_ec, passed_ec, tried_ec) in results:
            name = os.path.basename(tag_req)
            earned   = passed_req*weight_required + passed_ec*weight_extra_credit
            possible = tried_req *weight_required # + tried_ec *weight_extra_credit
            print("%10s : %3d / %3d = %5.2d %% (%d/%d*%d + %d/%d*%d)" % (
                                                            name,
                                                            earned,
                                                            possible, 
                                                            (earned/possible)*100,
                                                            passed_req,tried_req,weight_required,
                                                            passed_ec,tried_ec,weight_extra_credit
                                                          ))

def try_copy(filename1, filename2, numTries):
    have_copy = False
    i = 0
    while (not have_copy) and (i < numTries):
        try:
            # move the student's code to a valid file.
            shutil.copy(filename1,filename2)
            
            # wait for file I/O to catch up...
            if(not wait_for_access(filename2, numTries)):
                return False
                
            have_copy = True
        except PermissionError:
            print("Trying to copy "+filename1+", may be locked...")
            i += 1
            time.sleep(1)
        except BaseException as e:
            print("\n\n\n\n\n\ntry-copy saw: "+e)
    
    if(i == numTries):
        return False
    return True

def try_remove(filename, numTries):
    removed = False
    i = 0
    while os.path.exists(filename) and (not removed) and (i < numTries):
        try:
            os.remove(filename)
            removed = True
        except OSError:
            print("Trying to remove "+filename+", may be locked...")
            i += 1
            time.sleep(1)
    if(i == numTries):
        return False
    return True

def wait_for_access(filename, numTries):
    i = 0
    while (not os.path.exists(filename) or not os.access(filename, os.R_OK)) and i < numTries:
        print("Waiting for access to "+filename+", may be locked...")
        time.sleep(1)
        i += 1
    if(i == numTries):
        return False
    return True

# this will group all the tests together, prepare them as 
# a test suite, and run them.
def run_file(filename,wants=None,checking_ec = False):
    if wants==None:
        wants = []
    
    # move the student's code to a valid file.
    if(not try_copy(filename,"student.py", 5)):
        print("Failed to copy " + filename + " to student.py.")
        quit()
        
    # import student's code, and *only* copy over the expected functions
    # for later use.
    import importlib
    count = 0
    while True:
        try:
#           print("\n\n\nbegin attempt:")
            while True:
                try:
                    f = open("student.py","a")
                    f.close()
                    break
                except:
                    pass
#           print ("\n\nSUCCESS!")
                
            import student
            importlib.reload(student)
            break
        except ImportError as e:
            print("import error getting student... trying again. "+os.getcwd(), os.path.exists("student.py"),e)
            time.sleep(0.5)
            while not os.path.exists("student.py"):
                time.sleep(0.5)
            count+=1
            if count>3:
                raise ImportError("too many attempts at importing!")
        except SyntaxError as e:
            print("SyntaxError in "+filename+":\n"+str(e))
            print("Run your file without the tester to see the details")
            return(filename+"_SYNTAX_ERROR",None, None, None)
        except NameError as e:
            print("NameError in "+filename+":\n"+str(e))
            print("Run your file without the tester to see the details")
            return((filename+"_Name_ERROR",0,1))    
        except ValueError as e:
            print("ValueError in "+filename+":\n"+str(e))
            print("Run your file without the tester to see the details")
            return(filename+"_VALUE_ERROR",0,1)
        except TypeError as e:
            print("TypeError in "+filename+":\n"+str(e))
            print("Run your file without the tester to see the details")
            return(filename+"_TYPE_ERROR",0,1)
        except ImportError as e:            
            print("ImportError in "+filename+":\n"+str(e))
            print("Run your file without the tester to see the details or try again")
            return((filename+"_IMPORT_ERROR_TRY_AGAIN   ",0,1)) 
        except Exception as e:
            print("Exception in loading"+filename+":\n"+str(e))
            print("Run your file without the tester to see the details")
            return(filename+str(e.__reduce__()[0]),0,1)
    
    # make a global for each expected definition.
    for fn in REQUIRED_DEFNS+EXTRA_CREDIT_DEFNS :
        globals()[fn] = decoy(fn)
        try:
            globals()[fn] = getattr(student,fn)
        except:
            if fn in wants:
                print("\nNO DEFINITION FOR '%s'." % fn) 
    
    if not checking_ec:
        # create an object that can run tests.
        runner = unittest.TextTestRunner()
    
        # define the suite of tests that should be run.
        suite = TheTestSuite(wants)
    
    
        # let the runner run the suite of tests.
        ans = runner.run(suite)
        num_errors   = len(ans.__dict__['errors'])
        num_failures = len(ans.__dict__['failures'])
        num_tests    = ans.__dict__['testsRun']
        num_passed   = num_tests - num_errors - num_failures
        # print(ans)
    
    else:
        # do the same for the extra credit.
        runner = unittest.TextTestRunner()
        suite = TheExtraCreditTestSuite(wants)
        ans = runner.run(suite)
        num_errors   = len(ans.__dict__['errors'])
        num_failures = len(ans.__dict__['failures'])
        num_tests    = ans.__dict__['testsRun']
        num_passed   = num_tests - num_errors - num_failures
        #print(ans)
    
    # remove our temporary file.
    os.remove("student.py")
    if os.path.exists("__pycache__"):
        shutil.rmtree("__pycache__")
    if(not try_remove("student.py", 5)):
        print("Failed to remove " + filename + " to student.py.")
    
    tag = ".".join(filename.split(".")[:-1])
    
    
    return (tag, num_passed, num_tests)


# make a global for each expected definition.
def decoy(name):
        # this can accept any kind/amount of args, and will print a helpful message.
        def failyfail(*args, **kwargs):
            return ("<no '%s' definition was found - missing, or typo perhaps?>" % name)
        return failyfail

# this determines if we were imported (not __main__) or not;
# when we are the one file being run, perform the tests! :)
if __name__ == "__main__":
    main()
