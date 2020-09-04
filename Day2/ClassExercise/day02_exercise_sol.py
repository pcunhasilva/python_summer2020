# An exercise 

class Senator():
  def __init__(self, name):
    self.name = name
    self.bills_voted_on = [] ## list of Bill objects

  def vote(self, bill, choice):
    if choice not in ['yes', 'no', 'abstain']:  return print('Not a valid option.')
    bill.votes[choice].append(self.name)
    self.bills_voted_on.append(bill)
    return 'Senator ' + self.name + ' vote ' + choice + ' on ' + bill.title + ' bill.'

  def __str__(self): # print method
    return 'Senator {}'.format(self.name)


class Bill():
  def __init__(self, title):
    self.title = title
    self.votes = {"yes" : [], "no" : [], "abstain" : []}
    self.passed = None

  def __str__(self): # Print method
    return self.title + " Bill"

  def result(self):
    if len(self.votes['yes']) > len(self.votes['no']):
      self.passed = True
    else:
      self.passed = False
    return self.passed

## should be able to do these things
jane = Senator("Jane")
print(jane)
jack = Senator("Jack")
print(jack)
environment = Bill("Environmental Protection")
print(environment)
jane.vote(environment, "yes")
jack.vote(environment, "no")
environment.votes['yes']
environment.votes['no']
environment.result()
print(jack.bills_voted_on[0].passed)
