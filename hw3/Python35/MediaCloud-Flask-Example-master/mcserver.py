import configparser, logging, datetime, os

from flask import Flask, render_template, request

import mediacloud

CONFIG_FILE = 'settings.config'
basedir = os.path.dirname(os.path.realpath(__file__))

# load the settings file
config = configparser.ConfigParser()
config.read(os.path.join(basedir, 'settings.config'))

# set up logging
log_file_path = os.path.join(basedir,'logs','mcserver.log')
logging.basicConfig(filename=log_file_path,level=logging.DEBUG)
logging.info("Starting the MediaCloud example Flask app!")

# clean a mediacloud api client
mc = mediacloud.api.MediaCloud( config.get('mediacloud','api_key') )

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("search-form.html")

@app.route("/search",methods=['POST'])
def search_results():
    keywords = request.form['keywords']
    start_time = request.form['start_time']
    end_time = request.form['end_time']
    #print(datetime.date( 2015, 1, 1))
    now = datetime.datetime.now()
    start_time_split = start_time.split("-")
    end_time_split = end_time.split("-")
    start_time_int = [2000,1,1]
    end_time_int = [2001,1,1]
    for ii in range(3):
        start_time_int[ii] = int(start_time_split[ii])
        end_time_int[ii] = int(end_time_split[ii])

    start_datetime = datetime.date( start_time_int[0], start_time_int[1], start_time_int[2])
    end_datetime = datetime.date( end_time_int[0], end_time_int[1], end_time_int[2])
    delta = end_datetime-start_datetime
    if delta.days < 90:
        date_interval = "1 Day"
    elif delta.days >= 90 and delta.days < 180:
        date_interval = "3 Days"
    else:
        date_interval = "Week "
    date_interval = "Sentence Count Every " + date_interval 
    print
    results = mc.sentenceCount(keywords,
        solr_filter=[mc.publish_date_query( start_datetime, 
                                             end_datetime ),
                     'media_sets_id:1' ],
                     split = True,
                     split_start_date = start_time,
                     split_end_date = end_time)
    categories = []
    values = []
    sorted_keys = []
    for key in results['split'].keys():
        sorted_keys.append(key)
    sorted_keys.sort()

    for key in sorted_keys:
        if key != "gap" and key != "end" and key != "start":
            values.append(results['split'][key])
            categories.append(key[:10])


    category_string = ""
    value_string = ""
    for ii in range(len(categories)):
        category_string = category_string + "\'" + categories[ii] + "\'"
        value_string = value_string + str(values[ii])
        if ii < len(categories)-1:
            category_string = category_string + ","
            value_string = value_string + ","

    search_quote_string = "Counts of " + keywords
    return render_template("search-results.html", frequency = date_interval,
        keywords=keywords, sentenceCount=results['count'], category_placeholder = category_string, value_placeholder = value_string, search_quote = search_quote_string )

if __name__ == "__main__":
    app.debug = True
    app.run()
