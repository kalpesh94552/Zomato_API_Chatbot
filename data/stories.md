## complete path 1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* int_locationDetect{"detectLocation": "Mumbai"}
    - slot{"detectLocation": "Mumbai"}
    - utter_confirm_location
* int_locationDetect{"confirmLocation": "loc_Yes"}
    - slot{"confirmLocation": "loc_Yes"}
    - act_detectLocation
    - slot{"location": "Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - act_checkLocation
    - slot{"slt_checkOp": true}
    - action_search_restaurants
    - slot{"emailContent": "Found Yauatcha in 206, 2nd Floor, Krystal, Waterfield Road, Linking Road, Bandra West, Mumbai\nFound Hakkasan in 206, 2nd Floor, Krystal, Waterfield Road, Linking Road, Bandra West, Mumbai\nFound The Fatty Bao in Ground Floor, Summerville, 33rd Road, Linking Road, Bandra West, Mumbai\nFound Yazu - Pan Asian Supper Club in 9, Ground Floor, Raheja Classic Complex, Near Infinity Mall, Phase D, Shastri Nagar, Oshiwara, Andheri West, Mumbai\nFound Facing East in JVPD Scheme, 13th Road, Near Juhu Gymkhana, Juhu, Mumbai\n"}
    - act_sendEmail
    - utter_goodbye

## complete path 2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* int_locationDetect{"detectLocation": "khopoli"}
    - slot{"detectLocation": "khopoli"}
    - utter_confirm_location
* int_locationDetect{"confirmLocation": "loc_Yes"}
    - slot{"confirmLocation": "loc_Yes"}
    - act_detectLocation
    - slot{"location": "khopoli"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - act_checkLocation
    - slot{"slt_checkOp": false}
    - utter_dont_operate_in_area
    - utter_goodbye

* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* int_locationDetect{"detectLocation": "khalapur"}
    - slot{"detectLocation": "khalapur"}
    - utter_confirm_location
* int_locationDetect{"confirmLocation": "loc_No"}
    - slot{"confirmLocation": "loc_No"}
    - utter_ask_location
* int_locationDetect{"detectLocation": "kolhapur"}
    - slot{"detectLocation": "kolhapur"}
    - utter_confirm_location
* int_locationDetect{"confirmLocation": "loc_Yes"}
    - slot{"confirmLocation": "loc_Yes"}
    - act_detectLocation
    - slot{"location": "kolhapur"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - act_checkLocation
    - slot{"slt_checkOp": true}
    - action_search_restaurants
    - slot{"emailContent": "Found Littil Chinese & Roll in B-Ward, Rajarshi Shahu Feriwala, Khau Galli, Khasbag, Shahu Market Yard, Kolhapur\nFound China Dine Hotel in Chavan Chamber 1887, E Ward, 9th Lane, Rajarampuri, Kolhapur - 416008, Opposite Peter England And Omega Bar, Rajarampuri, Kolhapur\nFound WOK veg-non veg in DYP City, Food court 3rd floor old Pune Banglore Highway Kolhapur, Shahupuri, Kolhapur\nFound Cookies Chinese Center in 510/A e ward Near Bharti Vidyapeeth kadam wadi kolhapur, Ruikar Colony, Kolhapur, Kasaba Bawada, Kolhapur\nFound Chinu's Chinese Restaurant in Next to Kolhapur, Collector Office Road, Kanan Nagar, Urban Cooperative Bank, Tarabhai Park, Kolhapur\n"}
    - act_sendEmail
    - utter_goodbye

* greet
    - utter_greet
* restaurant_search{"detectLocation": "kanpur"}
    - slot{"detectLocation": "kanpur"}
    - utter_confirm_location
* int_locationDetect{"confirmLocation": "loc_No"}
    - slot{"confirmLocation": "loc_No"}
    - utter_ask_location
* int_locationDetect{"detectLocation": "kolhapur"}
    - slot{"detectLocation": "kolhapur"}
    - utter_confirm_location
* int_locationDetect{"confirmLocation": "loc_Yes"}
    - slot{"confirmLocation": "loc_Yes"}
    - act_detectLocation
    - slot{"location": "kolhapur"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - act_checkLocation
    - slot{"slt_checkOp": true}
    - action_search_restaurants
    - slot{"emailContent": "Found McDonald's in DY Patil City Mall, Plot 1 & CS 2104 /15, E-Ward, Next to Opal Hotel, Kawala Naka, Shahupuri, Kolhapur\nFound Laziz Pizza in Kakade Building, 4th Lane, Opposite Natural Ice Cream, Rajarampuri, Kolhapur\nFound Castle in 2014/15, DYP City Mall, E Ward, Kawala Naka, Opposite Sangam Talkies, Rajarampuri, Kolhapur\nFound Akkis Bistro in Shop 3 And 4, Near D Mart, Hind Nagar, Tarabhai Park, Kolhapur\nFound Davangiri Loni Dosa Centre in Ardha shivaji putala, Shivaji peth, Kolhapur, Mangalwar Peth, Kolhapur\n"}
    - act_sendEmail
    - slot{"emailContent": "Found McDonald's in DY Patil City Mall, Plot 1 & CS 2104 /15, E-Ward, Next to Opal Hotel, Kawala Naka, Shahupuri, Kolhapur\nFound Laziz Pizza in Kakade Building, 4th Lane, Opposite Natural Ice Cream, Rajarampuri, Kolhapur\nFound Castle in 2014/15, DYP City Mall, E Ward, Kawala Naka, Opposite Sangam Talkies, Rajarampuri, Kolhapur\nFound Akkis Bistro in Shop 3 And 4, Near D Mart, Hind Nagar, Tarabhai Park, Kolhapur\nFound Davangiri Loni Dosa Centre in Ardha shivaji putala, Shivaji peth, Kolhapur, Mangalwar Peth, Kolhapur\n"}
    - utter_goodbye

* greet
    - utter_greet
* restaurant_search{"detectLocation": "nagpur"}
    - slot{"detectLocation": "nagpur"}
    - utter_confirm_location
* int_locationDetect{"confirmLocation": "loc_No"}
    - slot{"confirmLocation": "loc_No"}
    - utter_ask_location
* int_locationDetect{"detectLocation": "hinjewadi"}
    - slot{"detectLocation": "hinjewadi"}
    - utter_confirm_location
* int_locationDetect{"confirmLocation": "loc_Yes"}
    - slot{"confirmLocation": "loc_Yes"}
    - act_detectLocation
    - slot{"location": "hinjewadi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - act_checkLocation
    - slot{"slt_checkOp": false}
    - utter_dont_operate_in_area
    - utter_goodbye
