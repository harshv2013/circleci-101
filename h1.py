from sanic import Sanic
from sanic.response import  json
from sanic import response

app = Sanic()
# CORS(app)

print('Hello Dear ')

@app.route("ner/test", methods=['GET'])
async def hello_world(request):

	    name = 'Harsh'
	    email = 'harsh@gmail.com'
	    return response.json({ 'name': name,'email':email})





if __name__ == "__main__":
    app.run(host="0.0.0.0",port=9034, debug=True)
