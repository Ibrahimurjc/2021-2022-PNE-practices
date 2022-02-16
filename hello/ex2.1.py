def count_bases(seq):
    d ={"A":0, "C":0,"0":0, "T":0}
    for b in seq:
        d[b] +=1
    return d

dna_seq = input("Introduce the sequence")
print("Total length;", len(dna_seq))
for K,V in count_bases(dna_seq).items():
    print(k + ":",V)