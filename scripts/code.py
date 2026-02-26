import re

# מוטיב Zinc Finger נכון לפי PROSITE
pattern = r'C.H.[LIVMFY]C.{2}C[LIVMYA]'

# פתיחת קבצים (כי את מריצה מתוך ZING FINGER)
file = open("data/orf_trans_all.fa.txt", "r")
out = open("results/yeast_zinc_finger_orf.txt", "w")

name = ""
sequence = ""
counter = 0

for line in file:
    line = line.strip()

    # אם זו שורת שם חלבון
    if line.startswith(">"):

        # בדיקת הרצף הקודם
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


# בדיקת הרצף האחרון בקובץ
if name != "":
    matches = re.findall(pattern, sequence)

    if matches:
        counter += 1
        out.write(name + "\n")

        for m in matches:
            out.write(m + "\n")

        out.write("\n")


# הדפסת מספר החלבונים הכולל
out.write("Number of proteins containing Zinc Finger Motif: " + str(counter))

file.close()
out.close()

print("Finished ✅")