#author: @noamorama (noamrubin.me)

#Pull in CGQ and CGA files, correspond Q and As, and random ask questions and match them to answers

from flask import Flask, request, render_template
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
    if num > 130:
		num = 130
    pairsToAsk = random.sample(pairs,num)
    pairsToAsk = cleanPairs(pairsToAsk)
    #~ pairsToAsk = [(to_unicode_or_bust(item[0]),to_unicode_or_bust(item[1])) for item in pairsToAsk] #convert questions to unicode for HTML
    return render_template('answer.html',questions=pairsToAsk)
    #~ answer = """<form method="POST" action="showAnswer()">"""
    #~ i = 1
    #~ for pair in pairsToAsk:
        #~ answer += waitForAnswer(pair, i)
        #~ i += 1
    #~ return answer + '</form>'
 
def to_unicode_or_bust(obj, encoding='utf-8'):
     if isinstance(obj, basestring):
         if not isinstance(obj, unicode):
             obj = unicode(obj, encoding)
     return obj
  
def cleanPairs(pairsToAsk):
	result = []
	index = 0
	for q,a in pairsToAsk:
		try:
			q = unicode(q)
			a = unicode(a)
		except:
			continue
		result.append((q,a,'q'+str(index),'a'+str(index)))
		index += 1
	result.reverse()
	return result
		
		

def waitForAnswer(pair, i):
    question = 'Question: %s \n' %pair[0]
    answer = 'Answer: %s \n' %pair[1]
    return """%s<br />
    <input type="text" name="answer" /><!--SOME KIND OF JS HERE THAT CHANGES THE DISPLAY ATTRIBUTE OF ANSWER FROM HIDDEN
    TO REGULAR WHEN THE USER PRESSES SUBMIT-->
    <input type="submit" value="Submit" />
    <div class="answer" id="%f" style="display:none;">
    %s
    </div><br />
    """ %(question, i, answer)
    
#~ def waitForAnswer2(pairsToAsk):
	#~ return render_template('answer.html',questions=pairsToAsk)
    
if __name__ == '__main__':
    port = int(os.environ.get('PORT',29348))
    app.run(host='0.0.0.0',port=port,debug=True)
