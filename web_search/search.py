import requests

def search(query:str):
    qr = query
    if qr == 'input':
        qr = input("type something>")

    url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/WebSearchAPI"
    querystring = {"q":f"{qr}","pageNumber":"1","pageSize":"50","autoCorrect":"true"}
    headers = {
    'x-rapidapi-key': "15f202366dmsh2ecff8357c3cfabp1392a9jsn47bb86b69162",
    'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    import json
    c = json.loads(response.text)
    r  = c['value'][0]["description"]
    return r




