while low < high:
    # Menggunakan dua pointer
    left = low
    right = high

    # Mengurutkan elemen
    while left < right:
        # Mencari elemen yang lebih besar dari elemen di posisi 'left'
        while left < right and data[left] <= data[right]:
            right -= 1
        if left < right:
            data[left], data[right] = data[right], data[left]  # Tukar elemen

        # Mencari elemen yang lebih kecil dari elemen di posisi 'right'
        while left < right and data[left] <= data[right]:
            left += 1
        if left < right:
            data[left], data[right] = data[right], data[left]  # Tukar elemen

    # Menentukan batas untuk iterasi berikutnya
    if left - 1 > low:
        high = left - 1  # Update high untuk bagian kiri
    else:
        break  # Jika tidak ada elemen di kiri

    if left + 1 < high:
        low = left + 1  # Update low untuk bagian kanan
    else:
        break  # Jika tidak ada elemen di kanan

# Menampilkan hasil
print("Array setelah diurutkan:", data)
