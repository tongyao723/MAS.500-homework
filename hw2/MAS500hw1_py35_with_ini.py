import configparser, mediacloud, datetime

##configfile = open('MAS500hw1.ini', 'r')

class hw1_wrapper():

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('MAS500hw1_config_template.ini')
        self.API_Key = config['MediaCloud']['api_key']
        self.subj1 = config['Query']['subject1']
        self.subj2 = config['Query']['subject2']
        self.mc = mediacloud.api.MediaCloud(self.API_Key)
        self.res1 = self.mc.sentenceCount(self.subj1, solr_filter=[
            self.mc.publish_date_query(datetime.date(2016, 9, 1), datetime.date(2016, 9, 30)), 'tags_id_media:1'])
        self.res2 = self.mc.sentenceCount(self.subj2, solr_filter=[
            self.mc.publish_date_query(datetime.date(2016, 9, 1), datetime.date(2016, 9, 30)), 'tags_id_media:1'])

    def get_mc(self):
        return self.mc

    def get_result_1(self):
        return self.res1

    def get_result_2(self):
        return self.res2

    def print_result(self):
        print ('# ', self.subj1, ' was mentioned on media: ', self.res1['count']) # prints the number of sentences found
        print ('# ', self.subj2, 'was mentioned on media: ', self.res2['count'])
        op1 = ' was talked about more frequently than '
        op2 = 'They were talked about as frequently as each other.'
        flag = True
        if self.res1['count'] > self.res2['count']:
            ver = self.subj1 + op1 + self.subj2 + ' in September 2016.'
            flag = True
        elif self.res1['count'] < self.res2['count']:
            ver = self.subj2 + op1 + self.subj1 + ' in September 2016.'
            flag = False
        else:
            ver = op2
        print(ver)
        return flag

if __name__ == "__main__":
    hw1_obj = hw1_wrapper()
    hw1_obj.print_result()
