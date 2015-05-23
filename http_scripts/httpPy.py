print("**********start**********")
import json
import requests

r = requests.get("http://csb.stanford.edu/class/public/pages/sykes_webdesign/05_simple.html")
print(json.dumps(r.content, indent=4))
#print r.status_code
#print r.headers
#print r.content
print("**********finished**********")