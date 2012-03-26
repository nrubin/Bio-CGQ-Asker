#author: @noamorama (noamrubin.me)

#Pull in CGQ and CGA files, correspond Q and As, and random ask questions and match them to answers

from flask import Flask
from flask import request
from wtforms import Form, validators, TextField
app = Flask(__name__)

def openQuestions():
    """
    Opens the file with questions in it
    """
    f = open('CGQ.txt')
    text = f.read()
    f.close()
    return text.split('\n')
    
def openAnswers():
    """
    Opens the file with answers in it
    """    
    f = open('CGA.txt')
    text = f.read()
    f.close()
    return text.split('\n')
    
def QAPairs():
    """
    Opens the question and answer files and zips the pairs together
    """
    qs = openQuestions()
    ans = openAnswers()
    return zip(qs,ans)

class StartForm(Form):
    """
    """
    num = TextField('Number of Questions', [validators.required(), validators.Length(min=1, max=3)])

@app.route('/', methods=['GET','POST'])
def getNum():
    """
    """
    form = Start(request.form)
    if request.method == 'POST' and form.validate():
        num = request.form['Number of Questions']
    return form

def askQuestion():
    """
    This does the work. It takes the number of questions you want, and
    randomly selects that many question and answer pairs and asks you them.
    """
    if request.method=='POST':
        num=request.form['Welcome to the CGQ Game. How many questions would you like?']
        
    else:
        import random
        pairs = QAPairs()
        pairsToAsk = random.sample(pairs,len(pairs))
        for pair in pairsToAsk:
            answer = raw_input('QUESTION: ' + pair[0] + '\n\n')
            print '\nANSWER: ', pair[1], '\n\n'
        
if __name__ == '__main__':
    app.run(debug=True)
