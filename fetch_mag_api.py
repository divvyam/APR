import httplib, urllib, base64
import threading
import json
import os
import sys
from multiprocessing import Queue

def load_json(year,sub_key,count=1,offset=0):
    expr = "Y=%d" % year
    offset = str(offset)
    count = str(count)
    attributes = "Id,Ti,AA.AuN,AA.AfN,E.VFN,Y,AA.AuId,F.FN,CC,RId,J.JN,C.CN,W,D,AA.AfId,AA.S,F.FId,J.JId,C.CId,E.DOI,E.CC,E.IA.IndexLength,E.IA.InvertedIndex,ECC"
    headers = {
        # Request headers
        'Ocp-Apim-Subscription-Key': sub_key,
    }
    params = urllib.urlencode({
        # Request parameters
        'expr': expr,
        'model': 'latest',
        'count': count,
        'offset': offset,
        # 'orderby': "Id",
        'attributes': attributes,
    })
    try:
        conn = create_connection()
        conn.request("GET", "/academic/v1.0/evaluate?%s" % params, "{body}", headers)
        response = conn.getresponse()
        response_code = response.status
        if response_code != 200:
            raise Exception("Invalid response code: {}".format(response_code))
        data = response.read()
        # print(data)
        conn.close()
    except Exception as e:
        print("[Error {0}]".format(e))
        raise
    #process the data and save to file
    json_obj = json.loads(data)
    entities = json_obj["entities"]
    return entities

def write_output_file(data, json_name):
    # json_name = "../data.json"
    with open(json_name,"a") as f:
        json.dump(data, f, indent=2)

def create_connection():
    conn = httplib.HTTPSConnection('api.labs.cognitive.microsoft.com')
    return conn

####################################
sub_key = os.getenv("SUB_KEY", None)
if not subkey:
    print "Environment variable \"SUB_KEY\" not set!!"
    print "set \"SUB_KEY\" using command: export SUB_KEY=<your_subscription_key>"
    sys.exit(1)
if len(sys.argv) < 2:
    print "Year is required!!!"
    sys.exit(1)
year = int(sys.argv[1])
start = 0
end = 15000000
count = 1000
json_name = "../{}_data.json".format(year)
for offset in range(start,end,count):
    print "downloading rows from {} to {}".format(offset, offset+count)
    try:
        entries = load_json(year, sub_key, count, offset)
    except Exception as e:
        print "Stopping the download received error!!!"
        sys.exit(1)
    write_output_file(entries, json_name)
#combine all different 


