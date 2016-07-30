from parse_fasta import parse_fastaq
from parse_fasta import parse_fasta_to_dict
from parse_fasta import order_seq_length


fastq = r"D:\python_workspace\tmp\data\test_fastq"
fasta = r"D:\python_workspace\tmp\data\some_fasta"

# with open(fastq) as fin:
#     for item in parse_fastaq(fin):
#         print (item[0])
#         print (item[1])
#         print (item[2])
#         print (item[3])


result=order_seq_length(parse_fasta_to_dict(fasta))
for key in result:
    print (key)
    print (result[key])