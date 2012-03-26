#author: @noamorama (noamrubin.me)

#Pull in CGQ and CGA files, correspond Q and As, and random ask questions and match them to answers

from flask import Flask, request
import os
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

@app.route('/', methods=['GET','POST'])
def getNum():
    """
    This does the work. It takes the number of questions you want, and
    randomly selects that many question and answer pairs and asks you them.
    """
    return """Welcome to the CGQ Game. How many questions would you like?<br />
    <form method="POST" action="/number">
    <input type="text" name="num" />
    <input type="submit" value="Submit" />
    </form>
    """

@app.route('/number', methods=['GET','POST'])
def viewNum():
    if request.method=='POST':
        num=request.form['num']
        return askQuestion(int(num))

def askQuestion(num):
    import random
    pairs = QAPairs()
    pairsToAsk = random.sample(pairs,num)
    answer = """<form method="POST" action="showAnswer()">"""
    i = 1
    for pair in pairsToAsk:
        answer += waitForAnswer(pair, i)
        i += 1
        #~ answer = raw_input('QUESTION: ' + pair[0] + '\n\n')
        #~ print '\nANSWER: ', pair[1], '\n\n'
    return answer + '</form>'

def waitForAnswer(pair, i):
    question = 'Question: %s \n' %pair[0]
    answer = 'Answer: %s \n' %pair[1]
    return """%s<br />
    <input type="text" name="answer" /><!--SOME KIND OF JS HERE THAT CHANGES THE DISPLAY ATTRIBUTE OF ANSWER FROM HIDDEN
    TO REGULAR WHEN THE USER PRESSES SUBMIT-->
    <input type="submit" value="Submit" />
    <div class="an
        swer" id="%f" style="display:none;">
    %s
    </div><br />
    """ %(question, i, answer)
    
if __name__ == '__main__':
    port = int(os.environ.get('PORT',29348))
    app.run(host='0.0.0.0',port=port,debug=True)
