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
- hi
- hi
- hello

## intent:restaurant_search
- i'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bengaluru](location)
- show me [chinese](cuisine) restaurants
- show me [chines](cuisine:chinese) restaurants in the [New Delhi](location:Delhi)
- show me a [mexican](cuisine) place in the [centre](location)
- i am looking for an [indian](cuisine) spot called olaolaolaolaolaola
- search for restaurants
- anywhere in the [west](location)
- I am looking for [asian fusion](cuisine) food
- I am looking a restaurant in [294328](location)
- [South Indian](cuisine)
- [North Indian](cuisine)
- [Italian](cuisine)
- [Chinese](cuisine:chinese)
- [chinese](cuisine)
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican indian fusion](cuisine)
- can you book a table in [rome](location) in a [moderate](price:mid) price range with [british](cuisine) food for [four](people:4) people
- [central](location) [indian](cuisine) restaurant
- please help me to find restaurants in [pune](location)
- Please find me a restaurant in [Bengaluru](location)
- show me restaurants
- please find me [chinese](cuisine) restaurant in [delhi](location)
- can you find me a [chinese](cuisine) restaurant
- please find me a restaurant in [ahmedabad](location)
- please show me a few [italian](cuisine) restaurants in [Bengaluru](location)
- search

## intent: int_locationDetect
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
## synonym:4
- four

## synonym:Delhi
- New Delhi
- dilli
- delhi

## synonym:Bengaluru
- bengaluru
- banglore
- Banglore

## synonym:Mumbai
- bombay
- Bombay
- mumbai

## synonym:Kolkata
- calcutta
- Calcutta 
- kolkata

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

## regex:greet
- hey[^\s]*

## regex:pincode
- [0-9]{6}

## regex:detectLocation
- ^[A-Za-z]+$