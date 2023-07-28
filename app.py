## Create a Simple Flask Application
from flask import Flask,render_template,request,redirect,url_for


app= Flask(__name__)

@app.route("/")
def home():
    return "<p>Hello World</p>"


@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    return f"the score is {score}"

@app.route('/calculate',methods=['POST','GET'])
def calculate():
    if request.method=='GET':
        return render_template('calculate.html')
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        english=float(request.form['english'])
        average_marks=(maths+science+english)/3
        result="" 
        if average_marks>=50:
            result="success"
        else:
            result="fail"

        #return redirect(url_for(result,score=average_marks))


        return render_template('result.html',results=average_marks)



    


if __name__=='__main__':
    app.run()