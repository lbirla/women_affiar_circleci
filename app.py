from flask import Flask, render_template, request
from flask_cors import cross_origin
import joblib
import logging
from sklearn.linear_model import LogisticRegression
logging.basicConfig(filename='logist.log',level=logging.DEBUG,format='%(asctime)s %(levelname)s %(message)s')

app=Flask(__name__)#initializing a flask app

@app.route('/',methods=['GET'])
@cross_origin()
def homePage():
    return render_template('index.html')

@app.route('/classification',methods=['POST','GET'])
@cross_origin()
def classification():
    if request.method == "POST":
        try:
            logging.info('Take input from user')
            AGE = float(request.form['age'])
            yrs_married=float(request.form['yrs_married'])
            children=float(request.form['children'])
            Rate_marriage = request.form['rate_marriage']
            if Rate_marriage == 'Very Poor':
                rat_mary_VP=1
                rat_mary_P=rat_mary_A=rat_mary_G=rat_mary_VG=0
            elif Rate_marriage=='Poor':
                rat_mary_P=1
                rat_mary_VP=rat_mary_A=rat_mary_G=rat_mary_VG=0
            elif Rate_marriage=='Average':
                rat_mary_A=1
                rat_mary_VP=rat_mary_P=rat_mary_G=rat_mary_VG=0
            elif Rate_marriage=='Good':
                rat_mary_G=1
                rat_mary_VP=rat_mary_A=rat_mary_P=rat_mary_VG=0
            else:
                rat_mary_VG=1
                rat_mary_VP=rat_mary_A=rat_mary_G=rat_mary_P=0

            religious = request.form['religious']
            if religious=='Not religious':
                rel_not=1
                rel_low=rel_ava=rel_good=rel_strong=0
            elif religious=='Low':
                rel_low = 1
                rel_not = rel_ava = rel_good = rel_strong = 0
            elif religious=='Average':
                rel_not = 0
                rel_ava=1
                rel_low = rel_good = rel_strong = 0
            elif religious=='Good':
                rel_not = 0
                rel_ava = 0
                rel_good=1
                rel_low  = rel_strong = 0
            else:
                rel_strong = 1
                rel_not = rel_ava = rel_good = rel_low =0


            Education_level = request.form['Education']

            if Education_level=="Grade School":
                edu_level_9=1
                edu_level_12=edu_level_14=edu_level_16=edu_level_17=edu_level_20=0
            elif Education_level=='High School':
                edu_level_12 = 1
                edu_level_9 = edu_level_14 = edu_level_16 = edu_level_17= edu_level_20 = 0
            elif Education_level=='Some College':
                edu_level_14 = 1
                edu_level_12 = edu_level_9 = edu_level_16 = edu_level_17=edu_level_20 = 0
            elif Education_level=='College Graduate':
                edu_level_16 = 1
                edu_level_12 = edu_level_14 = edu_level_9 = edu_level_17=edu_level_20 = 0
            elif Education_level=='Some Graduate':
                edu_level_17 = 1
                edu_level_12 = edu_level_14 = edu_level_16 = edu_level_9=edu_level_20 = 0
            else:
                edu_level_20 = 1
                edu_level_12 = edu_level_14 = edu_level_16 = edu_level_17= edu_level_9 = 0

            is_occupatoon_woman= (request.form['occupation_woman'])
            if is_occupatoon_woman=='student':
                occ_1=1
                occ_2=occ_3=occ_4=occ_5=0
            elif is_occupatoon_woman=='unskilled':
                occ_2 = 1
                occ_1 = occ_3 = occ_4 = occ_5 = 0
            elif is_occupatoon_woman=='skilled':
                occ_3 = 1
                occ_2 = occ_4 = occ_1 = occ_5 = 0

            elif is_occupatoon_woman=='business':
                occ_4 = 1
                occ_2 = occ_3 = occ_1 = occ_5 = 0
            else:
                occ_5=1
                occ_2 = occ_3 = occ_1 = occ_4 = 0
            is_occupatoon_husb = request.form['occupation_husb']
            if is_occupatoon_husb == 'student':
                occ_husb_1 = 1
                occ_husb_2 = occ_husb_3 = occ_husb_4 = occ_husb_5 = 0
            elif is_occupatoon_husb == 'unskilled':
                occ_husb_2 = 1
                occ_husb_1 = occ_husb_3 = occ_husb_4 = occ_husb_5 = 0
            elif is_occupatoon_husb == 'skilled':
                occ_husb_3 = 1
                occ_husb_2 = occ_husb_1 = occ_husb_4 = occ_husb_5 = 0
            elif is_occupatoon_husb == 'business':
                occ_husb_4 = 1
                occ_husb_2 = occ_husb_1 = occ_husb_3 = occ_husb_5 = 0
            else:
                occ_husb_5 = 1
                occ_husb_2 = occ_husb_1 = occ_husb_4 = occ_husb_3 = 0
            logging.info('All inputs are taken successfully')
            filename='final_logistic_model.joblib'
            load_model=joblib.load(open(filename,'rb'))
            logging.info('loading of model successful')
            print(type(occ_1),occ_1)
            print(type(occ_2),occ_2)
            print(type(occ_3),occ_3)
            print(type(occ_4),occ_4)
            print(type(occ_5),occ_5)
            print(type(AGE),AGE)
            print(type(children),children)
            print(type(occ_husb_1),occ_husb_1)
            print(type(occ_husb_2),occ_husb_2)
            print(type(occ_husb_3),occ_husb_3)
            print(type(occ_husb_4),occ_husb_4)
            print(type(occ_husb_5),occ_husb_5)
            print(type(yrs_married),yrs_married)
            print(type(Rate_marriage),Rate_marriage)
            print(type(religious),religious)
            print(type(Education_level),Education_level)
            classification=load_model.predict([[occ_1,occ_2,occ_3,occ_4,
                                                occ_5,AGE,children,occ_husb_1,
                                                occ_husb_2,occ_husb_3,occ_husb_4,occ_husb_5,
                                                yrs_married, rat_mary_VP,rat_mary_P,rat_mary_A,rat_mary_G,rat_mary_VG,
                                                rel_strong,rel_not , rel_ava , rel_good,
                                               edu_level_9,edu_level_12,edu_level_14,edu_level_16,edu_level_17,edu_level_20
                                                ]])
            print('class: ',classification[0])
            if classification[0]==1:
                affair = "Affair : Yes"
            else:
                affair = "Affair: NO"
            return render_template('result.html',affair=affair)

        except Exception as e:
            print('The Exception message is:', e)
            return 'something is wrong'
    else:
        return render_template('indext.html')



if __name__=='__main__':
    app.run(debug=True)

