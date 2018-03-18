import os
from   flask import Flask
from   flask import send_from_directory
application = Flask(__name__)
            
@application.route("/")
def blog():
    return send_from_directory(os.path.join(application.root_path, 'static'),'blog.html')

@application.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(application.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    application.run(host='0.0.0.0', port=port)
'bye'
