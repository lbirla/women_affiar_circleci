from flask import Flask, render_template, request
from flask_cors import cross_origin
import pickle
import logging
test=Flask(__name__)#initializing a flask app

@test.route('/',methods=['GET'])
@cross_origin()
def homePage():
    return render_template('testindex.html')

@test.route('/classification',methods=['POST','GET'])
@cross_origin()
def classification():
    if request.method == "POST":
        try:
            AGE = float(request.form['AGE'])
            yrs_married= float(request.form['yrs_married'])
            total_age=AGE+yrs_married
            return render_template('result.html',total_age=total_age)
        except Exception as e:
            print('The Exception message is:', e)
            return 'something is wrong'




if __name__=='__main__':
    test.run(debug=True)
