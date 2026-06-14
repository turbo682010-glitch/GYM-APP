import time
import random
done_workouts = {}
food_protein = ["meat","beans","chicken","eggs"]
food_carbohydrates = ["rice","spaghetti","bananna"]
workout_chest = ["chest press","butterfly","bench press"]
workout_back = ["lats pulldown","t bar","pulley"]
workout_leg = ["leg extinsion","leg curles","leg press"]
days = []
carried_weight ={}
def space():
    print("********************************************")
print("              WELCOME TO LIFTERS LEGACY             ")
space()
print("               SIGN UP                              ")
while True:
 space()
 sign_up_mail = input("EMAIL: ")
 sign_up_name = input("Name: ")
 sign_up_password = input("Password: ")
 sign_up_password_check = input("confirm your password: ")
 if "@gmail.com" not in sign_up_mail or sign_up_password_check != sign_up_password:
    space()
    print("ERROR OCCURED PLEASE TRY AGAIN")
 elif len(sign_up_password) > 7:
    print("Password chacters more than 7")
 else:
    break
print("CHECK YOUR INBOX")
while True:
    time.sleep(2)
    code = random.randint(100, 200)
    print(f"VERIFCATION CODE IS:\n      --{code}--")
    code_check = input("code:")
    if int(code_check) != code:
       print("INCORRECT CODE!\nWE WILL SEND ANOTHER ONE")
       space()
    else:
       break
space()
print(f"HELLO MR {sign_up_name}\nto complete our  journey we need to take some info of you")
space()
print("First your weight in kgs")
while True:
   weight = input("Weight: ")
   if weight.isalpha():
      space()
      print("please enter digits only")
   else:
      weight = float(weight)
      break
space()
print("Secoond your height in centimeters")
while True:
   height = input("height: ")
   if height.isalpha():
      space()
      print("please enter your age by digits only")
   else:
      height = float(height)
      break
space()
print("finally your age")
while True:
   age = input("Age: ")
   if age.isalpha():
      space()
      print("pleas enter your age in DIGITS only")
   else:
      age = int(age)
      break
space()
while True:
   space()
   print("1. suggested workouts\n2. start\stop workout\n3. food\n4.profile\n5. progress\n6. Your weights\n7.workut plan\n8. exit ")
   choose = input("choose (1 to 8): ")
   if choose == "1":
      space()
      while True:
       workout_suggest = input("what muscle will u train today: ")
       if workout_suggest not in ["chest","back","leg"]:
          print("please choose weather (chest or back or leg)")
       else:
          break
      if workout_suggest  == "chest":
         if weight  in range(50, 60):
            for workout in workout_chest:
               weights = random.randint(10, 30)
               print(f"{workout}---{weights}kg")
               print("***")
         if weight in range(60,70):
               for workout in workout_chest:  
                weights = random.randint(20, 50)
                print(f"{workout}---{weights}kg")
                print("***")
         if weight in range(70, 110):
               for workout in workout_chest:
                weights = random.randint(30, 60)
                print(f"{workout}---{weights}kg")
                print("***")
         input()
      if  workout_suggest == "back":
         if weight in range(50,60):
           for workout in workout_back:
             weights = random.randint(10,20)
             print(f"{workout}---{weights}kg")
             print("***")
         if weight in range(60,70):
           for workout in workout_back:
             weights = random.randint(20,40)
             print(f"{workout}---{weights}kg")
             print("***")
         if weight in range(70,110):
           for workout in workout_back:
             weights = random.randint(30,50)
             print(f"{workout}---{weights}kg")
             print("***")
         input()
      if workout_suggest == "leg":
         if weight in range(50,60):
           for workout in workout_leg:
             weights = random.randint(20,50)
             print(f"{workout}---{weights}kg")
             print("***")
         if weight in range(60,70):
           for workout in workout_leg:
             weights = random.randint(30,60)
             print(f"{workout}---{weights}kg")
             print("***")
         if weight in range(70,110):
           for workout in workout_leg:
             weights = random.randint(30,70)
             print(f"{workout}---{weights}kg")
             print("***")
         input()
   elif choose == "2":
      while True:
         space()
         done_workout = input("enter the workout(enter q to quit loop): ")
         if done_workout is None:
            print("you need to enter a workout to start")
         if done_workout == "q":
            break
         start = input(f"press enter to start{done_workout}")       
         start_time = time.time()
         print("--TIME STARTED--")
         input(f"press enter to stop{done_workout}")
         end_time = time.time()
         total_time = end_time - start_time
         minutes = total_time / 60
         done_workouts.update({done_workout:minutes})
   elif choose == "3":
      space()
      food_choice = input("what you need now(protein or energy): ")
      if food_choice == "protein":
         for food in food_protein:
            grams = random.randint(10, 30)
            print(f"food : {food} --- {grams} gram protein")
            print("-------------------")
      if food_choice == "energy":
         for food in food_carbohydrates:
            grams = random.randint(2, 10)
            print(f"food : {food}---{grams} gram energy")
            print("-------------------")
      input()
   elif choose == "4":
      space()
      print("----------PROFILE---------")
      print(f"Name: {sign_up_name}\nHeight: {height} cm\nWeight: {weight}kg\nAge: {age}")
      input()
      print("           WORKOUTS DONE TODAY")
      for key,value in done_workouts.items():
         print(f"{key}--{value:.2f} minutes")
         print()
         input()
   elif choose == "5":
      space()
      progress_choose = input("Which progress you want to check\n1.weight\n2workouts\nchoose:")
      if progress_choose == "1":
         space()
         while True:
            previous_weight= weight
            weight = input("New weight in (kg): ")
            if weight.isdigit():
               weight = int(weight)
               if int(previous_weight) < weight:
                  state = "ganied"
                  weight_diff = weight - int(previous_weight)
               else:
                  state = "lost"
                  weight_diff = int(weight) -int(previous_weight)
               bmi_balanced = 22 * pow(height/100,2)
               bmi_lowest = 18.5 * pow(height/100,2)
               bmi_max = 25 * pow (height/100,2)
               print(f"Summary:\nprevious weight: {previous_weight}kg\nNew weight: {weight} kg\nyou {state} {weight_diff} kg")
               input()
               space()
               print(f"balanced weight is: {bmi_balanced} kg\nMaximum: {bmi_max}kg\nLowest: {bmi_lowest} kg")
               input()
               break
            else:
             print("enter digits only")
      if progress_choose == "2":
         space()
         while True:
            space()
            progress_choose1 = input("which muscle you have been improved: ")
            if progress_choose1 in ["chest","back","leg"]:
               break
            else:
               print("enter weather (chest,back,leg)")
         if progress_choose1 =="chest":
            while  True:
             space()
             print("1. chest press\n2. bench press\n3. butter fly")
             choose_progress = input("choose form(1-3): ")
             if choose_progress in ["1","2","3"]:
                break
             else:
                print("enter 1,2,3")
            if choose_progress == "1":
               if  "chest press" in carried_weight.keys():
                  while True:
                   chest_press_new = input("chest press: ")
                   if chest_press_new.isdigit():
                     space()
                     print(f"your previous record was {carried_weight.get("chest press")} kg")
                     print(f"while now you carried {chest_press_new} kg")
                     input()
                     progress_chest_press = int(chest_press_new)  - carried_weight.get("chest press")
                     progress_chest_press_precentage = (int(progress_chest_press) / carried_weight.get("chest press")) * 100 
                     space()                     
                     print(f"PROGRESS:\nBeter with {progress_chest_press} kg\nWith precentage of {progress_chest_press_precentage:.2f} %")
                     input()
                     carried_weight.pop("chest press")
                     carried_weight.update({"chest press":int(chest_press_new)})
                     break
                   else:
                     print("enter digits only")
               else:
                  print("YOU HAVE NOT ENTERED YOUR WEIGHTS!")
            if choose_progress == "3":
               if "butter fly" in carried_weight.keys():
                while True:
                     butterfly_new = input("Butter fly: ")
                     if butterfly_new.isdigit():
                        space()
                        print(f"your previous record was {carried_weight.get("butter fly")} kg")
                        print(f"while now you carried {butterfly_new} kg")
                        input()
                        progress_butterfly = int(butterfly_new)  - carried_weight.get("butter fly")
                        progress_butterfly_precentage = (int(progress_butterfly) / carried_weight.get("butter fly")) * 100 
                        space()                     
                        print(f"PROGRESS:\nBeter with {progress_butterfly} kg\nWith precentage of {progress_butterfly_precentage::.2f} %")
                        input()
                        carried_weight.pop("butter fly")
                        carried_weight.update({"butter fly":int(butterfly_new)})
                        break
                     else:
                        print("enter digits only")
               else:
                  print("YOU HAVE NOT ENTERED YOUR WEIGHTS!")
            if choose_progress == "2":
               if "bench press" in carried_weight.keys():

                while True:
                     bench_press_new = input("Bench press: ")
                     if bench_press_new.isdigit():
                        space()
                        print(f"your previous record was {carried_weight.get("bench press")} kg")
                        print(f"while now you carried {bench_press_new} kg")
                        input()
                        progress_bench_press = int(bench_press_new)  - carried_weight.get("bench press")
                        progress_bench_press_precentage = (int(progress_bench_press) / carried_weight.get("bench press")) * 100 
                        space()                     
                        print(f"PROGRESS:\nBeter with {progress_bench_press} kg\nWith precentage of {progress_bench_press_precentage:.2f} %")
                        input()
                        carried_weight.pop("bench  press")
                        carried_weight.update({"bench press":int(bench_press_new)})
                        break
                     else:
                        print("enter digits only")
               else:
                  print("YOU HAVE NOT ENTERED YOUR WEIGHTS!")
         if progress_choose1 =="back":
            while  True:
              space()
              print("1. lats pulldown\n2. T BAR\n3. Pulley")
              choose_progress2 = input("choose form(1-3): ")
              if choose_progress2 in ["1","2","3"]:
                break
              else:
                print("enter 1,2,3")
            if choose_progress2 == "1":
               space()
               if "lats pulldown" in carried_weight.keys():
                 while True:
                    lats_pulldown_new = input("Lats pulldown: ")
                    if lats_pulldown_new.isdigit():
                        space()
                        print(f"your previous record was {carried_weight.get("lats pulldown")} kg")
                        print(f"while now you carried {lats_pulldown_new} kg")
                        input()
                        progress_lats_pulldown = int(lats_pulldown_new)  - carried_weight.get("lats pulldown")
                        progress_lats_pulldown_precentage = (int(progress_lats_pulldown) / carried_weight.get("lats pulldown")) * 100 
                        space()                     
                        print(f"PROGRESS:\nBeter with {progress_lats_pulldown} kg\nWith precentage of {progress_lats_pulldown_precentage:.2f} %")
                        input()
                        carried_weight.pop("lats pulldown")
                        carried_weight.update({"lats pulldown":int(lats_pulldown_new)})
                        break  
                    else:
                     print("enter digits only")
               else:
                print("YOU HAVE NOT ENTERED YOUR WEIGHTS BEFORE!!")
            if choose_progress2 =="2":
               space()
               if  "T bar" in carried_weight.keys():
                  while True:
                     t_bar_new = input("T BAR: ")
                     if t_bar_new.isdigit():
                        space()
                        print(f"your previous record was {carried_weight.get("T bar")} kg")
                        print(f"while now you carried {t_bar_new} kg")
                        input()
                        progress_t_bar = int(t_bar_new)  - carried_weight.get("T bar")
                        progress_t_bar_precentage = (int(progress_t_bar) / carried_weight.get("T bar")) * 100 
                        space()                     
                        print(f"PROGRESS:\nBetter with {progress_t_bar} kg\nWith precentage of {progress_t_bar_precentage:.2f} %")
                        input()
                        carried_weight.pop("T bar")
                        carried_weight.update({"T bar":int(t_bar_new)})
                        break
                     else:
                       print("Enter digits only")
               else:
                  print("YOU HAVE NOT ENTERED YOUR WEWIGHTS BEFORE")
            if choose_progress2 =="3":
                space()
                if  "pulley" in carried_weight.keys():
                    while True:
                      pulley_new = input("PULLEY: ")
                      if pulley_new.isdigit():
                        space()
                        print(f"your previous record was {carried_weight.get("pulley")} kg")
                        print(f"while now you carried {pulley_new} kg")
                        input()
                        progress_pulley = int(pulley_new)  - carried_weight.get("pulley")
                        progress_pulley_precentage = (int(progress_pulley) / carried_weight.get("pulley")) * 100 
                        space()                     
                        print(f"PROGRESS:\nBetter with {progress_pulley} kg\nWith precentage of {progress_pulley_precentage:.2f} %")
                        input()
                        carried_weight.pop("pulley")
                        carried_weight.update({"pulley":int(pulley_new)})
                        break
                      else:
                       print("Enter digits only")
            else:
               print("YOU HAVE NOT ENTERED YOUR WEWIGHTS BEFORE")
         if progress_choose1 =="leg":
            while  True:
              space()
              print("1. leg extension\n2. leg curles\n3. leg press")
              choose_progress2 = input("choose form(1-3): ")
              if choose_progress2 in ["1","2","3"]:
                break
              else:
                print("enter 1,2,3")
            if choose_progress2 == "1":
               space()
               if "leg extension" in carried_weight.keys():
                 while True:
                    leg_extension_new = input("Leg extension: ")
                    if leg_extension_new.isdigit():
                        space()
                        print(f"your previous record was {carried_weight.get("leg extension")} kg")
                        print(f"while now you carried {leg_extension_new} kg")
                        input()
                        progress_leg_extension = int(leg_extension_new)  - carried_weight.get("leg extension")
                        progress_leg_extension_precentage = (int(progress_leg_extension) / carried_weight.get("leg extension")) * 100 
                        space()                     
                        print(f"PROGRESS:\nBeter with {progress_leg_extension} kg\nWith precentage of {progress_leg_extension_precentage:.2f} %")
                        input()
                        carried_weight.pop("leg extension")
                        carried_weight.update({"leg extension":int(leg_extension_new)})
                        break  
                    else:
                     print("enter digits only")
               else:
                print("YOU HAVE NOT ENTERED YOUR WEIGHTS BEFORE!!")
            if choose_progress2 =="2":
               space()
               if  "leg curles" in carried_weight.keys():
                  while True:
                     leg_curles_new = input("Leg curles: ")
                     if leg_curles_new.isdigit():
                        space()
                        print(f"your previous record was {carried_weight.get("leg curles")} kg")
                        print(f"while now you carried {leg_curles_new} kg")
                        input()
                        progress_leg_curles = int(leg_curles_new)  - carried_weight.get("leg curles")
                        progress_leg_curles_precentage = (int(progress_leg_curles) / carried_weight.get("leg curles")) * 100 
                        space()                     
                        print(f"PROGRESS:\nBetter with {progress_leg_curles} kg\nWith precentage of {progress_leg_curles_precentage:.2f} %")
                        input()
                        carried_weight.pop("leg curles")
                        carried_weight.update({"T bar":int(leg_curles_new)})
                        break
                     else:
                       print("Enter digits only")
               else:
                  print("YOU HAVE NOT ENTERED YOUR WEWIGHTS BEFORE")
            if choose_progress2 =="3":
                space()
                if  "leg press" in carried_weight.keys():
                    while True:
                      leg_press_new = input("Leg press: ")
                      if leg_press_new.isdigit():
                        space()
                        print(f"your previous record was {carried_weight.get("leg press")} kg")
                        print(f"while now you carried {leg_press_new} kg")
                        input()
                        progress_leg_press = int(leg_press_new)  - carried_weight.get("leg press")
                        progress_leg_press_precentage = (int(progress_leg_press) / carried_weight.get("leg press")) * 100 
                        space()                     
                        print(f"PROGRESS:\nBetter with {progress_leg_press} kg\nWith precentage of {progress_leg_press_precentage:.2f} %")
                        input()
                        carried_weight.pop("leg press")
                        carried_weight.update({"leg press":int(leg_press_new)})
                        break
                      else:
                       print("Enter digits only")
            else:
               print("YOU HAVE NOT ENTERED YOUR WEWIGHTS BEFORE")      
   elif choose == "6":
      space()
      while True:
       choose_6 = input("Which muscle you want to enter: ")
       if choose_6 in  ["chest","back","leg"]:
          break
       else:
          print("please choose weather(chest,back,leg)")
      if choose_6 == "chest":
         while True:
            space()
            chest_press = input("Chest press in kgs: ")
            if chest_press.isdigit():
               chest_press = int(chest_press)
               carried_weight.update({"chest press":chest_press})
               break
            else:
               print("enter it on digits")
         while True:
            space()
            butterfly = input("butterfly weight in kgs: ")
            if butterfly.isdigit():
               butterfly = int(butterfly)
               carried_weight.update({"butter fly":butterfly})
               break
            else:
               print("enter kgs in digits only!")
         while True:
            space()
            bench_press = input("Weight (bench press): ")
            if bench_press.isdigit():
               bench_press = int(bench_press)
               carried_weight.update({"bench press":bench_press})
               break
            else:
               print("enter digits only!")
         input()
      if choose_6 == "back":
         space()
         while True:
            space()
            lats_pulldown = input("weight (lats pulldown) in kg: ")
            if lats_pulldown.isdigit():
               carried_weight.update({"lats pulldown":int(lats_pulldown)})
               break
            else:
               print("enter digits only")
         while True:
            space()
            t_bar = input("weight (T BAR) in kg: ")
            if t_bar.isdigit():
               carried_weight.update({"T bar":int(t_bar)})
               break
            else:
               print("enter digits only")
         while True:
            space()
            pulley = input("weight (pulley)in kg: ")
            if pulley.isdigit():
               carried_weight.update({"pulley":int(pulley)})
               break
            else:
               print("enter digits only")
      if choose_6 == "leg":
         while True:
            space()
            leg_extenision = input("weight (leg extenision) in kg")
            if leg_extenision.isdigit():
               carried_weight.update({"leg extension": int(leg_extenision)})
               break
            else:
               print("enter digits only!")
         while True:
            space()
            leg_curles = input("weight (leg curle) in kg: ")
            if leg_curles.isdigit():
               carried_weight.update({"leg curles":int(leg_curles)})
               break
            else:
               print("enter digits only!")
         while True:
            space()
            leg_press = input("weight (leg press) in kg: ")
            if leg_press.isdigit():
               carried_weight.update({"leg press":int(leg_press)})
               break
            else:
               print("enter digits only")
   elif choose == "7":
      print("please add your aviable days in week")
      while True:
         space()
         day = input("Day (q to exit): ")
         if day in ["saturday","sunday","monday","tuesday","wednesday","thursday","friday"]:
           if day in days:
            print(f"there was a duplicated day ({day})")
            input()
           else:
            days.append(day)
         elif day == "q":
            if len(days) < 3 or len(days) > 6:
               print("please enter atleast 3 days and macimum 5 days")
               input()
            else:
             break
         else:
          print("please enter a vailed day!!")
      if len(days) == 3:
         print(f"{days[0]}---push\n{days[1]}---pull\n{days[2]}---leg")
         input()
         print("Push:\n1.chest press---upper chest\n2.bench press---upper  chest\n3.butter fly--- mid chest\n4.triceps pull---triceps")
         input()
         space()
         print("Pull\n1. lats pulldown---lats\n2.pulley---lower lats\n3.bicep curl---bicep\n4.tbar---back")
         input()
         space()
         print("Leg\n1.leg extension---upper leg\n2.leg curles---back leg\n3.leg press---whole leg")
         input()
      if len(days) == 4:
         print(f"{days[0]}---chest&triceps\n{days[1]}---back&biceps\n{days[2]}---wrist& arm\n{days[3]}---leg")
         print("chest&triceps:\n1.chest press---upper chest\n2. high bench press--uper chest\n3. flat bench press---middle chest\n4. triceps pulldown---triceps")
         input()
         space()
         print("Back&biceps:\n1. lats pulldown--upper lats\n2. tbar---middle lats\n3. pulley---mioddle lats\n4.hammer---biceps")
         input()
         space()
         print("Wrist&arm:\n1. hammer---biceps\n2. bicpes caple---midlle biceps\n3. wrist bar--- wrist ")
         input()
         space()
         print("Leg\n1.leg extension---upper leg\n2.leg curles---back leg\n3.leg press---whole leg")
         input()
      if len(days) == 5:
         print(f"{days[0]}---chest\n{days[1]}---back\n{days[2]}---wrist\n{days[3]}---biceps and triceps\n{days[4]}---leg")
         input()
         print("chest:\n1.chest press---upper chest\n2. high bench press--uper chest\n3. flat bench press---middle chest")
         input()
         space()
         print("Back:\n1. lats pulldown--upper lats\n2. tbar---middle lats\n3. pulley---mioddle lats")
         input()
         space()
         print("Wrist:\n1. wrist bar---wrist\n2. wrist bar seated---wrist\n3. wrist bar reversed--- wrist  ")
         input()
         space()
         print("Biceps& triceps:\n1. hammer---middle biceps\n2. dumbel curl---whole bicpes\n3. caple curl---whole biceps")
         input()
         space()
         print("Leg\n1.leg extension---upper leg\n2.leg curles---back leg\n3.leg press---whole leg")
         input()
   elif choose == "8":
      space()
      print("EXITING....")
      time.sleep(2)
      exit("EXITED!")
   else:
      print("please choose categorie (1-7)!")            

            

         
         
