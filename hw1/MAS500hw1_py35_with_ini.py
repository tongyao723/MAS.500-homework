import configparser, mediacloud, datetime

##configfile = open('MAS500hw1.ini', 'r')

config = configparser.ConfigParser()
config.read('MAS500hw1_config_template.ini')
API_Key = config['MediaCloud']['api_key']
subj1 = config['Query']['subject1']
subj2 = config['Query']['subject2']
#print(subj1)

mc = mediacloud.api.MediaCloud(API_Key)
res1 = mc.sentenceCount( subj1, solr_filter = [mc.publish_date_query( datetime.date( 2016, 9, 1), datetime.date( 2016, 9, 30) ), 'tags_id_media:1' ])
res2 = mc.sentenceCount( subj2, solr_filter = [mc.publish_date_query( datetime.date( 2016, 9, 1), datetime.date( 2016, 9, 30) ), 'tags_id_media:1' ])
print ('# ', subj1, ' was mentioned on media: ', res1['count']) # prints the number of sentences found
print ('# ', subj2, 'was mentioned on media: ', res2['count'])

op1 = ' was talked about more frequently than '
op2 = 'They were talked about as frequently as each other.'

if res1['count'] > res2['count']:
   ver = subj1 + op1 + subj2 + ' in September 2016.'
elif res1['count'] < res2['count']:
    ver = subj2 + op1 + subj1 + ' in September 2016.'
else:
    ver = op2
print(ver)

