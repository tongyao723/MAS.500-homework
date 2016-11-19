import mediacloud, datetime
mc = mediacloud.api.MediaCloud('03c4af1a8327ec7ee8e305d3e52720a672feacee9894bc9136215d5a544b31ff')
res1 = mc.sentenceCount('(Trump)', solr_filter=[mc.publish_date_query( datetime.date( 2016, 9, 1), datetime.date( 2016, 9, 30) ), 'tags_id_media:1' ])
res2 = mc.sentenceCount('(Clinton)', solr_filter=[mc.publish_date_query( datetime.date( 2016, 9, 1), datetime.date( 2016, 9, 30) ), 'tags_id_media:1' ])
print ("coverage about Trump:", res1['count']) # prints the number of sentences found
print ("coverage about Clinton:", res2['count'])