from math import ceil


class Warikan:

    def calc(self, total_bill, members):

        member_bill = ceil(total_bill / members)
        kanji_bill = (member_bill * members) - total_bill
        
        return member_bill, kanji_bill 
