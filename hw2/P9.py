# DONE

def count_kmer(kmer, sequence):
    count = 0
    k = len(kmer)
    for i in range(len(sequence)):
        if sequence[i:i+k] == kmer:
            count += 1
        else :
            pass
    return count