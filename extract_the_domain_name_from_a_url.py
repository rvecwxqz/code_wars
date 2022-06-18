'''https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python'''


def domain_name(url):
    to_split = ['https://', 'http://', 'www.']
    for t in to_split:
        if t in url:
            url = url.split(t)[1]
    return url.split('.')[0]


print(domain_name('http://google.com'))
