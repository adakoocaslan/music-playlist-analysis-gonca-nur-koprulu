# [span_1](start_span)Bu fonksiyon listedeki tüm şarkıların sürelerini toplar[span_1](end_span)
def get_total_duration(songs):
    total = 0
    for song in songs:
        total += song["duration"]
    return total


# [span_2](start_span)Bu fonksiyon listenin ortalama süresini hesaplar[span_2](end_span)
def get_average_duration(songs):
    if len(songs) == 0:
        return 0
    return get_total_duration(songs) / len(songs)


[span_3](start_span)
Bu
fonksiyon
en
çok
dinlenen
şarkıyı
bulur[span_3](end_span)


def get_most_played_song(songs):
    if not songs:
        return None
    most_played = songs[0]
    for song in songs:
        if song["plays"] > most_played["plays"]:
            most_played = song
    return most_played


# [span_4](start_span)Bu fonksiyon şarkıları düzenli bir şekilde ekrana yazdırır[span_4](end_span)
def print_playlist(songs):
    print("\n--- Müzik Listesi ---")
    for song in songs:
        print(
            f"Şarkı: {song['title']} | Sanatçı: {song['artist']} | Süre: {song['duration']}s | Dinlenme: {song['plays']}")
    print("-" * 25)


# [span_5](start_span)Ana program akışı[span_5](end_span)
def main():
    # [span_6](start_span)En az 5 şarkıdan oluşan veri yapısı[span_6](end_span)
    # NOT: Gonca ve İbrahim'in ödevinde bu isimleri ve sayıları değiştir!
    songs = [
        {"title": "Müphem", "artist": "Mabel Matiz", "duration": 210, "plays": 55000},
        {"title": "Antidepresan", "artist": "Mert Demir", "duration": 190, "plays": 72000},
        {"title": "Bi' Tek Ben Anlarım", "artist": "KÖFN", "duration": 205, "plays": 81000},
        {"title": "Ali Cabbar", "artist": "Emir Can İğrek", "duration": 220, "plays": 94000},
        {"title": "Ateşini Yolla Bana", "artist": "Hakan Peker", "duration": 185, "plays": 32000}
    ]

    # [span_7](start_span)Metotların aktif olarak çağırılması[span_7](end_span)
    print_playlist(songs)

    total = get_total_duration(songs)
    avg = get_average_duration(songs)s
    most_played = get_most_played_song(songs)
    #

    print(f"Toplam Çalma Süresi: {total} saniye")
    print(f"Ortalama Şarkı Süresi: {avg:.2f} saniye")
    print(f"En Çok Dinlenen Şarkı: {most_played['title']} ({most_played['plays']} dinlenme)")


# Programı çalıştıran tetikleyici
if __name__ == "__main__":
    main()