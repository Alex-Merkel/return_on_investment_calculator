class RentalReturnPercent():
    def __init__(self, income=0, expenses=0, costs=0, flow=0):
        self.income = income
        self.expenses = expenses
        self.costs = costs
        self.flow = flow

    # take in monthly income
    def monthlyIncome(self):
        try:
            self.income = int(input("What is your total monthly rental income? "))
        except:
            print("Please enter whole numbers only (no commas, periods, etc.).\n")
            self.income = int(input("What is your total monthly rental income (in only whole numbers)? "))

    # take in monthly expenses
    def monthlyExpenses(self):
        try:
            self.expenses = int(input("What are your total monthly rental expenses (taxes, utilities, mortgage, management fee, etc.)? "))
        except:
            print("Please enter whole numbers only (no commas, periods, etc.).\n")
            self.expenses = int(input("What are your total monthly rental expenses (in only whole numbers)? (taxes, utilities, mortgage, management fee, etc.) "))

    # take in upfront costs (dp, cc, misc)
    def upfrontCosts(self):
        try:
            self.costs = int(input("What are your total upfront cash costs (down payment, closing costs, renovations, etc.)? "))
        except:
            print("Please enter whole numbers only (no commas, periods, etc.).\n")
            self.costs = int(input("What are your total upfront cash costs (in only whole numbers)? (down payment, closing costs, renovations, etc.) "))
        
    # calculate cash flow (Mon income - mon expenses)
    def cashFlow(self):
        self.flow = self.income - self.expenses

    # calculate ROI (Annual cash flow / upfront costs)
    def roiPercentage(self):
        answer = float((self.flow * 12) / self.costs)
        print(f'\nYour cash on cash Return on Investment(ROI) percentage for this property is, {answer * 100}%!')

# create a class
my_returnPercent = RentalReturnPercent()

# run () to run all the methods
def run(ROI):
    ROI.monthlyIncome()
    ROI.monthlyExpenses()
    ROI.upfrontCosts()
    ROI.cashFlow()
    ROI.roiPercentage()

run(my_returnPercent)
