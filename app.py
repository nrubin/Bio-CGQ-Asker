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
    return """
    <head>
    <script type="text/javascript">
    function checkNumber(){
    number = document.getElementById("num").value;
    if (!isNaN(parseInt(number)) && isFinite(number) && number > 0){
    numQuestions.submit()
    }else{
    alert("Please enter an integer number of questions greater than 0")
    return false;
    }
    }
    </script>
    </head>
   
    
    Welcome to the CGQ Game. How many questions would you like?<br />
    <form name="numQuestions" method="POST" action="/questions">
    <input type="text" name="num" id="num" />
    <input type="submit" value="Submit" onclick="checkNumber('numQuestions');return false;" />
    </form>
    """

@app.route('/questions', methods=['GET','POST'])
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
    return render_template('answer.html',total=len(pairsToAsk),questions=pairsToAsk)
  
def cleanPairs(pairsToAsk):
	result = []
	index = 0
	for q,a in pairsToAsk:
		try:
			q = unicode(q)
			a = unicode(a)
		except:
			continue
		toAppend = (q,a,'q'+str(index),'a'+str(index))
		print toAppend
		result.append(toAppend)
		index += 1
	#~ result.reverse()
	return result

    
if __name__ == '__main__':
    port = int(os.environ.get('PORT',29348))
    app.run(host='0.0.0.0',port=port,debug=True)
