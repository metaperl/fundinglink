
class Loan:
    pass


class TMMCashAdvance(Loan):

    name = "TMM Cash Advance"

    def requirements(self):
        return self.corporate.age > 3 and self.corporate.rev = 5

    def description(self):
        return "Underwriting 24-48 hours
        - Funding 5-7 business days after offer acceptance"""

    def loan_size(self):
        """Average loan size is 20k - 400K """
        return range(5,5000)

    def rate(self):
        """(the higher risk client, higher the rate)"""
        return range(8, 39.9)

    def terms(self):
        return [6, 9, 12, 18, 24]

    def payback(self):
        return "By Daily Rate (M-F) set by lender for the term of the loan.  Taken directly from bank account."

    def apply(self):
        return """What documents are required: Cash Advance

1. 1 page application

2. 3 mos bank statements (all pages)

3. 3 months of credit merchant statements (all pages)

If not accepting credit cards, we only need 3 months bank statements
"""


class RogerPersonal(Loan):

    def requirements(self):
        return self.credit_profile.personal.length > 24 and self.credit_profile.personal.fico >= 680

    def description(self):
        return """No income or employment verification needed!"""

    def forms_of_capital(self):
        return "Lines of credit, installment loans and credit cards."

    def payment_terms(self):
        pass

    def amount(self):
        return range(0, 250)

    def success_fee(self):
