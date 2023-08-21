
from app import app
app.secret_key = "keep it secret, keep it safe"

from app.controllers.surveys import *

if __name__ == "__main__":
    app.run(debug=True)