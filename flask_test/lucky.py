from flask import Flask
from flask import render_template
from random import randint

app=Flask(__name__)

@app.route('/')
def lucky():
  luck_num=randint(1,100)
  return render_template('lucky.html',lno=luck_num)
  
if __name__ == '__main__':
   app.run()  