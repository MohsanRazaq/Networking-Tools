import requests
def parse_robots_txt( url):
        robots_txt = requests.get(url + '/robots.txt')
        robots_txt_lines = robots_txt.text.split('\n')
        for line in robots_txt_lines:
            if 'Allow' in line:
                print(line)
url='https://daraz.pk'
parse_robots_txt(url)