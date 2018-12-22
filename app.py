
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
           
