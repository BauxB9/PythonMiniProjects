#Bou Haidara	
#bhaidara@uncc.edu
#Assignment2

#NOTES for the code
#percentages of sequences in the whole file 
#you only need the sequences, getting the records and percentages for them in an dictionary and that gives counts
#Part1
#use gunzip to unzip a file
#Mdomestica_491_v1.1.cds_primaryTranscriptOnly.fa.gz
#2 dictionaries and an empty list
#Build a function that takes a record from your FASTA file as an argument,
#returns a count of each amino acid coded for by the codons of the sequence. 
#parallel dictionary scenario
#you only need the sequences, getting the records and percentages for them in an dictionary and that gives counts
#haveing 2 dictionarys that gives a count which increase the amount of times. the seq is predetermined and how many times seen in that position
#codon used for this basises
#freq is codon /totoal
#hard code selection for the options that can be used
#Part2
#what AA going to find the codon <---#if statement and loop
#.index() to find the position of the codon or loop through with enumorate and the number within the index but getting the list first


#Dictionary for the codons

aa_dict = {'Met':['ATG'], 'Phe':['TTT', 'TTC'], 'Leu':['TTA', 'TTG', 'CTT', 'CTC', 
'CTA', 'CTG'], 'Cys':['TGT', 'TGC'], 'Tyr':['TAC', 'TAT'], 'Trp':['TGG'], 'Pro':
['CCT', 'CCC', 'CCA', 'CCG'], 'His':['CAT', 'CAC'], 
'Gln':['CAA', 'CAG'], 'Arg':['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'], 'Ile':
['ATT', 'ATC', 'ATA'], 'Thr':['ACT', 'ACC', 'ACA', 'ACG'], 
'Asn':['AAT', 'AAC'], 'Lys':['AAA', 'AAG'], 'Ser':['AGT', 'AGC', 'TCT', 'TCC', 
'TCA', 'TCG'], 'Val':['GTT', 'GTC', 'GTA', 'GTG'], 
'Ala':['GCT', 'GCC', 'GCA', 'GCG'], 'Asp':['GAT', 'GAC'], 'Glu':['GAA', 'GAG'], 
'Gly':['GGT', 'GGC', 'GGA', 'GGG'], '*':['TAA','TAG','TGA']}


#2nd Dictionary 

aa_dictCount = {'Met':{'ATG':0}, 'Phe':{'TTT':0, 'TTC':0}, 'Leu':{'TTA':0, 'TTG':0, 'CTT':0, 'CTC':0, 'CTA':0, 'CTG':0}, 'Cys':{'TGT':0, 'TGC':0}, 'Tyr':{'TAC':0, 'TAT':0}, 'Trp':{'TGG':0}, 'Pro':{'CCT':0, 'CCC':0, 'CCA':0, 'CCG':0}, 'His':{'CAT':0, 'CAC':0}, 
'Gln':{'CAA':0, 'CAG':0}, 'Arg':{'CGT':0, 'CGC':0, 'CGA':0, 'CGG':0, 'AGA':0, 'AGG':0}, 'Ile':{'ATT':0, 'ATC':0, 'ATA':0}, 'Thr':{'ACT':0, 'ACC':0, 'ACA':0, 'ACG':0}, 
'Asn':{'AAT':0, 'AAC':0}, 'Lys':{'AAA':0, 'AAG':0}, 'Ser':{'AGT':0, 'AGC':0, 'TCT':0, 'TCC':0, 'TCA':0, 'TCG':0}, 'Val':{'GTT':0, 'GTC':0, 'GTA':0, 'GTG':0}, 
'Ala':{'GCT':0, 'GCC':0, 'GCA':0, 'GCG':0}, 'Asp':{'GAT':0, 'GAC':0}, 'Glu':{'GAA':0, 'GAG':0}, 'Gly':{'GGT':0, 'GGC':0, 'GGA':0, 'GGG':0}, '*':{'TAA':0,'TAG':0,'TGA':0}}




#Part1
#Keep in mind that because these records are not necessarily in the proper reading frame, 
#so the user should be prompted to select a reading frame (0, +1, +2).
#The presentation of your results by your main function, making sure they are clear and readable.

def count_codon(FASTA, counts, frame):
	for key in aa_dict:
		#The key in the first dictionary is set to 0
		counts[key] = 0
		# loop through the file and pair the codon bases
	for i in range(0+frame, len(FASTA), 3): 
		start = i
		end = i + 3
		codon = FASTA[start:end]
	for aa, codons in aa_dict.items():
		if codon in codons:
			if aa in counts.keys():
				counts[aa] += 1



#This funciton uses the second dictionary
def aa_condons(FASTA, counts):   
	for i in range(0, len(FASTA), 3):
		start = i
		end = i + 3
		codon = FASTA[start:end]
		for aa, codon in aa_dictCount.items():   
			if codons in codon.keys():
				if aa in counts.keys(): 
					aa_dictCount[aa][codon]+=1  
				else:
					aa_dictCount[aa][codon]=1  

		return aa_dictCount

#global count
#Part2
# This is the first time you'll be using a full dataset.  Expect your numbers to get big
# You will probably want to use the dictionary of amino acids and codons from Assignment 2 Starter code for this
# We're looking for the frequency of the occurrence of a codon relative to other codons of the same amino acid.  
#As such, you will have multiple counts to keep track of.  
#Think about how you want to keep track of these counts, and what combinations of dictionaries, lists, and tuples are best suited to this task. 
#Plan this BEFORE you start.
# Just as important as it is to get these counts and generate a result, you must also consider how best to present these results. 
#Your code should generate a human-readable file that shows your frequencies in a way that is verbose and makes sense.  
#Your success in presenting the results will be considered just as important as how you arrived to them.

def main():
#another dictionary for the options needed
	codonCounts = {}
	for keys in aa_dict:
		codonCounts[keys] = 0
	with open("Mdomestica_491_v1.1.cds_primaryTranscriptOnly.fa",'r') as fh:   
		seqLst= ""
		headLst = ""
		print(headLst)
		for line in fh:
			if line.startswith(">"):
				headLst += line.rstrip()
			else:
				seqLst += line.rstrip()
	print("What would you like to do?")

	while 1:
		try:
			user = int(input("File options located below:\n\t1 The total count of codons\n\t2 The frequency of each codon set\n\t3 Completion of sequences\nWhich option (numbers listed above onaly): "))
			if user < 1:
				raise Exception
			elif user > 3:
				raise Exception
			else:
				break
		except Exception:
			print("Please enter the correct number choice")
	


	if user == 1:
		while 1:
			try:

				frame = int(input("Which frame would you like to view 0, 1, or 2:  "))
				if frame < 0:
					raise Exception
				if frame > 2:
					raise Exception
				else:
					break
			except Exception:
				print("You must choose frame of 0 or 1 or 2")

#using the dicitionary for the user to see the count of the codons in a new file
		count_codon(seqLst,count,frame)
		with open("codonCounting.txt", "w") as codonCounts:
			for aa, codonCounts in count.items():
				print(aa, codonCounts)
				codonCounts.write(f"\n\tThe amino acid: {aa} and the count: {codonCounts}")
			codonCounts.colse()
			print(f"\n\t{codonCounts} file has been updated")
	

	elif user == 2:
		newAADict = aa_condons(seqLst, counts)
		total = 0
		for key,value in newAADict.items():
			for codon,count in value.items():
				total += count
				newAADict[key][codon] = round((count/total) ,2)  
			codonFreq = open("FrequencyOfCondon.txt","w")
			codonFreq.write("\nCodon usage bias in the sequence")
			for key, value in newAADict.items():
				for codon, count in value.items():
					codonFreq.write(f"\nListed below are the current Frequency for the codons:\n\tFrequncy for amino acid: {key}\n\tFrequncy for codons: {codon}\n\t Frequncy for relative frequency: {count}" )
	else:
		exit()
if __name__ == "__main__":
	main()
