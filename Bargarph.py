import matplotlib.pyplot as Mplt

crime = ['Antisocial behaviour', 'Burglary', 'Criminal Damage and Arson', 'Drugs']
amount = [200, 50, 150, 75]

Mplt.barh(crime, amount, height=0.5, color=['blue', 'green'])

Mplt.ylabel('Crime')
Mplt.xlabel('Amount')

Mplt.title('Crime amounts')

Mplt.show()
