from math import ceil, floor
from decimal import Decimal, ROUND_HALF_UP


class Warikan:

    def calc_normal(self, total_bill, members):

        if members <= 0:
            return (0, 0)

        member_bill = ceil(total_bill / members)
        kanji_bill = (member_bill * members) - total_bill
        
        return member_bill, kanji_bill 

    def calc(self, total_bill, normal_members, large_members, small_members):

        ratio = small_members + normal_members * 2 + large_members * 3 

        if ratio <= 0:
            return (0, 0, 0, 0)
        
        bills = [(total_bill / ratio, small_members), (total_bill / ratio * 2, normal_members), (total_bill / ratio * 3, large_members)]

        round_bills = []
        kanji_bill = 0
        for each_bill, each_members in bills: 

            if each_members <= 0:
                round_bills.append(0)

            else:
                if each_bill%1 < 0.5:
                    round_bills.append(floor(each_bill))
                    kanji_bill += floor(each_bill) * each_members
                else:
                    round_bills.append(floor(each_bill)+1)
                    kanji_bill += (floor(each_bill)+1) * each_members

        kanji_bill -= total_bill

        return (round_bills[1], round_bills[2], round_bills[0], kanji_bill) 
