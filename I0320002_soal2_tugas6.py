n = int(input("Banyaknya data: "))
total = 0
i = 1

while i <= n:
    nilai_ujian = float(input("Nilai ujian ke-%d: " % i))
    total += nilai_ujian
    i = i + 1

nilai_rata_rata = total / n
print("Nilai rata-rata = %0.2f" % nilai_rata_rata)