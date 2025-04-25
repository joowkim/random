__author__ = 'JWKim'

from Bio.Blast import NCBIXML
import xlsxwriter
import glob
import sys


def make_output(blastf):
    file_name = blastf.split(".", 1)[0]
    workbook = xlsxwriter.Workbook(file_name + ".xlsx")
    worksheet = workbook.add_worksheet()
    row = 0
    bold = workbook.add_format({'bold': True})
    excel_header = ["Query Name", "Query Length", "DB Source", "Accession No",
                    "Hit Definition", "Sbjct Length", "Raw Score",
                    "Bits Score", "E-value", "Query Start", "Query End",
                    "Sjbct Start", "Sjbct End", "Identity", "Aligned Length",
                    "Pct.(%)"
                    ]
    for n in range(len(excel_header)):
        worksheet.write_rich_string(row, n, bold, excel_header[n])

    infile = open(blastf)
    for blast_record in NCBIXML.parse(infile):
        for alignment in blast_record.alignments:
            row += 1
            for hsp in alignment.hsps:
                worksheet.write(row, 0, blast_record.query)
                worksheet.write(row, 1, blast_record.query_length)
                worksheet.write(row, 2, alignment.hit_def.split("|")[2])
                worksheet.write(row, 3, alignment.hit_def.split("|")[3])
                worksheet.write(row, 4,
                                alignment.hit_def.split("|")[4].strip())
                worksheet.write(row, 5, alignment.length)
                worksheet.write(row, 6, hsp.score)
                worksheet.write(row, 7, hsp.bits)
                worksheet.write(row, 8, hsp.expect)
                worksheet.write(row, 9, hsp.query_start)
                worksheet.write(row, 10, hsp.query_end)
                worksheet.write(row, 11, hsp.sbjct_start)
                worksheet.write(row, 12, hsp.sbjct_end)
                worksheet.write(row, 13, hsp.positives)
                worksheet.write(row, 14, hsp.align_length)
                worksheet.write(row, 15, round(
                    float(hsp.positives) / float(hsp.align_length) * 100, 1))
    print(blastf, "is done.")
    workbook.close()
    infile.close()


def main(ext):
    for files in glob.glob("*" + ext):
        make_output(files)

    print("all is done.")


if __name__ == '__main__':
    main(sys.argv[1])
