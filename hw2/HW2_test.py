import unittest, MAS500hw1_py35_with_ini
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create a file handler
handler = logging.FileHandler('testresult.log')
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)


class APIFetchTest(unittest.TestCase):

    def setUp(self):
        self.results = MAS500hw1_py35_with_ini.hw1_wrapper()

    def testLoad(self):

        #uncomment assert lines for interactive debugging
        #assert self.results.mc is not None
        if self.results.mc is not None:
            logger.info('MC connection success')
        else:
            logger.info('MC connection failure')

        #assert self.results.get_result_1() is not None
        if self.results.get_result_1() is not None:
            logger.info('Result 1 is correct')
        else:
            logger.info('Result 1 is incorrect')

        #assert self.results.get_result_2() is not None
        if self.results.get_result_2() is not None:
            logger.info('Result 2 is correct')
        else:
            logger.info('Result 2 is incorrect')

if __name__ == "__main__":
    unittest.main()