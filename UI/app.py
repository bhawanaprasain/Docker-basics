from flask import Flask ,render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    print("Docker has started..........")
    return 'Intro to docker '

@app.route('/about')
def about_me():
    return render_template('./about.html')

if __name__ == '__main__':
   app.run(host='0.0.0.0')