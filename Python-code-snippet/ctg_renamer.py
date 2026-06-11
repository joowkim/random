import os
import shutil
import sys
import tempfile


def rename_fasta(prefix, fasta_file):
    backup_file = fasta_file + ".bak"

    # Make a backup first
    shutil.copy2(fasta_file, backup_file)

    count = 0

    dir_name = os.path.dirname(os.path.abspath(fasta_file)) or "."
    with open(backup_file, "r") as fin, tempfile.NamedTemporaryFile(
        "w", delete=False, dir=dir_name
    ) as tmp:
        tmp_name = tmp.name

        for line in fin:
            if line.startswith(">"):
                count += 1
                tmp.write(f">{prefix}_{count}\n")
            else:
                tmp.write(line)

    os.replace(tmp_name, fasta_file)
    print(f"Done. Backup saved as: {backup_file}")


def main():
    if len(sys.argv) != 3:
        print("\nRenames FASTA headers and creates a .bak backup.\n")
        print(f"Usage: {sys.argv[0]} prefix input_fasta")
        sys.exit(1)

    prefix = sys.argv[1]
    fasta_file = sys.argv[2]

    rename_fasta(prefix, fasta_file)


if __name__ == "__main__":
    main()
