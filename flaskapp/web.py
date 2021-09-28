from flask import Flask, render_template, request, url_for, redirect, session
import pymysql
from datetime import date, timedelta, datetime
import urllib.request

from werkzeug.utils import send_file

app = Flask(__name__)
app.secret_key = 'd589d3d0d15d764ed0a98ff5a37af547'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
@app.route('/')
@app.route('/home')
def home():
	try:
		logeado = session['logeado1']
	except:
		logeado = 0
	return render_template('inicio.html', title="Inicio", logeado = logeado)

@app.route('/citas', methods=['GET', 'POST'])
def citas():
	try:
		logeado = session['logeado1']
	except:
		logeado = 0
	if request.method == 'POST':
		fecha = request.form["fecha"]
		try:
			conexion = pymysql.connect(host='localhost', user='root', password='database', db='opticadb')
			try:
				with conexion.cursor() as cursor:
					consulta = "SELECT c.nombre, c.apellido, DATE_FORMAT(c.fecha,'%d/%m/%Y'), h.hora, c.telefono, c.idcitas from citas c inner join hora h on c.idhora = h.idhora where fecha = '" + str(fecha) + "' order by c.idhora asc;"
					cursor.execute(consulta)
					data = cursor.fetchall()
					consulta = "SELECT idhora, hora from hora;"
					cursor.execute(consulta)
					horas = cursor.fetchall()
			finally:
				conexion.close()
		except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
			print("Ocurrió un error al conectar: ", e)
		return render_template('citas.html', title="Citas", logeado = logeado, data=data, horas=horas)
	return render_template('citas.html', title="Citas", logeado = logeado)

@app.route('/nuevacita', methods=['GET', 'POST'])
def nuevacita():
	try:
		logeado = session['logeado1']
	except:
		logeado = 0
	try:
		conexion = pymysql.connect(host='localhost', user='root', password='database', db='opticadb')
		try:
			with conexion.cursor() as cursor:
				consulta = "SELECT idhora, hora from hora;"
				cursor.execute(consulta)
				horas = cursor.fetchall()
		finally:
			conexion.close()
	except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
		print("Ocurrió un error al conectar: ", e)
	if request.method == 'POST':
		nombre = request.form["nombre"]
		apellido = request.form["apellido"]
		telefono = request.form["telefono"]
		fecha = request.form["fecha"]
		hora = request.form["hora"]
		try:
			conexion = pymysql.connect(host='localhost', user='root', password='database', db='opticadb')
			try:
				with conexion.cursor() as cursor:
					consulta = "insert into citas(nombre, apellido, telefono, fecha, idhora) values(%s,%s,%s,%s,%s)"
					cursor.execute(consulta, (nombre, apellido, telefono, fecha,hora))
				conexion.commit()
			finally:
				conexion.close()
		except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
			print("Ocurrió un error al conectar: ", e)
		return redirect(url_for('citas'))
	return render_template('nuevacita.html', title="Nueva Cita", logeado = logeado, horas=horas)

@app.route('/ceditar/<idcita>', methods=['GET', 'POST'])
def ceditar(idcita):
	try:
		logeado = session['logeado1']
	except:
		logeado = 0
	try:
		conexion = pymysql.connect(host='localhost', user='root', password='database', db='opticadb')
		try:
			with conexion.cursor() as cursor:
				consulta = "SELECT idhora, hora from hora;"
				cursor.execute(consulta)
				horas = cursor.fetchall()
				consulta = "select nombre, apellido, telefono, fecha, idhora from citas where idcitas = "+idcita+";"
				print(consulta)
				cursor.execute(consulta)
				datacita = cursor.fetchall()
		finally:
			conexion.close()
	except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
		print("Ocurrió un error al conectar: ", e)
	if request.method == 'POST':
		nombre = request.form["nombre"]
		apellido = request.form["apellido"]
		telefono = request.form["telefono"]
		fecha = request.form["fecha"]
		hora = request.form["hora"]
		try:
			conexion = pymysql.connect(host='localhost', user='root', password='database', db='opticadb')
			try:
				with conexion.cursor() as cursor:
					consulta = "update citas set nombre = %s, apellido = %s, telefono = %s, fecha = %s, idhora = %s where idcitas = %s"
					cursor.execute(consulta, (nombre, apellido, telefono, fecha,hora, idcita))
				conexion.commit()
			finally:
				conexion.close()
		except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
			print("Ocurrió un error al conectar: ", e)
		return redirect(url_for('citas'))
	return render_template('ceditar.html', title="Editar Cita", logeado = logeado, horas=horas, datacita=datacita)

@app.route('/celiminar/<idcita>', methods=['GET', 'POST'])
def celiminar(idcita):
	try:
		conexion = pymysql.connect(host='localhost', user='root', password='database', db='opticadb')
		try:
			with conexion.cursor() as cursor:
				consulta = "delete from citas where idcitas = "+idcita+";"
				cursor.execute(consulta)
			conexion.commit()
		finally:
			conexion.close()
	except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
		print("Ocurrió un error al conectar: ", e)
	return redirect(url_for('citas'))

@app.context_processor
def utility_functions():
    def print_in_console(message):
        print(str(message))

    return dict(mdebug=print_in_console)

@app.route('/nuevaconsulta', methods=['GET', 'POST'])
def nuevaconsulta():
	try:
		logeado = session['logeado1']
	except:
		logeado = 0
	dateac = date.today()
	year = dateac.strftime("%Y")
	year = int(year)
	fechafoto = datetime.now().strftime("%d%m%Y")
	new_date = dateac + timedelta(days=183)
	anios = []
	nervos = []
	nervo = 1
	for i in range(11):
		nervos.append(nervo*i)
	for i in range(80):
		anios.append(year)
		year = year - 1
	numeros = []
	numero = 0
	for i in range(36):
		numeros.append(numero)
		numero = numero + 1
	mms = []
	mm = 0
	for i in range(8):
		mms.append(mm)
		mm = mm + 5
	cincos = []
	cinco = 0
	for i in range(15):
		cincos.append(cinco)
		cinco = cinco + 5
	meses = [[1, "Enero"],[2, "Febrero"],[3, "Marzo"],[4, "Abril"],[5, "Mayo"],[6, "Junio"],[7, "Julio"],[8, "Agosto"],[9, "Septiembre"],[10, "Octubre"],[11, "Noviembre"],[12, "Diciembre"]]
	enfermedades = [['Diabetes Mellitus'],['Hipertensión Arterial'],['Artritis Reumatoidea'],['Virus Inmunodeficiencia Humana'],['Hipertrigliceridemia'],['Colesterolemia']]
	try:
		conexion = pymysql.connect(host='localhost', user='root', password='database', db='opticadb')
		try:
			with conexion.cursor() as cursor:
				consulta = "select idsexo, sexo from sexo;"
				cursor.execute(consulta)
				sexo = cursor.fetchall()
				consulta = "select idusolen, uso from usolen;"
				cursor.execute(consulta)
				usolen = cursor.fetchall()
				consulta = "select idtipolen, tipo from tipolen;"
				cursor.execute(consulta)
				tipolen = cursor.fetchall()
				consulta = "select idmateriallen, material from materiallen;"
				cursor.execute(consulta)
				materiallen = cursor.fetchall()
				consulta = "select idfiltrolen, filtro from filtrolen order by filtro asc;"
				cursor.execute(consulta)
				filtrolen = cursor.fetchall()
				consulta = "select idcolorlen, color from colorlen;"
				cursor.execute(consulta)
				colorlen = cursor.fetchall()
				consulta = "select idrelacionvenaarteria, relacion from relacionvenaarteria;"
				cursor.execute(consulta)
				relva = cursor.fetchall()
				consulta = "select idojo, ojo from ojo;"
				cursor.execute(consulta)
				dataojo = cursor.fetchall()
				consulta = "select idtipoametropia, tipo from tipoametropia;"
				cursor.execute(consulta)
				dataametropia = cursor.fetchall()
				consulta = "select nombre1, nombre2, apellido1, apellido2, DATE_FORMAT(fechanac,'%Y-%m-%d'), idsexo, profesion, direccion, cui, telefono, telefono2 from paciente;"
				cursor.execute(consulta)
				datapac = cursor.fetchall()
		finally:
			conexion.close()
	except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
		print("Ocurrió un error al conectar: ", e)
	if request.method == 'POST':
		exicui = 0
		#panel1
		cui = request.form["cui"]
		telefono = request.form["telefono"]
		telefono1 = request.form["telefono1"]
		if len(telefono1) < 1:
			telefono1 = 0
		nombre1 = request.form["nombre1"]
		nombre2 = request.form["nombre2"]
		apellido1 = request.form["apellido1"]
		apellido2 = request.form["apellido2"]
		if len(nombre2) < 1:
			nombre2 = 0
		if len(apellido2) < 1:
			apellido2 = 0
		se = request.form["sexo"]
		fechanac = request.form["fechanac"]
		profesion = request.form["profesion"]
		direccion = request.form["direccion"]
		rutafoto = request.form["rutafoto"]
		aux = r'C:\\Users\\DELL\\Documents\\sistemaoptica\\flaskapp\static\\fotografias\\' + str(nombre1) + str(nombre2) + str(apellido1) + str(apellido2) + str(cui) + str(fechafoto) +'.jpeg'
		urllib.request.urlretrieve(rutafoto, aux)
		#ingreso paciente y estudiante
		try:
			conexion = pymysql.connect(host='localhost', user='root', password='database', db='opticadb')
			try:
				with conexion.cursor() as cursor:
					consulta = "select idpaciente from paciente where cui = %s and cui!= '0';"
					cursor.execute(consulta, cui)
					paciente = cursor.fetchall()
					if len(paciente) > 0:
						idpaciente = paciente[0][0]
						exicui = 1
					else:
						consulta = "select idpaciente from paciente where nombre1 = %s and nombre2 = %s and apellido1 = %s and apellido2 = %s;"
						cursor.execute(consulta, (nombre1, nombre2, apellido1, apellido2))
						paciente = cursor.fetchall()
						if len(paciente) > 0:
							idpaciente = paciente[0][0]
							exicui = 1
						else:
							consulta = "insert into paciente(nombre1, nombre2, apellido1, apellido2, fechanac, idsexo, profesion, direccion, cui, telefono, telefono2, ultimaev) values(%s, %s, %s, %s, %s, %s,%s, %s, %s,%s, %s, %s);"
							cursor.execute(consulta,(nombre1, nombre2,apellido1, apellido2, fechanac, se, profesion, direccion, cui, telefono, telefono1, date.today()))
				conexion.commit()
				if exicui == 0:
					with conexion.cursor() as cursor:
						consulta = "select max(idpaciente) from paciente;"
						cursor.execute(consulta)
						paciente = cursor.fetchall()
						idpaciente = paciente[0][0]
			finally:
				conexion.close()
		except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
			print("Ocurrió un error al conectar: ", e)
		#inserción de consulta a bd
		try:
			conexion = pymysql.connect(host='localhost', user='root', password='database', db='opticadb')
			try:
				with conexion.cursor() as cursor:
					consulta = "insert into consulta(fecha, idpaciente, idusolen, proximacita, dnp, dnp1, dnp2, dnp3, ultimaevmes, ultimaevanio, tiempolen, add1, add2, add3, add11, add22, add33, ojoambliopia, emetropia, antimetropia, tipoametropia, anisometropia, patologiaocular, lentesoftalmicos, lentescontacto, refoftalmologica, farmaco, aprobado,motivoconsulta) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,0, %s);"
					cursor.execute(consulta, (date.today(), idpaciente, 0, '0000-00-00', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
				conexion.commit()
			finally:
				conexion.close()
		except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
			print("Ocurrió un error al conectar: ", e)
		#insercion demas campos
		return redirect(url_for('home'))
	return render_template('nuevaconsulta.html', title="Nueva consulta", logeado = logeado, sexo = sexo, anios = anios, cincos=cincos, 
	proxcita = new_date, usolen = usolen, meses = meses, numeros=numeros, mms=mms, tipolen=tipolen, materiallen = materiallen, filtrolen=filtrolen, 
	colorlen=colorlen, relva = relva, nervos=nervos, dataojo=dataojo, dataametropia=dataametropia, enfermedades=enfermedades, datapac=datapac)

@app.route("/login", methods=['GET', 'POST'])
def login():
	try:
		logeado = session['logeado1']
	except:
		logeado = 0
	if logeado != 0:
		return redirect(url_for('home'))
	if request.method == 'POST':
		user = request.form["user"]
		pwd = request.form["pwd"]
		try:
			conexion = pymysql.connect(host='localhost', user='root', password='database', db='opticadb')
			try:
				with conexion.cursor() as cursor:
					consulta = "SELECT iduser, nombre, apellido FROM user WHERE user = %s and pwd = md5(%s)"
					cursor.execute(consulta, (user, pwd))
					data = cursor.fetchall()
					if len(data) == 0:
						return render_template('login.html', title='Iniciar sesión', logeado=logeado, mensaje="Datos inválidos, intente nuevamente")
					else:
						session['logeado1'] = 1
						session['iduser1'] = data[0][0]
						session['nombreuser1'] = data[0][1]
						session['apellidouser1'] = data[0][2]
						session['user1'] = user
						return redirect(url_for('home'))
			finally:
				conexion.close()
		except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
			print("Ocurrió un error al conectar: ", e)
	return render_template('login.html', title='Iniciar sesión', logeado=logeado, mensaje="")

@app.route("/logout")
def logout():
	session['logeado1'] = 0
	session['nombreuser1'] = ""
	session['apellidouser1'] = ""
	session['user1'] = ""
	session['iduser1'] = ""
	return redirect(url_for('home'))

@app.route("/pendaprobar", methods=['GET', 'POST'])
def pendaprobar():
	try:
		logeado = session['logeado1']
	except:
		logeado = 0
	if logeado == 0:
		return redirect(url_for('home'))
	
	try:
		conexion = pymysql.connect(host='localhost', user='root', password='database', db='opticadb')
		try:
			with conexion.cursor() as cursor:
				consulta = "SELECT c.idconsulta, p.nombre1, p.nombre2, p.apellido1, p.apellido2, DATE_FORMAT(c.fecha,'%d/%m/%Y') from consulta c inner join paciente p on p.idpaciente = c.idpaciente where aprobado = 0"
				cursor.execute(consulta)
				consultas = cursor.fetchall()
				
		finally:
			conexion.close()
	except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
		print("Ocurrió un error al conectar: ", e)
	return render_template('pendaprobar.html', title='Pendientes de aprobación', logeado=logeado, consultas=consultas)

@app.route("/aprobados", methods=['GET', 'POST'])
def aprobados():
	try:
		logeado = session['logeado1']
	except:
		logeado = 0
	try:
		conexion = pymysql.connect(host='localhost', user='root', password='database', db='opticadb')
		try:
			with conexion.cursor() as cursor:
				consulta = "SELECT idpaciente, nombre1, nombre2, apellido1, apellido2 from paciente order by apellido1 asc;"
				cursor.execute(consulta)
				consultas = cursor.fetchall()
				conteo = len(consultas)
				fechas = []
				for i in consultas:
					cons = "Select max(DATE_FORMAT(fecha,'%d/%m/%Y')) from consulta where idpaciente = '"+str(i[0])+"';"
					cursor.execute(cons)
					data = cursor.fetchall()
					fechas.append(data[0][0])
				idrecetas = []
				for i in consultas:
					cons = "Select max(idconsulta) from consulta where idpaciente = '"+str(i[0])+"';"
					cursor.execute(cons)
					data = cursor.fetchall()
					idrecetas.append(data[0][0])
		finally:
			conexion.close()
	except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
		print("Ocurrió un error al conectar: ", e)
	return render_template('aprobados.html', title='Aprobados', logeado=logeado, consultas=consultas, fechas=fechas, conteo=conteo, idrecetas=idrecetas)

@app.route("/recetas/<idconsulta>", methods=['GET', 'POST'])
def recetas(idconsulta):
	try:
		logeado = session['logeado1']
	except:
		logeado = 0
	rf = []
	lencons = []
	existe = 0
	try:
		conexion = pymysql.connect(host='localhost', user='root', password='database', db='opticadb')
		try:
			with conexion.cursor() as cursor:
				consulta = "SELECT esfera1, cilindro1, eje1, prisma1, avcc1 from reffin where idconsulta = %s and idojo = 2;"
				cursor.execute(consulta, idconsulta)
				aux = cursor.fetchone()
				rf.append(aux)
				consulta = "SELECT esfera1, cilindro1, eje1, prisma1, avcc1 from reffin where idconsulta = %s and idojo = 1;"
				cursor.execute(consulta, idconsulta)
				aux = cursor.fetchone()
				rf.append(aux)
				consulta = "SELECT DATE_FORMAT(fechacaducidad,'%d/%m/%Y'), poder, cb, dia, cil, eje, agregar, color, tipo from recetacontacto where idconsulta = " + str(idconsulta) + " and idojo = 2;"
				cursor.execute(consulta)
				aux = cursor.fetchall()
				if len(aux) < 1:
					lencons.append([0,0,0,0,0,0,0,0,0])
				else:
					lencons.append(aux[0])
					existe = existe + 1
				consulta = "SELECT DATE_FORMAT(fechacaducidad,'%d/%m/%Y'), poder, cb, dia, cil, eje, agregar, color, tipo from recetacontacto where idconsulta = " + str(idconsulta) + " and idojo = 1;"
				cursor.execute(consulta)
				aux = cursor.fetchall()
				if len(aux) < 1:
					lencons.append([0,0,0,0,0,0,0,0,0])
				else:
					lencons.append(aux[0])
					existe = existe + 1
				consulta = "SELECT medicamento1, descripcion1, medicamento2, descripcion2 from recetagotero where idconsulta = %s;"
				cursor.execute(consulta, idconsulta)
				aux = cursor.fetchall()
				if len(aux) < 1:
					datagotero = [0,0,0,0]
				else:
					datagotero = aux[0]
				consulta = "SELECT p.nombre1, p.nombre2, p.apellido1, p.apellido2, DATE_FORMAT(c.fecha,'%d/%m/%Y'), u.uso, DATE_FORMAT(c.proximacita,'%d/%m/%Y'), c.dnp, c.add11, c.add22, c.add33, o.nombre, o.apellido from paciente p inner join consulta c on p.idpaciente = c.idpaciente inner join usolen u on u.idusolen = c.idusolen inner join user o ON o.iduser = c.iduser where idconsulta = " + str(idconsulta) + ";"
				cursor.execute(consulta)
				dataconsulta = cursor.fetchall()
				consulta = "SELECT t.tipo, m.material, f.filtro, c.color, d.lentedetallado from lenterecomendado l inner join tipolen t on t.idtipolen=l.tipo inner join materiallen m on m.idmateriallen=l.material inner join filtrolen f on f.idfiltrolen=l.filtro inner join colorlen c on c.idcolorlen=l.color inner join lentedetallado d on d.idlentedetallado = l.lentedetallado where l.idconsulta = %s;"
				cursor.execute(consulta, idconsulta)
				lenterecomendado = cursor.fetchall()
		finally:
			conexion.close()
	except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
		print("Ocurrió un error al conectar: ", e)
	if request.method == 'POST':
		#lente de contacto
		lcfechacad = request.form["lcfechacad"]
		lcpoderod = request.form["lcpoderod"]
		lcpoderoi = request.form["lcpoderoi"]
		lccbod = request.form["lccbod"]
		lccboi = request.form["lccboi"]
		lcdiaod = request.form["lcdiaod"]
		lcdiaoi = request.form["lcdiaoi"]
		lccilod = request.form["lccilod"]
		lcciloi = request.form["lcciloi"]
		lcejeod = request.form["lcejeod"]
		lcejeoi = request.form["lcejeoi"]
		lcagregarod = request.form["lcagregarod"]
		lcagregaroi = request.form["lcagregaroi"]
		lccolorod = request.form["lccolorod"]
		lccoloroi = request.form["lccoloroi"]
		lctipood = request.form["lctipood"]
		lctipooi = request.form["lctipooi"]
		if len(lcfechacad) < 1:
			lcfechacad = 0
		else:
			datos=lcfechacad.split('/')
			try:
				lcfechacad = datos[2] + '-' + datos[1] + '-' + datos[0]
			except:
				lcfechacad = '0000-00-00'
		if len(lcpoderod) < 1:
			lcpoderod = 0
		if len(lcpoderoi) < 1:
			lcpoderoi = 0
		if len(lccbod) < 1:
			lccbod = 0
		if len(lccboi) < 1:
			lccboi = 0
		if len(lcdiaod) < 1:
			lcdiaod = 0
		if len(lcdiaoi) < 1:
			lcdiaoi = 0
		if len(lccilod) < 1:
			lccilod = 0
		if len(lcciloi) < 1:
			lcciloi = 0
		if len(lcejeod) < 1:
			lcejeod = 0
		if len(lcejeoi) < 1:
			lcejeoi = 0
		if len(lcagregarod) < 1:
			lcagregarod = 0
		if len(lcagregaroi) < 1:
			lcagregaroi = 0
		if len(lccolorod) < 1:
			lccolorod = 0
		if len(lccoloroi) < 1:
			lccoloroi = 0
		if len(lctipood) < 1:
			lctipood = 0
		if len(lctipooi) < 1:
			lctipooi = 0
		#gotas
		gfechacad = request.form["gfechacad"]
		datos=gfechacad.split('/')
		try:
			gfechacad = datos[2] + '-' + datos[1] + '-' + datos[0]
		except:
			gfechacad = '0000-00-00'
		gmed1 = request.form["gmed1"]
		gdesc1 = request.form["gdesc1"]
		gmed2 = request.form["gmed2"]
		gdesc2 = request.form["gdesc2"]
		if len(gmed1) < 1:
			gmed1 = 0
		if len(gdesc1) < 1:
			gdesc1 = 0
		if len(gmed2) < 1:
			gmed2 = 0
		if len(gdesc2) < 1:
			gdesc2 = 0
		try:
			conexion = pymysql.connect(host='localhost', user='root', password='database', db='opticadb')
			try:
				with conexion.cursor() as cursor:
					if existe == 0:
						consulta = "insert into recetacontacto(idconsulta, idojo,fechacaducidad, poder, cb, dia, cil, eje, agregar, color, tipo) values(%s,1,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
						cursor.execute(consulta, (idconsulta, lcfechacad, lcpoderoi,lccboi, lcdiaoi, lcciloi, lcejeoi, lcagregaroi, lccoloroi, lctipooi))
						consulta = "insert into recetacontacto(idconsulta, idojo,fechacaducidad, poder, cb, dia, cil, eje, agregar, color, tipo) values(%s,2,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
						cursor.execute(consulta, (idconsulta, lcfechacad, lcpoderod,lccbod, lcdiaod, lccilod, lcejeod, lcagregarod, lccolorod, lctipood))
						consulta = "insert into recetagotero(idconsulta, medicamento1, descripcion1, medicamento2,  descripcion2) values(%s,%s,%s,%s,%s)"
						cursor.execute(consulta, (idconsulta, gmed1, gdesc1,gmed2, gdesc2))
					else:
						consulta = "update recetacontacto set fechacaducidad = %s, poder = %s, cb = %s, dia = %s, cil = %s, eje = %s, agregar = %s, color = %s, tipo = %s where idconsulta = %s and idojo = 1;"
						cursor.execute(consulta, (lcfechacad, lcpoderoi, lccboi, lcdiaoi, lcciloi, lcejeoi, lcagregaroi, lccoloroi, lctipooi, idconsulta))
						consulta = "update recetacontacto set fechacaducidad = %s, poder = %s, cb = %s, dia = %s, cil = %s, eje = %s, agregar = %s, color = %s, tipo = %s where idconsulta = %s and idojo = 2;"
						cursor.execute(consulta, (lcfechacad, lcpoderod, lccbod, lcdiaod, lccilod, lcejeod, lcagregarod, lccolorod, lctipood, idconsulta))
						consulta = "update recetagotero set medicamento1 = %s, descripcion1 = %s, medicamento2 = %s, descripcion2 = %s where idconsulta = %s;"
						cursor.execute(consulta, (gmed1, gdesc1, gmed2, gdesc2, idconsulta))
					consulta = "update consulta set proximacita = %s where idconsulta = %s"
					cursor.execute(consulta, (gfechacad, idconsulta))
				conexion.commit()
			finally:
				conexion.close()
		except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
			print("Ocurrió un error al conectar: ", e)
		return redirect(url_for('recetas', idconsulta=idconsulta))
	return render_template('recetas.html', title='Recetas', logeado=logeado, dataconsulta=dataconsulta, rf = rf, lenterecomendado=lenterecomendado, lencons=lencons, datagotero=datagotero)

@app.route("/pendaprobarc/<idconsulta>", methods=['GET', 'POST'])
def pendaprobarc(idconsulta):
	try:
		logeado = session['logeado1']
	except:
		logeado = 0
	if logeado == 0:
		return redirect(url_for('home'))
	try:
		conexion = pymysql.connect(host='localhost', user='root', password='database', db='opticadb')
		try:
			with conexion.cursor() as cursor:
				consulta = "select idusolen, uso from usolen;"
				cursor.execute(consulta)
				usolen = cursor.fetchall()
		finally:
			conexion.close()
	except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
		print("Ocurrió un error al conectar: ", e)
	dateac = date.today()
	year = dateac.strftime("%Y")
	year = int(year)
	new_date = dateac + timedelta(days=183)
	nervos = []
	nervo = 1
	for i in range(11):
		nervos.append(nervo*i)
	numeros = []
	numero = 0
	for i in range(36):
		numeros.append(numero)
		numero = numero + 1
	mms = []
	mm = 0
	for i in range(8):
		mms.append(mm)
		mm = mm + 5
	anios = []
	for i in range(80):
		anios.append(year)
		year = year - 1
	cincos = []
	cinco = 0
	for i in range(15):
		cincos.append(cinco)
		cinco = cinco + 5
	meses = [[1, "Enero"],[2, "Febrero"],[3, "Marzo"],[4, "Abril"],[5, "Mayo"],[6, "Junio"],[7, "Julio"],[8, "Agosto"],[9, "Septiembre"],[10, "Octubre"],[11, "Noviembre"],[12, "Diciembre"]]
	enfermedades = [['Diabetes Mellitus'],['Hipertensión Arterial'],['Artritis Reumatoidea'],['Virus Inmunodeficiencia Humana'],['Hipertrigliceridemia'],['Colesterolemia']]
	try:
		conexion = pymysql.connect(host='localhost', user='root', password='database', db='opticadb')
		try:
			with conexion.cursor() as cursor:
				consulta = "SELECT idpaciente, ojoambliopia, tipoametropia, idusolen, proximacita, dnp, dnp1, dnp2, dnp3, ultimaevmes, ultimaevanio, tiempolen, add1, add2, add3, add11, add22, add33, emetropia, antimetropia, anisometropia, patologiaocular, lentesoftalmicos, lentescontacto, refoftalmologica, farmaco, DATE_FORMAT(fecha,'%d%m%Y'), motivoconsulta from consulta where idconsulta = "+ str(idconsulta) + ";"
				cursor.execute(consulta)
				dataconsulta = cursor.fetchall()
				idpaciente = dataconsulta[0][0]
				fechafoto = dataconsulta[0][26]
				
		finally:
			conexion.close()
	except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
		print("Ocurrió un error al conectar: ", e)
	try:
		conexion = pymysql.connect(host='localhost', user='root', password='database', db='opticadb')
		try:
			with conexion.cursor() as cursor:
				consulta = "select idrelacionvenaarteria, relacion from relacionvenaarteria;"
				cursor.execute(consulta)
				relva = cursor.fetchall()
				consulta = "select idtipolen, tipo from tipolen;"
				cursor.execute(consulta)
				tipolen = cursor.fetchall()
				consulta = "select idmateriallen, material from materiallen;"
				cursor.execute(consulta)
				materiallen = cursor.fetchall()
				consulta = "select idfiltrolen, filtro from filtrolen order by filtro asc;"
				cursor.execute(consulta)
				filtrolen = cursor.fetchall()
				consulta = "select idlentedetallado, lentedetallado from lentedetallado order by lentedetallado asc;"
				cursor.execute(consulta)
				lentedetalladolen = cursor.fetchall()
				consulta = "select idcolorlen, color from colorlen;"
				cursor.execute(consulta)
				colorlen = cursor.fetchall()
				consulta = "select idojo, ojo from ojo;"
				cursor.execute(consulta)
				dataojo = cursor.fetchall()
				consulta = "select idtipoametropia, tipo from tipoametropia;"
				cursor.execute(consulta)
				dataametropia = cursor.fetchall()
				consulta = "SELECT p.nombre1, p.nombre2, p.apellido1, p.apellido2, p.fechanac, s.sexo, p.profesion, p.direccion, p.cui, p.telefono, p.telefono2 from paciente p inner join sexo s on p.idsexo = s.idsexo where idpaciente = %s"
				cursor.execute(consulta, (idpaciente))
				paciente = cursor.fetchall()
				paciente = paciente[0]
		finally:
			conexion.close()
	except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
		print("Ocurrió un error al conectar: ", e)
	if request.method == 'POST':
		#panel2
		motivoconsulta = request.form["motivoconsulta"]
		if len(motivoconsulta) < 1:
			motivoconsulta = 0
		ultimaevmes = request.form["ultimaevmes"]
		ultimaevanio = request.form["ultimaevanio"]
		tiempolentes = request.form["tiempolentes"]
		if len(ultimaevmes) < 1:
			ultimaevmes = 0
		if len(ultimaevanio) < 1:
			ultimaevanio = 0
		if len(tiempolentes) < 1:
			tiempolentes = 0
		antoftal = request.form["antoftal"]
		if len(antoftal) < 1:
			antoftal = 0
		antfam = request.form["antfam"]
		antaler = request.form["antaler"]
		antgla = request.form["antgla"]
		if len(antfam) < 1:
			antfam = 0
		if len(antaler) < 1:
			antaler = 0
		if len(antgla) < 1:
			antgla = 0
		numantmed = request.form["numantmed"]
		numantqui = request.form["numantqui"]
		numantmed = int(numantmed)
		numantqui = int(numantqui)
		antmed = []
		antqui = []
		for i in range(numantmed):
			aux = 'enfermedad' + str(i+1)
			enfermedad = request.form[aux]
			if len(enfermedad) < 1:
				enfermedad = 0
			try:
				aux = 'medotro' + str(i+1)
				otro = request.form[aux]
				if len(otro) < 1:
					otro = 0
			except:
				otro = 0
			aux = 'tiempoevolucionm' + str(i+1)
			tiempoev = request.form[aux]
			if len(tiempoev) < 1:
				tiempoev = 0
			aux = 'controlm' + str(i+1)
			control = request.form[aux]
			if len(control) < 1:
				control = 0
			aux = [enfermedad, otro, tiempoev, control]
			antmed.append(aux)
		for i in range(numantqui):
			aux = 'cirugia' + str(i+1)
			cirugia = request.form[aux]
			if len(cirugia) < 1:
				cirugia = 0
			aux = 'tiempoevolucionq' + str(i+1)
			tiempoev = request.form[aux]
			if len(tiempoev) < 1:
				tiempoev = 0
			aux = 'controlq' + str(i+1)
			control = request.form[aux]
			if len(control) < 1:
				control = 0
			aux = [cirugia, tiempoev, control]
			antqui.append(aux)
		#panel3
		avlod = request.form["avlod"]
		avloi = request.form["avloi"]
		aeod = request.form["aeod"]
		aeoi = request.form["aeoi"]
		avcod = request.form["avcod"]
		avcoi = request.form["avcoi"]
		if len(avcod) < 1:
			avcod = 0
		if len(avcoi) < 1:
			avcoi = 0
		if len(avlod) < 1:
			avlod = 0
		if len(avloi) < 1:
			avloi = 0
		if len(aeod) < 1:
			aeod = 0
		if len(aeoi) < 1:
			aeoi = 0
		#panel4
		raeod = request.form["raeod"]
		racod = request.form["racod"]
		if len(raeod) < 1:
			raeod = 0
		if len(racod) < 1:
			racod = 0
		racod = float(racod)
		if racod > 0:
			racod = racod * -1
		raejod = request.form["raejod"]
		if len(raejod) < 1:
			raejod = 0
		rapod = request.form["rapod"]
		if len(rapod) < 1:
			rapod = 0
		raavcc1od = request.form["raavcc1od"]
		if len(str(raavcc1od)) < 1:
			raavcc1od = 0
		raeoi = request.form["raeoi"]
		racoi = request.form["racoi"]
		if len(raeoi) < 1:
			raeoi = 0
		if len(racoi) < 1:
			racoi = 0
		racoi = float(racoi)
		if racoi > 0:
			racoi = racoi * -1
		raejoi = request.form["raejoi"]
		if len(raejoi) < 1:
			raejoi = 0
		rapoi = request.form["rapoi"]
		if len(rapoi) < 1:
			rapoi = 0
		raavcc1oi = request.form["raavcc1oi"]
		if len(raavcc1oi) < 1:
			raavcc1oi = 0
		add1 = request.form["add1"]
		if len(add1) < 1:
			add1 = 0
		add2 = request.form["add2"]
		if len(add2) < 1:
			add2 = 0
		add3 = request.form["add3"]
		if len(add3) < 1:
			add3 = 0
		dnp1 = request.form["dnp1"]
		if len(dnp1) < 1:
			dnp1 = 0
		vceod = request.form["vceod"]
		vccod = request.form["vccod"]
		if len(vceod) < 1:
			vceod = 0
		if len(vccod) < 1:
			vccod = 0
		vccod = float(vccod)
		if vccod > 0:
			vccod = vccod * -1
		vcejod = request.form["vcejod"]
		if len(vcejod) < 1:
			vcejod = 0
		vcpod = request.form["vcpod"]
		if len(vcpod) < 1:
			vcpod = 0
		vcavccod = request.form["vcavccod"]
		vceoi = request.form["vceoi"]
		vccoi = request.form["vccoi"]
		if len(vcavccod) < 1:
			vcavccod = 0
		if len(vceoi) < 1:
			vceoi = 0
		if len(vccoi) < 1:
			vccoi = 0
		vccoi = float(vccoi)
		if vccoi > 0:
			vccoi = vccoi * -1
		vcejoi = request.form["vcejoi"]
		if len(vcejoi) < 1:
			vcejoi = 0
		vcpoi = request.form["vcpoi"]
		if len(vcpoi) < 1:
			vcpoi = 0
		vcavccoi = request.form["vcavccoi"]
		if len(vcavccoi) < 1:
			vcavccoi = 0
		#panel5
		roaeod = request.form["roaeod"]
		roacod = request.form["roacod"]
		if len(roaeod) < 1:
			roaeod = 0
		if len(roacod) < 1:
			roacod = 0
		roacod = float(roacod)
		if roacod > 0:
			roacod = roacod * -1
		roaejod = request.form["roaejod"]
		if len(roaejod) < 1:
			roaejod = 0
		roapod = request.form["roapod"]
		if len(roapod) < 1:
			roapod = 0
		roavod = request.form["roavod"]
		if len(roavod) < 1:
			roavod = 0
		roaavccod = request.form["roaavccod"]
		if len(roaavccod) < 1:
			roaavccod = 0
		roaeoi = request.form["roaeoi"]
		roacoi = request.form["roacoi"]
		if len(roaeoi) < 1:
			roaeoi = 0
		if len(roacoi) < 1:
			roacoi = 0
		roacoi = float(roacoi)
		if roacoi > 0:
			roacoi = roacoi * -1
		roaejoi = request.form["roaejoi"]
		if len(roaejoi) < 1:
			roaejoi = 0
		roapoi = request.form["roapoi"]
		if len(roapoi) < 1:
			roapoi = 0
		roavoi = request.form["roavoi"]
		if len(roavoi) < 1:
			roavoi = 0
		roaavccoi = request.form["roaavccoi"]
		if len(roaavccoi) < 1:
			roaavccoi = 0
		#panel6
		rseod = request.form["rseod"]
		rscod = request.form["rscod"]
		if len(rseod) < 1:
			rseod = 0
		if len(rscod) < 1:
			rscod = 0
		rscod = float(rscod)
		if rscod > 0:
			rscod = rscod * -1
		rsejod = request.form["rsejod"]
		rspod = request.form["rspod"]
		if len(rsejod) < 1:
			rsejod = 0
		if len(rspod) < 1:
			rspod = 0
		rsavccod = request.form["rsavccod"]
		rseoi = request.form["rseoi"]
		rscoi = request.form["rscoi"]
		if len(rsavccod) < 1:
			rsavccod = 0
		if len(rseoi) < 1:
			rseoi = 0
		if len(rscoi) < 1:
			rscoi = 0
		rscoi = float(rscoi)
		if rscoi > 0:
			rscoi = rscoi * -1
		rsejoi = request.form["rsejoi"]
		rspoi = request.form["rspoi"]
		if len(rsejoi) < 1:
			rsejoi = 0
		if len(rspoi) < 1:
			rspoi = 0
		rsavccoi = request.form["rsavccoi"]
		if len(rsavccoi) < 1:
			rsavccoi = 0
		try:
			pruamb = request.form["pruamb"]
		except:
			pruamb = 0
		try:
			pruest = request.form["pruest"]
		except:
			pruest = 0
		try:
			testbi = request.form["testbi"]
		except:
			testbi = 0
		try:
			equibino = request.form["equibino"]
		except:
			equibino = 0
		try:
			ciljackson = request.form["ciljackson"]
		except:
			ciljackson = 0
		#panel7
		rfe1od = request.form["rfe1od"]
		rfe2od = request.form["rfe2od"]
		rfe3od = request.form["rfe3od"]
		if len(rfe1od) < 1:
			rfe1od = 0
		if len(rfe2od) < 1:
			rfe2od = 0
		if len(rfe3od) < 1:
			rfe3od = 0
		rfc1od = request.form["rfc1od"]
		if len(rfc1od) < 1:
			rfc1od = 0
		rfc1od = float(rfc1od)
		if rfc1od > 0:
			rfc1od = rfc1od * -1
		rfc2od = request.form["rfc2od"]
		if len(rfc2od) < 1:
			rfc2od = 0
		rfc2od = float(rfc2od)
		if rfc2od > 0:
			rfc2od = rfc2od * -1
		rfc3od = request.form["rfc3od"]
		if len(rfc3od) < 1:
			rfc3od = 0
		rfc3od = float(rfc3od)
		if rfc3od > 0:
			rfc3od = rfc3od * -1
		rfej1od = request.form["rfej1od"]
		rfej2od = request.form["rfej2od"]
		rfej3od = request.form["rfej3od"]
		if len(rfej1od) < 1:
			rfej1od = 0
		if len(rfej2od) < 1:
			rfej2od = 0
		if len(rfej3od) < 1:
			rfej3od = 0
		rfp1od = request.form["rfp1od"]
		rfp2od = request.form["rfp2od"]
		rfp3od = request.form["rfp3od"]
		if len(rfp1od) < 1:
			rfp1od = 0
		if len(rfp2od) < 1:
			rfp2od = 0
		if len(rfp3od) < 1:
			rfp3od = 0
		rfavcc1od = request.form["rfavcc1od"]
		rfavcc2od = request.form["rfavcc2od"]
		rfavcc3od = request.form["rfavcc3od"]
		if len(rfavcc3od) < 1:
			rfavcc3od = 0
		if len(rfavcc2od) < 1:
			rfavcc2od = 0
		if len(rfavcc3od) < 1:
			rfavcc3od = 0
		rfe1oi = request.form["rfe1oi"]
		rfe2oi = request.form["rfe2oi"]
		rfe3oi = request.form["rfe3oi"]
		if len(rfe3oi) < 1:
			rfe3oi = 0
		if len(rfe2oi) < 1:
			rfe2oi = 0
		if len(rfe3oi) < 1:
			rfe3oi = 0
		rfc1oi = request.form["rfc1oi"]
		if len(rfc1oi) < 1:
			rfc1oi = 0
		rfc1oi = float(rfc1oi)
		if rfc1oi > 0:
			rfc1oi = rfc1oi * -1
		rfc2oi = request.form["rfc2oi"]
		if len(rfc2oi) < 1:
			rfc2oi = 0
		rfc2oi = float(rfc2oi)
		if rfc2oi > 0:
			rfc2oi = rfc2oi * -1
		rfc3oi = request.form["rfc3oi"]
		if len(rfc3oi) < 1:
			rfc3oi = 0
		rfc3oi = float(rfc3oi)
		if rfc3oi > 0:
			rfc3oi = rfc3oi * -1
		rfej1oi = request.form["rfej1oi"]
		rfej2oi = request.form["rfej2oi"]
		rfej3oi = request.form["rfej3oi"]
		if len(rfej1oi) < 1:
			rfej1oi = 0
		if len(rfej2oi) < 1:
			rfej2oi = 0
		if len(rfej3oi) < 1:
			rfej3oi = 0
		rfp1oi = request.form["rfp1oi"]
		rfp2oi = request.form["rfp2oi"]
		rfp3oi = request.form["rfp3oi"]
		if len(rfp1oi) < 1:
			rfp1oi = 0
		if len(rfp2oi) < 1:
			rfp2oi = 0
		if len(rfp3oi) < 1:
			rfp3oi = 0
		rfavcc1oi = request.form["rfavcc1oi"]
		rfavcc2oi = request.form["rfavcc2oi"]
		rfavcc3oi = request.form["rfavcc3oi"]
		if len(rfavcc1oi) < 1:
			rfavcc1oi = 0
		if len(rfavcc2oi) < 1:
			rfavcc2oi = 0
		if len(rfavcc3oi) < 1:
			rfavcc3oi = 0
		dnp = request.form["dnp"]
		dnp2 = request.form["dnp2"]
		dnp3 = request.form["dnp3"]
		if len(dnp) < 1:
			dnp = 0
		if len(dnp2) < 1:
			dnp2 = 0
		if len(dnp3) < 1:
			dnp3 = 0
		add11 = request.form["add11"]
		add22 = request.form["add22"]
		add33 = request.form["add33"]
		if len(add11) < 1:
			add11 = 0
		if len(add22) < 1:
			add22 = 0
		if len(add33) < 1:
			add33 = 0
		#panel8
		mmfod = request.form["mmfod"]
		mmfoi = request.form["mmfoi"]
		forod = request.form["forod"]
		foroi = request.form["foroi"]
		trood = request.form["trood"]
		trooi = request.form["trooi"]
		duccod = request.form["duccod"]
		duccoi = request.form["duccoi"]
		versiones = request.form["versiones"]
		convergencia = request.form["convergencia"]
		if len(mmfod) < 1:
			mmfod = 0
		if len(mmfoi) < 1:
			mmfoi = 0
		if len(forod) < 1:
			forod = 0
		if len(foroi) < 1:
			foroi = 0
		if len(trood) < 1:
			trood = 0
		if len(trooi) < 1:
			trooi = 0
		if len(duccod) < 1:
			duccod = 0
		if len(duccoi) < 1:
			duccoi = 0
		if len(versiones) < 1:
			versiones = 0
		if len(convergencia) < 1:
			convergencia = 0	
		try:
			ortoforico = request.form["ortoforico"]
		except:
			ortoforico = 0
		#panel9
		try:
			ojsal = request.form["ojsal"]
		except:
			ojsal = 0
		orbod = request.form["orbod"]
		orboi = request.form["orboi"]
		cejod = request.form["cejod"]
		cejoi = request.form["cejoi"]
		lagod = request.form["lagod"]
		lagoi = request.form["lagoi"]
		schod = request.form["schod"]
		schoi = request.form["schoi"]
		butod = request.form["butod"]
		butoi = request.form["butoi"]
		if len(orbod) < 1:
			orbod = 0
		if len(orboi) < 1:
			orboi = 0
		if len(cejod) < 1:
			cejod = 0
		if len(cejoi) < 1:
			cejoi = 0
		if len(lagod) < 1:
			lagod = 0
		if len(lagoi) < 1:
			lagoi = 0
		if len(schod) < 1:
			schod = 0
		if len(schoi) < 1:
			schoi = 0
		if len(butod) < 1:
			butod = 0
		if len(butoi) < 1:
			butoi = 0	
		vilagod = request.form["vilagod"]
		vilagoi = request.form["vilagoi"]
		pypod = request.form["pypod"]
		pypoi = request.form["pypoi"]
		conjod = request.form["conjod"]
		conjoi = request.form["conjoi"]
		esclod = request.form["esclod"]
		escloi = request.form["escloi"]
		cornod = request.form["cornod"]
		cornoi = request.form["cornoi"]
		if len(vilagod) < 1:
			vilagod = 0
		if len(vilagoi) < 1:
			vilagoi = 0
		if len(pypod) < 1:
			pypod = 0
		if len(pypoi) < 1:
			pypoi = 0
		if len(conjod) < 1:
			conjod = 0
		if len(conjoi) < 1:
			conjoi = 0
		if len(esclod) < 1:
			esclod = 0
		if len(escloi) < 1:
			escloi = 0
		if len(cornod) < 1:
			cornod = 0
		if len(cornoi) < 1:
			cornoi = 0	
		camaod = request.form["camaod"]
		camaoi = request.form["camaoi"]
		iriod = request.form["iriod"]
		irioi = request.form["irioi"]
		pupiod = request.form["pupiod"]
		pupioi = request.form["pupioi"]
		crisod = request.form["crisod"]
		crisoi = request.form["crisoi"]
		vitod = request.form["vitod"]
		vitoi = request.form["vitoi"]
		if len(camaod) < 1:
			camaod = 0
		if len(camaoi) < 1:
			camaoi = 0
		if len(iriod) < 1:
			iriod = 0
		if len(irioi) < 1:
			irioi = 0
		if len(pupiod) < 1:
			pupiod = 0
		if len(pupioi) < 1:
			pupioi = 0
		if len(crisod) < 1:
			crisod = 0
		if len(crisoi) < 1:
			crisoi = 0
		if len(vitod) < 1:
			vitod = 0
		if len(vitoi) < 1:
			vitoi = 0
		nervood = request.form["nervood"]
		nervooi = request.form["nervooi"]
		retppod = request.form["retppod"]
		retppoi = request.form["retppoi"]
		retpeod = request.form["retpeod"]
		retpeoi = request.form["retpeoi"]
		retmacod = request.form["retmacod"]
		retmacoi = request.form["retmacoi"]
		if len(nervood) < 1:
			nervood = 0
		if len(nervooi) < 1:
			nervooi = 0
		if len(retppod) < 1:
			retppod = 0
		if len(retppoi) < 1:
			retppoi = 0
		if len(retpeod) < 1:
			retpeod = 0
		if len(retpeoi) < 1:
			retpeoi = 0
		if len(retmacod) < 1:
			retmacod = 0
		if len(retmacoi) < 1:
			retmacoi = 0
		
		#panel10
		proxicita = request.form["proxicita"]
		usolent = request.form["usolent"]
		tipolent = request.form["tipolent"]
		materiallent = request.form["materiallent"]
		filtrolent = request.form["filtrolent"]
		colorlent = request.form["colorlent"]
		ambliopia = request.form["ambliopia"]
		ametropia = request.form["ametropia"]
		if len(ambliopia) < 1:
			ambliopia = 0
		if len(ametropia) < 1:
			ametropia = 0
		lentedetalladolent = request.form["lentedetalladolent"]
		if len(lentedetalladolent) < 1:
			lentedetalladolent = 15
		try:
			emetropia = request.form["emetropia"]
		except:
			emetropia = 0
		try:
			antimetropia = request.form["antimetropia"]
		except:
			antimetropia = 0
		try:
			anisometropia = request.form["anisometropia"]
		except:
			anisometropia = 0
		try:
			patologiaocular = request.form["patologiaocular"]
			patologiaoculartext = request.form["patologiaoculartext"]
		except:
			patologiaocular = 0
			patologiaoculartext = 0
		try:
			lentesoftalmicos = request.form["lentesoftalmicos"]
		except:
			lentesoftalmicos = 0
		try:
			lentescontacto = request.form["lentescontacto"]
		except:
			lentescontacto = 0
		try:
			refoftalmologica = request.form["refoftalmologica"]
		except:
			refoftalmologica = 0
		try:
			farmaco = request.form["farmaco"]
		except:
			farmaco = 0
		gmed1 = request.form["gmed1"]
		gdesc1 = request.form["gdesc1"]
		gmed2 = request.form["gmed2"]
		gdesc2 = request.form["gdesc2"]
		if len(gmed1) < 1:
			gmed1 = 0
		if len(gdesc1) < 1:
			gdesc1 = 0
		if len(gmed2) < 1:
			gmed2 = 0
		if len(gdesc2) < 1:
			gdesc2 = 0
		try:
			conexion = pymysql.connect(host='localhost', user='root', password='database', db='opticadb')
			try:
				with conexion.cursor() as cursor:
					#agudeza visual
					consulta = "insert into agudezavisual(idconsulta, idojo, avl, phae, avc) values (%s,%s,%s,%s,%s);"
					cursor.execute(consulta, (idconsulta, 1, avloi, aeoi, avcoi))
					consulta = "insert into agudezavisual(idconsulta, idojo, avl, phae, avc) values (%s,%s,%s,%s,%s);"
					cursor.execute(consulta, (idconsulta, 2, avlod, aeod, avcod))
					
					#refraccion actual
					consulta = "insert into refact(idconsulta, idojo, esfera, cilindro, eje, avcc1, prisma) values (%s,%s,%s,%s,%s,%s,%s);"
					cursor.execute(consulta, (idconsulta, 1, raeoi, racoi, raejoi, raavcc1oi, rapoi))
					consulta = "insert into refact(idconsulta, idojo, esfera, cilindro, eje, avcc1, prisma) values (%s,%s,%s,%s,%s,%s,%s);"
					cursor.execute(consulta, (idconsulta, 2, raeod, racod, raejod, raavcc1od, rapod))
					
					#Vision cercana
					consulta = "insert into ravc(idconsulta, idojo, esfera, cilindo, eje, avcc, prisma) values (%s,%s,%s,%s,%s,%s,%s);"
					cursor.execute(consulta, (idconsulta, 1, vceoi, vccoi, vcejoi, vcavccoi, vcpoi))
					consulta = "insert into ravc(idconsulta, idojo, esfera, cilindo, eje, avcc, prisma) values (%s,%s,%s,%s,%s,%s,%s);"
					cursor.execute(consulta, (idconsulta, 2, vceod, vccod, vcejod, vcavccod, vcpod))
					
					#Refraccion objetiva alumno
					consulta = "insert into refobjal(idconsulta, idojo, esfera, cilindro, eje, avcc, prisma, dvertice) values (%s,%s,%s,%s,%s,%s,%s,%s);"
					cursor.execute(consulta, (idconsulta, 1, roaeoi, roacoi, roaejoi, roaavccoi, roapoi, roavoi))
					consulta = "insert into refobjal(idconsulta, idojo, esfera, cilindro, eje, avcc, prisma, dvertice) values (%s,%s,%s,%s,%s,%s,%s,%s);"
					cursor.execute(consulta, (idconsulta, 2, roaeod, roacod, roaejod, roaavccod, roapod, roavod))
					
					#Refraccion subjetiva
					consulta = "insert into refsub(idconsulta, idojo, esfera, cilindro, eje, avcc, prisma, pruamb, testbi, equibino, pruest,ciljackson) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
					cursor.execute(consulta, (idconsulta, 1, rseoi, rscoi, rsejoi, rsavccoi, rspoi, pruamb, testbi, equibino, pruest, ciljackson))
					consulta = "insert into refsub(idconsulta, idojo, esfera, cilindro, eje, avcc, prisma, pruamb, testbi, equibino, pruest,ciljackson) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
					cursor.execute(consulta, (idconsulta, 2, rseod, rscod, rsejod, rsavccod, rspod, pruamb, testbi, equibino, pruest, ciljackson))
					
					#Refraccion final
					consulta = "insert into reffin(idconsulta, idojo, esfera1, esfera2, esfera3, cilindro1, cilindro2, cilindro3, eje1, eje2, eje3, avcc1, avcc2, avcc3, prisma1, prisma2, prisma3) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
					cursor.execute(consulta, (idconsulta, 1, rfe1oi, rfe2oi, rfe3oi, rfc1oi, rfc2oi, rfc3oi, rfej1oi, rfej2oi, rfej3oi, rfavcc1oi, rfavcc2oi, rfavcc3oi, rfp1oi, rfp2oi, rfp3oi))
					consulta = "insert into reffin(idconsulta, idojo, esfera1, esfera2, esfera3, cilindro1, cilindro2, cilindro3, eje1, eje2, eje3, avcc1, avcc2, avcc3, prisma1, prisma2, prisma3) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
					cursor.execute(consulta, (idconsulta, 2, rfe1od, rfe2od, rfe3od, rfc1od, rfc2od, rfc3od, rfej1od, rfej2od, rfej3od, rfavcc1od, rfavcc2od, rfavcc3od, rfp1od, rfp2od, rfp3od))
					
					#Motilidad Ocular
					consulta = "insert into motocu(idconsulta, idojo, mmf, forias, tropias, ducciones, versiones, convergencia, ortoforico) values (%s,%s,%s,%s,%s,%s,%s,%s,%s);"
					cursor.execute(consulta, (idconsulta, 1, mmfoi, foroi, trooi, duccoi, versiones, convergencia, ortoforico))
					consulta = "insert into motocu(idconsulta, idojo, mmf, forias, tropias, ducciones, versiones, convergencia, ortoforico) values (%s,%s,%s,%s,%s,%s,%s,%s,%s);"
					cursor.execute(consulta, (idconsulta, 2, mmfod, forod, trood, duccod, versiones, convergencia, ortoforico))
					
					#observaciones
					consulta = "insert into observaciones(idconsulta, idojo, valnormales, orbita, cejas, lagrima, viaslag, parpados, conjuntiva, esclera, cornea, camara, iris, pupila, cristalino, vitreo, nervioop, retinapp, retinape, retinamac, schirmer, but) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
					cursor.execute(consulta, (idconsulta, 1, ojsal, orboi, cejoi, lagoi, vilagoi, pypoi, conjoi, escloi, cornoi, camaoi, irioi, pupioi, crisoi, vitoi, nervooi, retppoi, retpeoi, retmacoi, schoi, butoi))
					consulta = "insert into observaciones(idconsulta, idojo, valnormales, orbita, cejas, lagrima, viaslag, parpados, conjuntiva, esclera, cornea, camara, iris, pupila, cristalino, vitreo, nervioop, retinapp, retinape, retinamac, schirmer, but) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
					cursor.execute(consulta, (idconsulta, 2, ojsal, orbod, cejod, lagod, vilagod, pypod, conjod, esclod, cornod, camaod, iriod, pupiod, crisod, vitod, nervood, retppod, retpeod, retmacod, schod, butod))

					#Lente recomendado
					consulta = "insert into lenterecomendado(idconsulta, tipo, material, filtro, color, lentedetallado) values (%s,%s,%s,%s,%s,%s);"
					cursor.execute(consulta, (idconsulta, tipolent, materiallent, filtrolent, colorlent, lentedetalladolent))

					#consulta
					consulta = "update consulta set idusolen=%s, proximacita=%s, dnp=%s,dnp1=%s, add1=%s, add2=%s, add3=%s, add11=%s, add22=%s, add33=%s, aprobado=1, iduser=%s, dnp2=%s, dnp3=%s, ojoambliopia=%s, emetropia=%s, antimetropia=%s, tipoametropia=%s, anisometropia=%s, patologiaocular=%s, lentesoftalmicos=%s, lentescontacto=%s, refoftalmologica=%s, farmaco=%s, motivoconsulta=%s, ultimaevmes=%s, ultimaevanio=%s, tiempolen=%s where idconsulta = %s;"
					cursor.execute(consulta, (usolent, proxicita, dnp, dnp1, add1, add2, add3, add11, add22, add33, session['iduser1'], dnp2, dnp3, ambliopia, emetropia, antimetropia, ametropia, anisometropia, patologiaoculartext, lentesoftalmicos, lentescontacto, refoftalmologica, farmaco, motivoconsulta, ultimaevmes, ultimaevanio, tiempolentes, idconsulta))

					#gotas
					consulta = "insert into recetagotero(idconsulta, medicamento1, descripcion1, medicamento2, descripcion2) values(%s,%s,%s,%s,%s)"
					cursor.execute(consulta, (idconsulta, gmed1, gdesc1,gmed2, gdesc2))
				conexion.commit()
			finally:
				conexion.close()
		except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
			print("Ocurrió un error al conectar: ", e)
		try:
			conexion = pymysql.connect(host='localhost', user='root', password='database', db='opticadb')
			try:
				with conexion.cursor() as cursor:
					consulta = "select idantecedentes from antecedentes where idpaciente = %s;"
					cursor.execute(consulta, idpaciente)
					antecedentes = cursor.fetchall()
					exicui = len(antecedentes)
					print(exicui)
					#antecedentes
					if exicui == 0:
						consulta = "insert into antecedentes(idpaciente, oftalmologicos, familiares, glaucoma, alergicas) values (%s,%s,%s,%s,%s);"
						cursor.execute(consulta, (idpaciente, antoftal, antfam, antgla, antaler))
					else:
						consulta = "update antecedentes set oftalmologicos = %s, familiares = %s, glaucoma = %s, alergicas = %s where idpaciente = %s;"
						cursor.execute(consulta, (antoftal, antfam, antgla, antaler, idpaciente))
				conexion.commit()
			finally:
				conexion.close()
		except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
			print("Ocurrió un error al conectar: ", e)
		try:
			conexion = pymysql.connect(host='localhost', user='root', password='database', db='opticadb')
			try:
				with conexion.cursor() as cursor:
					consulta = "select idantecedentes from antecedentes where idpaciente = %s;"
					cursor.execute(consulta, idpaciente)
					dataantecedentes = cursor.fetchall()
					idantecedentes = dataantecedentes[0][0]
					for i in range(numantmed):
						consulta = "insert into antmed(idantecedentes, enfermedad, tiempoevolucion, control, otro) values (%s,%s,%s,%s,%s);"
						cursor.execute(consulta, (idantecedentes, antmed[i][0], antmed[i][2],antmed[i][3],antmed[i][1]))
					for i in range(numantqui):
						consulta = "insert into antquir(idantecedentes, cirugia, tiempoevolucion, control) values (%s,%s,%s,%s);"
						cursor.execute(consulta, (idantecedentes, antqui[i][0], antqui[i][1],antqui[i][2]))
				conexion.commit()
			finally:
				conexion.close()
		except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
			print("Ocurrió un error al conectar: ", e)
		return redirect(url_for('home'))
	return render_template('pendaprobarc.html', title='Pendiente de aprobación', logeado=logeado, paciente = paciente, 
		dataconsulta=dataconsulta, anios=anios, cincos=cincos, meses=meses, usolen=usolen, 
		enfermedades=enfermedades,nervos=nervos, mms=mms, numeros=numeros, relva=relva, 
		tipolen=tipolen, materiallen=materiallen, filtrolen=filtrolen, colorlen=colorlen, 
		dataojo=dataojo, dataametropia=dataametropia, new_date=new_date, fechafoto=fechafoto,
		lentedetalladolen=lentedetalladolen)

@app.route("/ver/<idpaciente>", methods=['GET', 'POST'])
def ver(idpaciente):
	try:
		logeado = session['logeado1']
	except:
		logeado = 0
	try:
		conexion = pymysql.connect(host='localhost', user='root', password='database', db='opticadb')
		try:
			with conexion.cursor() as cursor:
				consulta = "select idusolen, uso from usolen;"
				cursor.execute(consulta)
				usolen = cursor.fetchall()
				consulta = "select idrelacionvenaarteria, relacion from relacionvenaarteria;"
				cursor.execute(consulta)
				relva = cursor.fetchall()
				consulta = "select idtipolen, tipo from tipolen;"
				cursor.execute(consulta)
				tipolen = cursor.fetchall()
				consulta = "select idmateriallen, material from materiallen;"
				cursor.execute(consulta)
				materiallen = cursor.fetchall()
				consulta = "select idfiltrolen, filtro from filtrolen order by filtro asc;"
				cursor.execute(consulta)
				filtrolen = cursor.fetchall()
				consulta = "select idlentedetallado, lentedetallado from lentedetallado order by lentedetallado asc;"
				cursor.execute(consulta)
				lentedetalladolen = cursor.fetchall()
				consulta = "select idcolorlen, color from colorlen;"
				cursor.execute(consulta)
				colorlen = cursor.fetchall()
				consulta = "select idojo, ojo from ojo;"
				cursor.execute(consulta)
				dataojo = cursor.fetchall()
				consulta = "select idtipoametropia, tipo from tipoametropia;"
				cursor.execute(consulta)
				dataametropia = cursor.fetchall()
		finally:
			conexion.close()
	except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
		print("Ocurrió un error al conectar: ", e)
	dateac = date.today()
	d3 = dateac.strftime("%d/%m/%y")
	d3 = str(d3)
	year = dateac.strftime("%Y")
	year = int(year)
	nervos = []
	nervo = 1
	for i in range(11):
		nervos.append(nervo*i)
	numeros = []
	numero = 0
	for i in range(36):
		numeros.append(numero)
		numero = numero + 1
	mms = []
	mm = 0
	for i in range(8):
		mms.append(mm)
		mm = mm + 5
	anios = []
	for i in range(80):
		anios.append(year)
		year = year - 1
	cincos = []
	cinco = 0
	for i in range(15):
		cincos.append(cinco)
		cinco = cinco + 5
	meses = [[1, "Enero"],[2, "Febrero"],[3, "Marzo"],[4, "Abril"],[5, "Mayo"],[6, "Junio"],[7, "Julio"],[8, "Agosto"],[9, "Septiembre"],[10, "Octubre"],[11, "Noviembre"],[12, "Diciembre"]]
	enfermedades = [['Diabetes Mellitus'],['Hipertensión Arterial'],['Artritis Reumatoidea'],['Virus Inmunodeficiencia Humana'],['Hipertrigliceridemia'],['Colesterolemia'], ['Otro']]

	try:
		conexion = pymysql.connect(host='localhost', user='root', password='database', db='opticadb')
		try:
			with conexion.cursor() as cursor:
				consulta = "SELECT idconsulta, DATE_FORMAT(fecha,'%d/%m/%Y') from consulta where idpaciente = "+ str(idpaciente) + " order by fecha asc;"
				cursor.execute(consulta)
				listconsultas = cursor.fetchall()
				conteo = len(listconsultas)
				consulta = "SELECT idconsulta from consulta where idpaciente = "+ str(idpaciente) + " and fecha = '"+ str(dateac) + "' and aprobado = 0 order by fecha asc;"
				cursor.execute(consulta)
				dateaux = cursor.fetchall()
				if len(dateaux) > 0:
					haynew = 1
					idconsulta = dateaux[0][0]
				else:
					haynew = 0
		finally:
			conexion.close()
	except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
		print("Ocurrió un error al conectar: ", e)

	ingresconsultas = []

	for i in listconsultas:
		ingreconsulta = []
		try:
			conexion = pymysql.connect(host='localhost', user='root', password='database', db='opticadb')
			try:
				with conexion.cursor() as cursor:
					consulta = "SELECT idpaciente, ojoambliopia, tipoametropia, idusolen, proximacita, dnp, dnp1, dnp2, dnp3, ultimaevmes, ultimaevanio, tiempolen, add1, add2, add3, add11, add22, add33, emetropia, antimetropia, anisometropia, patologiaocular, lentesoftalmicos, lentescontacto, refoftalmologica, farmaco, DATE_FORMAT(fecha,'%d%m%Y'), motivoconsulta, tipoametropiaoi, referenciaoftal from consulta where idconsulta = "+ str(i[0]) + ";"
					cursor.execute(consulta)
					dataconsulta = cursor.fetchall()
					idpaciente = dataconsulta[0][0]
					fechafoto = dataconsulta[0][26]
					ingreconsulta.append(dataconsulta)
					ingreconsulta.append(fechafoto)
			finally:
				conexion.close()
		except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
			print("Ocurrió un error al conectar: ", e)
		try:
			conexion = pymysql.connect(host='localhost', user='root', password='database', db='opticadb')
			try:
				with conexion.cursor() as cursor:
					consulta = "SELECT p.nombre1, p.nombre2, p.apellido1, p.apellido2, p.fechanac, s.sexo, p.profesion, p.direccion, p.cui, p.telefono, p.telefono2 from paciente p inner join sexo s on p.idsexo = s.idsexo where idpaciente = %s"
					cursor.execute(consulta, (idpaciente))
					paciente = cursor.fetchall()
					paciente = paciente[0]
					ingreconsulta.append(paciente)
					consulta = "SELECT oftalmologicos, familiares, glaucoma, alergicas, idantecedentes from antecedentes where idpaciente = %s;"
					cursor.execute(consulta, idpaciente)
					antecedentes = cursor.fetchone()
					idantecedentes = antecedentes[4]
					ingreconsulta.append(antecedentes)
					ingreconsulta.append(idantecedentes)
					consulta = "SELECT enfermedad, tiempoevolucion, control, otro from antmed where idantecedentes = %s;"
					cursor.execute(consulta, idantecedentes)
					antmed = cursor.fetchall()
					numantmed = len(antmed)
					ingreconsulta.append(antmed)
					ingreconsulta.append(numantmed)
					consulta = "SELECT cirugia, tiempoevolucion, control from antquir where idantecedentes = %s;"
					cursor.execute(consulta, idantecedentes)
					antqui = cursor.fetchall()
					numantqui = len(antqui)
					ingreconsulta.append(antqui)
					ingreconsulta.append(numantqui)
					consulta = "SELECT tipo, material, filtro, color, lentedetallado from lenterecomendado where idconsulta = %s;"
					cursor.execute(consulta, i[0])
					lenterecomendado = cursor.fetchall()
					ingreconsulta.append(lenterecomendado)
					av = []
					consulta = "SELECT avl, phae, avc from agudezavisual where idojo = 2 and idconsulta = %s;"
					cursor.execute(consulta, i[0])
					aux = cursor.fetchone()
					av.append(aux)
					consulta = "SELECT avl, phae, avc from agudezavisual where idojo = 1 and idconsulta = %s;"
					cursor.execute(consulta, i[0])
					aux = cursor.fetchone()
					av.append(aux)
					ingreconsulta.append(av)
					ra = []
					consulta = "SELECT esfera, cilindro, eje, prisma, avcc1 from refact where idojo = 2 and idconsulta = %s;"
					cursor.execute(consulta, i[0])
					aux = cursor.fetchone()
					ra.append(aux)
					consulta = "SELECT esfera, cilindro, eje, prisma, avcc1 from refact where idojo = 1 and idconsulta = %s;"
					cursor.execute(consulta, i[0])
					aux = cursor.fetchone()
					ra.append(aux)
					ingreconsulta.append(ra)
					vc = []
					consulta = "SELECT esfera, cilindo, eje, prisma, avcc from ravc where idojo = 2 and idconsulta = %s;"
					cursor.execute(consulta, i[0])
					aux = cursor.fetchone()
					vc.append(aux)
					consulta = "SELECT esfera, cilindo, eje, prisma, avcc from ravc where idojo = 1 and idconsulta = %s;"
					cursor.execute(consulta, i[0])
					aux = cursor.fetchone()
					vc.append(aux)
					ingreconsulta.append(vc)
					roa = []
					consulta = "SELECT esfera, cilindro, eje, prisma, dvertice, avcc from refobjal where idojo = 2 and idconsulta = %s;"
					cursor.execute(consulta, i[0])
					aux = cursor.fetchone()
					roa.append(aux)
					consulta = "SELECT esfera, cilindro, eje, prisma, dvertice, avcc from refobjal where idojo = 1 and idconsulta = %s;"
					cursor.execute(consulta, i[0])
					aux = cursor.fetchone()
					roa.append(aux)
					ingreconsulta.append(roa)
					rs = []
					consulta = "SELECT esfera, cilindro, eje, prisma, avcc, pruamb, testbi, equibino, pruest, ciljackson from refsub where idojo = 2 and idconsulta = %s;"
					cursor.execute(consulta, i[0])
					aux = cursor.fetchone()
					rs.append(aux)
					consulta = "SELECT esfera, cilindro, eje, prisma, avcc, pruamb, testbi, equibino from refsub where idojo = 1 and idconsulta = %s;"
					cursor.execute(consulta, i[0])
					aux = cursor.fetchone()
					rs.append(aux)
					ingreconsulta.append(rs)
					rf = []
					consulta = "SELECT esfera1, esfera2, esfera3, cilindro1, cilindro2, cilindro3, eje1, eje2, eje3, prisma1, prisma2, prisma3, avcc1, avcc2, avcc3 from reffin where idojo = 2 and idconsulta = %s;"
					cursor.execute(consulta, i[0])
					aux = cursor.fetchone()
					rf.append(aux)
					consulta = "SELECT esfera1, esfera2, esfera3, cilindro1, cilindro2, cilindro3, eje1, eje2, eje3, prisma1, prisma2, prisma3, avcc1, avcc2, avcc3 from reffin where idojo = 1 and idconsulta = %s;"
					cursor.execute(consulta, i[0])
					aux = cursor.fetchone()
					rf.append(aux)
					ingreconsulta.append(rf)
					mo = []
					consulta = "SELECT mmf, forias, tropias, ducciones, versiones, convergencia, ortoforico from motocu where idojo = 2 and idconsulta = %s;"
					cursor.execute(consulta, i[0])
					aux = cursor.fetchone()
					mo.append(aux)
					consulta = "SELECT mmf, forias, tropias, ducciones, versiones, convergencia, ortoforico from motocu where idojo = 1 and idconsulta = %s;"
					cursor.execute(consulta, i[0])
					aux = cursor.fetchone()
					mo.append(aux)
					ingreconsulta.append(mo)
					obs = []
					consulta = "SELECT valnormales, orbita, cejas, lagrima, viaslag, parpados, conjuntiva, esclera, cornea, camara, iris, pupila, cristalino, vitreo, nervioop, retinapp, retinape,retinamac, schirmer, but from observaciones where idojo = 2 and idconsulta = %s;"
					cursor.execute(consulta, i[0])
					aux = cursor.fetchone()
					obs.append(aux)
					consulta = "SELECT valnormales, orbita, cejas, lagrima, viaslag, parpados, conjuntiva, esclera, cornea, camara, iris, pupila, cristalino, vitreo, nervioop, retinapp, retinape,retinamac, schirmer, but from observaciones where idojo = 1 and idconsulta = %s;"
					cursor.execute(consulta, i[0])
					aux = cursor.fetchone()
					obs.append(aux)
					ingreconsulta.append(obs)
					consulta = "SELECT medicamento1, descripcion1, medicamento2, descripcion2 from recetagotero where idconsulta = %s;"
					cursor.execute(consulta, i[0])
					gotas = cursor.fetchone()
					ingreconsulta.append(gotas)
					ingresconsultas.append(ingreconsulta)
			finally:
				conexion.close()
		except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
			print("Ocurrió un error al conectar: ", e)
	if request.method == 'POST':
		#panel2
		motivoconsulta = request.form["motivoconsulta"]
		if len(motivoconsulta) < 1:
			motivoconsulta = 0
		ultimaevmes = request.form["ultimaevmes"]
		ultimaevanio = request.form["ultimaevanio"]
		tiempolentes = request.form["tiempolentes"]
		if len(ultimaevmes) < 1:
			ultimaevmes = 0
		if len(ultimaevanio) < 1:
			ultimaevanio = 0
		if len(tiempolentes) < 1:
			tiempolentes = 0
		antoftal = request.form["antoftal"]
		if len(antoftal) < 1:
			antoftal = 0
		antfam = request.form["antfam"]
		antaler = request.form["antaler"]
		antgla = request.form["antgla"]
		if len(antfam) < 1:
			antfam = 0
		if len(antaler) < 1:
			antaler = 0
		if len(antgla) < 1:
			antgla = 0
		numantmed = request.form["numantmed"]
		numantqui = request.form["numantqui"]
		numantmed = int(numantmed)
		numantqui = int(numantqui)
		antmed = []
		antqui = []
		for i in range(numantmed):
			aux = 'enfermedad' + str(i+1)
			enfermedad = request.form[aux]
			if len(enfermedad) < 1:
				enfermedad = 0
			try:
				aux = 'medotro' + str(i+1)
				otro = request.form[aux]
				if len(otro) < 1:
					otro = 0
			except:
				otro = 0
			aux = 'tiempoevolucionm' + str(i+1)
			tiempoev = request.form[aux]
			if len(tiempoev) < 1:
				tiempoev = 0
			aux = 'controlm' + str(i+1)
			control = request.form[aux]
			if len(control) < 1:
				control = 0
			aux = [enfermedad, otro, tiempoev, control]
			antmed.append(aux)
		for i in range(numantqui):
			aux = 'cirugia' + str(i+1)
			cirugia = request.form[aux]
			if len(cirugia) < 1:
				cirugia = 0
			aux = 'tiempoevolucionq' + str(i+1)
			tiempoev = request.form[aux]
			if len(tiempoev) < 1:
				tiempoev = 0
			aux = 'controlq' + str(i+1)
			control = request.form[aux]
			if len(control) < 1:
				control = 0
			aux = [cirugia, tiempoev, control]
			antqui.append(aux)
		#panel3
		avlod = request.form["avlod"]
		avloi = request.form["avloi"]
		aeod = request.form["aeod"]
		aeoi = request.form["aeoi"]
		avcod = request.form["avcod"]
		avcoi = request.form["avcoi"]
		if len(avcod) < 1:
			avcod = 0
		if len(avcoi) < 1:
			avcoi = 0
		if len(avlod) < 1:
			avlod = 0
		if len(avloi) < 1:
			avloi = 0
		if len(aeod) < 1:
			aeod = 0
		if len(aeoi) < 1:
			aeoi = 0
		#panel4
		raeod = request.form["raeod"]
		racod = request.form["racod"]
		if len(raeod) < 1:
			raeod = 0
		if len(racod) < 1:
			racod = 0
		racod = float(racod)
		if racod > 0:
			racod = racod * -1
		raejod = request.form["raejod"]
		if len(raejod) < 1:
			raejod = 0
		rapod = request.form["rapod"]
		if len(rapod) < 1:
			rapod = 0
		raavcc1od = request.form["raavcc1od"]
		if len(str(raavcc1od)) < 1:
			raavcc1od = 0
		raeoi = request.form["raeoi"]
		racoi = request.form["racoi"]
		if len(raeoi) < 1:
			raeoi = 0
		if len(racoi) < 1:
			racoi = 0
		racoi = float(racoi)
		if racoi > 0:
			racoi = racoi * -1
		raejoi = request.form["raejoi"]
		if len(raejoi) < 1:
			raejoi = 0
		rapoi = request.form["rapoi"]
		if len(rapoi) < 1:
			rapoi = 0
		raavcc1oi = request.form["raavcc1oi"]
		if len(raavcc1oi) < 1:
			raavcc1oi = 0
		add1 = request.form["add1"]
		if len(add1) < 1:
			add1 = 0
		add2 = request.form["add2"]
		if len(add2) < 1:
			add2 = 0
		add3 = request.form["add3"]
		if len(add3) < 1:
			add3 = 0
		dnp1 = request.form["dnp1"]
		if len(dnp1) < 1:
			dnp1 = 0
		vceod = request.form["vceod"]
		vccod = request.form["vccod"]
		if len(vceod) < 1:
			vceod = 0
		if len(vccod) < 1:
			vccod = 0
		vccod = float(vccod)
		if vccod > 0:
			vccod = vccod * -1
		vcejod = request.form["vcejod"]
		if len(vcejod) < 1:
			vcejod = 0
		vcpod = request.form["vcpod"]
		if len(vcpod) < 1:
			vcpod = 0
		vcavccod = request.form["vcavccod"]
		vceoi = request.form["vceoi"]
		vccoi = request.form["vccoi"]
		if len(vcavccod) < 1:
			vcavccod = 0
		if len(vceoi) < 1:
			vceoi = 0
		if len(vccoi) < 1:
			vccoi = 0
		vccoi = float(vccoi)
		if vccoi > 0:
			vccoi = vccoi * -1
		vcejoi = request.form["vcejoi"]
		if len(vcejoi) < 1:
			vcejoi = 0
		vcpoi = request.form["vcpoi"]
		if len(vcpoi) < 1:
			vcpoi = 0
		vcavccoi = request.form["vcavccoi"]
		if len(vcavccoi) < 1:
			vcavccoi = 0
		#panel5
		roaeod = request.form["roaeod"]
		roacod = request.form["roacod"]
		if len(roaeod) < 1:
			roaeod = 0
		if len(roacod) < 1:
			roacod = 0
		roacod = float(roacod)
		if roacod > 0:
			roacod = roacod * -1
		roaejod = request.form["roaejod"]
		if len(roaejod) < 1:
			roaejod = 0
		roapod = request.form["roapod"]
		if len(roapod) < 1:
			roapod = 0
		roavod = request.form["roavod"]
		if len(roavod) < 1:
			roavod = 0
		roaavccod = request.form["roaavccod"]
		if len(roaavccod) < 1:
			roaavccod = 0
		roaeoi = request.form["roaeoi"]
		roacoi = request.form["roacoi"]
		if len(roaeoi) < 1:
			roaeoi = 0
		if len(roacoi) < 1:
			roacoi = 0
		roacoi = float(roacoi)
		if roacoi > 0:
			roacoi = roacoi * -1
		roaejoi = request.form["roaejoi"]
		if len(roaejoi) < 1:
			roaejoi = 0
		roapoi = request.form["roapoi"]
		if len(roapoi) < 1:
			roapoi = 0
		roavoi = request.form["roavoi"]
		if len(roavoi) < 1:
			roavoi = 0
		roaavccoi = request.form["roaavccoi"]
		if len(roaavccoi) < 1:
			roaavccoi = 0
		#panel6
		rseod = request.form["rseod"]
		rscod = request.form["rscod"]
		if len(rseod) < 1:
			rseod = 0
		if len(rscod) < 1:
			rscod = 0
		rscod = float(rscod)
		if rscod > 0:
			rscod = rscod * -1
		rsejod = request.form["rsejod"]
		rspod = request.form["rspod"]
		if len(rsejod) < 1:
			rsejod = 0
		if len(rspod) < 1:
			rspod = 0
		rsavccod = request.form["rsavccod"]
		rseoi = request.form["rseoi"]
		rscoi = request.form["rscoi"]
		if len(rsavccod) < 1:
			rsavccod = 0
		if len(rseoi) < 1:
			rseoi = 0
		if len(rscoi) < 1:
			rscoi = 0
		rscoi = float(rscoi)
		if rscoi > 0:
			rscoi = rscoi * -1
		rsejoi = request.form["rsejoi"]
		rspoi = request.form["rspoi"]
		if len(rsejoi) < 1:
			rsejoi = 0
		if len(rspoi) < 1:
			rspoi = 0
		rsavccoi = request.form["rsavccoi"]
		if len(rsavccoi) < 1:
			rsavccoi = 0
		try:
			pruamb = request.form["pruamb"]
		except:
			pruamb = 0
		try:
			pruest = request.form["pruest"]
		except:
			pruest = 0
		try:
			testbi = request.form["testbi"]
		except:
			testbi = 0
		try:
			equibino = request.form["equibino"]
		except:
			equibino = 0
		try:
			ciljackson = request.form["ciljackson"]
		except:
			ciljackson = 0
		#panel7
		rfe1od = request.form["rfe1od"]
		rfe2od = request.form["rfe2od"]
		rfe3od = request.form["rfe3od"]
		if len(rfe1od) < 1:
			rfe1od = 0
		if len(rfe2od) < 1:
			rfe2od = 0
		if len(rfe3od) < 1:
			rfe3od = 0
		rfc1od = request.form["rfc1od"]
		if len(rfc1od) < 1:
			rfc1od = 0
		rfc1od = float(rfc1od)
		if rfc1od > 0:
			rfc1od = rfc1od * -1
		rfc2od = request.form["rfc2od"]
		if len(rfc2od) < 1:
			rfc2od = 0
		rfc2od = float(rfc2od)
		if rfc2od > 0:
			rfc2od = rfc2od * -1
		rfc3od = request.form["rfc3od"]
		if len(rfc3od) < 1:
			rfc3od = 0
		rfc3od = float(rfc3od)
		if rfc3od > 0:
			rfc3od = rfc3od * -1
		rfej1od = request.form["rfej1od"]
		rfej2od = request.form["rfej2od"]
		rfej3od = request.form["rfej3od"]
		if len(rfej1od) < 1:
			rfej1od = 0
		if len(rfej2od) < 1:
			rfej2od = 0
		if len(rfej3od) < 1:
			rfej3od = 0
		rfp1od = request.form["rfp1od"]
		rfp2od = request.form["rfp2od"]
		rfp3od = request.form["rfp3od"]
		if len(rfp1od) < 1:
			rfp1od = 0
		if len(rfp2od) < 1:
			rfp2od = 0
		if len(rfp3od) < 1:
			rfp3od = 0
		rfavcc1od = request.form["rfavcc1od"]
		rfavcc2od = request.form["rfavcc2od"]
		rfavcc3od = request.form["rfavcc3od"]
		if len(rfavcc3od) < 1:
			rfavcc3od = 0
		if len(rfavcc2od) < 1:
			rfavcc2od = 0
		if len(rfavcc3od) < 1:
			rfavcc3od = 0
		rfe1oi = request.form["rfe1oi"]
		rfe2oi = request.form["rfe2oi"]
		rfe3oi = request.form["rfe3oi"]
		if len(rfe3oi) < 1:
			rfe3oi = 0
		if len(rfe2oi) < 1:
			rfe2oi = 0
		if len(rfe3oi) < 1:
			rfe3oi = 0
		rfc1oi = request.form["rfc1oi"]
		if len(rfc1oi) < 1:
			rfc1oi = 0
		rfc1oi = float(rfc1oi)
		if rfc1oi > 0:
			rfc1oi = rfc1oi * -1
		rfc2oi = request.form["rfc2oi"]
		if len(rfc2oi) < 1:
			rfc2oi = 0
		rfc2oi = float(rfc2oi)
		if rfc2oi > 0:
			rfc2oi = rfc2oi * -1
		rfc3oi = request.form["rfc3oi"]
		if len(rfc3oi) < 1:
			rfc3oi = 0
		rfc3oi = float(rfc3oi)
		if rfc3oi > 0:
			rfc3oi = rfc3oi * -1
		rfej1oi = request.form["rfej1oi"]
		rfej2oi = request.form["rfej2oi"]
		rfej3oi = request.form["rfej3oi"]
		if len(rfej1oi) < 1:
			rfej1oi = 0
		if len(rfej2oi) < 1:
			rfej2oi = 0
		if len(rfej3oi) < 1:
			rfej3oi = 0
		rfp1oi = request.form["rfp1oi"]
		rfp2oi = request.form["rfp2oi"]
		rfp3oi = request.form["rfp3oi"]
		if len(rfp1oi) < 1:
			rfp1oi = 0
		if len(rfp2oi) < 1:
			rfp2oi = 0
		if len(rfp3oi) < 1:
			rfp3oi = 0
		rfavcc1oi = request.form["rfavcc1oi"]
		rfavcc2oi = request.form["rfavcc2oi"]
		rfavcc3oi = request.form["rfavcc3oi"]
		if len(rfavcc1oi) < 1:
			rfavcc1oi = 0
		if len(rfavcc2oi) < 1:
			rfavcc2oi = 0
		if len(rfavcc3oi) < 1:
			rfavcc3oi = 0
		dnp = request.form["dnp"]
		dnp2 = request.form["dnp2"]
		dnp3 = request.form["dnp3"]
		if len(dnp) < 1:
			dnp = 0
		if len(dnp2) < 1:
			dnp2 = 0
		if len(dnp3) < 1:
			dnp3 = 0
		add11 = request.form["add11"]
		add22 = request.form["add22"]
		add33 = request.form["add33"]
		if len(add11) < 1:
			add11 = 0
		if len(add22) < 1:
			add22 = 0
		if len(add33) < 1:
			add33 = 0
		#panel8
		mmfod = request.form["mmfod"]
		mmfoi = request.form["mmfoi"]
		forod = request.form["forod"]
		foroi = request.form["foroi"]
		trood = request.form["trood"]
		trooi = request.form["trooi"]
		duccod = request.form["duccod"]
		duccoi = request.form["duccoi"]
		versiones = request.form["versiones"]
		convergencia = request.form["convergencia"]
		if len(mmfod) < 1:
			mmfod = 0
		if len(mmfoi) < 1:
			mmfoi = 0
		if len(forod) < 1:
			forod = 0
		if len(foroi) < 1:
			foroi = 0
		if len(trood) < 1:
			trood = 0
		if len(trooi) < 1:
			trooi = 0
		if len(duccod) < 1:
			duccod = 0
		if len(duccoi) < 1:
			duccoi = 0
		if len(versiones) < 1:
			versiones = 0
		if len(convergencia) < 1:
			convergencia = 0	
		try:
			ortoforico = request.form["ortoforico"]
		except:
			ortoforico = 0
		#panel9
		try:
			ojsal = request.form["ojsal"]
		except:
			ojsal = 0
		orbod = request.form["orbod"]
		orboi = request.form["orboi"]
		cejod = request.form["cejod"]
		cejoi = request.form["cejoi"]
		lagod = request.form["lagod"]
		lagoi = request.form["lagoi"]
		schod = request.form["schod"]
		schoi = request.form["schoi"]
		butod = request.form["butod"]
		butoi = request.form["butoi"]
		if len(orbod) < 1:
			orbod = 0
		if len(orboi) < 1:
			orboi = 0
		if len(cejod) < 1:
			cejod = 0
		if len(cejoi) < 1:
			cejoi = 0
		if len(lagod) < 1:
			lagod = 0
		if len(lagoi) < 1:
			lagoi = 0
		if len(schod) < 1:
			schod = 0
		if len(schoi) < 1:
			schoi = 0
		if len(butod) < 1:
			butod = 0
		if len(butoi) < 1:
			butoi = 0	
		vilagod = request.form["vilagod"]
		vilagoi = request.form["vilagoi"]
		pypod = request.form["pypod"]
		pypoi = request.form["pypoi"]
		conjod = request.form["conjod"]
		conjoi = request.form["conjoi"]
		esclod = request.form["esclod"]
		escloi = request.form["escloi"]
		cornod = request.form["cornod"]
		cornoi = request.form["cornoi"]
		if len(vilagod) < 1:
			vilagod = 0
		if len(vilagoi) < 1:
			vilagoi = 0
		if len(pypod) < 1:
			pypod = 0
		if len(pypoi) < 1:
			pypoi = 0
		if len(conjod) < 1:
			conjod = 0
		if len(conjoi) < 1:
			conjoi = 0
		if len(esclod) < 1:
			esclod = 0
		if len(escloi) < 1:
			escloi = 0
		if len(cornod) < 1:
			cornod = 0
		if len(cornoi) < 1:
			cornoi = 0	
		camaod = request.form["camaod"]
		camaoi = request.form["camaoi"]
		iriod = request.form["iriod"]
		irioi = request.form["irioi"]
		pupiod = request.form["pupiod"]
		pupioi = request.form["pupioi"]
		crisod = request.form["crisod"]
		crisoi = request.form["crisoi"]
		vitod = request.form["vitod"]
		vitoi = request.form["vitoi"]
		if len(camaod) < 1:
			camaod = 0
		if len(camaoi) < 1:
			camaoi = 0
		if len(iriod) < 1:
			iriod = 0
		if len(irioi) < 1:
			irioi = 0
		if len(pupiod) < 1:
			pupiod = 0
		if len(pupioi) < 1:
			pupioi = 0
		if len(crisod) < 1:
			crisod = 0
		if len(crisoi) < 1:
			crisoi = 0
		if len(vitod) < 1:
			vitod = 0
		if len(vitoi) < 1:
			vitoi = 0
		nervood = request.form["nervood"]
		nervooi = request.form["nervooi"]
		retppod = request.form["retppod"]
		retppoi = request.form["retppoi"]
		retpeod = request.form["retpeod"]
		retpeoi = request.form["retpeoi"]
		retmacod = request.form["retmacod"]
		retmacoi = request.form["retmacoi"]
		if len(nervood) < 1:
			nervood = 0
		if len(nervooi) < 1:
			nervooi = 0
		if len(retppod) < 1:
			retppod = 0
		if len(retppoi) < 1:
			retppoi = 0
		if len(retpeod) < 1:
			retpeod = 0
		if len(retpeoi) < 1:
			retpeoi = 0
		if len(retmacod) < 1:
			retmacod = 0
		if len(retmacoi) < 1:
			retmacoi = 0
		
		#panel10
		proxicita = request.form["proxicita"]
		usolent = request.form["usolent"]
		tipolent = request.form["tipolent"]
		materiallent = request.form["materiallent"]
		filtrolent = request.form["filtrolent"]
		colorlent = request.form["colorlent"]
		ambliopia = request.form["ambliopia"]
		ametropia = request.form["ametropia"]
		ametropiaoi = request.form["ametropiaoi"]
		if len(ambliopia) < 1:
			ambliopia = 0
		if len(ametropia) < 1:
			ametropia = 0
		if len(ametropiaoi) < 1:
			ametropiaoi = 0
		lentedetalladolent = request.form["lentedetalladolent"]
		if len(lentedetalladolent) < 1:
			lentedetalladolent = 15
		try:
			emetropia = request.form["emetropia"]
		except:
			emetropia = 0
		try:
			antimetropia = request.form["antimetropia"]
		except:
			antimetropia = 0
		try:
			anisometropia = request.form["anisometropia"]
		except:
			anisometropia = 0
		try:
			patologiaocular = request.form["patologiaocular"]
			patologiaoculartext = request.form["patologiaoculartext"]
		except:
			patologiaocular = 0
			patologiaoculartext = 0
		try:
			lentesoftalmicos = request.form["lentesoftalmicos"]
		except:
			lentesoftalmicos = 0
		try:
			lentescontacto = request.form["lentescontacto"]
		except:
			lentescontacto = 0
		try:
			refoftalmologica = request.form["refoftalmologica"]
		except:
			refoftalmologica = 0
		try:
			farmaco = request.form["farmaco"]
		except:
			farmaco = 0
		gmed1 = request.form["gmed1"]
		gdesc1 = request.form["gdesc1"]
		gmed2 = request.form["gmed2"]
		gdesc2 = request.form["gdesc2"]
		recreferencia = request.form["recreferencia"]
		if len(recreferencia) < 1:
			recreferencia = 0
		if len(gmed1) < 1:
			gmed1 = 0
		if len(gdesc1) < 1:
			gdesc1 = 0
		if len(gmed2) < 1:
			gmed2 = 0
		if len(gdesc2) < 1:
			gdesc2 = 0
		try:
			conexion = pymysql.connect(host='localhost', user='root', password='database', db='opticadb')
			try:
				with conexion.cursor() as cursor:
					#agudeza visual
					consulta = "insert into agudezavisual(idconsulta, idojo, avl, phae, avc) values (%s,%s,%s,%s,%s);"
					cursor.execute(consulta, (idconsulta, 1, avloi, aeoi, avcoi))
					consulta = "insert into agudezavisual(idconsulta, idojo, avl, phae, avc) values (%s,%s,%s,%s,%s);"
					cursor.execute(consulta, (idconsulta, 2, avlod, aeod, avcod))
					
					#refraccion actual
					consulta = "insert into refact(idconsulta, idojo, esfera, cilindro, eje, avcc1, prisma) values (%s,%s,%s,%s,%s,%s,%s);"
					cursor.execute(consulta, (idconsulta, 1, raeoi, racoi, raejoi, raavcc1oi, rapoi))
					consulta = "insert into refact(idconsulta, idojo, esfera, cilindro, eje, avcc1, prisma) values (%s,%s,%s,%s,%s,%s,%s);"
					cursor.execute(consulta, (idconsulta, 2, raeod, racod, raejod, raavcc1od, rapod))
					
					#Vision cercana
					consulta = "insert into ravc(idconsulta, idojo, esfera, cilindo, eje, avcc, prisma) values (%s,%s,%s,%s,%s,%s,%s);"
					cursor.execute(consulta, (idconsulta, 1, vceoi, vccoi, vcejoi, vcavccoi, vcpoi))
					consulta = "insert into ravc(idconsulta, idojo, esfera, cilindo, eje, avcc, prisma) values (%s,%s,%s,%s,%s,%s,%s);"
					cursor.execute(consulta, (idconsulta, 2, vceod, vccod, vcejod, vcavccod, vcpod))
					
					#Refraccion objetiva alumno
					consulta = "insert into refobjal(idconsulta, idojo, esfera, cilindro, eje, avcc, prisma, dvertice) values (%s,%s,%s,%s,%s,%s,%s,%s);"
					cursor.execute(consulta, (idconsulta, 1, roaeoi, roacoi, roaejoi, roaavccoi, roapoi, roavoi))
					consulta = "insert into refobjal(idconsulta, idojo, esfera, cilindro, eje, avcc, prisma, dvertice) values (%s,%s,%s,%s,%s,%s,%s,%s);"
					cursor.execute(consulta, (idconsulta, 2, roaeod, roacod, roaejod, roaavccod, roapod, roavod))
					
					#Refraccion subjetiva
					consulta = "insert into refsub(idconsulta, idojo, esfera, cilindro, eje, avcc, prisma, pruamb, testbi, equibino, pruest,ciljackson) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
					cursor.execute(consulta, (idconsulta, 1, rseoi, rscoi, rsejoi, rsavccoi, rspoi, pruamb, testbi, equibino, pruest, ciljackson))
					consulta = "insert into refsub(idconsulta, idojo, esfera, cilindro, eje, avcc, prisma, pruamb, testbi, equibino, pruest,ciljackson) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
					cursor.execute(consulta, (idconsulta, 2, rseod, rscod, rsejod, rsavccod, rspod, pruamb, testbi, equibino, pruest, ciljackson))
					
					#Refraccion final
					consulta = "insert into reffin(idconsulta, idojo, esfera1, esfera2, esfera3, cilindro1, cilindro2, cilindro3, eje1, eje2, eje3, avcc1, avcc2, avcc3, prisma1, prisma2, prisma3) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
					cursor.execute(consulta, (idconsulta, 1, rfe1oi, rfe2oi, rfe3oi, rfc1oi, rfc2oi, rfc3oi, rfej1oi, rfej2oi, rfej3oi, rfavcc1oi, rfavcc2oi, rfavcc3oi, rfp1oi, rfp2oi, rfp3oi))
					consulta = "insert into reffin(idconsulta, idojo, esfera1, esfera2, esfera3, cilindro1, cilindro2, cilindro3, eje1, eje2, eje3, avcc1, avcc2, avcc3, prisma1, prisma2, prisma3) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
					cursor.execute(consulta, (idconsulta, 2, rfe1od, rfe2od, rfe3od, rfc1od, rfc2od, rfc3od, rfej1od, rfej2od, rfej3od, rfavcc1od, rfavcc2od, rfavcc3od, rfp1od, rfp2od, rfp3od))
					
					#Motilidad Ocular
					consulta = "insert into motocu(idconsulta, idojo, mmf, forias, tropias, ducciones, versiones, convergencia, ortoforico) values (%s,%s,%s,%s,%s,%s,%s,%s,%s);"
					cursor.execute(consulta, (idconsulta, 1, mmfoi, foroi, trooi, duccoi, versiones, convergencia, ortoforico))
					consulta = "insert into motocu(idconsulta, idojo, mmf, forias, tropias, ducciones, versiones, convergencia, ortoforico) values (%s,%s,%s,%s,%s,%s,%s,%s,%s);"
					cursor.execute(consulta, (idconsulta, 2, mmfod, forod, trood, duccod, versiones, convergencia, ortoforico))
					
					#observaciones
					consulta = "insert into observaciones(idconsulta, idojo, valnormales, orbita, cejas, lagrima, viaslag, parpados, conjuntiva, esclera, cornea, camara, iris, pupila, cristalino, vitreo, nervioop, retinapp, retinape, retinamac, schirmer, but) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
					cursor.execute(consulta, (idconsulta, 1, ojsal, orboi, cejoi, lagoi, vilagoi, pypoi, conjoi, escloi, cornoi, camaoi, irioi, pupioi, crisoi, vitoi, nervooi, retppoi, retpeoi, retmacoi, schoi, butoi))
					consulta = "insert into observaciones(idconsulta, idojo, valnormales, orbita, cejas, lagrima, viaslag, parpados, conjuntiva, esclera, cornea, camara, iris, pupila, cristalino, vitreo, nervioop, retinapp, retinape, retinamac, schirmer, but) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
					cursor.execute(consulta, (idconsulta, 2, ojsal, orbod, cejod, lagod, vilagod, pypod, conjod, esclod, cornod, camaod, iriod, pupiod, crisod, vitod, nervood, retppod, retpeod, retmacod, schod, butod))

					#Lente recomendado
					consulta = "insert into lenterecomendado(idconsulta, tipo, material, filtro, color, lentedetallado) values (%s,%s,%s,%s,%s,%s);"
					cursor.execute(consulta, (idconsulta, tipolent, materiallent, filtrolent, colorlent, lentedetalladolent))

					#consulta
					consulta = "update consulta set idusolen=%s, proximacita=%s, dnp=%s,dnp1=%s, add1=%s, add2=%s, add3=%s, add11=%s, add22=%s, add33=%s, aprobado=1, iduser=%s, dnp2=%s, dnp3=%s, ojoambliopia=%s, emetropia=%s, antimetropia=%s, tipoametropia=%s, anisometropia=%s, patologiaocular=%s, lentesoftalmicos=%s, lentescontacto=%s, refoftalmologica=%s, farmaco=%s, motivoconsulta=%s, ultimaevmes=%s, ultimaevanio=%s, tiempolen=%s, tipoametropiaoi=%s, referenciaoftal=%s where idconsulta = %s;"
					cursor.execute(consulta, (usolent, proxicita, dnp, dnp1, add1, add2, add3, add11, add22, add33, session['iduser1'], dnp2, dnp3, ambliopia, emetropia, antimetropia, ametropia, anisometropia, patologiaoculartext, lentesoftalmicos, lentescontacto, refoftalmologica, farmaco, motivoconsulta, ultimaevmes, ultimaevanio, tiempolentes, ametropiaoi, recreferencia, idconsulta))

					#gotas
					consulta = "insert into recetagotero(idconsulta, medicamento1, descripcion1, medicamento2, descripcion2) values(%s,%s,%s,%s,%s)"
					cursor.execute(consulta, (idconsulta, gmed1, gdesc1,gmed2, gdesc2))
				conexion.commit()
			finally:
				conexion.close()
		except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
			print("Ocurrió un error al conectar: ", e)
		try:
			conexion = pymysql.connect(host='localhost', user='root', password='database', db='opticadb')
			try:
				with conexion.cursor() as cursor:
					consulta = "select idantecedentes from antecedentes where idpaciente = %s;"
					cursor.execute(consulta, idpaciente)
					antecedentes = cursor.fetchall()
					exicui = len(antecedentes)
					print(exicui)
					#antecedentes
					if exicui == 0:
						consulta = "insert into antecedentes(idpaciente, oftalmologicos, familiares, glaucoma, alergicas) values (%s,%s,%s,%s,%s);"
						cursor.execute(consulta, (idpaciente, antoftal, antfam, antgla, antaler))
					else:
						consulta = "update antecedentes set oftalmologicos = %s, familiares = %s, glaucoma = %s, alergicas = %s where idpaciente = %s;"
						cursor.execute(consulta, (antoftal, antfam, antgla, antaler, idpaciente))
				conexion.commit()
			finally:
				conexion.close()
		except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
			print("Ocurrió un error al conectar: ", e)
		try:
			conexion = pymysql.connect(host='localhost', user='root', password='database', db='opticadb')
			try:
				with conexion.cursor() as cursor:
					consulta = "select idantecedentes from antecedentes where idpaciente = %s;"
					cursor.execute(consulta, idpaciente)
					dataantecedentes = cursor.fetchall()
					idantecedentes = dataantecedentes[0][0]
					for i in range(numantmed):
						consulta = "insert into antmed(idantecedentes, enfermedad, tiempoevolucion, control, otro) values (%s,%s,%s,%s,%s);"
						cursor.execute(consulta, (idantecedentes, antmed[i][0], antmed[i][2],antmed[i][3],antmed[i][1]))
					for i in range(numantqui):
						consulta = "insert into antquir(idantecedentes, cirugia, tiempoevolucion, control) values (%s,%s,%s,%s);"
						cursor.execute(consulta, (idantecedentes, antqui[i][0], antqui[i][1],antqui[i][2]))
				conexion.commit()
			finally:
				conexion.close()
		except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
			print("Ocurrió un error al conectar: ", e)
		return redirect(url_for('home'))
	return render_template('ver.html', title='Historico', logeado=logeado,anios=anios, cincos=cincos, 
	meses=meses, usolen=usolen, enfermedades=enfermedades, nervos=nervos, mms=mms, numeros=numeros, 
	relva=relva, tipolen=tipolen, materiallen=materiallen, filtrolen=filtrolen, colorlen=colorlen,
	dataojo=dataojo, dataametropia=dataametropia, lentedetalladolen=lentedetalladolen, haynew=haynew, 
	ingresconsultas=ingresconsultas, conteo=conteo, listconsultas=listconsultas)

@app.route("/crearusuario", methods=['GET', 'POST'])
def crearusuario():
	try:
		logeado = session['logeado1']
	except:
		logeado = 0

	if request.method == 'POST':
		nombre = request.form["nombre"]
		apellido = request.form["apellido"]
		user = request.form["user"]
		pwd = request.form["pwd"]
		try:
			conexion = pymysql.connect(host='localhost', user='root', password='database', db='opticadb')
			try:
				with conexion.cursor() as cursor:
					consulta = "INSERT INTO user(nombre, apellido, user, pwd) values (%s, %s, %s, MD5(%s));"
					cursor.execute(consulta, (nombre, apellido, user, pwd))
				conexion.commit()
			finally:
				conexion.close()
		except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
			print("Ocurrió un error al conectar: ", e)
		return redirect(url_for('home'))
	return render_template('crearusuario.html', title='Nuevo Usuario', logeado=logeado)

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=5001, threaded=True, debug=True)