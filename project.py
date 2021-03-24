f = open('Groups.txt', '+w', encoding='utf-8')
class Band:
    def __init__(self, name, participants, date):
        self.name = name
        self.participants = participants.split(',')
        self.date = date
        self.albums = []
        self.n = 0
    def add_album(self, album_name, date, songs):
        self.n += 1
        return self.albums.append(f'name : {album_name}, date : {date}, songs : {songs}')
    def __str__(self):
        return f'{self.name}\n\nParticipants:\n\n{self.participants}\nDate of creation: {self.date}\n\nAlbums\n{self.albums}\n\n\n'
work = True
while work:
    band_name = input('Enter band\'s name: ')
    while True:
        band_participants = input('Enter band\'s participants separated by comma (e.g. "Oleg, Kakashi"): ')
        if ',' not in band_participants and ' ' in band_participants:
            print('Enter the value in a right way')
            continue
        else:
            break
    while True:
        try:
            band_date = int(input('Enter the year of band\'s creation: '))
            if band_date <= 1900 or band_date >= 2022:
                print('Enter the right value')
                continue
            else:
                add_album = True
                break
        except ValueError:
            print('Enter the value in a right way')
            continue
    band = Band(band_name, band_participants, band_date)
    while add_album:
        while True:
            try:
                nascar = int(input('If you want to add an album enter 1, if you want to add a new band enter 2, if you want to stop enter 3: '))
                if nascar <= 0 or nascar >= 4:
                    print('Enter the right value')
                    continue
                else: 
                    break
                break
            except ValueError:
                print('Enter the value in a right way')
                continue
        if nascar == 1:
                while True:
                    band_album_name = input('Enter album name: ')
                    band_album_date = input('Enter date of the album released: ')
                    while True:
                        band_album_songs = input('Enter album songs separated by comma (e.g. "Цветы в вазе, Зать"): ')
                        if ',' not in band_album_songs:
                            print('Enter the value in a right way')
                            continue
                        else:
                            break
                    band.add_album(band_album_name, band_album_date, band_album_songs)
                    while True:
                        try:
                            glass_of_water = int(input('If you want to continue enter 1, if you want to add a new band enter 2, if you want to stop enter 3: '))
                            if glass_of_water <= 0 or glass_of_water >= 4:
                                print('Enter the right value')
                                continue
                            else:
                                break
                        except ValueError:
                            print('Enter the value in a right way')
                            continue
                    if glass_of_water == 1:
                        break
                    elif glass_of_water == 2:
                        f.write(str(band))
                        add_album = False
                        break
                    elif glass_of_water == 3:
                        f.write(str(band))
                        add_album = False
                        work = False
                        break
                        
        elif nascar == 2:
            f.write(str(band))
            add_album = False
        elif nascar == 3:
            f.write(str(band))
            add_album = False
            work = False
            break