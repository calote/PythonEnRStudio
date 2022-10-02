download.file(url = "https://raw.githubusercontent.com/roberthryniewicz/datasets/master/airline-dataset/flights/flights.csv",
              destfile = "flights.csv")



library(reticulate)
source_python("ejemplo04.py")
flights <- read_flights("flights.csv")

library(ggplot2)
ggplot(flights, aes(CarrierDelay, ArrDelay)) + 
  geom_point() + 
  geom_jitter()
