#1
def nugzar_chubinidze(sadgerdzelo, limit):
    if sadgerdzelo > limit:
        return "ლუიზა: ნუგზარი აღარ დალიო მეტი!"
    else:
        return "მოდი ახლა მართლა, დამილოცნე!"
    
    
#2
def yuri_gagarini():
    pressure = int(input("pressure: "))
    pulse = int(input("pulse: "))
    
    if pressure == 120 and pulse == 80:
        return True
    else:
        return False
    
    
#3
def caribian():
     gold_coin = int(input("How many gold coins: "))
     ship1 = 150
     ship2 = 200
     ship3 = 250
     ship4 = 300
     ship5 = 350
 
     ekipagi = [ship1, ship2, ship3, ship4,ship5]
 
     if sum(ekipagi) > gold_coin:
         return "ajanyeba"
     else:
         return "jer cocxali xar, samkmarisia oqro"


#4
apples = ["პანტა", "პანტა", "გორული"]

apples = set(apples)

print(apples)


#5
def solve(s):
    lower_count = 0
    upper_count = 0
    for char in s:
        if char.islower():
            lower_count += 1
        else:
            upper_count += 1
    if lower_count >= upper_count:
        return s.lower()
    else:
        return s.upper()
