#!/usr/bin/env python
#-*- coding: utf-8 -*-

import random

correct_answers = {}
incorrect_answers = {}

def check_guess(guess, country, countries):
    if guess.lower() == countries[country].lower():
        return True
    else:
        return False

def main():
    countries = {
    "Afghanistan": "Kabul","Albania": "Tirana","Algeria": "Algiers","Andorra": "Andorra la Vella","Angola": "Luanda","Antigua and Barbuda": "Saint John's","Argentina": "Buenos Aires","Armenia": "Yerevan","Australia": "Canberra","Austria": "Vienna","Azerbaijan": "Baku",
    "Bahamas": "Nassau","Bahrain": "Manama","Bangladesh": "Dhaka","Barbados": "Bridgetown","Belarus": "Minsk","Belgium": "Brussels","Belize": "Belmopan","Benin": "Porto - Novo","Bhutan": "Thimphu","Bolivia": "Sucre","Bosnia and Herzegovina": "Sarajevo","Botswana": "Gaborone","Brazil": "Brasilia","Brunei": "Bandar Seri Begawan","Bulgaria": "Sofia","Burkina Faso": "Ouagadougou","Burundi": "Bujumbura",
    "Cabo Verde": "Praia","Cambodia": "Phnom Penh","Cameroon": "Yaounde","Canada": "Ottawa","Central African Republic": "Bangui","Chad": "N'Djamena","Chile": "Santiago","China": "Beijing","Colombia": "Bogotá","Comoros": "Moroni","Democratic Republic of the Congo": "Kinshasa","Republic of the Congo": "Brazzaville","Costa Rica": "San Jose","Cote d'Ivoire": "Yamoussoukro","Croatia": "Zagreb","Cuba": "Havana","Cyprus": "Nicosia","Czech Republic": "Prague",
    "Denmark": "Copenhagen","Djibouti": "Djibouti","Dominica": "Roseau","Dominican Republic": "Santo Domingo",
    "Ecuador": "Quito","Egypt": "Cairo","El Salvador": "San Salvador","Equatorial Guinea": "Malabo","Eritrea": "Asmara","Estonia": "Tallinn","Ethiopia": "Addis Ababa",
    "Fiji": "Suva","Finland": "Helsinki","France": "Paris",
    "Gabon": "Libreville","Gambia": "Banjul","Georgia": "Tbilisi","Germany": "Berlin","Ghana": "Accra","Greece": "Athens","Grenada": "Saint George's","Guatemala": "Guatemala City","Guinea": "Conakry","Guinea - Bissau": "Bissau","Guyana": "Georgetown",
    "Haiti": "Port - au - Prince","Honduras": "Tegucigalpa","Hungary": "Budapest",
    "Iceland": "Reykjavik","India": "New Delhi","Indonesia": "Jakarta","Iran": "Tehran","Iraq": "Baghdad","Ireland": "Dublin","Israel": "Jerusalem","Italy": "Rome",
    "Jamaica": "Kingston","Japan": "Tokyo","Jordan": "Amman",
    "Kazakhstan": "Astana","Kenya": "Nairobi","Kiribati": "Tarawa","Kosovo": "Pristina","Kuwait": "Kuwait City","Kyrgyzstan": "Bishkek",
    "Laos": "Vientiane","Latvia": "Riga","Lebanon": "Beirut","Lesotho": "Maseru","Liberia": "Monrovia","Libya": "Tripoli","Liechtenstein": "Vaduz","Lithuania": "Vilnius","Luxembourg": "Luxembourg",
    "Macedonia": "Skopje","Madagascar": "Antananarivo","Malawi": "Lilongwe","Malaysia": "Kuala Lumpur","Maldives": "Male","Mali": "Bamako","Malta": "Valletta","Marshall Islands": "Majuro","Mauritania": "Nouakchott","Mauritius": "Port Louis","Mexico": "Mexico City","Micronesia": "Palikir","Moldova": "Chisinau","Monaco": "Monaco","Mongolia": "Ulaanbaatar","Montenegro": "Podgorica","Morocco": "Rabat","Mozambique": "Maputo","Myanmar(Burma)": "Naypyidaw",
    "Namibia": "Windhoek","Nauru": "Yaren District","Nepal": "Kathmandu","Netherlands": "Amsterdam","New Zealand": "Wellington","Nicaragua": "Managua","Niger": "Niamey","Nigeria": "Abuja","North Korea": "Pyongyang","Norway": "Oslo",
    "Oman": "Muscat",
    "Pakistan": "Islamabad","Palau": "Ngerulmud","Palestine": "Jerusalem(East)","Panama": "Panama City","Papua New Guinea": "Port Moresby","Paraguay": "Asunción","Peru": "Lima","Philippines": "Manila","Poland": "Warsaw","Portugal": "Lisbon",
    "Qatar": "Doha",
    "Romania": "Bucharest","Russia": "Moscow","Rwanda": "Kigali",
    "Saint Kitts and Nevis": "Basseterre","Saint Lucia": "Castries","Saint Vincent and the Grenadines": "Kingstown","Samoa": "Apia","San Marino": "San Marino","Sao Tome and Principe": "São Tomé","Saudi Arabia": "Riyadh","Senegal": "Dakar","Serbia": "Belgrade","Seychelles": "Victoria","Sierra Leone": "Freetown","Singapore": "Singapore","Slovakia": "Bratislava","Slovenia": "Ljubljana","Solomon Islands": "Honiara","Somalia": "Mogadishu","South Africa": "Cape Town","South Korea": "Seoul","South Sudan": "Juba","Spain": "Madrid","Sri Lanka": "Sri Jayawardenepura Kotte","Sudan": "Khartoum","Suriname": "Paramaribo","Swaziland": "Mbabane(administrative), Lobamba","Sweden": "Stockholm","Switzerland": "Bern","Syria": "Damascus",
    "Taiwan": "Taipei","Tajikistan": "Dushanbe","Tanzania": "Dodoma","Thailand": "Bangkok","Timor - Leste": "Dili","Togo": "Lomé","Tonga": "Nukuʻalofa","Trinidad and Tobago": "Port of Spain","Tunisia": "Tunis","Turkey": "Ankara","Turkmenistan": "Ashgabat","Tuvalu": "Funafuti",
    "Uganda": "Kampala","Ukraine": "Kiev","United Arab Emirates": "Abu Dhabi","United Kingdom": "London","United States of America": "Washington, D.C.","Uruguay": "Montevideo","Uzbekistan": "Tashkent",
    "Vanuatu": "Port Vila","Vatican": "Vatican","Venezuela": "Caracas","Vietnam": "Hanoi","Yemen": "Sana'a",
    "Zambia": "Lusaka","Zimbabwe": "Harare"
    }

    again = "yes"

    while again.lower() == "yes":
        rand = random.randint(0, 196) #zgenerira nakljucna stevila

        country = countries.keys()[rand] # to je nov key

        guess = raw_input("Guess the capital of: " + country + ": ").lower()

        if check_guess(guess, country, countries) == True:
            correct_answers[country] = countries[country]
            print ("Congratulations!")
        else:
            incorrect_answers[country] = guess
            print ("Wrong answer! The capital is: " + countries[country])

        again = raw_input("Do you want to guess again? ")

    print ("END. Your answers are: ")

    with open("countries_capitals_answers.txt", "w+") as countries_capitals_answers_file:
        i = 1
        print ("Correct answers: ")
        countries_capitals_answers_file.write("Correct answers: \n \n")
        for country in correct_answers:
            if correct_answers[country]:
                print (str(i) + ". " + "Country: " + country + ";  Capital: " + countries[country])
                i += 1
                countries_capitals_answers_file.write(str(i - 1) + ". " + "Country: " + country + ";  Capital: " + countries[country] + "\n")

        i = 1
        print ("Incorrect answers: ")
        countries_capitals_answers_file.write("\n Incorrect answers: \n \n")
        for country in incorrect_answers:
            if incorrect_answers[country]:
                print (str(i) + ". " + "Country: " + country + ";  Incorrect answer: " + incorrect_answers[country] + ";  Capital: " + countries[country])
                i += 1
                countries_capitals_answers_file.write(str(i - 1) + ". " + "Country: " + country + ";  Incorrect answer: " + incorrect_answers[country] + ";  Capital: " + countries[country] + "\n")

        percentage = float(len(correct_answers)) / (float(len(correct_answers))+ float(len(incorrect_answers))) * 100
        print ("Your were correct in " + str("%.2f" % percentage) + "% of guesses")
        countries_capitals_answers_file.write("\n Your were correct in " + str("%.2f" % percentage) + "% of guesses.")

if __name__ == "__main__":
    main()