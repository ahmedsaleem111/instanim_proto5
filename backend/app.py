from ...instanim import *


app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return render_template('index.html')