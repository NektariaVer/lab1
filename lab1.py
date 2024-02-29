import requests
import http.cookies

while True:
    url = input('URL:')
    if url == '': break
    if not url.startswith('http'):
        url = 'http://'+ url
    try:
        with requests.get(url) as response:
            print("\nRESPONSE STATUS: ", response.status_code)
        print("RESPONSE HEADER")
        for key, value in response.headers.items():
            print("{:30s} {}".format(key, value))
        if 'Server' in response.headers:
            print("\n\nWeb server: " + response.headers['Server'])
        else:
            print("\nWeb server not found.")
    except:
        print('error opening', url)

    if 'Set-Cookie' in response.headers:
        print("\nThis page uses cookies.")

        raw_cookies = response.headers['Set-Cookie']
        cookies = http.cookies.SimpleCookie(raw_cookies)

        print("\nCookies information:")
        for key, morsel in cookies.items():
            print("Name: " + key)
            print("Valid until: " + morsel['expires'])
            print()
    else:
        print("\nThis page does not use cookies.")