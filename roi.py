def responseAsInt(text):
    while True:
        try:
            response = int(input(text))
            return response
        except ValueError:
            print("Please enter whole numbers only (no commas, periods, blanks, words, etc.).\n")


class RentalReturnPercent():
    def __init__(self, income=0, expenses=0, costs=0, flow=0):
        self.income = income
        self.expenses = expenses
        self.costs = costs
        self.flow = flow
    

    # take in monthly income
    def monthlyIncome(self):
        print("\nPlease use only whole numbers for ALL answers (no commas, decimals, blanks, words, etc.). We'll start with monthly income...\n")
        while True:
                rental = responseAsInt("What is your monthly rental income? ")
                laundry = responseAsInt("What is your monthly laundry income? ")
                storage = responseAsInt("What is your monthly storage income? ")
                misc = responseAsInt("What is your monthly miscellaneous income? ")
                if misc != "":
                    break
            
        self.income = rental + laundry + storage + misc
        print(f"\nYour total monthly income is: ${self.income}. Next up is monthly expenses...\n")


    # take in monthly expenses
    def monthlyExpenses(self):
        while True:
            tax = responseAsInt("What is your monthly tax expense? ")
            insurance = responseAsInt("What is your monthly insurance expense? ")
            utilities = responseAsInt("What are your monthly utility expenses (electric, water, sewer, gas, garbage, etc.)? ")
            hoa = responseAsInt("What is your monthly HOA (Home Owner's Association) expense? ")
            lawns = responseAsInt("What is your monthly lawn/snow removal expense? ")
            vacancy = responseAsInt("What is your monthly vacancy expense? ")
            repairs = responseAsInt("What is your monthly repair expense? ")
            capex = responseAsInt("What is your monthly capital expenditures amount? ")
            management = responseAsInt("What is your monthly management fee expense? ")
            mortgage = responseAsInt("What is your monthly mortgage expense? ")
            if mortgage != "":
                break
            
        self.expenses = tax + insurance + utilities+ hoa + lawns + vacancy + repairs + capex + management + mortgage
        print(f"\nYour total monthly expenses are: ${self.expenses}. Finally, we have upfront cash expenses...\n")


    # take in upfront costs (dp, cc, misc)
    def upfrontCosts(self):
        while True:
            down_payment = responseAsInt("How much was your down payment? ")
            closing_costs = responseAsInt("How much were your closing costs? ")
            rehab_budget = responseAsInt("How much was your rehab/renovations? ")
            misc_other = responseAsInt("How much were your miscellaneous cash expenses? ")
            if misc_other != "":
                break
         
        self.costs = down_payment + closing_costs + rehab_budget + misc_other
        print(f"\nYour total upfront cash costs are: ${self.costs}")
        

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