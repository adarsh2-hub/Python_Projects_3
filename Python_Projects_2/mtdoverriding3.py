class Bank:
    def get_interest_rate(self):
        pass
class SBI(Bank):
    def get_interest_rate(self):
        print("SBI interest rate is 7%..")
class HDFC(Bank):
    def get_interest_rate(self):
        print("HDFC interest rate is 7.5%..")
bank=Bank()
sbi=SBI()
hdfc=HDFC()
sbi.get_interest_rate()
hdfc.get_interest_rate()