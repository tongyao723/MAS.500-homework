import mediacloud, datetime, unittest, logging
class APITest(unittest.TestCase):
    mc = mediacloud.api.MediaCloud('03c4af1a8327ec7ee8e305d3e52720a672feacee9894bc9136215d5a544b31ff')
    res1 = mc.sentenceCount('( Trump )', solr_filter=[mc.publish_date_query( datetime.date( 2016, 9, 1), datetime.date( 2016, 9, 30) ), 'tags_id_media:1' ])
    res2 = mc.sentenceCount('( Clinton)', solr_filter=[mc.publish_date_query( datetime.date( 2016, 9, 1), datetime.date( 2016, 9, 30) ), 'tags_id_media:1' ])
    print ("# Trump was mentioned: ",res1['count']) # prints the number of sentences found
    print ("# Clinton was mentioned: ",res2['count'])

    def mediacloud_test(self):
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger(__name__)


        # # create a file handler
        # handler = logging.FileHandler('HW2_mediacloudAPItest.log')
        # handler.setLevel(logging.INFO)
        #
        # # create a logging format
        # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # handler.setFormatter(formatter)
        #
        # # add the handlers to the logger
        # logger.addHandler(handler)

        assert self.mc is not None
        logger.info("MediaCloud API was loaded successfully.")
        assert self.res1 is not None
        logger.info("Result for Trump was loaded successfully: %s", self.res1)
        assert self.res2 is not None
        logger.info("Result for Clinton was loaded successfully: %s", self.res2)

if __name__ == '__main__':
    unittest.main()




    