def seq_ping():
    print("ok")

def valid_filename():
    exit = False
    while not exit:
        filename = input("Enter a filename:")
        try:
            f = open("../SESION 4/" + filename + ".txt","r")
            exit = True
            return "../SESION 4/" + filename + ".txt"
        except FileNotFoundError:
            print("File doesnt exist.Provide another file")

def seq_read_fasta(filename):
    seq = open(filename, "r").read()
    seq = seq[seq.find("\n"):].replace("\n","")
    return seq
