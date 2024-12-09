data = [12, 11, 13, 5, 6]
print ("Array sebelum diurutkan:", data)
# Menentukan panjang array
n = len(data)

# Melakukan Insertion Sort
for i in range(1, n):
    key = data[i]  # Elemen yang akan disisipkan
    j = i - 1

    # Pindahkan elemen yang lebih besar dari key ke satu posisi di depan
    while j >= 0 and data[j] > key:
        data[j + 1] = data[j]
        j -= 1

    # Menempatkan key di posisi yang benar
    data[j + 1] = key

# Menampilkan hasil
print("Array setelah diurutkan:", data)
