#import the library and elements needed for the server to run
from flask import Flask, render_template

#setting the folder that the html pages come from
template_folder = '/templates'

#__name__ is a built in python variable that holds the current moduale name
#bacicaly tells flask where to look for the files
app = Flask(__name__)

#connect all the html pages to each other
#routes to the page name(page_name is a place holder)
@app.route("/<page_name>") 
#defines the python function that will exicute when the request matches the @app.route
def serve_html_page(page_name):
    #renders the template and creates a f-string(allows for any variable to be inserted)
    return render_template(f"{page_name}")

#the first page or index that is seen when opening the website
#when the url or the ip is placed into the webserch this is the first page to show up
@app.route('/')
#definds the function as home
def home():
    #exicutes the file of index as the home function
    return render_template('index.html')

#make the server run on any host of the server and on a spesific port 
if __name__ == '__main__':
    #specify the flask framework, listen to any avaliable network interfaces, run on port 8434 through the guest
    app.run(host="0.0.0.0", debug=True, port=8434)