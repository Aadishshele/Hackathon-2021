import time
from googlesearch import search


def wrap_func():
    print("Hello dear customer, thank you for visiting syntax error's very own support bot.I am here for support and helping you through these times that surround us.")
    time.sleep(3)
    print("When you are ready, please choose an option from these listed values so i will be able to assist you\n1.Therapy\n2.Helpline")
    a = (input("Which do you choose: "))

    if a == "Therapy":

        b = (input("What are you struggling with right now: \n1.Stress\n2.Anxiety\n3.PTSD\n"))
        time.sleep(3)
        if b == "1" or "Stress" or "stress":
            query = "Best tips for stress relief"

            for j in search(query, tld="co.in", num=3, stop=3, pause=2):
                print("From our algorithm we have derived the best possible result to cope up with stress", j)

        elif b == "2" or "Anxiety" or "anxiety":
            query = "Tips for getting rid of anxiety"

            for m in search(query, tld="co.in", num=3, stop=3, pause=2):
                print("From our algorithm we have derived the best possible result to overcome anxiety", m)
                
        elif b == "3" or "PTSD" or "ptsd":
            query = "best tips to overcome ptsd"

            for p in search(query, tld="co.in", num=3, stop=3, pause=2):
                print("From our algorithm have derived the best possible result to combat PTSD", p)

        else:
            print("We can not help you")

    if a == "Helpline":

        b = (input("What Helpline do you want with right now\n1.Suicide\n2.Eating\n3.Mental Health\n4.Depression"))
        time.sleep(3)
        if b == "1" or "Suicide Prevention" or "suicide Prevention" or "Suicide prevention":
            query = "What is the hotline number for suicide prevention"

            for k in search(query, tld="co.in", num=1, stop=1, pause=2):
                print("From our algorithm we found the suicide hotline number : ", k)

        elif b == "2" or "Eating Disorder" or "Eating disorder" or "eating Disorder":
            query = "What is the hotline number for Eating Disorder"

            for l in search(query, tld="co.in", num=1, stop=1, pause=2):
                print("From our algorithm we found the Eating disorder hotline number : ", l)

        elif b == "3" or "Mental Health" or "Mental health" or "mental health":
            query = "What is the hotline number for Mental health"

            for m in search(query, tld="co.in", num=1, stop=1, pause=2):
                print("From our algorithm we found the Mental Health hotline number : ", m)

        elif b == "4" or "Depression" or "depression":
            query = "What is the hotline number for Depression"

            for o in search(query, tld="co.in", num=1, stop=1, pause=2):
                print("From our algorithm we found the Depression hotline number : ", o)
        else:
            print("We can't help you")


print(wrap_func())
