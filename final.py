Records = []

def load_data():
    try:
        with open('demo.txt', 'r') as f:
            for line in f:
                data = line.strip().split(',')
                thisdict = {
                    'name': data[0],
                    'age': data[1],
                    'gender': data[2],
                    'blood': data[3],
                    'disease': data[4]
                }
                Records.append(thisdict)
    except FileNotFoundError:
        pass

def save_data():
    with open('demo.txt', 'w') as f:
        for thisdict in Records:
            f.write(','.join([thisdict['name'], thisdict['age'], thisdict['gender'], thisdict['blood'], thisdict['disease']]) + "\n")

def addpatient():
    name = input("ENTER THE NAME OF PATIENT:")
    age = input("ENTER AGE :")
    gender = input("INPUT GENDER:")
    blood = input("ENTER THE BLOOD GROUP:")
    disease = input("ENTER THE NAME OF DISEASE:")

    thisdict = {
        'name': name,
        'age': age,
        'gender': gender,
        'blood': blood,
        'disease': disease
    }

    Records.append(thisdict)
    save_data()
    print("PATIENT ADDED SUCCESSFULLY")
    print("--------------------------------------------------------------------------------------")

def displaydata():
    print("WRITE THE NAME OF PATIENT WANT TO DISPLAY:")
    name = input("NAME:-")
    
    found = False
    for thisdict in Records:
        if thisdict['name'] == name:
            print('name:', thisdict['name'])
            print('age:', thisdict['age'])
            print('gender:', thisdict['gender'])
            print('blood:', thisdict['blood'])
            print('disease:', thisdict['disease'])
            print("-----------------------------------------------------------------")
            found = True
            break
    if not found:
        print("PATIENT NOT FOUND")

def updatepatient():
    print("WRITE THE NAME OF PATIENT WANT TO UPDATE:")
    name = input("NAME:-")
    
    for thisdict in Records:
        if thisdict['name'] == name:
            print("FOUND PATIENT")
            print("UPDATE THE DATA OF PATIENT")
            print("1. NAME\n2. AGE\n3. GENDER\n4. BLOOD GROUP\n5. DISEASE")
            choice = input("CHOOSE THE OPTION TO UPDATE:")

            match choice:
                case '1':
                    thisdict['name'] = input("ENTER THE NEW NAME:")
                case '2':
                    thisdict['age'] = input("ENTER THE NEW AGE:")
                case '3':
                    thisdict['gender'] = input("ENTER THE NEW GENDER:")
                case '4':
                    thisdict['blood'] = input("ENTER THE NEW BLOOD GROUP:")
                case '5':
                    thisdict['disease'] = input("ENTER THE NEW DISEASE:")
                case _:
                    print("INVALID OPTION")
                    return
            
            save_data()
            print("PATIENT UPDATED SUCCESSFULLY")
            print("--------------------------------------------------------------------------------------")
            return

    print("UNABLE TO FIND PATIENT")

def list_patients():
    print("PATIENTS COMPLETE LIST:-")
    if not Records:
        print("NO PATIENT RECORDS FOUND")
        return
    for thisdict in Records:
        print('name:', thisdict['name'])
        print('age:', thisdict['age'])
        print('gender:', thisdict['gender'])
        print('blood:', thisdict['blood'])
        print('disease:', thisdict['disease'])
        print('-----------------------------------------------------------------------')

# Load existing patient data at the start
load_data()

while True:
    print("1. ADD PATIENT   2. PATIENTS COMPLETE LIST   3. UPDATE PATIENT   4. DISPLAY PATIENT   5. EXIT")
    select = input("ENTER THE SELECTION:-")

    match select:
        case '1':
            addpatient()
        case '2':
            list_patients()
        case '3':
            updatepatient()
        case '4':
            displaydata()
        case '5':
            break
        case _:
            print("INVALID INPUT")
