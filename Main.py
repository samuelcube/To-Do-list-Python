import json

try:
    with open("todos.json", 'r') as file:
        todos = json.load(file)
except:
   todos = []

while True:
    print(" ===To Do menu===")
    print("1 - Todo Hinzufügen")
    print("2 - Todo Löschen")
    print("3 - Todo Anzeigen")
    print("4 - Beenden")
    
    choise = input("Wähle eine Option: ")
    
    if choise == "1":
        todo = input("Neue Todo: ")
        todos.append(todo)
        
      
        with open("todos.json", 'r') as file:
            json.dump(todos, file)
        
        print("Hinzugefügt und gespeichert")
        
    elif choise == "2":
        if len(todos) == 0:
            print("Keine Todos Vorhanden")
        else:
            print("Deine Todos")
            for i in range(len(todos)):
                print(i + 1, todos[i])
            
            try:   
             nummer = int(input("Welche nummer Willst du löschen: ")) -1
             if 0 <= nummer < len(todos):
                entfernt =  todos.pop(nummer)
                
                with open("todos.json", "w") as file:
                    json.dump(todos, file)
                    print('Gelöscht', entfernt)
             else:
                 print("Üngültige Zahl")
            except:
                print("Bitte eine zahl eingeben")
    elif choise == "3":
        print(" Deine Todos")
        for i in range(len(todos)):
                print(i + 1, todos[i])
        
    elif choise == "4":
        print("Pogramm Beendet")
        break
    else:
        print("Üngüldige eingabe")