from flask import Flask, render_template, request 
import Test
import time
from googlesearch import search


app = Flask(__name__)


@app.route('/')
def hello():
     
    return render_template('index.html')

@app.route('/hi')
def page2():
    return render_template('hi.html')

@app.route('/hello')
def page3():   
    return render_template('hello.html')

@app.route('/form')
def form():
    return render_template('Form.html')

@app.route("/data", methods=["POST" , "GET"])
def login():
    if request.method == "POST":
        form_data = request.form
        if form_data["a"]=="yes":
            if form_data["ab"]=="Stress" or form_data["ab"]=="stress":
                query = "Best tips for stress relief"
                for j in search(query, tld="co.in", num=3, stop=3, pause=2):
                    return "From our algorithm we have derived the best possible result to cope up with stress", j
            elif form_data["ab"]=="Anxiety" or form_data["ab"]=="anxiety":
                query = "Tips for getting rid of anxiety"
                for m in search(query, tld="co.in", num=3, stop=3, pause=2):
                    return "From our algorithm we have derived the best possible result to overcome anxiety", m
            elif form_data["ab"]=="PTSD" or form_data["ab"]=="ptsd":
                query = "best tips to overcome ptsd"
                for p in search(query, tld="co.in", num=3, stop=3, pause=2):
                    return "From our algorithm have derived the best possible result to combat ptsd", p
            else:
                return "We can not help you"
        if form_data["b"]=="yes":
            if form_data["ba"]=="Suicide Prevention" or form_data["ba"]=="suicide prevention":
                query = "What is the hotline number for suicide prevention"
                for k in search(query, tld="co.in", num=1, stop=1, pause=2):
                    return "From our algorithm we found the suicide hotline number : ", k
            elif form_data["ba"] == "2" or "Eating Disorder" or "Eating disorder" or "eating Disorder":
                query = "What is the hotline number for Eating Disorder"

                for l in search(query, tld="co.in", num=1, stop=1, pause=2):
                    print("From our algorithm we found the Eating disorder hotline number : ", l)

            elif form_data["ba"] == "3" or "Mental Health" or "Mental health" or "mental health":
                query = "What is the hotline number for Mental health"

                for m in search(query, tld="co.in", num=1, stop=1, pause=2):
                    print("From our algorithm we found the Mental Health hotline number : ", m)

            elif form_data["ba"] == "4" or "Depression" or "depression":
                query = "What is the hotline number for Depression"

                for o in search(query, tld="co.in", num=1, stop=1, pause=2):
                    print("From our algorithm we found the Depression hotline number : ", o)
        else:
            print("We can't help you")
        return render_template('data.html',form_data = form_data)
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)