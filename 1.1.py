TickType = input('input')
while TickType not in ('E','S'):
    TickType = input('qw')

BaggageWeight = int(input('weight'))

if TickType == 'E':
    All = 16
    Carge = 3.5
else:
    All = 20
    Carge = 5.75

ExWeight = BaggageWeight - All

if ExWeight > 0:
    Ex = ExWeight * Carge
else:
    Ex = 0

print(Ex)
