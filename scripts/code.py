import re

# תבנית Zinc Finger
pattern = "C..C.{12}H.{3,4}H"

# פתיחת הקובץ הקיים אצלך
file = open("data/orf_trans_all.fa.txt", "r")
out = open("results/yeast_zinc_finger_orf.txt", "w")

name = ""
sequence = ""
counter = 0

for line in file:
    line = line.strip()

    if line.startswith(">"):
        if name != "":
            matches = re.findall(pattern, sequence)
            if matches:
                counter += 1
                out.write(name + "\n")
                for m in matches:
                    out.write(m + "\n")
                out.write("\n")

        name = line
        sequence = ""

    else:
        sequence += line

# בדיקה לרצף האחרון
if name != "":
    matches = re.findall(pattern, sequence)
    if matches:
        counter += 1
        out.write(name + "\n")
        for m in matches:
            out.write(m + "\n")
        out.write("\n")

out.write("Number of proteins containing Zinc Finger Motif: " + str(counter))

file.close()
out.close()
