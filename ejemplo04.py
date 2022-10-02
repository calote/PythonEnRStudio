import pandas

def read_flights(file):
  flights = pandas.read_csv(file)
  flights=flights[flights['Dest']=="TPA"]
  flights=flights[['CarrierDelay','DepDelay', 'ArrDelay']]
  flights=flights.dropna()
  return flights
