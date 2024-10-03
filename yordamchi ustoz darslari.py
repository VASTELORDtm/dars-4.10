class BankAccount:
    def __init__(self, owner_name, card_number, card_code, balance):
        self.owner_name = owner_name
        self.card_number = card_number
        self.card_code = card_code
        self.balance = balance

    def transfer(self, amount, recipient_card_number, recipient_card_code):
        if self.card_number != recipient_card_number or self.card_code != recipient_card_code:
            print("Karta raqami yoki kodi noto'g'ri!")
            return

        if amount > self.balance:
            print("Yetarli pul yo'q!")
            return

        self.balance -= amount
        print(f"{self.owner_name} dan {amount} pul o'tkazildi.")
        print(f"Qolgan balans: {self.balance}")

account1 = BankAccount("VASTELORD", "1234-5678-9101-1121", "123", 10000)
account2 = BankAccount("GSGxLATIF_CMBK", "1111-2222-3333-4444", "456", 500)

account1.transfer(100, "1234-5678-9101-1121", "123")
account1.transfer(800, "1234-5678-9101-1121", "123")
account1.transfer(300, "1111-2222-3333-4444", "456")
