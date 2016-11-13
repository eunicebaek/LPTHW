print "You enter a restaurant with two menus. Do you choose a blue menu or a red menu?"

menu = raw_input("-> ")

if menu == "blue":
    print "There are vegetarian and non-vegetarian dish. Which one you choose?"
    print "1. vegetarian"
    print "2. non-vegetarian"

    dish = raw_input("-> ")

    if dish == "vegetarian":
        print "You have chosen vegetarian dish. What do you drink?"
        print "1. cola"
        print "2. soy milk"

        drink = raw_input("-> ")

        if drink == "cola":
            print "You lack protein! You don't know how to take care of yourself."
        elif drink == "soy milk":
            print "Salad with Soy Milk. Not an attractive combination but you know the nutritional balance!"
            print "You got your food and drink."
            print "Now you finished your meal. It's time to pay your bill."
            print "Pay by cash or card?"

            pay = raw_input("-> ")

            if pay == "cash":
                print "You don't have any cash in your purse."
                print "You can't pay for what you've eaten?!"
                print "You are arrested by not paying for your food."
            elif pay == "card":
                print "You don't have any money in your card."
                print "You can't pay for what you've eaten?!"
                print "You are arrested by not paying for your food."
            else:
                print "What do you mean?"
                print "We cannot accept that. You get arrested for not paying for your food."
        else:
            print "Well, we don't sell that here. Please get out."

    elif dish == "non-vegetarian":
        print "You have chosen non-vegetarian dish. You savage!"
    else:
        print "Why did you come to our restaurant? Please get out before my chef gets mad at you."
        print "You got kicked out of the restaurant and now you are starving."
        print "You see a dark forest and a cave. Where do you go?"

        where = raw_input("-> ")

        if where == "dark forest":
            print "You cannot find any fruits or animals. You starve to death."
        elif where == "cave":
            print "You see a big rock blocking the way. Do you move it?"

            rock = raw_input("-> ")

            if rock == "Yes":
                print "You see a treasure box."
                print "Now you can pay for what you've eaten in restaurant. Hurray!"
            elif rock == "No":
                print "What can you do with that lazy attitude? You starve to death."
            else:
                print "Suddenly the mouth of cave is blocked with falling rocks."
                print "You are trapped in the cave. You starve to death."
        else:
            print "You don't know where you are going. You get lost and starve to death."

elif menu == "red":
    print "You see nothing."
    print "You ask the waiter what's going on."
    print "\" You have chosen menu of nothing.\""
    print "You can choose nothing. You starve to death."
