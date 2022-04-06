def get_field(filename = 'field.csv', delimiter = ';'):
    try:
        with open(filename, "r") as field:
            field_list =[]
            while True:
                line = field.readline()
                
                if not line:
                    break
                field_list.append([int(item) for item in line.split(delimiter)])
   
            return field_list
    except FileNotFoundError:
        print("File doesn't exists")
        return [[]]
    except ValueError:
        print('Wrong data in file')
        return [[]]
