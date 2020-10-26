## intent:affirm
- yes
- yep
- yeah
- indeed
- that's right
- ok
- great
- right, thank you
- correct
- great choice
- sounds really good
- thanks

## intent:goodbye
- bye
- goodbye
- good bye
- stop
- end
- farewell
- Bye bye
- have a good one

## intent:greet
- hey
- howdy
- hey there
- hello
- hi
- good morning
- good evening
- dear sir
- heyyy

## intent:restaurant_search
- i'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bengaluru](location)
- show me [chinese](cuisine) restaurants
- show me [chines]{"entity": "cuisine", "value": "chinese"} restaurants in the [New Delhi]{"entity": "location", "value": "Delhi"}
- show me a [mexican](cuisine) place in the [centre](location)
- i am looking for an [indian](cuisine) spot called olaolaolaolaolaola
- search for restaurants
- anywhere in the [west](location)
- I am looking for [asian fusion](cuisine) food
- I am looking a restaurant in [294328](location)
- [South Indian](cuisine)
- [North Indian](cuisine)
- [Italian](cuisine)
- [Chinese]{"entity": "cuisine", "value": "chinese"}
- [chinese](cuisine)
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican indian fusion](cuisine)
- can you book a table in [rome](location) in a [moderate]{"entity": "price", "value": "mid"} price range with [british](cuisine) food for [four]{"entity": "people", "value": "4"} people
- [central](location) [indian](cuisine) restaurant
- please help me to find restaurants in [pune](location)
- Please find me a restaurant in [Bengaluru](location)
- show me restaurants
- please find me [chinese](cuisine) restaurant in [delhi](location)
- can you find me a [chinese](cuisine) restaurant
- please find me a restaurant in [ahmedabad](location)
- please show me a few [italian](cuisine) restaurants in [Bengaluru](location)
- search
- search restaurants
- restaurants near me
- fine me restaurants
- restuarant in [khopoli](detectLocation)
- search in [kanpur](detectLocation)
- food in [nagpur](detectLocation)
- [North Indian](cuisine)

## intent:int_locationDetect
- [khopoli](detectLocation)
- [sion](detectLocation)
- [dombivali](detectLocation)
- [thane](detectLocation)
- [kalyan](detectLocation)
- [Lithuania](detectLocation)
- [delhi](detectLocation)
- [mumbai](detectLocation)
- in [Gurgaon](detectLocation)
- Oh, sorry, in [Italy](detectLocation)
- in [khopoli](detectLocation)
- in [sion](detectLocation)
- in [dombivali](detectLocation)
- in [thane](detectLocation)
- [badlapur](detectLocation)
- [shelu](detectLocation)
- [neral](detectLocation)
- [bhivpuri](detectLocation)
- [karjat](detectLocation)
- [palasdhari](detectLocation)
- [panvel](detectLocation)
- [kharghar](detectLocation)
- [loc_Yes](confirmLocation)
- [loc_No](confirmLocation)
- [Mumbai](detectLocation)
- [khalapur](detectLocation)
- [kolhapur](detectLocation)
- search in [kolhapur](detectLocation)
- [loc_No](confirmLocation)
- [hinjewadi](detectLocation)
- [loc_Yes](confirmLocation)

## synonym:4
- four

## synonym:Bengaluru
- bengaluru
- banglore
- Banglore

## synonym:Delhi
- New Delhi
- dilli
- delhi

## synonym:Kolkata
- calcutta
- Calcutta
- kolkata

## synonym:Mumbai
- bombay
- Bombay
- mumbai

## synonym:Pune
- pune
- poona
- Poona

## synonym:chinese
- chines
- Chinese
- Chines

## synonym:mid
- moderate

## synonym:vegetarian
- veggie
- vegg

## regex:detectLocation
- ^[A-Za-z]+$

## regex:greet
- hey[^\s]*

## regex:pincode
- [0-9]{6}
