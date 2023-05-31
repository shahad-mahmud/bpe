from bpe import BPE

file_path = 'files/Pride and Prejudice.txt'

bpe = BPE(file_path)
bpe.train(1000)

print(bpe.tokenize('python'))