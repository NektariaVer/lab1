import requests
import http.cookies

while True:
    url = input('URL:')
    if url == '': break
    if not url.startswith('http'):
        url = 'http://'+ url
    try:
        with requests.get(url) as response:
            print("RESPONSE HEADER")
            for key, value in response.headers.items():
                print("{:30s} {}".format(key, value))

            server = response.headers.get('Server')
            if server:
                print(f"\n\nWeb server: {server}")
            else:
                print("\nWeb server not found.")

            if 'Set-Cookie' in response.headers:
                print("\nCookies information:")
                raw_cookies = response.headers['Set-Cookie']
                cookies = http.cookies.SimpleCookie(raw_cookies)
                for key, value in cookies.items():
                    print("Name: " + key)
                    print("Valid until: " + value['expires'])
            else:
                print("No cookies found")
    except:
        print('error opening', url)