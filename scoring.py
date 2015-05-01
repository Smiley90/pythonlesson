def MatchQuality(seq1, seq2):
    '''
    Inputs: seq1 & seq2 are FASTA sequences obtained from genome 
sequencing
    Return: Score describing quality of the match based on:
    +1 for each matching basepair
    -1 for each mismatching basepair
    +0 for missing partner/gap
    '''
    matchcounter = 0
    for x in range(len(seq1)):
        seq1char = seq1[x]      
        seq2char = seq2[x]
        if seq2char == seq1char:
            if seq1char == '-' and seq2char == '-':
                matchcounter = matchcounter
            else:
                matchcounter = matchcounter + 1
        elif seq2char == '-':
            matchcounter = matchcounter
        elif seq1char == '-':
            matchcounter = matchcounter
        elif x == (len(seq1)+1):
            break
        elif x == (len(seq2)+1):
            break
        else:
            matchcounter = matchcounter - 1

    return matchcounter
    
            
def MatchQuality(seq1, seq2):
    '''
    Inputs: seq1 & seq2 are FASTA sequences obtained from genome 
sequencing
    Return: Score describing quality of the match based on:
    +1 for each matching basepair
    -1 for each mismatching basepair
    +0 for missing partner/gap
    '''
    
    bestmatch = 0
    for i in range(abs(len(seq1) - len(seq2))+1):
        matchcounter = 0
        if len(seq1) > len(seq2):
            length = range(len(seq2))
        else:
            length = range(len(seq1))
        for x in length:
            if len(seq1) > len(seq2):
                seq1char = seq1[x+i]      
                seq2char = seq2[x]
            elif len(seq2) > len(seq1):
                seq1char = seq1[x]
                seq2char = seq2[x+i]
            else:
                seq1char = seq1[x]
                seq2char = seq2[x]
            if seq2char == seq1char:
                if seq1char == '-' and seq2char == '-':
                    matchcounter = matchcounter
                else:
                    matchcounter = matchcounter + 1
            elif seq2char == '-':
                matchcounter = matchcounter
            elif seq1char == '-':
                matchcounter = matchcounter
            else:
                matchcounter = matchcounter - 1
                
        if matchcounter > bestmatch:
            bestmatch = matchcounter
            
            mseq1='-'
            mseq2='-'
            time = 0
            if len(seq1) > len(seq2):
                while time < i:
                    mseq2 += mseq2[0]
                    time += 1
                mseq1 += seq1
                mseq2 += seq2
                time = 0
                while time < (abs(len(seq1) - len(seq2))  - i):
                    mseq2 += mseq2[0]
                    time += 1
            elif len(seq2) > len(seq1):
                while time < i:
                    mseq1 += mseq1[0]
                    time += 1
                mseq1 += seq1
                mseq2 += seq2
                time = 0
                while time < (abs(len(seq1) - len(seq2))  - i):
                    mseq1 += mseq1[0]
                    time += 1
                
            else:
                mseq1 += seq1
                mseq2 += seq2
            mseq1 += mseq1[0]
            mseq2 += mseq2[0]
                
    print mseq1
    print mseq2
    return bestmatch
