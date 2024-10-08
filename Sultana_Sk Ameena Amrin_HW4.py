#6-1
Jasmine = {
    "first_name": "jasmine" , 
    "last_name" : "Haniff" , 
    "age" : 18 ,
    "city" : "New York"
}

print("First Name - ", Jasmine["first_name"])
print("Last Name - ", Jasmine["last_name"])
print("Age - " , Jasmine ["age"])
print("City - ", Jasmine["city"])

#6-2

Fav_Numbers =  { "Amrin": "Amrin's Favorite number is  96",
                "Jasmine": "Jasmine's Favorite number is  12",
                "Joey": "Joey's Favorite number is  96",
                "Suba" :"Suba's Favorite number is 74",
                "Elma":"Elma's Favorite number is  12"  }

print("Amrin - ",Fav_Numbers["Amrin"])
print("Jasmine - ",Fav_Numbers["Jasmine"])
print("Joey - ",Fav_Numbers["Joey"])
print("Suba - ",Fav_Numbers["Suba"])
print("Elma - ",Fav_Numbers["Elma"])

#6-3
Prog_words = {"Var" : "Var is the short form of variable." ,
              "Loop":"A system/action that occurs repeatedly.",
              "Data type": "Type of data a variable can hold",
              "Indentation" : "The space that is used to define code blocks",
              "Comment" : " The line of code that is avoided in programming language."

}
print("Var - ",Prog_words["Var"])
print("Loop - ",Prog_words["Loop"])
print("Data type - ",Prog_words["Data type"])
print("Indentation - ",Prog_words["Indentation"])
print("Comment - ",Prog_words["Comment"])

#6-4

Prog_words = {"Var" : "Var is the short form of variable." ,
              "Loop":"A system/action that occurs repeatedly.",
              "Data type": "Type of data a variable can hold",
              "Indentation" : "The space that is used to define code blocks",
              "Comment" : " The line of code that is avoided in programming language.",
              "List" :  "Collection of coding statements.",
              "Dictionary":"Collection of Key-value pairs",
              "If-Else": "A conditional statements which defines if the statement is true or false and execute accordingly.",
              "Syntax-error": "An error wth Syntax.",
              "Operator":"Symbols to find operate."
}

for key,value in Prog_words.items():
    print(f"\nkey:{key}")
    print(f"Value:{value}")

    
    #6-5
    Rivers = {"Nile":"Egypt",
               "Turag":"Bangladesh",
               "Misissipi":"America",
               "Meckenzie":"Canada",
               "Amazon": "Brazil"
               }


print("\nRivers:")
for river in Rivers.keys():
    print(river)

print("\nCountries:")
for country in Rivers.values():
    print(country)


# 6-6
Favorite_languages = {
    "Jen": "Python",
    "Amrin": "Java",
    "Elma": "C++",
    "Jasmine": "JavaScript"
}

poll = ["Jen", "Amrin", "Elma", "Jasmine"]

for people in poll:
    if people in Favorite_languages:
        print(f"Thank you for the poll, {people.title()}.")
    else:
        print(f"Please take the poll, {people.title()}.")


        #6-7
        people_1 =[ 
             {
    "first_name": "jasmine" , 
    "last_name" : "Haniff" , 
    "age" : 18 ,
    "city" : "New York"
    },
    {"first_name": "Amrin" , 
    "last_name" : "Sultana" , 
    "age" : 20,
    "city" : "New York"
    },
    {"first_name": "Joey" , 
    "last_name" : "Samson" , 
    "age" : 22 ,
    "city" : "New York"
    }
        ]

        for people in people_1:
            print(people["first_name"])
            print(people["last_name"])
            print(people["age"])
            print(people["city"])

#6-8
Pets= [
    {
        "Animal_Type": "Cat",
        "Owner": "Adrita"
    },
    {
        "Animal_Type": "Snake",
        "Owner": "Amrin"
    },
    {
        "Animal_Type": "Monkey",
        "Owner": "Jasmine"
    }
]

for pet in Pets:
    print(pet["Animal_type"])
    print(pet["Owner"])
    

    #6-9
    Fav_places= {
        "Amrin":["Paris","Istanbul","New York"],
        "Saira":["Cape Town","LA","Santorini"],
        "Ana":["Chicago","Florida","Sydney"],

    }
    for name , place in Fav_places:
        print(name)
        for place in Fav_places:
            print(place)
            print()

#6-10
Fav_Numbers =  { "Amrin": "Amrin's Favorite number are  96,7,21,84986",
                "Jasmine": "Jasmine's Favorite number is  4,12,84",
                "Joey": "Joey's Favorite number is  33,11,22,6",
                "Suba" :"Suba's Favorite number is 81,00,72,27",
                "Elma":"Elma's Favorite number is  89,90,09,12"  }


print("Amrin - ",Fav_Numbers["Amrin"])
print("Jasmine - ",Fav_Numbers["Jasmine"])
print("Joey - ",Fav_Numbers["Joey"])
print("Suba - ",Fav_Numbers["Suba"])
print("Elma - ",Fav_Numbers["Elma"])

#6-11
cities = {
    "New York": {
        "country": "United States",
        "population": "8.336M" ,
        "fact": "People don't care in NY"
    },
    "Dhaka": {
        "country": "Bangladesh",
        "population": "10.2M",
        "fact": "Peple care too much in Dhaka"
    },
     "Paris": {
        "country": "France",
        "population": "2.16M",
        "fact": "The City of Lights."
    },

    }

for city, information in cities.items():
    print(f"{city}:")
    for key, value in information.items():
        print(f"\t{key}: {value}")







