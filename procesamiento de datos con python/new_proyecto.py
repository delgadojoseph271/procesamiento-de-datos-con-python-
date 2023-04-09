from datetime import date, datetime, time, timezone
import pandas as pd
import matplotlib.pyplot as plt



def open_csv(file):
    data = pd.read_csv(file,sep=";")
    return data

c.csv"
df_mat = open_csv(csv_mat)
df_por = open_csv(csv_por)sv_mat = r"C:\Users\Administrador\Desktop\joseph tareas\sic\student_mat.csv"
csv_por = r"C:\Users\Administrador\Desktop\joseph tareas\sic\student-por
print (df_mat)
print("____________________________________________")

def csv_data(df):
    s_school = df["school"]
    s_sex = df["sex"]
    s_age = df["age"]
    s_address = df["address"]
    s_Pstatus = df["Pstatus"]
    s_guardian = df["guardian"]
    s_traveltime = df["traveltime"]
    s_studytime = df["studytime"]
    s_failures = df["failures"]
    s_paid = df["paid"]
    s_internet = df["internet"]
    s_health = df["health"]
    s_absences = df["absences"]
    s_G1 = df["G1"]
    s_G2 = df["G2"]
    s_G3 = df["G3"]

    data = {"school": s_school,
            "sex": s_sex,
            "age": s_age,
            "address": s_address,
            "Pstatus": s_Pstatus,
            "guardian": s_guardian,
            "traveltime": s_traveltime,
            "studytime": s_studytime,
            "failures": s_failures,
            "paid": s_paid,
            "internet": s_internet,
            "health": s_health,
            "absences": s_absences,
            "G1": s_G1,
            "G2": s_G2,
            "G3": s_G3,
            }
    dt = pd.DataFrame(data)
    #dt.set_index("school",inplace=True)
    dt.dropna()
    return dt

new_csv_mat = csv_data(df_mat)
new_csv_por = csv_data(df_por)
print(new_csv_mat)
print("____________________________________________")
mujeres = 0
hombres = 0
print(new_csv_mat)

df_school_GP_Mat = new_csv_mat[new_csv_mat["school"] == "GP"]
df_school_MS_mat = new_csv_mat[new_csv_mat["school"] == "MS"]
df_school_GP_Por = new_csv_por[new_csv_por["school"] == "GP"]
df_school_MS_por = new_csv_por[new_csv_por["school"] == "MS"]

school_ms =pd.concat([df_school_MS_mat, df_school_MS_por], axis=0)
school_GP =pd.concat([df_school_GP_Mat, df_school_GP_Por], axis=0)

#Para cada escuela muestre un gráfico de barras donde se muestre la cantidad de estudiantes que tienen la misma edad

def grafico_pastel(dt):
    mujeres = 0
    hombres = 0

    for i in dt["sex"].values:
        if i  == "F":
            mujeres +=1
        if i  == "M":
            hombres += 1
    """if dt["sex"] ==df_school_GP_Mat["sex"]:
        x = "Escuela GP curso Matematica "
    elif dt["sex"] ==df_school_MS_mat["sex"]:
        x = "Escuela MS curso Matematica "
    elif dt["sex"] ==df_school_GP_Por["sex"]:
        x = "Escuela GP curso Portugues "
    elif dt["sex"] ==df_school_MS_por["sex"]:
        x = "Escuela MS curso Portugues " """

    tablas_HM = ["Mujeres","Hombres"]
    porcentaje_HM = [mujeres,hombres]
    fig = plt.figure(figsize =(10, 7))
    plt.pie(porcentaje_HM, labels = tablas_HM)
    """plt.title(x)"""
    plt.show()

grafico_pastel(df_school_GP_Mat)#agregarle los titulos a las graficas
grafico_pastel(df_school_MS_mat)#
grafico_pastel(df_school_GP_Por)#
grafico_pastel(df_school_MS_por)#


"""print(df_school_GP_Mat)

print("____________________________________________")

print(df_school_MS_mat)
print("____________________________________________")

print(df_school_GP_Por)
print("____________________________________________")

print(df_school_MS_por)
print("____________________________________________")
print(school_ms)
print("____________________________________________")
print(school_GP)"""

#Para cada escuela muestre un gráfico de barras donde se muestre la cantidad de estudiantes que tienen la misma edad
def grafico_barras_edad(dt):
    cantidad = dt['age'].value_counts()
    data_frame_cantidad= pd.DataFrame(cantidad)
    edad = cantidad.index
    cantidad_y = data_frame_cantidad.iloc[:,0]

    plt.bar(edad,cantidad_y)
    plt.show()

"""grafico_barras_edad(school_ms)
grafico_barras_edad(school_GP)"""

#

#Muestre el promedio de las edades de cada curso de cada escuela
def Promedio_edad(dt):
    promedio_edad = sum(dt["age"].astype(int)) // dt["age"].size
    print("el promedio de edad es: ", promedio_edad)
Promedio_edad(df_school_GP_Mat)
Promedio_edad(df_school_MS_mat)
Promedio_edad(df_school_GP_Por)
Promedio_edad(df_school_MS_por)



#Muestre el promedio de las notas G1, G2, G3 de cada curso de cada escuela
def Promedio_notas(dt):
    promedio_notas = (dt["G1"].sum() + dt["G2"].sum() + dt["G3"].sum()) // (
                len(dt["G1"]) + len(dt["G2"]) + len(dt["G3"]))
    return promedio_notas
promedio_GP_mat =Promedio_notas(df_school_GP_Mat)
promedio_MS_mat =Promedio_notas(df_school_MS_mat)
promedio_GP_por =Promedio_notas(df_school_GP_Por)
promedio_MS_por =Promedio_notas(df_school_MS_por)
#Muestre el promedio de las notas G1, G2, G3 de cada curso de cada escuela

def Promedio_notas_escuelas(dt):
    promedio_G1 = (dt["G1"].sum()) // (len(dt["G1"]))
    promedio_G2 = (dt["G2"].sum()) // (len(dt["G2"]))
    promedio_G3 = (dt["G3"].sum()) // (len(dt["G3"]))
    print("promedio G1 es: ",promedio_G1)
    print("promedio G2 es: ",promedio_G2)
    print("promedio G3 es: ",promedio_G3)

Promedio_notas_escuelas(df_school_GP_Mat)
Promedio_notas_escuelas(df_school_MS_mat)
Promedio_notas_escuelas(df_school_GP_Por)
Promedio_notas_escuelas(df_school_MS_por)
#Grafique el promedio de las notas en un gráfico de barras horizontal
x = ["promedio_GP_mat","promedio_MS_mat","promedio_GP_por","promedio_MS_por"]
y = [promedio_GP_mat,promedio_MS_mat,promedio_GP_por,promedio_MS_por]
color =["r","r","m","m"]

plt.barh(x,y, color = color)
plt.show()

#Halle el valor máximo de las ausencias y considere dicho valor como el total de clases del curso, de manera que pueda
# sacar un porcentaje de asistencia para cada estudiante
def Valor_total_ausencias(dt):
    valor_total_ausencias = dt["absences"].max()
    print("el valor total: ",valor_total_ausencias)
    s_extras = ( valor_total_ausencias - dt["absences"])*100 //  valor_total_ausencias
    dt["extras"] = s_extras
    print("s_extras: ",s_extras)

Valor_total_ausencias(new_csv_mat)
Valor_total_ausencias(new_csv_por)

#Cree una nueva columna llamada “approved” en la cual determine si el estudiante aprueba o reprueba el curso
s_aprovados = []
def Aprobados(dt):
    for i,j in zip(dt["extras"],dt["G3"]):
        if i  >= 80 and j >= 10:
            s_aprovados.append(1)
        else:
            s_aprovados.append(0)
    print(s_aprovados)

    dt["aprovados"] = s_aprovados
    print(dt)

Aprobados(new_csv_mat)
#Aprobados(new_csv_por)

s_aprovados = []
for i,j in zip(new_csv_por["extras"],new_csv_por["G3"]):
    if i  >= 80 and j >= 10:
        s_aprovados.append(1)
    else:
        s_aprovados.append(0)
print(s_aprovados)

new_csv_por["aprovados"] = s_aprovados
print(new_csv_por)
new_csv_por.to_csv("new_csv_por_{}.csv".format(date.today()))
new_csv_mat.to_csv("new_csv_mat_{}.csv".format(date.today()))

