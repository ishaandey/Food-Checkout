from unsplash.api import Api
from unsplash.auth import Auth

client_id = "NPmSc3FjJfHkYFq5idCJn99iao-5yNyViqO8upWtkiw"
client_secret = "1RTXdel6BrOpDr_wOWuaxwV4yQn9QC6BT8wP54KB07o"
redirect_uri = ""
code = ""

auth = Auth(client_id, client_secret, redirect_uri, code=code)
api = Api(auth)


