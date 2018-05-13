import xml.etree.ElementTree as ET
from collections import Counter
import argparse

aparser = argparse.ArgumentParser(description='Evaluation of prediction')
aparser.add_argument('output', help='Output file')
args = aparser.parse_args()
goldstandard = []
predict = []

def evaluate(path):
	xmlcorpus = ET.parse(path)
	docs = xmlcorpus.getroot().getchildren()
	#print(docs)
	for i in range(len(docs)):
		doc = docs[i]
		fake = 0 
		goldstandard.append(doc.get('class'))
		predict.append(doc.get('classpredict'))
	print(len(goldstandard), len(predict))
	cnt_gold = Counter()
	cnt_predict = Counter()
	T_fake, T_trusted, T_parodic =0,0,0
	fake, trusted, parodic = 0,0,0
	for i in range(len(goldstandard)):
		cnt_gold[goldstandard[i]] +=1 
		cnt_predict[predict[i]] +=1 
		if goldstandard[i] == predict[i]:
			if goldstandard[i] == 'fake':
				T_fake+=1
			if goldstandard[i] == 'trusted':
				T_trusted+=1
			if goldstandard[i] == 'parodic':
				T_parodic+=1
		if predict[i] == 'fake':fake+=1
		if predict[i] == 'trusted':trusted+=1
		if predict[i] == 'parodic':parodic+=1
	#print(cnt_gold, cnt_predict)
	print('VP fake:'+str(T_fake), ' VP trusted:'+str(T_trusted), ' VP parodic:'+str(T_parodic))
	print('fake trouvé:'+str(fake), ' trusted trouvé:'+str(trusted), ' parodic trouvé:'+str(parodic))
	print('fake total:'+str(cnt_gold['fake']), ' trusted total:'+str(trusted), ' parodic total:'+str(parodic))

	file = open('table.txt', 'w', encoding ='utf-8')
	file.write('\tPrécision\tRappel\tF-mesure\t\n')
	file.write('fake\t%.2f' % (T_fake/fake)+'\t%.2f' % (T_fake/cnt_gold['fake'])+'\t%.2f' %((T_fake/fake)*(T_fake/cnt_gold['fake'])*2/((T_fake/fake)+(T_fake/cnt_gold['fake'])))+'\n')
	file.write('trusted\t%.2f' % (T_trusted/trusted)+'\t%.2f' % (T_trusted/cnt_gold['trusted'])+'\t%.2f' %((T_trusted/trusted)*(T_trusted/cnt_gold['trusted'])*2/((T_trusted/trusted)+(T_trusted/cnt_gold['trusted'])))+'\n')
	file.write('parodic\t%.2f' % (T_parodic/parodic)+'\t%.2f' % (T_parodic/cnt_gold['parodic'])+'\t%.2f' %((T_parodic/parodic)*(T_parodic/cnt_gold['parodic'])*2/((T_parodic/trusted)+(T_trusted/cnt_gold['parodic'])))+'\n')

	
evaluate(args.output)