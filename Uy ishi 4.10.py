# class Talaba:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# class Kurs:
#     def __init__(self, kurs_name, kurs_teacher):
#         self.kurs_name = kurs_name
#         self.kurs_teacher = kurs_teacher
#         self.talabalar_soni = 0
#         self.talabalar = []
#
#     def ass(self, new_student):
#         self.talabalar.append(new_student)
#         self.talabalar_soni += 1
#
#     def delete(self, student_name):
#         for student in self.talabalar:
#             if student.name == student_name:
#                 self.talabalar.remove(student)
#                 self.talabalar_soni -= 1
#                 break
#
#     def info_kurs(self):
#         print(f"Kurs: {self.kurs_name}, O'qituvchi: {self.kurs_teacher}, Talabalar soni: {self.talabalar_soni}")
#         for student in self.talabalar:
#             print(f" - {student.name}, Yosh: {student.age}")
#
# kurs1 = Kurs("Matematika", "Mr. Ali")
# for i in range(10):
#     talaba = Talaba(f"Talaba {i+1}", 18 + i)
#     kurs1.ass(talaba)
#
#
# kurs2 = Kurs("Fizika", "Ms. Fatima")
# for i in range(10):
#     talaba = Talaba(f"Talaba {i+11}", 18 + i)
#     kurs2.ass(talaba)
#
# print("Matematika kursi:")
# kurs1.info_kurs()
# print("\nFizika kursi:")
# kurs2.info_kurs()
#
# kurs1.delete("Talaba 3")
# kurs2.delete("Talaba 12")
#
# print("\nYangilangan Matematika kursi:")
# kurs1.info_kurs()
# print("\nYangilangan Fizika kursi:")
# kurs2.info_kurs()
# import datetime
#
# class Telegram:
#     def __init__(self, user_name):
#         self.user_name = user_name
#         self.send_chat_text = ""
#         self.accept_chat_text = ""
#         self.chat_status = ""
#         self.chat_time = None
#
#     def kiritish(self, user_name):
#         self.user_name = user_name
#         print(f"User nomi: {self.user_name}")
#
#     def send(self, other, message):
#         self.send_chat_text = message
#         other.accept_chat_text = message
#         other.chat_status = "sending"
#         other.chat_time = datetime.datetime.now()
#         print(f"{self.user_name} xabar yubordi: {message} (Status: {other.chat_status})")
#
#     def read(self):
#         if self.accept_chat_text:
#             self.chat_status = "reading"
#             print(f"{self.user_name} xabarni o'qidi: {self.accept_chat_text} (Status: {self.chat_status})")
#         else:
#             print(f"{self.user_name} uchun xabar yo'q.")
#
#     def delete(self):
#         self.accept_chat_text = ""
#         self.chat_status = "deleting"
#         print(f"{self.user_name} xabarni o'chirdi (Status: {self.chat_status})")
#
# user1 = Telegram("VASTELORD")
# user1.kiritish("VASTELORD")
#
# user2 = Telegram("LATIF")
# user2.kiritish("LATIF")
#
# user1.send(user2, "Salom, LATIF!")
#
# user2.read()
#
# user2.delete()
# class Karta:
#     def __init__(self, card_name):
#         self.card_name = card_name
#
#     def kiritish(self, card_name):
#         self.card_name = card_name
#         print(f"Karta nomi: {self.card_name}")
#
#     def chiqarish(self):
#         return self.card_name
#
#     def compare(self, other):
#         card_values = {
#             '2': 2,
#             '3': 3,
#             '4': 4,
#             '5': 5,
#             '6': 6,
#             '7': 7,
#             '8': 8,
#             '9': 9,
#             '10': 10,
#             'J': 11,
#             'Q': 12,
#             'K': 13,
#             'A': 14
#         }
#
#         self_value = card_values[self.card_name]
#         other_value = card_values[other.card_name]
#
#         if self_value > other_value:
#             return 1
#         elif self_value < other_value:
#             return -1
#         else:
#             return 0
#
# player1 = Karta("K")
# player2 = Karta("9")
#
# print(f"Player 1 kartasi: {player1.chiqarish()}")
# print(f"Player 2 kartasi: {player2.chiqarish()}")
#
# result = player1.compare(player2)
#
# if result == 1:
#     print("Player 1 g'olib!")
# elif result == -1:
#     print("Player 2 g'olib!")
# else:
#     print("Kartalar teng!")
# class Alphabet:
#     def __init__(self, til, harflar):
#         self.til = til
#         self.harflar = harflar
#
#     def harflarni_chiqar(self):
#         return self.harflar
#
#     def harflarni_sanash(self):
#         return len(self.harflar)
#
#
# class EngAlphabet(Alphabet):
#     def __init__(self):
#         super().__init__('English', list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
#         self.harf_soni = len(self.harflar)
#
#     def alfavitni_sanash(self):
#         return self.harf_soni
#
#     def harf_tegishliligini_tekshirish(self, harf):
#         return harf in self.harflar
#
#     def example_text(self):
#         return "This is an example sentence in English."
#
#
# eng_alphabet = EngAlphabet()
#
# print("Harflar:", eng_alphabet.harflarni_chiqar())
#
# print("Harflar soni:", eng_alphabet.alfavitni_sanash())
#
# print("'F' harfi tegishlimi:", eng_alphabet.harf_tegishliligini_tekshirish('F'))
#
# print("'щ' harfi tegishlimi:", eng_alphabet.harf_tegishliligini_tekshirish('щ'))
#
# print("Example text:", eng_alphabet.example_text())
