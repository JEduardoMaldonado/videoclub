import web
from web import form
from data import clien
from data import peli
render=web.template.render('templates')
urls = (
    '/(.*)', 'index'
)

db = web.database(dbn='mysql', db='pelis', user='root', pw='utec')

clien = clien()  
clien.read()
peli=peli()
peli.read()
myform = form.Form( 
    form.Dropdown('Cliente', clien.getCliente()), 
    form.Dropdown('Pelicula',peli.getPeliculas()), 
    form.Dropdown('Formato', ["Blueray","DVD"]),
    form.Dropdown('Tiempo', ["1","2","3","4","5","6","7"])
    
    ) 
class index:
    def GET(self,results):
        form = myform()
        result=db.select('datos')
        return render.index(form,result)
        
    def POST(self,results): 
        form = myform() 
        if not form.validates(): 
            return render.index(form)
        else:
            costo=0
            if form.d.Formato=="Blueray":
                costo=20
            elif form.d.Formato=="DVD":
                costo=10
            total=int(form.d.Tiempo)*costo
            db.insert('datos',pelicula=form.d.Pelicula, formato=form.d.Formato,cliente=form.d.Cliente, tiempo=form.d.Tiempo,total=total)
            
            result=db.select('datos')
           
            return render.index(form,result)
    

if __name__ == "__main__":
    
    app = web.application(urls, globals())
    app.run()