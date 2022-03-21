# List  is  collection waana  ordered ,changeable,duplicate
# wxaaad ku dari karta data type ku dari kartaa

             # Example

# fruit = ["mango","apple","Grape"]
# print(fruit)
#
# # list have index
# print(fruit[2])

# slicing = jarjarid ama qaayb ka qadasho

# fruit = ["mango","apple","Grape","grio",]
# print(fruit[-1])    # uising slicing oo markad doonayso kan ugu danbeya
#                      # inaad qadatyo ayaa isticmalysan is negative index

# fruit = ["mango","apple","Grape","grio",]   # kan ugu danbeya raba inaan
# print(fruit[:-1])                           # ka reebo using slicing

  # range
# fruit = ["mango","apple","Grape","grio",]  # kan ugu horeya kaliya ka reeb
# print(fruit[1:])

# fruit = ["mango","apple","Grape","grio",]  # dhamaan soo sar
# print(fruit[0:])

# fruit = ["mango","apple","Grape","grio", "kaluun","bariis","sonkor"]
# print(fruit[3:])      # sadexad ka bulaw soona saar

# fruit = ["mango","apple","Grape","grio", "kaluun","bariis","sonkor"]
# print(fruit[3:8])  # this calle excluded  intaa ilaa inta ii adabac

#  # negative with slicing
# fruit = ["mango","apple","Grape","grio", "kaluun","bariis","sonkor"]
# print(fruit[-5:-1])

     #   change list atimes

# fruit = ["mango","apple","Grape","grio", "kaluun","bariis","sonkor"]
# fruit[1] ="bedel"
# print(fruit)

# list looop

# fruit = ["mango","apple","Grape","grio", "kaluun","bariis","sonkor"]
#
# for x in fruit:
#     print(x)

# enumrate  xaraf kasta index ayaa soo saraya

# fruit = ["mango","apple","Grape","grio", "kaluun","bariis","sonkor"]
#
# for index,x in enumerate(fruit):   # xaraf  kasta index soo sara
#     print(index,x)

# check items exists

# fruit = ["mango","apple","Grape","grio", "kaluun","bariis","sonkor"]
#
# if "Banaana" in fruit:
#     print("yes Banana in list")
# else:
#     print('not belong banan in list')

# # lenght  inta dheere yaya
#
# fruit = ["mango","apple","Grape","grio", "kaluun","bariis","sonkor"]
# print(len(fruit))

# List  Add

# Append  ku dar

# fruit = ["mango","apple","Grape","grio", "kaluun","bariis","sonkor"]
# fruit.append("laws")
# print(fruit)

# insert  font Add to you need index and thing aad

# fruit = ["mango","apple","Grape","grio", "kaluun","bariis","sonkor"]
# fruit.insert(0,"fontadd")
# print(fruit)


# Extend   Add to list  isku dar laba array  Extend use

# fruit = ["mango","apple","Grape","grio", "kaluun","bariis","sonkor"]
# fruit2 = ["sharab","saytuun","mushakal"]
# fruit.extend(fruit2)
# print(fruit)


# Removing list

# fruit = ["mango","apple","Grape","grio", "kaluun","bariis","sonkor"]
# fruit.remove("grio")   # kad ka saraysay
# print(fruit)

# Another way to removing

# fruit = ["mango","apple","Grape","grio", "kaluun","bariis","sonkor"]
# fruit.pop()  # this called building fuction , kan ugu danbeya ka saray
# print(fruit)  # removing least

# marka oganyso kii laga bixiyey

# fruit = ["mango","apple","Grape","grio", "kaluun","bariis","sonkor"]
# removedItem =fruit.pop()
# print(removedItem)     # kii laga saaray ku sheegay


# revers  loo rogo ama laka bedelo
#
# fruit = ["mango","apple","Grape","grio", "kaluun","bariis","sonkor"]
# fruit.reverse()    # is a building objcet
# print(fruit)  # la kala wareejiyo

# Sort        wuxu samaynaya alphabetic ukal horaysinaya listiga

# fruit = ["mango","apple","Grape","grio", "kaluun","bariis","sonkor"]
# fruit.sort()
# print(fruit)

 # reverse and Sort

# fruit = ["mango","apple","Grape","grio", "kaluun","bariis","sonkor"]
# fruit.sort(reverse=True)
# print(fruit)   # wuna kal wareejiyey wuuna kala hormariyey APhabetic
#
#
# nomber = [1,2,3,4,5,6]
# nomber.sort(reverse=True)
# # print(lnabra)
#
# sortedNumber = sorted(nomber)
# print(sortedNumber)
# print(nomber)

# max , min , sum

# nomber = [1,2,3,4,5,6]
# print(max(nomber))  # ugu weyn

#  # sum
# nomber = [1,2,3,4,5,6]
# print(sum(nomber))  # isku geeyntooda


# make list a String   string ka dhig list

# fruit = ["mango","apple","Grape","grio", "kaluun","bariis","sonkor"]
# 
# fruit_str = " , ".join(fruit)
# print(type(fruit_str))  # this is string

# # Split   Dib u soo celi
#
# fruit_list = fruit_str.split(" , ")
# print(fruit_list)   # dib list ugu celi
