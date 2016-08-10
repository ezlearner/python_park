from flask import Flask

app=Flask(__name__)

@app.route('/<rtpath>/')
def test_page(rtpath):
   return "This is a {} page".format(rtpath)

if __name__ =="__main__":
    app.run()