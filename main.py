def pichachu():
  pichachu.HP = 1000
  Attack = 90
  sp_attack = 1000
  defense = 1000
  print("pichachu")
def polyworl():
  polyworl.HP = 50
  Attack = 50
  sp_attack = 50
  defense = 50
  print("polyworl")
def Mimikyu():
  Mimikyu.HP = 500
  Attack = 40
  sp_attack = 500
  defense = 500
  print("Mimikyu")
def fight(A):
  pichachu()
  polyworl()
  Mimikyu()
  if A == "1":
    fight = input("Press 1 to Use Fire Attack \nPress 2 for Special Attack\nPress 3 to Spawn a Wither at the other person's base")
    if fight == "1":
      polyworl.HP -10
      Mimikyu.HP -1
      print(polyworl.HP-10,Mimikyu.HP-1)
    elif fight == "2":
      polyworl.HP -1000
      Mimikyu.HP -500  
      print(polyworl.HP-1000,Mimikyu.HP-100000000000000)
    elif fight == "3":
      polyworl.HP -16476298576852976345764357826349587634676426438923746528973465732587256576578485710398572
      Mimikyu.HP -16476298576852976345764357826349587634676426438923746528973465732587256576578485710398572
      print(polyworl.HP,Mimikyu.HP)
    else:
      print("01000111 01001111 00100000 01010010 01001001 01000111 01001000 01010100 00100000 01001110 01000101 01011000 01010100 00100000 01010100 01001001 01001101 01000101 00100000 01000010 01001111 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001")
  elif A == "2":
    
    fight = input("Press 1 to Use Bow Attack \nPress 2 for Special Attack\nPress 3 to Spawn a Killer Rabbit at the other person's base")
    if fight == "1":
      pichachu.HP -0
      Mimikyu.HP -0
      print(pichachu.HP,Mimikyu.HP)
    elif fight == "2":
      pichachu.HP -1
      Mimikyu.HP -1
      print(pichachu.HP,Mimikyu.HP)
    elif fight == "3":
      pichachu.HP -2
      Mimikyu.HP -2
      print(pichachu.HP,Mimikyu.HP)
    else:
      print("01000111 01001111 00100000 01010010 01001001 01000111 01001000 01010100 00100000 01001110 01000101 01011000 01010100 00100000 01010100 01001001 01001101 01000101 00100000 01000010 01001111 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001")
  elif A == "3":
    fight = input("Press 1 to Use Poison Attack \nPress 2 for Special Attack\nPress 3 to Spawn a Wither Skeleton at the other person's base")
    if fight == "1":
      pichachu.HP -3
      polyworl.HP -3
      print(pichachu.HP,polyworl.HP)
    elif fight =="2":
      pichachu.HP -2
      polyworl.HP -1000673648726345876345
      print(pichachu.HP,polyworl.HP)
    elif fight == "3":
      pichachu.HP -1
      polyworl.HP -4768732649736494387256948765
      print(pichachu.HP,polyworl.HP)
    else:
      print("01000111 01001111 00100000 01010010 01001001 01000111 01001000 01010100 00100000 01001110 01000101 01011000 01010100 00100000 01010100 01001001 01001101 01000101 00100000 01000010 01001111 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001")
  else:
    print("01000111 01001111 00100000 01010010 01001001 01000111 01001000 01010100 00100000 01001110 01000101 01011000 01010100 00100000 01010100 01001001 01001101 01000101 00100000 01000010 01001111 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001")
def bag(A):
  if A == "1":
    bag = input("Press 1 for Apple Pie \nPress 2 for Level 1000 healing potion \nPress 3 for XP BOOST LVL 1000000")
    if bag == "1":
      pichachu.HP +20
    elif bag == "2":
      pichachu.HP +1000
    elif bag == "3":
      pichachu.HP +1000000
    else:
      print("YEETUS MY FEETUS GO COMMIT SELF DELETEUS")
  elif A == "2":
    bag = input("Press 1 for Apple Pie\nPress 2 for HEALING POTION LVL 1000\nPress 3 for XP LVL1000000")
    if bag == "1":
      polyworl.HP +20
    elif bag == "2":
      polyworl.HP +1000
    elif bag == "3":
      polyworl.HP +1000000
    else:
      print("YEETUS MY FEETUS GO COMMIT SELF DELETEUS")
  elif A == "3":
    bag = input("Press 1 for Apple Pie\nPress 2 for HEALING POTION LVL 1000\nPress 3 for XP LVL1000000")
    if bag == "1":
      Mimikyu.HP +20
    elif bag == "2":
      Mimikyu.HP +1000
    elif bag == "3":
      Mimikyu.HP +1000000
    else:
      print("YEETUS MY FEETUS GO COMMIT SELF DELETEUS")
  else:
    print("BUN DUN DUN DUN DUN DUN DUN DUN DUN DUN DUN DUN DUN DUN DUN")
redo = "y"
while redo == "y":
  trainer = input("Press 1 for Ash503 \nPress 2 for Scottie \nPress 3 for Bettie")
  if trainer == "1":
    pichachu()
  elif trainer == "2":
    polyworl()
  elif trainer == "3":
    Mimikyu()
  else:
    print("01000111 01001111 00100000 01010010 01001001 01000111 01001000 01010100 00100000 01001110 01000101 01011000 01010100 00100000 01010100 01001001 01001101 01000101 00100000 01000010 01001111 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001 01001001")
  action = input ("Press 1 for FIGHT \nPress 2 for bag \nPress 3 for RUN")
  if action == "1":
    fight(trainer)
  elif action == "2":
    bag(trainer)
  elif action == "3":
    print("Gotta go fast, gotta go fast Gotta go faster, faster, faster, faster, faster!")
  else:
    print("YEETUS MY FEETUS GO COMMIT SELF DELETEUS")
  redo = input("DO U WANT TO PLAY AGAIN y OR n")
