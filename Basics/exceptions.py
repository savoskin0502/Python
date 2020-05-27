import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        response = requests.get(url, timeout=1)
        response.raise_for_status()
    except requests.Timeout:
        print("timeout", url)
    except requests.HTTPError as err:
        code = err.response.status_code
        print("url: {0}, code: {1}".format(url, code))
    except requests.RequestException:
        print("download error", url)
    else:
        print(response.content)