# Output welcome message and purpose of the program
print("Welcome to Bella's MAD LIBS")
print('The purpose of this program is to create a interactive MAD LIB.')
print('')

# Ask user to input a number 1-5 to choose a MAD LIB to do
MADLIB_choice = input('Enter a number 1,2, or 3 to choose which MAD LIB you want to complete. '
                      '\nIf you want to exit the game then enter 0: ')

while (MADLIB_choice != 1) and (MADLIB_choice != 2) and (MADLIB_choice != 3) and (MADLIB_choice != 0):
    print('You entered an incorrect input.')
    MADLIB_choice = input('Enter a number 1 through 3 to choose which MAD LIB you want to complete: '
                          '\nIf you want to exit the game then enter 0:')
    MADLIB_choice = int(MADLIB_choice)

while MADLIB_choice != 0:
    if MADLIB_choice == 1:
        print('You chose the Space MAD LIB!')
        print('')
        adjective_1 = input('Input an adjective: ')
        adjective_1 = (adjective_1).lower().strip()
        while adjective_1 != str(adjective_1):
            print('You did not enter a string. ')
            adjective_1 = input('Input an adjective: ')
            adjective_1 = str(adjective_1).lower().strip()

        person_1 = input('Enter the name of a person: ')
        person_1 = (person_1).lower().strip()
        while person_1 != str(person_1):
            print('You did not enter a string. ')
            person_1 = input('Input the name of a person: ')
            person_1 = str(person_1).lower().strip()

        adjective_2 = input('Input an adjective: ')
        adjective_2 = (adjective_2).lower().strip()
        while adjective_2 != str(adjective_2):
            print('You did not enter a string. ')
            adjective_2 = input('Input an adjective: ')
            adjective_2 = str(adjective_2).lower().strip()

        number_1 = input('Input a number: ')
        while number_1 != int(number_1):
            print('You did not enter an integer. ')
            number_1 = input('Input a number: ')
            number_1 = int(number_1)

        planet_1 = input('Input the name of a planet: ')
        planet_1 = (planet_1).lower().strip()
        while planet_1 != str(planet_1):
            print('You did not enter a string. ')
            planet_1 = input('Input the name of a planet: ')
            planet_1 = str(planet_1)

        food_1 = input('Input the name of food: ')
        food_1 = (food_1).lower().strip()
        while food_1 != str(food_1):
            print('You did not enter a string. ')
            food_1 = input('Input the name of food: ')
            food_1 = str(food_1)

        adjective_3 = input('Input an adjective: ')
        adjective_3 = (adjective_3).lower().strip()
        while adjective_3 != str(adjective_3):
            print('You did not enter a string. ')
            adjective_3 = input('Input an adjective: ')
            adjective_3 = str(adjective_3).lower().strip()

        verb_1 = input('Input a verb: ')
        verb_1 = (verb_1).lower().strip()
        while verb_1 != str(verb_1):
            print('You did not enter a string. ')
            verb_1 = input('Input a verb: ')
            verb_1 = str(verb_1).lower().strip()

        place_1 = input('Input a place: ')
        place_1 = (place_1).lower().strip()
        while place_1 != str(place_1):
            print('You did not enter a string. ')
            place_1 = input('Input a place: ')
            place_1 = str(place_1).lower().strip()

        person_2 = input('Enter the name of a person: ')
        person_2 = (person_2).lower().strip()
        while person_2 != str(person_2):
            print('You did not enter a string. ')
            person_2 = input('Input the name of a person: ')
            person_2 = str(person_2).lower().strip()

        object_1 = input('Enter the name of an object: ')
        object_1 = (object_1).lower().strip()
        while object_1 != str(object_1):
            print('You did not enter a string. ')
            object_1 = input('Input the name of an object: ')
            object_1 = str(object_1).lower().strip()

        print('')
        print("Last week, I decided to take a", adjective_1, "trip to outer space! "
                "\n I packed my spaceship with", person_1,"and some snacks for the journey. "
                "\n As I blasted off, I couldn’t stop", adjective_2, "with excitement.\n After "
                "traveling for", number_1, "light-years, I landed on a mysterious planet called "
                "", planet_1, ".\n The locals were friendly, but they only ate", food_1, "for "
                "breakfast.\n I was a bit", adjective_3, "but decided to try some.\n Suddenly, an "
                "alien appeared and asked me to", verb_1, "with him to the nearest \n ", place_1, "."
                " I thought, “What a weird place!” Just then, I heard a voice shout, \n"
                " It was none other than ", person_2, "! \n He told me that the aliens were actually "
                "collecting", object_1, " to send back to Earth. \n I joined their mission, and we "
                "all danced around \n in our space suits, laughing like there was no tomorrow!")

    elif MADLIB_choice == 2:
        print('You chose the Superhero MAD LIB!')
        print('')

        person_1 = input('Enter the name of a person: ')
        person_1 = (person_1).lower().strip()
        while person_1 != str(person_1):
            print('You did not enter a string. ')
            person_1 = input('Input the name of a person: ')
            person_1 = str(person_1).lower().strip()

        activity_1 = input('Enter the name of an activity: ')
        activity_1 = (activity_1).lower().strip()
        while activity_1 != str(activity_1):
            print('You did not enter a string. ')
            activity_1 = input('Input the name of a person: ')
            activity_1 = str(activity_1).lower().strip()

        school_grade = input('Enter the a grade level: ')
        while school_grade != (1 <= school_grade <= 12):
            print('You did not enter a string. ')
            school_grade = input('Input a grade level: ')
            school_grade = int(school_grade)

        food_1 = input('Input the name of food: ')
        food_1 = (food_1).lower().strip()
        while food_1 != str(food_1):
            print('You did not enter a string. ')
            food_1 = input('Input the name of food: ')
            food_1 = str(food_1)

        bug_type = input('Input the name of a bug: ')
        bug_type = (bug_type).lower().strip()
        while bug_type != str(bug_type):
            print('You did not enter a string. ')
            bug_type = input('Input the name of a bug: ')
            bug_type = str(bug_type)

        day_of_week = input('Input a day of the week: ')
        day_of_week = (day_of_week).lower().strip()
        while day_of_week != str(day_of_week):
            print('You did not enter a string. ')
            day_of_week = input('Input a day of the week: ')
            day_of_week = str(day_of_week)

        plant = input('Input the name of a plant: ')
        plant = (plant).lower().strip()
        while plant != str(plant):
            print('You did not enter a string. ')
            plant = input('Input the name of a plant: ')
            plant = str(plant)

        adjective_1 = input('Input an adjective: ')
        adjective_1 = (adjective_1).lower().strip()
        while adjective_1 != str(adjective_1):
            print('You did not enter a string. ')
            adjective_1 = input('Input an adjective: ')
            adjective_1 = str(adjective_1).lower().strip()

        color = input('Input a color: ')
        color = (color).lower().strip()
        while color != str(color):
            print('You did not enter a string. ')
            color = input('Input a color: ')
            color = str(color).lower().strip()

        number_1 = input('Input a number: ')
        while number_1 != int(number_1):
            print('You did not enter an integer. ')
            number_1 = input('Input a number: ')
            number_1 = int(number_1)

        clothing = input('Input a type of clothing: ')
        clothing = (clothing).lower().strip()
        while clothing != str(clothing):
            print('You did not enter a string. ')
            clothing = input('Input a color: ')
            clothing = str(clothing).lower().strip()

        smell = input('Input a type of smell: ')
        smell = (smell).lower().strip()
        while smell != str(smell):
            print('You did not enter a string. ')
            smell = input('Input a smell: ')
            smell = str(smell).lower().strip()

        movie = input('Input a movie: ')
        movie = (movie).lower().strip()
        while movie != str(movie):
            print('You did not enter a string. ')
            movie = input('Input a movie: ')
            movie = str(movie).lower().strip()

        verb_1 = input('Input a verb: ')
        verb_1 = (verb_1).lower().strip()
        while verb_1 != str(verb_1):
            print('You did not enter a string. ')
            verb_1 = input('Input a verb: ')
            verb_1 = str(verb_1).lower().strip()

        print("A superhero named", person_1, " is really, really good at", activity_1, ". They weren't always this"
                " way, when they were in ", school_grade, ", all they did was eat ", food_1, " and say mean "
                "things about ", bug_type, ". Then one day, on ", day_of_week, ", they stepped on a ", plant, ""
                " and started to transform. Their boring outfit suddenly became ", adjective_1, " and their"
                " hair turned ", color, ". The best part was they had ", number_1, " jewels on their ", clothing, " that"
                " sparkled in the sun. They smelled like ", smell, " and knew all the words to ", movie, ". Everyone"
                " wanted to be their friend so they could ", verb_1, " together.")

    elif MADLIB_choice == 3:
        print('You chose the Blob MAD LIB!')
        print('')

        adjective_1 = input('Input an adjective: ')
        adjective_1 = (adjective_1).lower().strip()
        while adjective_1 != str(adjective_1):
            print('You did not enter a string. ')
            adjective_1 = input('Input an adjective: ')
            adjective_1 = str(adjective_1).lower().strip()

        place_1 = input('Input a place: ')
        place_1 = (place_1).lower().strip()
        while place_1 != str(place_1):
            print('You did not enter a string. ')
            place_1 = input('Input a place: ')
            place_1 = str(place_1).lower().strip()

        noun_1 = input('Input a plural noun: ')
        noun_1 = (noun_1).lower().strip()
        while noun_1 != str(noun_1):
            print('You did not enter a string. ')
            noun_1 = input('Input a plural noun: ')
            noun_1 = str(noun_1).lower().strip()

        color = input('Input a color: ')
        color = (color).lower().strip()
        while color != str(color):
            print('You did not enter a string. ')
            color = input('Input a color: ')
            color = str(color).lower().strip()

        noun_2 = input('Input a plural noun: ')
        noun_2 = (noun_2).lower().strip()
        while noun_2 != str(noun_2):
            print('You did not enter a string. ')
            noun_2 = input('Input a plural noun: ')
            noun_2 = str(noun_2).lower().strip()

        verb_1 = input('Input a verb: ')
        verb_1 = (verb_1).lower().strip()
        while verb_1 != str(verb_1):
            print('You did not enter a string. ')
            verb_1 = input('Input a verb: ')
            verb_1 = str(verb_1).lower().strip()

        verb_2 = input('Input a verb ending with "ing": ')
        verb_2 = (verb_2).lower().strip()
        while verb_2 != str(verb_2):
            print('You did not enter a string. ')
            verb_2 = input('Input a verb ending with "ing": ')
            verb_2 = str(verb_2).lower().strip()

        verb_3 = input('Input a verb ending with "ed": ')
        verb_3 = (verb_3).lower().strip()
        while verb_3 != str(verb_3):
            print('You did not enter a string. ')
            verb_3 = input('Input a verb ending with "ed": ')
            verb_3 = str(verb_3).lower().strip()

        adjective_2 = input('Input an adjective: ')
        adjective_2 = (adjective_2).lower().strip()
        while adjective_2 != str(adjective_2):
            print('You did not enter a string. ')
            adjective_2 = input('Input an adjective: ')
            adjective_2 = str(adjective_2).lower().strip()

        color_2 = input('Input a color: ')
        color_2 = (color_2).lower().strip()
        while color_2 != str(color_2):
            print('You did not enter a string. ')
            color_2 = input('Input a color: ')
            color_2 = str(color_2).lower().strip()

        adverb = input('Input an adverb: ')
        adverb = (adverb).lower().strip()
        while color_2 != str(adverb):
            print('You did not enter a string')
            adverb = input('Input an adverb: ')
            adverb = str(adverb).lower().strip()

        place_2 = input('Input a place: ')
        place_2 = (place_2).lower().strip()
        while place_2 != str(place_2):
            print('You did not enter a string. ')
            place_2 = input('Input a place: ')
            place_2 = str(place_2).lower().strip()

        verb_4 = input('Input a verb ending with "ing": ')
        verb_4 = (verb_4).lower().strip()
        while verb_4 != str(verb_4):
            print('You did not enter a string. ')
            verb_4 = input('Input a verb ending with "ing": ')
            verb_4 = str(verb_4).lower().strip()

        verb_5 = input('Input a verb ending with "ing": ')
        verb_5 = (verb_5).lower().strip()
        while verb_2 != str(verb_5):
            print('You did not enter a string. ')
            verb_5 = input('Input a verb ending with "ing": ')
            verb_5 = str(verb_5).lower().strip()

        vehicle = input('Input a vehicle: ')
        vehicle = (vehicle).lower().strip()
        while vehicle != str(vehicle):
            print('You did not enter a string. ')
            vehicle = input('Input a vehicle: ')
            vehicle = str(vehicle).lower().strip()

        noun_3 = input('Input a plural noun: ')
        noun_3 = (noun_3).lower().strip()
        while noun_3 != str(noun_3):
            print('You did not enter a string. ')
            noun_3 = input('Input a plural noun: ')
            noun_3 = str(noun_3).lower().strip()

        verb_6 = input('Input a verb: ')
        verb_6 = (verb_6).lower().strip()
        while verb_6 != str(verb_6):
            print('You did not enter a string. ')
            verb_6 = input('Input a verb: ')
            verb_6 = str(verb_6).lower().strip()

        verb_7 = input('Input a verb ending with "ed": ')
        verb_7 = (verb_7).lower().strip()
        while verb_7 != str(verb_7):
            print('You did not enter a string. ')
            verb_7 = input('Input a verb ending with "ed": ')
            verb_7 = str(verb_7).lower().strip()

        verb_8 = input('Input a verb: ')
        verb_8 = (verb_8).lower().strip()
        while verb_8 != str(verb_8):
            print('You did not enter a string. ')
            verb_8 = input('Input a verb: ')
            verb_8 = str(verb_8).lower().strip()

        print("It all started with a ", adjective_1," explosion at the ", place_1,", with ", noun_1," and ", color," "
              "", noun_2," ", verb_2,". The scientists did their best to ", verb_1," the lab but they must have "
              "", verb_3," something wrong. Soon after a ", adjective_2," ",color_2," Blob was seen very ", adverb," moving"
              " down the ", place_2," Street. The police did not know what to do about it, so they let the Blob keep"
              " ", verb_4,". But the Blob kept ", verb_5," everything in its path including ", vehicle,"s and "
              "", noun_3,". No one could ", verb_6," the Blob so the townspeople ", verb_7," to ", verb_8," it somewhere else")


    print('')
    print('Would you like to play again?')
    MADLIB_choice = input('Enter a number 1,2, or 3 to choose which MAD LIB you want to complete. '
                          'If you want to exit the game then enter 0: ')
    print('')

    while (MADLIB_choice != 1 and MADLIB_choice != 2 and MADLIB_choice != 3 and MADLIB_choice != 0):
        print('You entered an incorrect input.')
        MADLIB_choice = input('Enter a number 1 through 5 to choose which MAD LIB you want to complete: ')
        MADLIB_choice = int(MADLIB_choice)

print('Thanks for playing! Goodbye!!')