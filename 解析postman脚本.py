import json


def print_postman_url(path):
    with open(path, encoding='utf-8') as file:
        s = file.read()
        items = json.loads(s)["item"]
        for item in items:
            url = item["request"]["url"]
            if "raw" in url:
                print("我有raw")
                print(url["raw"])
            else:
                print("我没有raw")
                host_result = ""
                for index, host in enumerate(url["host"]):
                    host_suffix = "" if index == len(url["host"]) - 1 else "."
                    host_result += host + host_suffix
                path_result = "/"
                path_in_url = url["path"]
                if str == type(path_in_url):
                    path_result = path_in_url
                else:
                    for index, path in enumerate(path_in_url):
                        path_suffix = "" if index == len(path_in_url) - 1 else "/"
                        path_result += path + path_suffix

                if "query" in url:
                    path_query = ""
                    for index, query in enumerate(url["query"]):
                        query_prefix = "?" if index == 0 else "&"
                        path_query += query_prefix + query['key'] + "=" + query["value"]
                else:
                    path_query = ""
                print(host_result + path_result + path_query)


print_postman_url("parse_json.json")
