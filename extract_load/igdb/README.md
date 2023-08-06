# IGDB.com: Internet Game Database

## Setup

Postman collection for API development can be found here: https://www.postman.com/brentbrewington/workspace/github-com-bbrewington-gaming-data/overview
(this is what the file `postman_env_twitch_and_igdb.json` is for)

Run the code below (Mac/Linux: use Terminal, Windows: use git bash).  This will create a [virtual environment](https://docs.python.org/3/library/venv.html), which lets us isolate Python packages we're using.  Once you run this, you should see `(.venv)` in the terminal and a `.gitignore` file in `/extract_load/igdb`

When this virtual environment is activated in the terminal, when you run Python, it uses the Python binary/executable within the `.venv` folder instead of the one on your system - and it uses the folder `.venv/lib` for packages.  It's a scrappy/quick way to try to prevent this situation: https://xkcd.com/1987/

```bash
cd "$(git rev-parse --show-toplevel)"
source extract_load/igdb/setup.sh
```

## Authenticating to Twitch API

(this is copy+paste from [IGDB's Authentication instructions](https://api-docs.igdb.com/#authentication))

Make a POST request to https://id.twitch.tv/oauth2/token with the following query string parameters, substituting your Client ID and Client Secret accordingly.

```text
client_id=Client ID
client_secret=Client Secret
grant_type=client_credentials
```

Example
If your Client ID is `abcdefg12345` and your Client Secret is `hijklmn67890`, the whole url should look like the following.

POST: `https://id.twitch.tv/oauth2/token?client_id=abcdefg12345&client_secret=hijklmn67890&grant_type=client_credentials`
The response from this will be a json object containing the access token and the number of second until the token expires.


```json
{
  "access_token": "access12345token",
  "expires_in": 5587808,
  "token_type": "bearer"
}
```

Now, we can use this `access_token` value in our API calls to IGDB

## IGDB API

