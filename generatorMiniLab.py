#Bou Haidara
#Bhaidara@uncc.edu


def fastaParser():
    with open("seqs.fa") as fh:
        
        header = ""
        sequence = ""
        for line in fh:

            line = line.strip()
            #this would be for the header
            if line.startswith(">"): 
                if sequence != "":
                    yield(header,sequence) 
                    sequence = ""
                header = line.lstrip(">")

            else:
                sequence += line 
        yield(header,sequence) 
