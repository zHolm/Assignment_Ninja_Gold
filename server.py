from flask import Flask, render_template, request, redirect, session
import random
import datetime

app = Flask(__name__)
app.secret_key ="''asd';bjjflkhvkhh443468g'"


@app.route("/")
def hello():
    #initialize  variables
    if 'money_arr' in session:
        pass
    else:
        session['money_arr'] = []
        session['money'] = 0
        print('no money key')

    if 'choice_arr' in session:
        pass 
    else:
        session['choice_arr'] = []

    if 'date_time_arr' in session:
        pass
    else:
        session['date_time_arr'] = []
    
    if 'increment' in session:
        pass
    else:
        session['increment'] = []

        


     

    print(session['money'])
    
    
    return render_template("/index.html", increment= session['increment'], money= session['money'], money_arr=session['money_arr'], choice_arr= session['choice_arr'], date_time_arr= session['date_time_arr'])

@app.route("/process_money", methods=['POST'])
def money():
    #add random value of money depending on choice
    if request.form['choice'] == 'farm':
        increment = random.randint(10,20)
        money = session['money'] +increment
    elif request.form['choice'] =='cave':
        increment = random.randint(5,10)
        money = session['money'] +random.randint(5,10)
    elif request.form['choice'] =='house':
        increment = random.randint(2,5)
        money = session['money'] +increment
    elif request.form['choice'] =='casino':
        increment = random.randint(-50,50)
        money = session['money'] +increment

    #set total value of money for the session
    session['money'] = money
    

    #store each transaction value in session
    temp_arr = session['increment']
    temp_arr.append(increment)
    session['increment'] = temp_arr
    
    #store an array of choices in session
    temp_arr = session['choice_arr']
    temp_arr.append(request.form['choice'])
    session['choice_arr'] =temp_arr

    #Store an array of payouts in session
    temp_arr = session['money_arr']
    temp_arr.append(session['money'])
    session['money_arr'] =temp_arr

    #Store an array of date/times choices where made in session
    now = datetime.datetime.now()
    temp_arr = session['date_time_arr']
    temp_arr.append(now)
    session['date_time_arr'] =temp_arr
    
    #print arrays
    print(session['date_time_arr'] )
    print(session['money_arr'] )
    print(session['choice_arr'])

    return redirect("/")

@app.route("/destroy_session")
def reset():
    session.clear()		# clears all keys
    # session.pop('money_arr', None)
    # session.pop('choice_arr', None)
    # session.pop('date_time_arr', None)
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)

