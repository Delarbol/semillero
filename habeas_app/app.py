from flask import Flask, render_template,  request, make_response, send_file, send_from_directory, abort
from fpdf import FPDF, HTMLMixin #para el pdf
from datetime import date
from poderdocx import creaPoder
from habeasdocx import crea_habeas


app = Flask(__name__)
#pdf = FPDF('P', 'mm', 'letter') #

# @app.route('/')
# def index():
#     title = 'HC4A - Codext'
#     return render_template("index.html", title=title)

@app.route('/about')
def about():
    names = ['Peter','Emma','Juan','Chipss']
    return render_template("about.html", names=names)

@app.route('/about_poder')
def about_poder():
    return render_template("about_poder.html")

@app.route('/')
def inicio():
    return render_template("inicio.html")

@app.route('/habeas', methods=['GET', 'POST'])  #ruta inicial y el metodo post es una forma de recibir la información
def casa():
    #datoshabeas = formulario.Datos(request.form)
    #if request.method == 'POST' and datoshabeas.validate():


    return render_template('main.html')

@app.route('/form', methods=['POST'])
def form():

    title = 'Todo listo!'
    #datoshabeas = formulario.Datos(request.form)

    nom_solicitante = request.form.get('nom_solicitante').upper()
    fecha = date.today()
    ciudad = request.form.get('ciudad').upper()
    condi_solici = request.form.get('condi_solici')
    direccion_solicitante = request.form.get('direccion_solicitante')
    email_solicitante = request.form.get('email_solicitante').lower()
    ced_solicitante = request.form.get('ced_solicitante')
    id_solicitante = request.form.get('id_solicitante')
    num_solicitante =  request.form.get('num_solicitante')

    #gen_poder = datoshabeas.genero_dante.data
    #gen_poder = 'o' if gen_poder == 'm' else 'a'

    ### AFECTADO
    nom_afectado = request.form.get('nom_afectado').upper()
    nom_autoridad = request.form.get('nom_autoridad').upper()
    fecha_hechos = request.form.get('fecha_hechos')

    #ape_apo = datoshabeas.apellido_rado.data.upper()
    #correo_poderado = datoshabeas.correo_rado.data.lower()
    sujeto_ordeno = request.form.get('sujeto_ordeno').upper()
    if sujeto_ordeno == None or len(sujeto_ordeno)< 3:
        sujeto_ordeno = 'alguien desconocido.'
    cargo_txt = request.form.get('cargo_txt').capitalize()
    ced_afectado = request.form.get('ced_afectado')
    id_afectado = request.form.get('id_afectado')

    num_dias = request.form.get('num_dias')
    gen_afectado = request.form.get('gen_afectado')
    gen_afectado = 'o' if gen_afectado == 'm' else 'a'
    sitio = request.form.get('sitio')
    hechos = request.form.get('hechos')
    if hechos == None or len(hechos)<3:
        hechos='Actualmente no se cuenta con información adicional.'
    crea_habeas(id_solicitante=id_solicitante, id_afectado=id_afectado, fecha= fecha, title = title, nom_solicitante = nom_solicitante, ciudad = ciudad, condi_solici = condi_solici, direccion_solicitante = direccion_solicitante , email_solicitante = email_solicitante, ced_solicitante = ced_solicitante, num_solicitante = num_solicitante, nom_afectado = nom_afectado, nom_autoridad = nom_autoridad, fecha_hechos = fecha_hechos, sujeto_ordeno = sujeto_ordeno, cargo_txt = cargo_txt, ced_afectado = ced_afectado, num_dias = num_dias, gen_afectado = gen_afectado, sitio = sitio , hechos = hechos)




    return render_template("form.html", id_solicitante=id_solicitante, id_afectado=id_afectado, fecha= fecha, title = title, nom_solicitante = nom_solicitante, ciudad = ciudad, condi_solici = condi_solici, direccion_solicitante = direccion_solicitante , email_solicitante = email_solicitante, ced_solicitante = ced_solicitante, num_solicitante = num_solicitante, nom_afectado = nom_afectado, nom_autoridad = nom_autoridad, fecha_hechos = fecha_hechos, sujeto_ordeno = sujeto_ordeno, cargo_txt = cargo_txt, ced_afectado = ced_afectado, num_dias = num_dias, gen_afectado = gen_afectado, sitio = sitio , hechos = hechos)#, datoshabeas=datoshabeas.ciudad.data)
app.config ["DOWNLOADS"] = "./downloads"

@app.route('/downloads/<file_name>')
def download_file(file_name):

    try:
        return send_from_directory(app.config["DOWNLOADS"],
                                    filename = file_name,
                                    as_attachment =True)
    except FileNotFoundError:
        abort(404)

#=====================================PODER AUTOMATIZADO========================================
@app.route('/poder', methods=['GET', 'POST'])  #ruta inicial y el metodo post es una forma de recibir la información
def poder():
    return render_template('poder.html')




@app.route('/form_poder',methods=['POST'])
def form_poder():
    title = 'Poder Automatizado'
    tipo_proceso = request.form.get('tipo_proceso').upper()
    num_car = None
    #---------------PODERDANTE
    nom_poder = request.form.get('nom_poder').upper()
    print(nom_poder)
    email = request.form.get('email').lower()
    gen_poder = request.form.get('gen_poder')
    gen_poder = 'o' if gen_poder == 'm' else 'a'
    ced_poder = request.form.get('ced_poder').replace('.','').replace(",","")
    id_poder = request.form.get('id_poder')
    #---------------APODERADO---------------------------------------------

    nom_apo = request.form.get('nom_apo').upper()
    gen_apo = request.form.get('gen_apo')
    gen_apo = 'o' if gen_apo == 'm' else 'a'
    portadore = '' if gen_apo == 'o' else 'a'
    email_apo = request.form.get('email_apo').lower()
    email_apo_otro = request.form.get('email_apo_otro').lower()
    id_apo = request.form.get('id_apo')
    ced_apo = request.form.get('ced_apo').replace('.','').replace(",","")
    num_car = request.form.get('num_car').replace('.','')
    #--------------CONTRAPARTE--------------------------------------------

    nom_contra = request.form.get('nom_contra').upper()
    gen_contra = request.form.get('gen_contra')
    gen_contra = 'o' if gen_contra == 'm' else 'a'
    id_contra = request.form.get('id_contra')
    ced_contra = request.form.get('ced_contra').replace('.','').replace(",","")

    print("Soy Email contra",request.form.get('email_contra'))
    if request.form.get('email_contra') != "":
        email_2 = request.form.get('email_contra').lower()
        email_2 = f', con dirección de notificación electrónica:\u00A0{email_2}.'
    else:
        email_2 = "."
# Diccionario de correos
    correos = { 'civil':'conjurcivil@uexternado.edu.co' ,
                'economico':'conjureconomico@uexternado.edu.co',
                'penal':'conjurpenal@uexternado.edu.co',
                'publico':'conjurpublico@uexternado.edu.co',
                'laboral': 'conjurlaboral@uexternado.edu.co'
               }

    if email_apo_otro is not None and email_apo == '':
        email_apo = email_apo_otro
    else:
        email_apo = correos[email_apo]


    creaPoder(tipo_proceso=tipo_proceso,
        nom_poder = nom_poder, email = email,
        gen_poder = gen_poder, ced_poder = ced_poder,
        id_poder = id_poder, nom_apo = nom_apo,
        gen_apo = gen_apo,
        portadore = portadore, email_apo = email_apo,
        id_apo = id_apo, ced_apo = ced_apo,
        nom_contra = nom_contra, id_contra = id_contra,
        ced_contra = ced_contra, gen_contra = gen_contra,
        email_2 = email_2, num_car = num_car,
        email_apo_otro = None)



    return  render_template("form_poder.html",
    nom_poder=nom_poder,
    gen_poder=gen_poder,
    id_poder = id_poder,
    ced_poder = ced_poder,
    email=email,
    nom_apo=nom_apo,
    gen_apo=gen_apo,
    id_apo = id_apo ,
    ced_apo=ced_apo,
    portadore = portadore,
    num_car = num_car,
    email_apo=email_apo,
    tipo_proceso = tipo_proceso,
    nom_contra=nom_contra,
    gen_contra=gen_contra,
    id_contra = id_contra,
    ced_contra=ced_contra,
    email_2=email_2,

    )



if __name__ == '__main__':
    app.run(debug = True)
