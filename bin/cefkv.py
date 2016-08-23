import re
import splunk.Intersplunk
import splunk.search as search
import string

# Build key/value pairs
##CEF_KV_RE = re.compile('([\w.]+)=(((?!(\w+=)).)*)(\s|$)')
CEF_KV_RE = re.compile('([\w.]+)=(((?!(\w+=)).)*)(\s|$)')

# Identify basic fields
CEF_DATA_RE = re.compile('CEF:\d+\|[^|]*\|[^|]*\|[^|]*\|[^|]*\|[^|]*\|[^|]*\|(.*)')

# Identify Labels
CEF_LABEL_RE = re.compile('(([\w.]+\d)Label)')

try:
	results,dummyresults,settings = splunk.Intersplunk.getOrganizedResults()

	for r in results:
		cefRaw  = r["_raw"]
		z       = {}
		k       = CEF_DATA_RE.search(cefRaw)
		if k:
			cefData = k.group(1)
	 
			for kvpair in CEF_KV_RE.findall(cefData):
				z[kvpair[0]] = kvpair[1]

			for key in z:
				isLabel=CEF_LABEL_RE.search(key)
				if isLabel:
					v = isLabel.group(2)
					if v in z: 
						# Normalize key name
						t = re.sub(r'\W','_',z[key])
						r[t] = z[v]

except:
	import traceback
	stack =  traceback.format_exc()
	results = splunk.Intersplunk.generateErrorResults("Error : Traceback: " + str(stack))

splunk.Intersplunk.outputResults(results)

