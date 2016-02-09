import re
def main(endpoint, StoredParameterName, StringWithValue):
	return {StoredParameterName: re.findall('[0-9]+.+[0-9]', StringWithValue)[0]}
