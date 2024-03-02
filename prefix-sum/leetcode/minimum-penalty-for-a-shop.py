class Solution:
    def bestClosingTime(self, customers: str) -> int:
        # Since the penalty at i^th hour will be the sum of the suffix of the Y and the prefix of the Y
        # we can calculate using simple methods
        no_customer = 0
        having_customer = customers.count("Y")
        min_penality = no_customer + having_customer
        closing_hour = 0
        for i,cus in enumerate(customers):
            penality = no_customer + having_customer
            having_customer -= cus == "Y"
            no_customer += cus == "N"
            if penality < min_penality:
                closing_hour = i
                min_penality = min(penality,min_penality)
        if no_customer + having_customer < min_penality:
            closing_hour = len(customers)
        return closing_hour
        