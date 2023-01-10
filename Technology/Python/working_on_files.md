# Working on Files
-  Best practise to use `with` keyword for opening any file as it utilizes python contest manager which takes care of resource utilization like automatically closing the file and freeing up resources.
-  Example
^
    with open('pagehead.section.htm', 'r') as f:
        output = f.read()
^

### JSON File
-  module `import json` can be used for json files.
-  Example
^
    f = open('Files/sample.json')
    data = json.load(f)
    for key, value in data.items():
        print(key, value)
^
