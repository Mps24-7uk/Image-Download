import requests

f = open("C:/Users/mayank singh/desktop/family6.txt")
content = f.read()
urls = content.split("\n")

def write_to_file(url, path):
    try:
        requests.get(url)
    except Exception as e:
        print(e)
    else:
        with open(path, 'wb') as f:
            f.write(requests.get(url).content)

i = 1
for url in urls:
    if len(url) == 0 or url=='':
        continue
    print(url)
    write_to_file(url,"C:/Users/mayank singh/desktop/family123/" +"xxxxz"+str(i)+ ".jpg")
    i += 1