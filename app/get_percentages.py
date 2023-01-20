
# %%
import read_csv 

date = read_csv.read("date.csv")

#  esta funcion obtiene los paises y los porcentajes
def get_percentages(date):
    # obtenemos solo los continentes de la data 
    continent = [item["Continent"] for item in date]
    # nesesitamos un set para eliminar elementos repetidos 
    continent = set(continent)
    # preguntamos al usuario mostrando una lista de opciones 
    quest = input(" choose a Continent \n " + str(continent))

    # retornamos los  solo si son iguales a los datos de la variable quest 
    date = [item for item in date if item["Continent"] == quest]
    


    # este dictsconprenhension  obtine en key , paises y en valor los porcentajes de los datos  
    select = {item["Country/Territory"]:item["World Population Percentage"]  for item in date}
    # almacenamos las llaves del dictconprenhension  
    world =select.keys()
    # almacenamos los valores del dicsconprenhension
    percentages = select.values()
    # retornamos las variables  
    return world,percentages




if __name__== "__main__":
    get_percentages(date)
    