
# def display_message(username):
#     print(f"Hello, {username.title()}!")
# display_message('jim')

# print("\n")
# def favorite_book(title):
#     print(f"One my of my favorite books is {title.title()}.")
# favorite_book('alice in wonderland')    

# #8.3

# def make_shirt(size, label):
#     print(f"Your size {size.title()} and label: {label.title()}.")
# make_shirt('l', 'adidas')    
# make_shirt('M', label='nike')   

# #8.4
# print("\n")
# def make_shirt(label, size='l'):
#     print(f"Your size {size.title()} and label: {label.title()}.")
# make_shirt('adidas', 'xl')    
# make_shirt(label='i love python')  

# #8.6
# print("\n")
# def city_country(city, country):
#     location = f"{city.title()}, {country.title()}!"
#     print(location)
# city_country('santiago', 'chili')    
# city_country('moscow', 'russia')    
# city_country('ukraine', 'kyiv')

# #8.7
# print("\n")

# def make_album(name_song, name_album, track=None):
#     mus_album = {'song': name_song, 'album': name_album}
#     if track:
#         mus_album['track'] = track
#     return mus_album
# musicant_0 = make_album('linkin park', 'meteora')
# musicant_1 = make_album('linkin', 'meteorizm', track=12)
# musicant_2 = make_album('park', 'ora')
# print(musicant_0)    
# print(musicant_1)    
# print(musicant_2)    

# #8.8
# print("\n")
# while True:
#     print("\nPlease enter album: ")
#     print("\n(enter 'q' at any time quit)")

#     n_song = input("Name song: ")
#     if n_song == 'q':
#         break

#     n_album = input("Name album: ")
#     if n_album == 'q':
#         break
#     formatted_album = make_album(n_song, n_album)
#     print(f"Wow, new album: {formatted_album}")


#8.9



# def show_message(welcomes):
#     """Вывод приветствия"""
#     for welcome in welcomes:
#         print(f"{welcome.title()} my friend!")        

# message_list = ['good morning', 'good afternoon' , 'good night']
# show_message(message_list)

#8.10 and 8.11


def send_message(message_list, sent_message):
    """Отправленные сообщения перемещаются в sent_message"""
    while message_list:
        current_msg = message_list.pop()
        sent_message.append(current_msg)


def show_message(welcomes):
    """Вывод приветствия"""
    for welcome in welcomes:
        print(f"{welcome.title()} my friend!")        

message_list = ['good morning', 'good afternoon' , 'good night']
sent_message = []

send_message(message_list[:], sent_message) # Copy list message_list
show_message(sent_message)
print(message_list)
print(sent_message)


#8.12
print("\n")
def component_sandwich(*component):
    """Выводит компоненты сандвича"""
    print(f"Ваш сандвич состоит из: {component}")

component_sandwich('колбаса')    
component_sandwich('сыр', 'айсберг')    

#8.13
print("\n")
def build_profile(first, last, **user_info):
    """Строит с информацией о пользователе."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('alex', 'gri', year=1988, born='kemerovo')
print(user_profile)

