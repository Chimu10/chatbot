from flask import Flask, render_template, request, jsonify,json , redirect

from chat import get_response


app= Flask(__name__)
jsnfile = 'data.json'

@app.get("/")
def index_get():
    return render_template("base.html")

@app.post("/predict")
def predict():
    text=request.get_json().get("message")
    response=get_response(text)
    message={"answer":response}
    return jsonify(message)

@app.route("/adminpanel")
def main():
    with open(jsnfile) as f:
        conttag = json.load(f)
        tagss = [intent['tag'] for intent in conttag['intents']]
        #pat = [intent['pattern']for intent in conttag['intents']]
    return render_template("index.html" , new = tagss)


@app.route("/addtag", methods = ['GET','POST'])
def addcar():
    if request.method == 'GET':
        return render_template("addtag.html", car = {})
    if request.method == 'POST':
        tag = request.form["tag"]
        patterns = request.form["patterns"]
        responses = request.form["responses"]
    

        
        with open(jsnfile) as cr:
            cars = json.load(cr)
            carss = cars['intents']
        arr = patterns.split(",")
        res = responses.split(",")
        
        #carss.append({"tag": tag, "patterns": request.get_json(patterns), "responses": request.get_json(responses)})
        carss.append({"tag": tag, "patterns": arr, "responses": res})

        with open(jsnfile, 'w') as cw:
            json.dump(cars, cw)
        return redirect('/adminpanel')




@app.route('/deletetag/<string:tagg>')
def deletetag(tagg):
    print("1111")
    with open(jsnfile) as cr:
        cars = json.load(cr)
        myData_clean = [x for x in cars['intents'] if x['tag'] != tagg]
        myData_clean = {'intents':myData_clean}
    
    with open(jsnfile, 'w') as cw:
        json.dump(myData_clean, cw)
    return redirect('/adminpanel')



if __name__=="__main__":
    app.run(debug=True)

