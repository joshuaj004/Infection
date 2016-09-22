# This is the main file that will use the Users class
from User import User

def main():
    zero = User("Natashia Hillery")
    zero.addTrainee(User("Fannie Bezio"))
    zero.addTrainee(User("Sherise Kincannon"))
    zero.addTrainee(User("Mitsue Ballas"))
    zero.addTrainee(User("Angelena Barreto"))
    zero.addTrainee(User("Maxine Henrich"))
    zero.addTrainee(User("Coleen Okelly"))
    zero.addTrainee(User("Erick Magyar"))
    zero.addTrainee(User("Antonette Oppenheimer"))
    zero.addTrainee(User("Noelle Florey"))
    zero.addTrainee(User("Harriett Fleet"))
    zero.addTrainee(User("Nikia Adamczyk"))
    zero.addTrainee(User("Afton Morency"))
    zero.addTrainee(User("Delsie Wassink"))
    zero.addTrainee(User("Leonora Owusu"))
    zero.addTrainee(User("Hermina Warner"))
    zero.addTrainee(User("Dedra Sowder"))
    zero.addTrainee(User("Salvatore Elie"))
    zero.addTrainee(User("Marcell Przybylski"))
    zero.addTrainee(User("Scarlett Boyers"))
    zero.addTrainee(User("Shona Motley"))
    zero.addTrainee(User("Yahaira Knupp"))
    zero.addTrainee(User("Magali Caplinger"))
    zero.addTrainee(User("Leo Deluna"))
    zero.addTrainee(User("Alfred Espiritu"))
    zero.addTrainee(User("Minerva Bjerke"))
    one = User("Dorine Ouzts")
    one.addTrainee(User("Christoper Juhasz"))
    one.addTrainee(User("Rosendo Coffield"))
    one.addTrainee(User("Dwight Cantor"))
    one.addTrainee(User("Kattie Esquivel"))
    one.addTrainee(User("Stella Beauchamp"))
    one.addTrainee(User("Charley Fabrizio"))
    one.addTrainee(User("Shavonne Madia"))
    one.addTrainee(User("Dulce Maloney"))
    one.addTrainee(User("Myesha Palin"))
    one.addTrainee(User("Golden Laviolette"))
    one.addTrainee(User("Dusty Clinard"))
    one.addTrainee(User("Jacquetta Mckeighan"))
    one.addTrainee(User("Kristie Maxon"))
    one.addTrainee(User("Dollie Treadaway"))
    one.addTrainee(User("Janella Borda"))
    one.addTrainee(User("Essie Stage"))
    one.addTrainee(User("Thresa Faust"))
    one.addTrainee(User("Shenika Reuther"))
    two = User("Darin Styles")
    two.addTrainee(User("Kaitlin Brittingham"))
    two.addTrainee(User("Yanira Klug"))
    two.addTrainee(User("Alene Greig"))
    two.addTrainee(User("Carlita Bartkowiak"))
    three = User("Jerica Albe")
    three.addTrainee(User("Marguerita Paez"))
    three.addTrainee(User("Deb Wollman"))
    three.addTrainee(User("Leonel Whalley"))
    three.addTrainee(User("Saturnina Creason"))
    three.addTrainee(User("Jeanette Mccallie"))
    three.addTrainee(User("Reed Moultrie"))
    three.addTrainee(User("Lavette Moneypenny"))
    three.addTrainee(User("Dario Sandin"))
    three.addTrainee(User("Dortha Mally"))
    three.addTrainee(User("Karin Feliciano"))
    three.addTrainee(User("Dexter Risk"))
    three.addTrainee(User("Dorcas Portera"))
    three.addTrainee(User("Lilliam Giancola"))
    three.addTrainee(User("Mariela Mcquay"))
    three.addTrainee(User("Corene Hagel"))
    three.addTrainee(User("Celsa Teneyck"))
    three.addTrainee(User("Roger Narron"))
    three.addTrainee(User("Margarett Chancey"))
    three.addTrainee(User("Luciano Portalatin"))
    three.addTrainee(User("Jackelyn Hayes"))
    three.addTrainee(User("Dorine Besecker"))
    three.addTrainee(User("Jazmin Lolley"))
    three.addTrainee(User("Temika Mathews"))
    three.addTrainee(User("Margery Luth"))
    three.addTrainee(User("Latasha Bodin"))
    three.addTrainee(User("Sergio Brockett"))
    three.addTrainee(User("Alysa Quandt"))
    three.addTrainee(User("Stanton Pearse"))
    three.addTrainee(User("Roosevelt Flett"))
    three.addTrainee(User("Gwyn Drysdale"))
    three.addTrainee(User("Britany Hilario"))
    three.addTrainee(User("Eusebio Whittier"))
    three.addTrainee(User("Marguerite Veach"))
    three.addTrainee(User("Thomasina Edgley"))
    three.addTrainee(User("Dudley Rippel"))
    three.addTrainee(User("Marybeth Egan"))
    three.addTrainee(User("Carmel Hanson"))
    four = User("Pierre Pilon")
    four.addTrainee(User("Duane Mishoe"))
    four.addTrainee(User("Carmina Asher"))
    four.addTrainee(User("Mai Schilling"))
    five = User("Sharilyn Allaire")
    five.addTrainee(User("Anabel Treacy"))
    five.addTrainee(User("Lamont Denning"))
    five.addTrainee(User("Norberto Puga"))
    six = User("Sofia Allard")
    seven = User("Marge Klar")
    eight = User("Virgen Temme")
    nine = User("Herschel Allgood")
    nine.addTrainee(eight)
    users = User.getUsers()
    User.limited_infection(58, 1)
    four.fullInfection(1)
    zero.fullInfection(2)
    three.fullInfection(3)
    six.fullInfection(4)
    seven.fullInfection(5)
    eight.fullInfection(4)
    User.generateJS()

# For an ascii representation of the current state of users
def printer(users):
    for x in users:
        print(x)
    print("*"*50)

if __name__ == "__main__":
    main()