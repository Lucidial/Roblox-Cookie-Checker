import requests

logo = """
█       ▄   ▄█▄    ▄█ ██▄   ▄█ ██   █     
█        █  █▀ ▀▄  ██ █  █  ██ █ █  █     
█     █   █ █   ▀  ██ █   █ ██ █▄▄█ █     
███▄  █   █ █▄  ▄▀ ▐█ █  █  ▐█ █  █ ███▄  
    ▀ █▄ ▄█ ▀███▀   ▐ ███▀   ▐    █     ▀ 
       ▀▀▀                       █        
                                ▀
"""

def check_roblox_cookie(cookie):
    headers = {
        'Cookie': '.ROBLOSECURITY=' + cookie
    }
    response = requests.get('https://auth.roblox.com/v1/auth/metadata', headers=headers)

    if response.status_code == 200:
        return True
    elif response.status_code == 403:
        return False
    else:
        raise Exception('An error occurred while checking the cookie.')

print(logo)

# Ask user for the .ROBLOSECURITY cookie
cookie = input('Enter your .ROBLOSECURITY cookie: ')

# Check the validity of the cookie
valid = check_roblox_cookie(cookie)

# Print the result
if valid:
    print('The cookie is valid.')
else:
    print('The cookie is invalid.')
