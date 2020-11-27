from math import ceil


class Warikan:

    def calc_normal(self, total_bill, members):

        if members <= 0:
            return (0, 0)

        member_bill = ceil(total_bill / members)
        kanji_bill = (member_bill * members) - total_bill
        
        return member_bill, kanji_bill 

    def calc(self, total_bill, normal_members, large_members, small_members):
        return (0, 0, 0, 0) 
