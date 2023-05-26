#Bou Haidara
#bhaidara@uncc.edu
#Dictionary Lab

headerLst = ['>seq1A', '>seq2A', '>seq3A', '>seq4A', '>seq5A', '>seq6A', '>seq7A', '>seq8A', '>seq9A', '>seq10A', '>seq11A', '>seq12A', '>seq13A', '>seq14A', '>seq15A', '>seq16A', '>seq17A', '>seq18A', '>seq19A', '>seq20A', '>seq21A', '>seq22A', '>seq23A', '>seq24A', '>seq25A']

seqLst = ['ATGTGCATTCAAGCTGTGACACTGAGATACTCAAAGTCTCTTAAGAAGCCACGATTGGCTATGTGTGCTTTGGTCTCTTTGAAGATGGATGCTGAGCTTTCAGACGGTCTCGCATGGGATTATCGCGCAGAAGCTATCATGCTCATGCGAACAATCGTAGGAGGAATCCCAGGACATACTAGAAAATCAAGGGGATATACGTCGCCATGCCCTATGGAGACTAAACTTATCTTAGGAGGTATTATCCCTGTTGTGAAGTTAGACTCACTCTTAAGATTGTTTAGGGATAGTACAGCCCCACTCCAAACTTTGAACGTTATTGTTGGTATTAGAGAAAGCGACGCAAAGGTTGAGGTCCGGCTTACCATACTTTCATTGAAAGCTAGTGATTTTCAGATCGCCTACACGACAGCGTCCAATGAGCATTCAGGAGGAACAAGTGACGTGTACCAGGCTGCTCCTTTCGGATCTACGATGAGACGAAGACGTTGTAGTGTAGACAGAGGAGCCAGCGCTACAGCATCCCCGCTATATTTCACTCCGGCGTATCGGTGTAGAGGACTTGGAGCACTCCGCATCCAGAATATCCCTGAATCTCGAGTACTTTCGACCACT', 'ATGACCGTGCCACCTATCAAGCTTGCAAAAGGCATTATCACCGTCTCAGATTGTGGGGTTAAATACGAGTACATGGTTAAAGACATTGGAAATGCCCCTACAGTTACTGCTTTTGGTAAGAACTCTCTAGATCGGACTATGAGTTTTCAGATCCTTGTAGGTCGAATCACTCGGCACCTTTTAGGATTCTTAGATTATGGTCCGACAGGTCTACATGAACACTCTCCATTTTGGGTGGGGGCTCCAGTTCAAGTTGCCGCGTTGCCTACTGAAGCAATATCTGGGAAAGAGCTAACCGCTTTGTTCGTTATCCGACCATCTAATCCAACCAAGCCACACCTTCATCGCTCTGCGGGTCCTGCTATTCCTGCTTGCTTGAGACCACACTATCATGTGGCACACCCCCTGTCGATGGCGTATTCTCACGAACTTAAATTTAAACGGATTATTATTGCTCCCCCGTCTAGGCCTCCGCGTGAACACACATATGACTCTATTTCCACTCTGCAGCCCTCTCTTGCTAGGTATCAGACTTTGGACGAGTGCCTAGAGGGAACCCTTGCTGGGCAAGATATCGCTGCGATCGGTCCTATAAGTCTGGTTCTCGGAGGGCACCAGATTTCAGCCAGACGCAAGCGTTCGGGCCTCCAACCAAGCGCTCCTAGACGGTATGCTACCACACTAACATGTCCAACTCCGAGTCTTTTGCGTGGAGATAAACATGGAGGTGAAAGTCAACTTGGAAGATACACACAAATCGCAGAACTATCCTATCCCTTACAAGCAGGGGTAGGTAGGAGAACAACGGCCGTGGCCGCAACGAGCTGTACTCGGATGTCTGGTCCTAGCGATTCTTGTGATCGTTTGATTCCAAAGCCTATGTTGAAATCTCAGTTGCTTGACGGAACCGCGCGTCGACAGGCCAATGCTCTTCATTCGCATTCGCCTCTTGCGCCTGCTTTGTCCCTTGCAAAAAAGAGTAACCCAAGCAGCCTTTACGTTCTATGTCTTATTCTGAGAAGTGGATCTAGTGCATCAGATCGTTTACGATTTGCCGCAATTGATGGTGCTACTGTCAATGCAAAAGTGAATGGAAAAAAGACG', 'ATGGGAGCGCTTCAAACACTTGGTCCCATGCTTTTGTCCAACCCTACCCTGCCTTCAAATCGTTTTACTAATGGGGAAGCAAAGCTTGGTTTGGTATACAGTAAACAGCATATCTGCCGTCCTGAATTCCATACTTATCCACTTAGGAAAAGAGCTGGTATGGCTTCTTTCTTGGCAGCGGAAATAGCTGCCGGTGCTGTCCTAGTTCATTCAGTTAATGTTGTTTCTTCTAGGACTGATAGGGTACTAACTAGAGATGAGGAAGTTGGTGATGAGGAGGAGATCAAGTGGGAATTATTATTCTCTTATTCACAACTCGCTGGTGGAAAATATAGGGTTTGTGCACCAAAAGCCTTGACACTTCCAGTTCCTATCTGGTTAACACTTGGTGTTTACCTCCATCTTGCACATATTAGGATGCCGCCTCATACCATCCGGTTGGAGCTCCATAGCCTCACAAAAGCCTCA', 'ATGGTTGGTATCAGGCAGGCTCATGACGAACAATGGGCTAGATATCTTCTTCAATGGAACCGACACGCCACCTCATGTGCGGCAAGACAAGCAAGATGCCAGGCGATCAGTTGGGACGCAACAGAAAGCTCATTGAGTGCGAGAGAAAACAGACGCAAAACCTTGCCATCTTGTTATTTTCAGAGAAAACGGACTGGTTGGGATAGTTTGGATAAGATCCATGCGCAGTTGCAGATGCTTGGGCATTGTGAGCCGCAAAAACATTTCGCCCCTCACCAAAGATCCTATGTCGTGCTTGTTAGTCGTGTCCCCTTCGGACGGCCTGTGTCTGATAAAGGATTACCAGGGCAAGTGTCCTTTGCTGATAAAGAGTTAATGACCCGATCGTCAATGCATTCTAGTCGACTCAATAAAGGGTGTACAGCAGCTTACGATGGCGGAGACTCAGGATCAGCAGGGACCATGGGTTTTACCAATGGTCTCGAGAGATCTCATGTTTTGGCTATGCCGAAAGACTCCTGCTACTCCATATATCCAGGAGATGTCCTCGAAACGTCTGTGTCGAAAGTCCGTACGAGAATTACTAGATCAGGATGCACACACCATTATCTATTGAGATCACCAGTAGCGCTAGCCGCTCAGGAA', 'ATGGATTTCATCAACACTCCTGGTGACCCAGTGATGCACACTACGATGCTAGAGCCATGTTTGTCTAATAACTATGTCGGTGTTGCGAGAAGACGGTTAGCTGCCTTCCAATTAGCTGTAACGGGAAATACGGGGGTTCGCCGTAACGGTGGAGATGTACCTTCACGTTCATCGGTGCGAAAGTGGAGAGTGGCTCATGCCGTTGGTGCGCAACTCCGTGTTAGTTTAGCTGCTATCGTTACTAAGCGAGTAAATGAAAAACACGATTTTAACGCTATCCGTCCAGCACGCGAGCACGACAGCAGAGTGGGTAATTCCTGCTTATTACCGTATATAACCCCTCACGAGAATCAGCTCGGAGCATTCTTTATTAGCTATCCTCATAAGGACCCAAATCAGAGGTTTAGACAGGAACTTGAACATTATGCACAAATGCTAGCTTTTCGAAACTCTACATCCTCCATTTGGTCAAGACTAGTTGACCCTGATGTTTCGATTGGTTATGATCATCCGGTGATGTGGTCTTGTCAACAAACCAACAGAGTCGCTTCAAAGGCTAGGGGAACATTCGGACGAAAAGGACATGTGCACGCTCTACGCCAAAGTTCGAAGTTGGCATACAGGGCGATCATTTGTGGTTGGATTGGTGTGGTTCATGCACTGCGTGAACAACAAGAGAACGAATGTTACCGTACTGGTTGTCTTGAAATCCCTCCCATGGCGTTTGTCGGTAGACAAAGATGCTCTGTGTGCTGCGCTCAGTCTGACCCTAGATACCGAGGTCGAATCCACATCTTCGATGTTTACAGGTCTAGACAGTACGGTCGGATCTTTCCATTGCCGCTGCTAGAAATTGCTCTTCCCACCGAGCATTGTCGTTCCGCTGCGCAACCGATTGATCTAATAGCGATGAACATTCTTACGTACGCAGTTTGTAGTCTTTTGCCGGGCTCCCGTCAACGGCAGGATTTTAGACATTCTTGGCCGGTAGATCTGTATAGTATTGCACCAGCCGCTGTTGGTTTTGCGGAGGTTAGGTTTTCTTTCTTACTATTCTTTACCACACCAGCTTCTAGGCCATCCGGCATTACTCTTTTCTCTAAGACGATGTATGAATCAAGA', 'ATGTGGGCCCCTGGACCACATGCAGATAGACGCAGGCAATCACTGCACGTGAGAGGGACCTTCACGGCAATTCATACGGTGACGTGTAAAACTGCCAGAGGAGACAGATCATTAATAAGAGAGAGGTCATGGCCGGCTTGGAAATTGTTAAGATGGAGGTACCGCCCTCGATCTTTTGGTAGGTCCTCTGTTTCCCTCCTTAACTCTATTATTGCTTGCTTCCTCCTGAGGCACGCTGAAACCTCTGCCCTCACGTTGAGCATTGGTAACAACTTAATGAAGATACATCTGTGTCATCCGTCACCAAGCCGTACCTGGGCGAAATGGACGCCTAGGTGGTTTTACTTTTGGCTCTTGAGCGCGGACAAACGGACTCCATGTAGTAGGCGTGTCCCGAGTAGAATTGGCGTTTCACCATTAGCAAAGTCTTCCAAGATTTACTGGCAAACAAAGGAGGAGGATAAGAAGCTTATCCAAATCAGTTTGAGAAGTTGGTTGTTCGAGATTCTGCAAGAGACAACGACCCACCAGGTGTTTTATACGATCTTTGATGTCCATACTTCCATGGGGCTCAAATTTCAATTCCATCAGACCGACAGCACATACAACTCTTGTGGAAAGCAGGGCATCCAGTGTCCATTTGTGTCAGGTTTGTCAAGTGTTATCGTTCCATGTCATTACAAATATGAATTGGGCACAAATGCAGAACGGAACCCAAGGTCAATCGTACCTGAACTAGCAACTGATTGTCACGACCTTCCAATGAGTATTCTGACCTCTTTCCTCGCTTTCTCA', 'ATGATTCTTAGTGCGCGAGCGACCTGTAAACAAATCTCTTATCGTCGAAACTGCCGTAAGGTGTCGCCGCATCATAGGTTGGTGCTTAGTGATAGTCTTGGTCTGCAAGGCCATACTTTTCTCCTAACATTGTTTAAAAGGTTCGCTACACTATCTTCCAGACTTCCGGGACGGAGCGGGGCAACTGTGCGGGGTCACTTTATAGTGGTGAGAGTTGGATCTTTCACATGCCAACGAAGATCCAGAATTTTGAGACGTGTAGTTATCACTAGGCAGATTAGAAGAGGCTTGGCTACGGTATGTAACAACGGCTCACGACCAACACGGAGATTGGTTCAGAGCTGGTCCCTGGGTATCAGCATACCTATCGATGACCATTTGGCTGCAACTTTTTATTGGGGTATCATGATCCACCTCATCTCGTCCTTACCTATGACAGCGTGGGATCCATTTAGAGTTGTCGCAACTCCTGAGCTGCAGGTGCTCTTGAAAGAAATCTACGAAGCTGACGTTCTTCCACGTAAGGTGCCTCAATGTACGCACCGAGTCCTCTTTATGGATCAGCCTATCTCTGCAATTAGTACCTTTTTTGATGTTTCTACTTCATCTGATAGCCCT', 'ATGACTCATATCTGTGCTGGGAACGGTGCTCTTAGACTTAGGATGCCTACTGTTGGTGATCTTAAGGGCAACAGCGATTATTGCTTTAAATTCCGTTTGGGCTTCATTCGCGACACTGCGCTCACTCGGGTTTGTGTTAAGAAGCCTAAGTTAGTTCTCACTATTTTCAAGTGCGTTCACGCAGGTCACCGAAACTCCTTTCCTAAATTTACAGGAGAGGCGTACGGATGTTTGAATACCGGGATGCAACGGCAACCCCACTCTGTGACTGCCGGTACCGCTCTCGCTCTTTTCACAGGCATCGTTAGAGGATCGAAGTCTCAACCGGCATGTGTTTGTGCCTGTTATGTGTCACCCGAGTTAACCGGAGGATATCAGTACAGGCCTACCCTCTCAAGCGTACTGGTCCCGTTCTGTTTGAAGTGCCAAAGTTCTCCTTCAGAAGTGAAGGCAAATCGCGAAAATTTGTCCATTCAATTGACATCCGAATTAGCAGTTAGCTTCGTGGGCTTAGTTTGTAGCATTAGATGTTCTCCAAGCAGTTCGTTGTACCACGAACCAGTGATGGGTAGGACTGGAAGAGCAACCCAACTCGTAAAAGTCTCTAACTCAACAGCCTCGGCTCCATCCTTAATTGGGAGGAAGTGCGAACTTCAATGTACA', 'ATGGTAGATTATTATCATGTTTTTACACATGTACTCCAGATTCTTCCTAGTTGCACGCCTTGTGTCTACGCTAAATTCCATCCTGCTACACTAGTGGTGGACTGCTTTGTGATCTTCCTTCCGGTGGCAGGCTCTCCCTCATTATGTTGCCGTACCTCGTACGGTATCGCCCTTATGTTGTACTTGGGTAGACTGATACGCCCATACAGAACTGGAAGAATCTGGTTGATATCAGAAAACAATGTGTCAGCTCGTACTAACATCAACCCATATTGGTACGACGCAGAGGGACCGATCTCGACAGAGAGGGGTGAGGCACATTTAATATCTTCATTGGCTGCTATAGAGGTCCACTGCCCGTACTTCCCCGCACGTCGTGTTACACTTTGCACATCTCCAAAATTTGCTTCAAGAACCGCCGCGTCTAGTACATACTGTTCAAGTTGTCTAATTTGTTTCCATAATTACAAACCTACTGTTTTGATCGGTCTAACACCACGATCAATTTCTGCATGGTCACCCCAAAGAGAGAGTGCTTCGTTGGACTTGTCTGCTGAAAGACGTGTAGCTCCGTTTTCGTCTCTTCATAGAGGCCAAATGACAGGGATGACTACGAGACACAGCGCTGAGCGGATCCGACCGAGTTGCTATATTCCAGGATCTACTGAGACCGATAGAGCAGTGGATGGCATGCCTCCACCGGAACCTTCCCCTCAGGCTGTTCTACCTTATCGTGATTTATGCGGATGGTTTAGGCTTCTCCTTAATAGTGGAATGAAGTATCCGCAAACTGATTGCAGGTTGGGGCGCCCCACCGCGCATGCTTTCATCATCTCCACAAAGGTTCAATGTTGTGCTTGCGTTACGCGGCTAGGCAGGTCAACAGGATACCAGCAAGAGGTCTCTGCTTTAGATGCGCCGTCAAGCCAGAGTTCTCTTCGGATAGCTTGTGGTGGAGGTTCAAATTGGGTCCTCTACCGTGACAGTAAGTGCCTGGAATGGTATCTCGTCCTCAATTATCGTTCTAAGCTCCCAATTAATCCACAGAGGGCTGGTTGCAAAGTACTTGGCTTGGTGGGTCCTACTCAATATAATTGCATCACAGGAGCCCTCAGAGGAAGACGGAACGACAATGCGCGCAGAATC', 'ATGAGATTAACGGTTAGAAAAGGAAAATTAGTTTCTTCAATCCCTGTGGTACATGTTCCACCTTGGTCCTGTATGCCTATAGTGATTTCATCAGCTTTGGAGCTCGCTGCTTTGATAGCCGGAGTACAATCCAGTTCAAGGGCTTTTGTACACCCTTTTAGGTGCACTATCTGCCGAGATGTCTCCCATCAACACTTGGTAGGACTGGAGCGATCATCCGTCCCAGCGGGTAACTACCAGAGCCTAGGCGTTGGTGATGCTCGTACATGGGGCCTTGCTGTGTATCGTATGATAGGTACGCGGCCTGCATTAGAAAAACAACGCGCAACAACGGAGGCATCCTGTCCGGGCATAGTTAGCGATTCAGCTCCTTTTCTGAATAGAAGTGTCGCGAATTGGGTGAGAGCAGGATTGATCGGGTTAATTCCCGTTCAGCCTGGTGATAGTCAAGTTGTGATTTGCCAGCGGATCCATAGGTGTCAAATGACTTTTATCAGGGCTTCAGCCCCTATCAGACCGGGCAAAATCGTTCGGCAGTGTTGTCTACCTAGGTGCTGGCTTTTAGCAGTCAGAAAAACGAGATTCCGCGCTAAGGTGGAGGGGCAAGTAGCTATGTGGGGAACAAGGTTTCGTATCTCCCAGTCATCTCATGTCTGTGCTTCTAGACCACACCGAGGAACAAGATCTATCTATGGTCCATCTACATTTCCAGTTTCTCCACCTGCACACGGACTCCTCAAGAGAACCACCTCAAGGGAGCCAACTAGTTTGATCTGCGGAGATGGCACATTTAACTTGGGAAGAAGTCTGGAATCGCGCGATTCCCATGAGTCA', 'ATGGCTCTTTTCATGTCACTGCCAAACAACGGTCGTGTTAAGACACTCATTTTTAGAGATCAGGGCCATCATCTTACTTTCCCTACTGCCTATATCGAGCTTTTGCCTCTTACCTGCCGGTTACCCGAGATCTGGGAAAACCCTATCCTCGTAATAGTTCACCGAGCGCATATCTGTAGGACTAGGAACGAAAGGACTCAGTCTAGCGAACCAATCACGCTGAGCGATAAGACAGGCACAGTGGCTAAAGGTCAAAAAATTCGTAGACCATTTGCGCCATCTTTGAACAAGGGAGGTCTTTCATTATCACGTCAAATCTTCCCTGCATCCCGTACCGCGCATATACTGGTAAGAACATGTAGGATAGTTTTCGCTCCTCCAATTTACCTATCGTATCCCCTTATAAGAAGGGATGGTTCCTATAGGTTAGCTTTCTGGACCGGTTTTCCTCTTTCTGAAAGGTCTCTCCCACTCTATTCACAACTTTCAAGTGAAACCGGAACGTTATGGACTATGGGTAGGCCAGCTCTACCTCGTTGTTCTGGTCTTATGGAAAGACACGTTCCTTACCCAAGTGGCTGCAGCGTTTTCCGCGTCAGAGTTTTCTTGAGACAGACACCTTCACATTCAAAATCCTTCCAGGGGTGTCTTACTTCTGCGTTGAACATTTCTTGTGTCGGTTCAGTGTACCCTAAAAGTGTGGGTAAATCTCGTCCATCTTCACAGAGAGCTGTAAAGTTTAAATCAACCGCAGGAACTGGAATCGGTTGTAGATTCTTGTTTTCTGACACTCAATTCGATCTTTCTAAACCACTTTCTGATAACATTAGAACTGCCTCCCGTTCACTATCACACAGGGCTTCTCCGCGTCTCACTACATCACTGACAGCTGTGCATAAGGGTAACGAGCCATCTCAAAATAGCCCTCCTTTACACAGAAGTTGTTACAACAACGTGGGATCTGAAATTCGGCCACAACTTCCAGGTTTGGCTGGCAAGGGTTTTGCTATGGTTATCTGTAGAAGGCTTTACAAACTTCATAGGAACAGAAGTGGTGTTCCGCGAAACCAATCTCTTCTTTGTCCGCGTAGTGTCAATTCTTTTCATGTGTCACTAATGTTAACCCATGCAATTAGATCTCAGGCGATTTTCCCTCACCTTGGGCCAGCCAGGGTGCCCGAGTGGGAATCTCTTGGAGGCGCTAAACATCCTTTAGGCTTGATCTCAATTAGTTTTCGCATTTTTTGT', 'ATGGAGAGCCAACCTCGAGTGTATGGTCGTGACAACGGTTACCGCTTCGCAAATTATGGAGATGCACTTACACCAGCGTTATCTCACGGCTGTAACGCTGATAACGAAGGGGTTGCACCATCTTCAAGTATGATTTTTGCTACTGCTTACTTGAGCATGCCAATTATCAAAGGCCCAAGACTTCTAGTGAACAGCAAGGGTACATGCTTAATGCAATATACTCGCAACCACAGGGTCTGGTCTCTGTGCGATTCGCGTGTGCTTAAGATCGAACTGTCCCTTGTGAGTCGTCATCACATAGATAGCCCGGCTCTCGACTTGGAGGGAGTTCCTGTTTGGAGAAATAAGCTTCTTGCAACAACAACGTTTAAGTATCTGAAAATGTGCACCCTATGGGATATAGATTATCTTTGCGATTTTTATCTGTCTCACAAACTTTACCCAAGCTCGGAGGGAACTAATCCGTTCAAAAATTGCCGTTGTCGCTACTCCTGCCTCAAGAGAAATCGATCTTTCAAGAGCATCAGACATAACACAGGAATGCCTACAAAGCCACGTATCCCATGCAACCCATTTGACGACTTGGGCGCATCCCCTAACTATCAACTAACTGGTATAGCGCGGATATGTTACGACGTCGCTGGAAAAGGCCACCTTGCAGGTAAGTTGAGAACTAAGTTTGACAAAATATCGTTGCTTCAATCGCAGTCCGCGGATAACGGTAGGCCCCCGACCGTATTAGTGCCAATTCTTGCTAGCCTCGCTCGAGTATACTGTGTTGTCCAGGTCAGTATGGAAATGCCTGGAAACCGCAGAAAGGTAAACGTGAATGATGTATCCAGCTTGAGACGTCGTCAGGGTGTTGCTGCCGGGACAGCTTACAATGATCAGAAAGTTGAT', 'ATGTATCGGCAGAGGCCGGTGGTCCCACCTACCCATCCAGCTCCAACAGATCCCTGTTTGCCAGATAGGTCAATTCCGAATGTTGCACCTATCTGCGCTACAGCCGGCAGGCATTGGACAACTGCAGGGTATCGGTTCAGGTTACCCAACCTTGGGGCGATAATTCTTGGTAGGAGTCGTAAGACGGATTCTAATCTTACAGTACGGTTGTCACAGGAAGCACACGCAGATTGGGCCGAATGGCAGCTCAGCTTCCATCTCATATATGTCTTTGGTCTGTCTATCTATCCATCCGTAGCCCTGAGAGGTAGAACATCTTTTGGTCTAGCTGGCCGTAATGAAAGAATATGGGTAGCGTACTCTCGGACCACCGGACCACCAGTAACTAGTGGTATTTCCGCGTGGTATCCTCTAGACTTTCTTTCGGAACAGACAGTCCATTATATGAACTTCTTACAGCATGGTCGGTTGTCTGCAGCTTTGCGAGTTCGTGATTTGGTGAGTCATTGCGCAAACAAGTACCTCCTTCCCTTCTACGTCACGAGGAGCCCTCTCTGGGTTTTAGGTAATGGTCCAGCAAGCCGCACCGATACTTGGGGTTGCATGAACGTATTCCCAATTTACGGTGGTCAGCGTGTGAATGCATCCTCCTTAAGAACTATAGCCGAACGGTTGGGTCGTTCAATTCAGCGCAGGTTGGAGAGTGTTCAGTCTGACGCACCTCTTTCTATAAGAAATCCTATGGGTCCTGATTGTCTGTTGGCTGTTGGATTTTTAGAGCGA', 'ATGAAGGGAGCTCGGCTTAGAATCCAACGACCGCTTTATGGACCGCTTGGGAGTGCAAACGGTGTGAACCAGAGAAAGGTGATGTGTTGCAGGCTTGGAACTACGGGAAAAAAGGTTCTATTACTTCTTGCAAGATGTCCCGGGACTCTCAGCGCTAATCCTTGTCTGCGTCGACGAGTTCCTGCCGTTAAAGCATCTGCTGGAAGACGTAATTACTTCTTTGCAAATTATGGGCCACGGTATTGCGCTTTATCTCAAAGATTGCGCCTCCGTGTGGTGGAGACAGACTGTTTGGTGAAAAACAGCCTCATCTACAACCCGCATAAGTCGACGGTTAGGCTCTGTATTATGGGTACCAAGGCATCCGACAGACGAGATATGGGATGTAACAGTGGAATTATCCATAAGACACTTTTCCCTCGCTTAAATGGATCTACTCCCACGCAGGACATCTTCAGTTGGGCTTGGGACAGTTTCCGGTCTATAATACAATGGGATGTGTTTCCACTTTACCCTCATCCAAGAGGATACCGAGTTGTTATTAAATCTTTCAGTCTCACAGAGTCAAGGACACGGGAATCTAGGCCGTATTCACACTGGTGCCGAGCCAACTCTTGGAAGATACCTGTTTACGCTATTAGGGCGTGCATGCGTCCCGAGGTGTGTTACCGTCTTAGTAGGTCTATGGCACGGAACTGTCCGTACAGCTCCAGGAAATTAAGACTCGTTTCGTTTGACTATATATCCCTAAGGGTTCTTCATGTTATGCCAATGAAGCGTCTATCTCTCAGGTCTAACAAGACTTGCTCTAATTGCTTTGTTACTCATACTAATGGAAGGTCGACATGGAATTCGCAGCCTAGTATGCATTCGGGCATGCGAACAGATTCATTTGTGTCCAGGCATGCCGGTTCAAGTTACCGACTTGCCAGACTCTCCTGCCATAAGACAGGTCCGCGTGATGGATCTCGTATTTGGGGCCACATTCGTATGACTGGATATGTCGGAGTGATTATTCCTTTCTTCCCTTTTTACATACCACTGTTGTATGTCGGTGTCATACCAGAATATCCTATGTTGCTCTTACTCCACTGGACGGTTCCGGTGCCCGCTGTTGATTTGAGCTCCAGATATCTAAGCTCTGATACT', 'ATGACTCTAAGACTGGTTAGAATTTCACATTCTATTGGTAATCTTCCGGTCGAAAGGGTGCCCAAATTCCGTGGATCCTCTCCATCACCACGCGTCTGTCAAGAAACTACTAGGAAGCGAGCACCATTAAGAGCATCTGTGGAACCTACCTCAATCCATATTTACTGTTACATCAGTAAATACGGACGGGGCGAAACCGTGGGGGTTACTGCTCAAAGCATCGAGCTCGTGTGTGTCTGTGTGACGGGCCGACACGGGGGTGGTCTGCGACCCTATGAGGGCCACGTCTACGAATTCCTCCAGTCCATCTATAGATCCGGTGCAGGAACTGTAATTAATTGTCCAGCTGGCCATAGCGTGACTAGATCTGTAGGGAGGCCCCCTAAAATGCTCTACGCTATTACTGGGTCTGTTAATACAAGAGTGCTTGGACACGCTGTGCCTGGTGATGGGGTTCAAGCTTACGAGAGGCCAAAAGCACGCCATACTGGTCCGCCTCTGTCACCTGGTTCACCATGCCGAGTTTTCGAGTATGTTGAGATATTGACCCTTCGGGGTCCGGTGACGTACTGGTGTGTGACTCAAGAGGGAGGAAATTCGAGAATGCCTCTAGCCTTTTTTACTTGCCCTAGACGTTTGGGAGGTTTCTCTTTTATGCAAGTGGTTATTTCT', 'ATGTCCGTCACATGGCTGCGTCCGATCCGAAGAACAGCCATTGCTGTGCATAGTATGCAGATCTCCATCACACACTCATTAACACTCACAGTTAATGTTAAGATCTACTTGTTGCGAACTCAAGCTGCAACTCATGCCGGGAGAGGACGTTTAGCCCGGCATTCCTTATTGTGTTCACTTCTCTTCGTAAGATTGGTTACGGTTGTGGGGTGTCATGAGCATGATGACTCGACTCACAAAGTACTTGCCTCGTTTGGATCGTGCAAAAGAGGACCTACTGTGTTATGTAGCTATTGGTATTTGCATGGATTTAGGCTGACAAGGCGTGAACCCACTCCTAATACCGGTCAAACAGGCGGAGAATTCAGTTGGGGTCTCTCGGTTCTTTCTCTGGATACCAGGATTATGAGACCAGGCGTTCGAATAGTTACCGTTGTTATTGGAATCGTGACCACTAAGGTCACACCGTTCGTTTCCGAATGTTCTTATAAGGGTGCTGGTCGACCAATACAGTTATATACGTTGTCCACCCCAATCAGAATGTTGTTAGTTCTGATACTTCTTGCTCCTTCTCAGACTGGGGGATACAGACATTCGATGCTGCACAGAAGACCAGCTTGCTCTGTTCTCCGTTGCGGCCTTTGGGTCGCCTATTTTACAGCACATGAAGTTCGAGGATCATTATTGGTGCGTACTACCAACATATGGTATAAAACGAGCTTGGCGTTCGTGTCCACTATCTTGACAAGGCGATGTTTAAGAACCCTTGGAAGCGGACTGAAGCAAAGCGTAAAGACTGGGAGAATTGGAATTCGTGTTGCGATAGCAAAGTGTGTGTCCAATGCCATCTTCGGCTCACATAGA', 'ATGAGATCCGTTAGACATATAAGAGGATCCGCACATGAGTTCTGCCCACGTACAGAAAGCAACTGTGCTGAATGTCACCTTAAGAGCTTGTCAGAAGCTCTATGTGGAAGGAGGCTGTCTTTGCCCGTTTTTGGGCTTTATCGTCCAGCCTTCGGAAACTATGAGGCAGAACATCCAGCTCCAAGAGTTCTTTCTCGAGCAGTCTGGAACGTCCCTCATTTTAAACGTATATCACCGCACAATCGTTTATGCGGCTCATTTAATAAAGCTCACCACTTAAGTCGTGGATCAGTCCTCTCGGCAACTGGACCAGCTATTGATGCTAGACAGAGCTCTCTAAACCGGGGGAATTCCACTCCAGATGTAGATCGAATGCTTATAGGTAATACAATAAACCCTATTTCCGCATTGGGAGAGAGAGGAGGTTCCATGCCTTGTTTTACAGAAAAAGGTTTGGCTTATATAAGTCTTCCGGACGATCGATACCCTGTGCAGCACTGGGATCGCCAGACTGGGTTTCTCGAGCAGCTGATAAGACCACCGGACCCTTCAGCCGCTTACAATGGTTTCGTACCTTCTGCTGAGTTGAGAAGAATCAAGAACAGGATTCTGCACGAAAGAGATTCAACATCTGGTCTTTTGGATGTAGCTCAAAATAACCACTCCATATCTCTGACATCTTTTCTCTTTCCTGATGCTCCGCCTTCAATCGAGGAAATTAGCTTAGCATATCTAGCGCTTTTGTTGGATGCAAAGACATTCGAGACGATACCATGGTACTCGGTACTCAAAGGAATCCCATGTAGTTCTCCTTACATGGTATACGAGTGTTACCGGGTAGGTACTTTCAAAAGATATTCGTTGTTGTCCACGCTGATTACTAAGAATATAATATGTACAATGGTGCCAAAGACTGATCCTGATAGGCGATTATGGTTTAAATTTAGCAGGAGATTAAAATTGGGAGGGCTTCCAGCCGTGCCCAGAGAGAAGCTGGCATATCAATTTTTCCATGGTCGTGGAGCATTCAACTCTTTGTTGTTTGTTAAAGCTAAGCAATTG', 'ATGGTTCAACGTATAAGGTCGTGTTGCCCAAGCTCGCACCTCGCTCGACATCCTGTGGATCATGAAGCACCTTTTAGACCTCATGTTAGAGCTGGCTCCACTCACGTACCATATAGAGGTCTCGAATCACCACTTTGCGACACATATGTTGGCTACACAACAAGACGTACAGATCATCGCTTTGGACATAGGGGATTCAAAATGGTTACTTTCTCAGATGATTTCTGCTTGACCTATACTCACGTTATTACTCTGCAGTACGGCGAAATTAGGACCCATATCCGCCCAACTCTTCCTTATCCAGGAGACAGAATGGGATTGTGCCAGTACCACCCACGTCCTAAGGATTTCTCAGAAAGGAAAGCTTGCCATTCATTAACTTCCCCTGAGGGCCCAGAAAGGGGACTGGTGGGAAAAGCATATCGGGTTAGGAGCAGGTCTAATGTCTCCCCAAGATACGGGAGAGAGGCTGAAATATCGAAAGCAGCGCACAGGAAGTTTTCTGACCCTTCTGGAGCTCCAGATAGCAAGGTATGTCCGACGGGAATAGTTACAATAACTCGGAGGTCTCACAGACTTACATCTCCACACCTCCGTATCTGTAATAAGACTGACACGCATGAGAGAATCCAGGCTGTACCGGCCGATGTAGGTGGGAGAAGCCCTCAGTCTAGAGCAATACGAGCGCGTGTCGGTGAAGTTGACGAGACAGTTTACAGTAGAGCAACATTAAACCCATCACTACCAGATTCCACTGGTGCATTCTTGGGAGACTTTTACTTGCTGGTGAATTCATGCAGAGTACGAAGCTTGCTTCTGAGAAAATCTCTTCTCAATGTCAACGCCCCCATCCGTTGTACACATTTGGGCATCATATTGGGTCGTAAGTCCTCGCACCAGTTTTTATTATCCAAA', 'ATGAAAGCCAAAATTAGAACAGATATTGAAACTTGTAGGCCTCAACTTGGTGGAGCACTCTTACTAGAAGCTGATCGGCTTCGAGTATTTTCGGACCAACGGCTTTTGCAAAGGCTATATCAGGAGTATCCTACTGAACGTGGTTTTACAGTTACTCACAGTCCAGCTTACCTATTTCATGTCAAAGAACTTGCAAGCACTGTCGGAAGGGCCCAAAGACTGCCGTATCTGATCACTTCTGTAAACAGCGCCGCCTGGGTGCGTTCGCTATGTACATTGGAGTCCCGGGTTCCAGAAGCCATATGGTGTATAACAAAACATCCAAAAGTAGATTTGTTAGAGCGCTGGAAATGCGAATACAGATTAATAAGCGTCGGACTAATCCTCGCAGATGAATACGAACAATCTGCTAAGTACGTGGATCATGGACCAAATTTGGCCCGAACATCACCACGGGTAATCCACACCTGGAGAGATCTTAGGTTTTTGGCAAGAAATTCTGGTTTGGGGCCCTTATCTTTCAGAACTCAGGTATATGCGCTTGAGCCTTTGCATCTTGAGCTTTATGCTGCTTTGGAGGAATTTTTGGAACATGCTTTTCACGACTGTTGTCGTGCATCATTTGATACGATGCTCCCGGGGGCCCGTCCAGTCCCTATGCCTCTAACTCCAAGCAACGAAATTTCTGTTCATTCAGAGCTAGTAGATGTCAAACAGAGGACTTATCAGGCTACATCAAGTCAGATAGTTATAATGAGACTTGCTTATGTCCACCAAAAAGTGATCCCCCTTCTGAGATTCGAAGACTTCGATGGAATTACCGACAGCTGGCCATTGGCAATTGGTTCTAGCTGTTATACAAAAGCCGAAAGTGTCGGTGCTTTAATCAGGACAGTGGATTCTGCTTCGGTACTTGTCCCTTTGAAACAACATAAGAGTGCATCTCTTGAGACATCTTGGGATGCATCTGAGCCTCCGGGTGCTTCTCAAAATCTCCATGAGCCGGCTGGACATGAAAGGTGCCGTCCATCTACGTATTGTATGGTTGAC', 'ATGATCTGTAGAGTAATCGCAAGATCTGTAGTGAACAAGCTTCCGCCTGCATTTGGATACCATTTGTTTACCGAGGTATCAAGACATGGCCAGTACTACATTACAGCTGCCCTGTCGTTAAGTGATGATAAAAGGGGACTGATTTGGTTCCTATGCTTGCCGTACCCTGTACATAGCTGCGCACCAGCGAGTGCACTCGGTTTTTCTACTGCTGCTTTCGGTCACTTAACAGTGCCAATTTTAGGATGTCAGTACAAGTCCTACACTAAATACTTCTTATTGCCCTTTATTGCAAATGCTTGCGGACCTATTGGGGGTGTTCCAAATCCTTTCAAGTACGAGTTCTCATGTCCTGGTTCTCAAAAGTCTGCTCTTTGTCTGAAGCAATTAGTCGGTGAATTGTATTTAGCTTGTACCCCAGTAACTCACCCATACTACAGTGTGCTTAGAGCTAGAATGAATGCAGGACACAGACAAGTTTCTCGTGAGGATGAAATTAGGTCTTCAAAGGATTTGGTGAAAAAGATGCGATCATCTAGGGGTATGGTTATTCTTGATCATAGGCCTCCAAGCGCTTTCATTTTCTACTTGGAAAGACCTTATAACCGG', 'ATGAGTCAACTTTCTATGATACTAGAGAAGAAGACACGCGCCACGCTTCCTAGACAAAGTAGAGATAACCTTAGACGTGGAGGAGGAATGAGAGTATACTATGTATACAGTCCACCGGAAAGCGGTTGGACACACGGATCTTTTGAATCACAGGGACCATGGCATTACCTCCTAGAGGTTTCCTCTGGTATGAAAAACCTGCAGCTCCCACGTCGTTCAGGACTCAATGATATGGGGACATTACCATTTTGTAATGCAGAACGCTCTGAAAGCTACCGTGAACGTTGTATCGCAGCAAACACTGCTGCATGTGGACTTGATAGGGCCACATTAAGAAAACTTGTAGAGTTTCCCTTTCAGTACTATAGTTGTTGGAGCGCGGGTTACGAGCTTTATTCCTACGGTTCTATGTGCAAATGCGCTCGAAAGGGAGTCTCTATGGTGGTTCATACATTCCCAGACCTCGGACAATTGATGTGTCTGTGTGCGGCTTCATGTCTAACACCTGGAAGCTTTCTGTGTATCTTTGTTACTGCGGGTTCTAGAAGAGAAATT', 'ATGCCGCACTATCTGAACGTTAAAAGACTTGGTAGCTACTCAGCTAAGGGGCTCAGAGCAAGAAAAGATGCTTATTTGACCGCCATCGAGCAGGCCTGTGGATACAATGACGGTATCGGAGATTGTGAGCTTATTAAGATCGGGTCACCACTGCGGACTACTCCTCACCCTCGTAACAGACAGAATCGATGGTCTCCACCTTTATACAAGGATGGCCCTATGGGGGCACTTGGCGACTCATCGCCAAGACGAGGACGACCATTGGCTGTGGTACATATGCCTCCAAGTACGACTCATGACAGACTCCCAAATAGCACCCCTCTAAAGATGCATCCGCGGACTTGTCCATGGAGACGCAGTAATGAAAGCTTTAGGTTCAGGACAATGTGTACAATCCTCACCCATGCTGCTGCTGGGATGACTAACAATATTGGTAATAGAAAATTGGGTAGCATCGCGCATGCTCACTTTAACTCTCAGGTGGCACGGTGTGCTGACGCTGAGCTGCATGTGGTAACTCATCCATGCTCTCCTCGGGCTCAAGATAACCAGACCGCTGCTCTATGCGAATTTAGCTGGTTGGCTCAGGAAGAAGGTTCGGTTGGCGTTTCAGGCTTTACGTGCCTAAGGGTGATTGGTAGAGGCGTAAGGTCACCTCCTATTTTAAGAGGTCCATCAGGGAGAGTTAACCTAAACATGTCTAGTACTACGTATGGATTACTTATAGATTACCTTTTGGGGCGTTTGACCTTTCCACTGCCTGGGTGTGGATCTACATTCCATTGGGTTCCCCGCAAGACATTTGCTACCTATCTGACTTCAACCACACGCATACCACTCTCCAGGAGATGCAGAAGACTCCGACACTCTGTTAAGCACAAGCTGAACTGGGATCTTGATAGACACTCGGAGTCTCTGTTCTTAAAATGCTTATTGTCTACCAGAACAACGGAAATGTCCAAGTTTGCTCGCTCTACAGGACAGGTAGCTGTATCTCCGAGGGCTCGTACAGCAATGGGAGGAGAGTTGTGTTACGTCACACGTGGATATTATATGTTGGGGAGACCATGCCGAGAGAGTGAGCTTGGACTTCTTAGCTTGCCGACTGGTACGGCTCTTTCGCTTCTTAGCTCTGTGCTGAGGCCAGGTGTTAGTGAATCTAACTGCCATGGTTCTCATTGTATCGTAGATAGATTTGCTGTTAGTGCGCTCTTC', 'ATGTGCGTATTGTTGTTCCCATTGTTTGCCCCGAGGATAGTTTGTAGTCATAATTCTCCTACTAGCGATTGGTTGTGTAGTAGTGTTATTTTGAGTAGATCTGGTGGGCCATGGCCCATCCTTAACGCTCTTATGGATAAGCTCACCTTAGTAACATACTATGGTTGCAATACCCATGAGATCCTTACTACGTTTGAAGCTTATGCCTCTGGGCAAGGTCCGACAAGGCTTAGGTGCCAAGGACTCGCCTGGGGATGTGGGCATGCTAGATCGTCTAGCACCCTCTTAACGTCTCGTCGCGTTGATGATAGTCTGGGGGCGTCTCCGGGTACCAGCAACCTAAGAGTTGCGTGGTGCCTATCTTCAACATATCCAATCTCACCTGCTTACCCTAAATACCTTAGGGCCGCTCAAATTGATCTTCATGGTGTATCTAGACCCTGTCATTTATACAGACCTCATTTCATGTTTCTCATTATCCGAACAGGGGCCAAGGCCAAGTTGAGGGAGGCTTTACCTGCCGGCGAACATAGAGTTTTGCAATTCAGGTCAGCATGTACATACACTGCCGATCAGTATTGCCAAGTTACAAGAAAACCATTTATGGTGCGGGGAGGTCAAGAGGGCCATCAGTCGAATCAACGAGTTGGATATCATCCCAATTTTGGGTTAGGCGACTGCCTACCAACGGCAGGAATGTTGTGCAATGTACCATCAGCGAGGTATAAACCTCTCAACGATCGGGGGCACAGATACGGACAAAGACAAATTCTATACTGCCCGTCTATAGATCGCAATCTCTTAGTGCTCCTTTCATTTTCAACCGGTACTGAGCACCCAGATCATTCCGCTATCGCGCCACATTCAAGACAGCAGATTAATGCCCTACCTGATAAGTCACTCTGGTCAGCAACGTTG', 'ATGTGTACCGGTATATTTTCAAGTTATGCCGCATGCACAAGTGATCCCTGCGTACAGCCAGAACCGGCTTGCGATCCACTCTGGCATGAGAACAACGCGCATCCACAACTTGACAACGGAGAGCTCTTCCACACTGTATTCAGATACGGAGCTCATATTTACATCACTGGAATATTATTAATAAAAGGTTTTTGTGCTACAATGTCAACAATTAGAATTTTTGGAACCGAGTTCGTTACTTACTCCATAGAATGGCCTCCAATCCTAAGATTTCGTATTATTCCGTACATGCCATCCCCTCCAGTCAGGTATTCGGCTCGGCCTTGCAGTATCCATCAAGATGAACACCTCCCGGGGGGTCTTACCATCCGTATCAGGATGAAAGCATCATTTCTCATTCAATGGACCTTTAGGGTTAATTGTACCACTACTGGAGTGACCTTCATCGTTAACTCATACATGAACTCGCCGGTCGCGAAAACATGTAGGATGCCAAAGAGTTGTGTGGCTCAAAGACGTTTGGCCCCTCACTACTCAACTACCGTCGACGGAGCCTGGAAGTCAAAACAACAAGGGGCAGTTTCAAGAGTTAGCATAATGGGA', 'ATGTTGCCAGTGTACCGTCGCCTCTCCTCATCATTCAGAGGAAGTAATTACGGCTACGGAAACAGAGTGGCGTCTTATAACATTCATGACCGAACTAGGCCGGTTTCGTTGAGAAAGACTCGTTGGCTGGGAGTCCTCCGTTTGTATACAAGTTACACACAATCTCATATAAGAAGAGCCGTCTCTTGCCTGTTGAGAATTTCTAGAATGCTTTTACTTTATGTTACTTCGACACCAATGGGCCCTTTATATAAGGGGACTGGTGTTGTGAGTAAGTGGTCTAGTCCTTATGCAGCATTTCTCCCTGACACTAAGCAAGTTAACGTTAAAACACTACCTACACTGTATGATGTAGAACTCCCTAAGCCGAATGAACCTTGGTATGTCAGTGTTCCATACGCCCTTTTCACATCTGTCTCTAGTTTGTGCGATTGCACATTGGCTAGTTTGTCTACTAATATAGATCCACGGCATAAGACTACCACAGCAGTGATCTCGTACAAATTAAGGACCGGCGGAGCTAAACTCAGATACGGTCATCTTCTAAGTATAACCACCACATCCGTAATTAGACTCGGAGGATACGATCTTTCTTCGAATAAGGCGGCTGATGCCCTCTTTTCAATTAAAACTGTCGGTAGAAGAGTACCAAGAACGGCTAGACCATTCCACGTTTTTGAGCTGTCGAGTTTACACTGGCACCCTAAGCATGAAAAAGCTACCAACTCTTCTACGGGTTTGCATCGTCCCAATACACCTTTCGCCGAGAATTGCAGACATGGAACAAGATTTTACACGGTTCGTCTTAGACTTGTTTTAAGAAGATGGCTTATCGTTAGGTTTAGGCAGGAGTTGACAAAGTGTTTAGTTTGCTTTACATCTCTCCACCGTCTCATC']


#Write a function that combines the header list and the sequence list to make a dictionary
def dict1(headerLst,seqLst):
    seqDict = {}
    i = 0
    for i in range(0+len(headerLst),3):
        seqDict[headerLst[i]] = seqLst[i]
        i+=1
    return seqDict

#This function takes a sequence and returns the gc content of that string
def gcContent(seq):
    #Setting the contents to 0 so I can start counting
    gContent = 0
    cContent = 0
    totalContent = 0
    #This for loop goes through the sequence and counts up how many G's and C's were found along with keeping track of the total content
    for base in seq:
        if base == "G":
            gContent += 1
            totalContent += 1
        elif base == "C":
            cContent += 1
            totalContent += 1
        else:
            totalContent += 1
    #Gets the percent of the G's and C's
    gContentPercent = int((gContent/totalContent)*100)
    cContentPercent = int((cContent/totalContent)*100)
    gcContentPercent = int(gContentPercent+cContentPercent)
    # print(f"{gContentPercent}% of this string is G and {cContentPercent}% of this string is C. The total GC content is {gcContentPercent}%")
    return gcContentPercent

#This function looks through the fasta dictionary and checks the gc content of every entry then returns that to a string 
def contentScanner(fastaDict):
    #an empty list to fill with the names of the keys in fasta dictionary
    keyList = []
    #adding the keyes to the empty list
    keyList += fastaDict.keys()
    #initializing the while loop for searching through the dictionary
    i = 0
    returnString = ""
    while i < len(fastaDict):
        gcResult = gcContent(seq = fastaDict[keyList[i]])
        if gcResult >= 46:
            returnString += f"{headerLst[i]} with gc content {gcResult}%\n{fastaDict[headerLst[i]]}\n"
        i+=1
    return returnString

#This function formats the results from the search into a file and asks the user for a file name
def formatResult(searchResult):
    while 1:
            try:
                fileName = input("What would you like to name your file? Please just write the name with no spaces. The extension .txt will be placed automatically\nEnter your filename here: ")
                #checks if there are spaces in the file name
                if " " in fileName:
                    raise Exception
                #checks if there are periods in the file name
                elif "." in fileName:
                    raise Exception
                elif ".txt" in fileName:
                    raise Exception
                else:
                    break
            except Exception:
                print("I'm sorry, please do not use spaces or extensions in this file name")
    #sets an output file using the inputted file name
    outputFile = open(f"{fileName}.txt","w")
    #writing the reworked string to the new file
    outputFile.write(searchResult)
    #closing the file
    outputFile.close()

def main():
    #calling the dictionary maker sequence and saving the result
    fastaDict = dictMaker(headerLst,seqLst)
    #using the return from the dictionary maker and putting that into the content scanner
    fastaString = contentScanner(fastaDict)
    #taking the results from the content scanner and inputting that into a function that will save the results to a .txt file
    formatResult(searchResult=fastaString)
    
if __name__ == "__main__":
    main()