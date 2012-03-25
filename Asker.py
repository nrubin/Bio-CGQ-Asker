#Pull in CGQ and CGA files, correspond Q and As, and random ask questions and match them to answers

def openQuestions():
    f = open('CGQ.txt')
    text = f.read()
    f.close()
    return text.split('\n')
    
def openAnswers():    
    f = open('CGA.txt')
    text = f.read()
    f.close()
    return text.split('\n')
    
def QAPairs():
    qs = openQuestions()
    ans = openAnswers()
    return zip(qs,ans)
    
def askQuestion(num):
    import random
    pairs = QAPairs()
    pairsToAsk = random.sample(pairs,num)
    for pair in pairsToAsk:
        answer = raw_input('QUESTION: ' + pair[0] + '\n\n')
        print '\nANSWER: ', pair[1], '\n\n'
    
if __name__ == '__main__':
    num = raw_input('Welcome to the CGQ game. How many questions would you like?\n')
    askQuestion(int(num))
