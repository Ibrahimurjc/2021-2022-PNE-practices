def count_bases(seq):
    d ={"A":0, "C":0,"0":0, "T":0}
    for b in seq:
        d[b] +=1
    return d
with open("sequences.txt","r") as f:
    sequences = f.readlines()
    for seq in sequences:
        new_seq = seq.replace("\n","")
        print("Total length;", len(new_seq))
        for K,V in count_bases(new_seq).items():
            print(k + ":",V)