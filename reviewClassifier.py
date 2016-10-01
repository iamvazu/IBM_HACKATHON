import json
>>> from watson_developer_cloud import ToneAnalyzerV3
>>> 
>>> 
>>> tone_analyzer = ToneAnalyzerV3(username='8c82d78a-0598-4abb-9270-b5e53f62031d', password='Cgo5uTaoH4wH',version='2016-05-19')
>>> data = json.dumps(tone_analyzer.tone(text='A word is dead when it is said, some say. Emily Dickinson'), indent=2)
>>> customer_sentiscore=[]
>>> customer_sentiscore.append(temp1['document_tone']['tone_categories'][0]['tones'][0]['score'])
>>> customer_sentiscore.append(temp1['document_tone']['tone_categories'][0]['tones'][1]['score'])
>>> customer_sentiscore.append(temp1['document_tone']['tone_categories'][0]['tones'][2]['score'])
>>> customer_sentiscore.append(temp1['document_tone']['tone_categories'][0]['tones'][3]['score'])
>>> customer_sentiscore.append(temp1['document_tone']['tone_categories'][0]['tones'][4]['score'])

>>> if(customer_sentiscore[0]>0.4 and customer_sentiscore[1]>0.4):
...     print("Very Bad product!")
>>> if(customer_sentiscore[1]>0.4 and customer_sentiscore[4]>0.4):
...     print("Bad product!")
>>> if(customer_sentiscore[0]>0.4 and customer_sentiscore[2]>0.4):
...     print("Couldn't generate appropiate reviews for the particular product!")
>>> if(customer_sentiscore[2]>0.4 and customer_sentiscore[4]>0.4):
...     print("Bad product!")

