# DBpedia-script

## About

Retrieve attributes from a DBpedia webpage.

## Project Directory

* ```main.py```: script to retrieve and save attributes from (colleges) listed in ```college_list_urls.json```.
* ```README.md```: README file
* ```requirements.txt```: Python packages required
* ```utils.py```: utils for crawler
* ```/json```: saved data

## Usage

### Retrieve and save attributes from a new item

```Python
import sys
import json

import utils

name = 'Rensselaer Polytechnic Institute'
url = 'http://dbpedia.org/page/Rensselaer_Polytechnic_Institute'

spider = utils.DBpediaSpider(url)
try:
    attr = spider.get_attributes()
except ValueError as e:
    print('Cannot retrieve attributes from {:s}: {}'.format(name, e))
    sys.exit(1)
s = json.dumps(attr, indent=4)

with open(name+'.json', 'w') as f:
    f.write(s)
```

### Load attributes from saved data

```Python
import json

import utils

filename = 'Rensselaer Polytechnic Institute.json'

with open(filename, 'r') as f:
    raw = f.read()

attr = json.loads(raw.strip())

# attr is a Python dictionary
attr.keys()
attr['dbp:academicStaff']
attr['dbo:president']
```

## About attribute prefixes

See [DBpedia.org](http://dbpedia.org/sparql?help=nsdecl) for help.
