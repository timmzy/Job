
from Job import Job
import IndeedSearch
import webbrowser, time
import requests, json, sys
from googlesearch import search
import urllib

#Take jobs retrieved from search and format them as dicts using serialize
def jobFormat(jobs: list):
    serialized = []
    for i in range(len(jobs)):
        serialized.append(jobs[i].serialize())
    return serialized

# Execute a job search using a given query string
"""
Example

query = Software Engineering Internship

1. Google search is conducted for "Software Engineering Internship"

2. First indeed and glassdoor results are saved. (only indeed link is used for now).

3. IndeedSearch.py is executed and a list of jobs is returned

"""
def execute(query: str):
    indeedLink = ""
    glassdoorLink = ""
    try:
        for x in search(query, tld='com', lang='en', num=10, stop=10, pause=1):
            if(len(indeedLink) > 1 and len(glassdoorLink) > 1):
                break
            if("indeed" in x):
                if(len(indeedLink) > 1):
                    continue
                indeedLink = x
            if("glassdoor" in x):
                if(len(glassdoorLink) > 1):
                    continue
                glassdoorLink = x
        indeed = IndeedSearch.execute(indeedLink)
        return jobFormat(indeed)
    except urllib.error.HTTPError as httperr:
        print(httperr.headers)  # Dump the headers to see if there's more information
        print(httperr.read())

if __name__ == "__main__":
    y = json.dumps(execute(sys.argv[1]))
    file_name = str(time.time()).replace(".", "-") + ".txt"
    with open("home/temp/" + file_name, 'w') as f:
        f.write(y)
    print(file_name)