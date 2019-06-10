from flask import Flask, render_template, request, redirect, session
import random
app = Flask (__name__)
app.secret_key = 'secret key'

@app.route('/')
def index():
    if not 'gold' in session:
        session['gold'] = 0

    if not 'activities_list' in session:
        session['activities_list'] = []

    print('_' *120)
    print(session['gold'])
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    session['activities_list'] = []
    if 'activities' in session:
        activities = session['activities']
    else: 
        activities = ""
    
    if 'gold' in session:
        gold = session['gold']
    else:
        gold = 0
    
    income = 0
    income_on_template =""
    
    if request.form['location'] == 'farm':
        income = random.randint(10,20)
        income_on_template = f"Earned {income} golds from the farm!"
    elif request.form['location'] == 'cave':
        income = random.randint(5,10)
        income_on_template = f"Earned {income} golds from the cave!"
    elif request.form['location'] == 'house':
        income = random.randint(2,5)
        income_on_template = f"Earned {income} golds from the house!"
    elif request.form['location'] == 'casino':
        income = random.randint(-50,50)
        if income < 0:
            income_on_template = f"Entered a casino and lost {income} golds... Ouch.."
        if income > 0:
            income_on_template = f"Entered a casino and won {income} golds!!! Woopie!!"
    
    
    gold = gold + income
    session['gold'] = gold
    session['activities'] = activities + income_on_template
    session['activities_list'].append(session['activities'])



    print(session['activities_list'])
    print(session['activities'])
    print(income_on_template)
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)