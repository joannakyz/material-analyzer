#Project Python 
#libraries included
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import fitz
import os #I want to know in which dir the project is, to change it later, so I can open files.

print("Current working directory:", os.getcwd()) #Prints the current dir
os.chdir("D:\Python\Project_Python_Kyzeridou")  #Replacing the dir you want
print("New working directory:", os.getcwd())  # Confirming the change to user

#Defining units
cm = "cm" 
b = "\u00b3" #x^3
omega = "\u03A9m"
minus_one_superscript = "\u207B\u00B9" #e.g. 10^-1

#Define classes
class Materials:
    def __init__(self, name, chem_name, type, comp_type, density, crystal_structure):
        self.name = name
        self.chem_name = chem_name
        self.type = type #defines if a material is a chemical element or a chemical compound or an alloy
        self.comp_type = comp_type #defines if a material is a metal, polymer, ceramic or composite
        self.density = density
        self.crystal_structure = crystal_structure

    def get_name(self):
        return f"Material Name: {self.name}"
    def get_chem_name(self):
        return f"Material Symbol: {self.chem_name}"
    def get_type(self):
        return f"Material Type: {self.type}"
    def get_comp_type(self):
        return f"Composition Type: {self.comp_type}"
    def get_density(self):
        return f"Material Density: {self.density} g/{cm}{b}"
    def get_crystal_structure(self):
        return f"Crystal Structure: {self.crystal_structure}"
    
    def display_all_materials(self):
        print(f"Material Name: ", self.name)
        print(f"Material Symbol: ", self.chem_name)
        print(f"Material Type: ", self.type)
        print(f"Composition type: ", self.comp_type)
        print(f"Material Density: {self.density} g/{cm}{b}")
        print(f"Crystal Structure: ", self.crystal_structure)

class Mechanical_Properties(Materials):
    def __init__(self, name, chem_name, type, comp_type, density, crystal_structure, young_modulus, poisson_ratio, yield_strength, tensile_strength):
        super().__init__(name, chem_name, type, comp_type, density, crystal_structure)
        self.young_modulus = young_modulus
        self.poisson_ratio = poisson_ratio
        self.yield_strength = yield_strength
        self.tensile_strength = tensile_strength  

    def get_young_modulus(self):
        return f"Young's Modulus: {self.young_modulus} GPa"
    def get_poisson_ratio(self):
        return f"Poisson's ratio: {self.poisson_ratio} (dimensionless)"
    def get_yield_strength(self):
        return f"Yield strength: {self.yield_strength} MPa"
    def get_tensile_strength(self):
        return f"Tensile strength: {self.tensile_strength} MPa"
    
    def display_all_mech_prop(self):
        print(f"Young Modulus: ", self.young_modulus, " GPa")
        print(f"Poisson's Ratio: ", self.poisson_ratio)
        print(f"Yield Strength: ", self.yield_strength, " MPa")
        print(f"Tensile Strength: ", self.tensile_strength, "MPa")

class Electrical_Properties(Materials):
    def __init__(self, name, chem_name, type, comp_type, density, crystal_structure, el_conductivity, permittivity, dielectric_const, electrical_resistivity):
        super().__init__(name, chem_name, type, comp_type, density, crystal_structure)
        self.el_conductivity = el_conductivity #S/m
        self.permittivity = permittivity
        self.dielectric_const = dielectric_const
        self.electrical_resistivity = electrical_resistivity

    def get_el_conductivity(self):
        return f"Electrical conductivity: {self.el_conductivity} S/m"
    def get_permittivity(self):
        return f"Permittivity: {self.permittivity} F/m"
    def get_dielectric_const(self):
        return f"Dielectric constant: {self.dielectric_const}"
    def get_electrical_resistivity(self):
        return f"Electrical Resistivity: {self.electrical_resistivity} m"
    
    def display_all_el_prop(self):
        print(f"Electrical Conductivity: ", self.el_conductivity, " S/m")
        print(f"Permittivity: ", self.permittivity, " F/m")
        print(f"Dielectric Constant: ", self.dielectric_const)
        print(f"Electrical Resistivity: ", self.electrical_resistivity, omega + "m")

class Thermal_Properties(Materials):
    def __init__(self, name, chem_name, type, comp_type, density, crystal_structure, th_conductivity, coefficient_expansion, specific_heat):
        super().__init__(name, chem_name, type, comp_type, density, crystal_structure)
        self.th_conductivity = th_conductivity
        self.coefficient_expansion = coefficient_expansion
        self.specific_heat = specific_heat

    def get_th_conductivity(self):
        return f"Thermal conductivity: {self.th_conductivity} W/mK"
    def get_coefficient_expansion(self):
        return f"Coefficient of expansion: {self.coefficient_expansion} K{minus_one_superscript}"
    def get_specific_heat(self):
        return f"Specific Heat: {self.specific_heat} J/kgK"
    
    def display_all_therm_prop(self):
        print(f"Thermal Conductivity: ", self.th_conductivity, " W/mK")
        print(f"Coefficient of expansion: ", self.coefficient_expansion, "K" + minus_one_superscript)
        print(f"Specific Heat: ", self.specific_heat, "J/kgK")

class Chemical_Properties(Materials):
    def __init__(self, name, chem_name, type, comp_type, density, crystal_structure, pH): #ssa = specific surface area
        super().__init__(name, chem_name, type, comp_type, density, crystal_structure)
        self.pH = pH

    def get_pH(self):
        return f"pH: {self.pH}"
    
    def display_all_chem_prop(self):
        print(f"pH: ", self.pH)
    
class Optical_Properties(Materials):
    def __init__(self, name, chem_name, type, comp_type, density, crystal_structure, color):
        super().__init__(name, chem_name, type, comp_type, density, crystal_structure)
        self.color = color

    def get_color(self):
        return f"Color: {self.color}"
    
    def display_all_opt_prop(self):
        print(f"Color: ", self.color)

class Atomic_Properties(Materials):
    def __init__(self, name, chem_name, type, comp_type, density, crystal_structure, atomic_weight, atomic_number, ionic_radius, atomic_radius):
        super().__init__(name, chem_name, type, comp_type, density, crystal_structure)
        if type == "element" or "Element":
            self.atomic_weight = atomic_weight
            self.atomic_number = atomic_number
            self.ionic_radius = ionic_radius
            self.atomic_radius = atomic_radius
        else:
            print(name, "is not a chemical element. Cannot be assigned with chemical properties.")

    def get_atomic_weight(self):
        return f"Atomic weight: {self.atomic_weight} u"
    def get_atomic_number(self):
        return f"Atomic number: {self.atomic_number}"
    def get_ionic_radius(self):
        return f"Ionic radius: {self.ionic_radius} pm"
    def get_atomic_radius(self):
        return f"Atomic radius {self.atomic_radius} pm"
    
    def display_all_atom_prop(self):
        print(f"Atomic Weight: ", self.atomic_weight, " u")
        print(f"Atomic Number: ", self.atomic_number)
        print(f"Ionic Radius: ", self.ionic_radius, " pm")
        print(f"Atomic Radius: ", self.atomic_radius, " pm")

#Function for opening files containing elements from objects and create list for the objects (I will change later the print(read), cuz it's not useful.)
#Function for Materials file 
def Materials_file():
    material_list = [] #empty list that will contain the materials from the file
    try:
        Materials_txt = open("Materials.txt", "r")
        
        for line in Materials_txt:
            line = line.strip()

            element = line.strip().split(",")
            if len(element) == 6: #cuz we have 6 objects in class Materials
                name = element[0]
                chem_name = element[1]
                type = element[2]
                comp_type = element[3]
                density = element[4]
                crystal_structure = element[5]

                material = Materials(name,chem_name, type, comp_type, density, crystal_structure)
                material_list.append(material)
        Materials_txt.close()
        return material_list
        
    except FileNotFoundError:
        print("Materials file not found! Please check if the file is in the correct path.")

def Materials_count():
    Material_count = open("Materials.txt", "r")
    readlines = Material_count.read()
    count = readlines.count("\n")
    Material_count.close()
    print(count)
    #there must be a change in line in order to have the correct count. otherwise the last line is not measured.
        
#Function for Mechanical Properties file
def Mech_Prop_file():
    mech_prop_list = []
    try:
        Mech_Prop_txt = open("Mechanical_Properties.txt", "r")

        strt, end = "(", ")" #range min, max

        for line in Mech_Prop_txt:
            line = line.strip()

            element = line.strip().split(",")

            for i in range(len(element)):
                if "-" in element[i]:
                    parts = element[i].split("-")
                    element[i] = (float(parts[0]), float(parts[1]))

            if len(element) == 10:
                name = element[0]
                chem_name = element[1]
                type = element[2]
                comp_type = element[3]
                density = element[4]
                crystal_structure = element[5]
                young_modulus = element[6]
                poisson_ratio = element[7]
                yield_strength = element[8]
                tensile_strength = element[9]
                
                mech_props = Mechanical_Properties(name, chem_name, type, comp_type, density, crystal_structure, young_modulus, 
                                                   poisson_ratio, yield_strength, tensile_strength)
                mech_prop_list.append(mech_props)
        Mech_Prop_txt.close()
        return mech_prop_list
    
    except FileNotFoundError:
        print("Mechanical_Properties file not found! Please check if the file is in the correct path.")
#Function for Electrical Properties File
def Elec_Prop_file():
    el_prop_list = []
    try:
        Elec_Prop_txt = open("Electrical_Properties.txt", "r")

        for line in Elec_Prop_txt:
            line = line.strip()
            element = line.strip().split(",")

            for i in range(len(element)):
                if "-" in element[i]:
                    parts = element[i].split("-")
                    element[i] = (float(parts[0]), float(parts[1]))
            
            if len(element) == 10:
                name = element[0]
                chem_name = element[1]
                type = element[2]
                comp_type = element[3]
                density = element[4]
                crystal_structure = element[5]
                el_conductivity = element[6]
                permittivity = element[7]
                dielectric_const = element[8]
                electrical_resistivity = element[9]

                el_props = Electrical_Properties(name, chem_name, type, comp_type, density, crystal_structure, el_conductivity, 
                                                 permittivity, dielectric_const, electrical_resistivity)
                el_prop_list.append(el_props)
                        
        Elec_Prop_txt.close()
        return el_prop_list
    
    except FileNotFoundError:
        print("Electrical_Properties file not found! Please check if the file is in the correct path.")
#Function for Thermal Properties File
def Therm_Prop_file():
    therm_prop_list = []
    try:
        Therm_Prop_txt = open("Thermal_Properties.txt", "r")

        for line in Therm_Prop_txt:
            line = line.strip()
            element = line.strip().split(",")

            for i in range(len(element)):
                if "-" in element[i]:
                    parts = element[i].split("-")
                    element[i] = (float(parts[0]), float(parts[1]))
            
            if len(element) == 9:
                name = element[0]
                chem_name = element[1]
                type = element[2]
                comp_type = element[3]
                density = element[4]
                crystal_structure = element[5]
                th_conductivity = element[6]
                coefficient_expansion = element[7]
                specific_heat = element[8]

                therm_props = Thermal_Properties(name, chem_name, type, comp_type, density, crystal_structure, th_conductivity, coefficient_expansion, specific_heat)

                therm_prop_list.append(therm_props)
                
        Therm_Prop_txt.close()
        
        return therm_prop_list
    except FileNotFoundError:
        print("Thermal_Properties file not found! Please check if the file is in the correct path.")
#Function for Chemical Properties File
def Chem_Prop_file():
    chem_prop_list = []
    try:
        Chem_Prop_txt = open("Chemical_Properties.txt", "r")
        
        for line in Chem_Prop_txt:
            line = line.strip()
            element = line.strip().split(",")

            for i in range(len(element)):
                if "-" in element[i]:
                    parts = element[i].split("-")
                    element[i] = (float(parts[0]), float(parts[1]))

            if len(element) == 7:
                name = element[0]
                chem_name = element[1]
                type = element[2]
                comp_type = element[3]
                density = element[4]
                crystal_structure = element[5]
                pH = element[6]

                chem_props = Chemical_Properties(name, chem_name, type, comp_type, density, crystal_structure, pH)

                chem_prop_list.append(chem_props)

        Chem_Prop_txt.close()

        return chem_prop_list
    except FileNotFoundError:
        print("Chemical_Properties file not found! Please check if the file is in the correct path.")
#Function for Optical Properties File
def Opt_Prop_file():
    opt_prop_list = []
    try:
        Opt_Prop_txt = open("Optical_Properties.txt", "r")
        
        for line in Opt_Prop_txt:
            line = line.strip()
            element = line.strip().split(",")

            for i in range(len(element)):
                if "-" in element[i]:
                    parts = element[i].split("-")
                    element[i] = (parts[0]), (parts[1])

            if len(element) == 7:
                name = element[0]
                chem_name = element[1]
                type = element[2]
                comp_type = element[3]
                density = element[4]
                crystal_structure = element[5]
                color = element[6]

                opt_props = Optical_Properties(name, chem_name, type, comp_type, density, crystal_structure, color)

                opt_prop_list.append(opt_props)

        Opt_Prop_txt.close()

        return opt_prop_list
    except FileNotFoundError:
        print("Optical_Properties file not found! Please check if the file is in the correct path.")
#Function for Atomic Properties File
def Atom_Prop_file():
    atom_prop_list = []
    try:
        Atom_Prop_txt = open("Atomic_Properties.txt", "r")
        
        for line in Atom_Prop_txt:
            line = line.strip()
            element = line.strip().split(",")

            if len(element) == 10:
                name = element[0]
                chem_name = element[1]
                type = element[2]
                comp_type = element[3]
                density = element[4]
                crystal_structure = element[5]
                atomic_weight = element[6]
                atomic_number = element[7]
                ionic_radius = element[8]
                atomic_radius = element[9]

                atom_props = Atomic_Properties(name, chem_name, type, comp_type, density, crystal_structure, atomic_weight, atomic_number, ionic_radius, atomic_radius)
                
                atom_prop_list.append(atom_props)

        Atom_Prop_txt.close()
        
        return atom_prop_list
    except FileNotFoundError:
        print("Atomic_Properties file not found! Please check if the file is in the correct path.")

#Function for writing in files but there shouldn't be any line void, or any object, so the user should put 
#either Don't know if they don't know or none if it doesn't exist

#Functions for printing every property from each file. 
def print_all_Materials(): #prints all materials with their properties
    material = Materials_file() 
    for i in material:
        i.display_all_materials()
def print_all_mech_props(): #prints all mechanical properties of materials
    mechanical = Mech_Prop_file()
    for i in mechanical:
        i.display_all_mech_prop()
def print_all_elec_prop():
    electrical = Elec_Prop_file()
    for i in electrical:
        i.display_all_el_prop()
def print_all_therm_prop(): #prints all thermal properties of materials
    thermal = Therm_Prop_file()
    for i in thermal:
        i.display_all_therm_prop()
def print_all_chem_prop(): #prints all chemical properties of materials
    chemical = Chem_Prop_file()
    for i in chemical:
        i.display_all_chem_prop()
def print_all_opt_prop(): #prints all optical properties of materials
    optical = Opt_Prop_file()
    for i in optical:
        i.display_all_opt_prop()
def print_all_atom_prop(): #prints all atomic properties of materials
    atomic = Atom_Prop_file()
    for i in atomic:
        i.display_all_atom_prop()
                        
#Function main menu
def main_menu():
    print("~~ Main menu ~~")
    print("1. Search for a material")
    print("2. Ask Chatbot")
    print("3. Insert new material")
    print("4. Plot cells: ")
    print("5. Exit")

#Function for validating choice
def get_valid_choice():
    choice = 0 #setting an invalid choice to enter the loop
    while (choice != 1 and choice != 2):
        print("Do you want to proceed?")
        choice = int(input("Select:\n1. Yes\n2. No\n"))

        if(choice == 1):
            print("Proceeding..")
            return True #to continue to choice 1
        elif(choice == 2):
            print("Going back to main menu")
            return False #to go back to main menu and choose again
        else:
            print("Invalid choice. Please enter 1 to continue or 2 to go back..")

#function for opening file of materials and checking if an element already exists
def materials_read(name):
    try:
        materials_reading = open("Materials.txt", "r")
        for line in materials_reading:
            line = line.strip()
            elements = line.strip().split(",")
            if elements[0].lower() == name.lower():
                materials_reading.close()
                return True
        materials_reading.close()
        return False
    except FileNotFoundError:
        print("Materials file not found! Please check if the file is in the correct path")
                                                        
#Function for inserting materials
def new_material_register():
    print("--New Material Register--")
    print("1. Make sure to enter every element or property of each material you want to enter\n" \
    "   If you don't know any property or you want to insert it later, insert the phrase: 'to be determined'.")
    print("2. Don't enter the units, only the values, of a property and be careful of the ones the program uses, so you don't accidentally insert an incorrect one.")

    name = input("Enter the name of the Material: ")
    while materials_read(name):
        print("Material already in database. Please enter another one.")
        name = input("Enter the name of the Material: ")
    chem_name  = input("Enter chemical symbol: ")
    type = input("Enter the material type (element, compound or alloy): ")
    while type.lower() not in ["element", "compound", "alloy"]:
        print("Invalid input of type.")
        type = input("Enter the material type (element, compound or alloy): ")
    comp_type = input("Enter composition type (metal/polymer/ceramic/composite): ")
    while comp_type.lower() not in ["ceramic", "polymer", "metal", "composite"]:
        print("Invalid input of composition.")
        comp_type = input("Enter composition type (metal/polymer/ceramic/composite): ")        
    density = input(f"Enter density (g/{cm}{b}): ")
    crystal_structure = input("Enter the crystal structure (bcc, fcc, hcp, hexagonal, diamond cubic, etc.): ")

    new_material = Materials(name, chem_name, type, comp_type, density, crystal_structure)

    try:
        Material_file_txt = open("Materials.txt", "a")
        line =(','.join([new_material.name, new_material.chem_name, new_material.type, new_material.comp_type, new_material.density, new_material.crystal_structure]) 
        + "\n")
        Material_file_txt.write(line)
        Material_file_txt.close()
        print("Material added successfully!")
        
    except FileNotFoundError:
        print("Materials file not found! Please check if the file is in the correct path")

    choice = 0
    while choice != '1' and choice != '2':
        print("Do you want to insert properties?")
        choice = input("Select:\n1. Yes\n2. No\n")
        if(choice == '1'):
            print("Proceeding..")
            break #to continue to choice 1
        elif(choice == '2'):
            print("Going back to main menu")
            #Mechanical Properties:
            young_modulus = 'to be determined'
            poisson_ratio  = 'to be determined'
            yield_strength = 'to be determined'
            tensile_strength = 'to be determined'

            new_mech_prop = Mechanical_Properties(name, chem_name, type, comp_type, density, crystal_structure, young_modulus, poisson_ratio,  yield_strength, 
                                            tensile_strength)
            try:
                Mech_prop_file_txt = open("Mechanical_Properties.txt", "a")
                line =(','.join([new_material.name, new_material.chem_name, new_material.type, new_material.comp_type, new_material.density, 
                            new_material.crystal_structure, new_mech_prop.young_modulus, new_mech_prop.poisson_ratio, new_mech_prop.yield_strength, 
                            new_mech_prop.tensile_strength]) + "\n")
                Mech_prop_file_txt.write(line)
                Mech_prop_file_txt.close()
                print("Mechanical Properties added successfully!")
            except FileNotFoundError:
                print("Mechanical_Properties file not found! Please check if the file is in the correct path")

            #Electrical Properties
            el_conductivity = 'to be determined'
            permittivity = 'to be determined'
            dielectric_const = 'to be determined'
            electrical_resistivity = 'to be determined'

            new_el_prop = Electrical_Properties(name, chem_name, type, comp_type, density, crystal_structure, el_conductivity, 
                                        permittivity, dielectric_const, electrical_resistivity)
            try:
                El_Prop_file_txt = open("Electrical_Properties.txt", "a")
                line =(','.join([new_material.name, new_material.chem_name, new_material.type, new_material.comp_type, new_material.density, 
                        new_material.crystal_structure, new_el_prop.el_conductivity, new_el_prop.permittivity, 
                        new_el_prop.dielectric_const, new_el_prop.electrical_resistivity]) + "\n")
                El_Prop_file_txt.write(line)
                El_Prop_file_txt.close()
                print("Electrical Properties added successfully.")
            except:
                print("Electrical_Properties file not found! Please check if the file is in the correct path")
            #Chemical Properties
            pH = 'to be determined'

            new_chem_prop = Chemical_Properties(name, chem_name, type, comp_type, density, crystal_structure, pH)
            try:
                Chem_prop_file_txt = open("Chemical_Properties.txt", "a")
                line =(','.join([new_material.name, new_material.chem_name, new_material.type, new_material.comp_type, new_material.density, 
                        new_material.crystal_structure, new_chem_prop.pH]) + "\n")
                Chem_prop_file_txt.write(line)
                Chem_prop_file_txt.close()
                print("Chemical Properties added successfully.")
            except:
                print("Chemical_Properties file not found! Please check if the file is in the correct path")
            #Optical Properties
            color = 'to be determined'

            new_opt_prop = Optical_Properties(name, chem_name, type, comp_type, density, crystal_structure, color)
            try:
                Opt_Prop_file_txt = open("Optical_Properties.txt", "a")
                line =(','.join([new_material.name, new_material.chem_name, new_material.type, new_material.comp_type, new_material.density, 
                        new_material.crystal_structure, new_opt_prop.color]) + "\n")
                Opt_Prop_file_txt.write(line)
                Opt_Prop_file_txt.close()
            except:
                print("Optical_Properties file not found! Please check if the file is in the correct path")
            #Thermal Properties
            th_conductivity = 'to be determined'
            coefficient_expansion = 'to be determined'
            specific_heat = 'to be determined'

            new_therm_prop = Thermal_Properties(name, chem_name, type, comp_type, density, crystal_structure, 
                                        th_conductivity, coefficient_expansion, specific_heat)
            try:
                Therm_Prop_file_txt = open("Thermal_Properties.txt", "a")
                line =(','.join([new_material.name, new_material.chem_name, new_material.type, new_material.comp_type, new_material.density, 
                        new_material.crystal_structure, new_therm_prop.th_conductivity, new_therm_prop.coefficient_expansion, 
                        new_therm_prop.specific_heat]) + "\n")
                Therm_Prop_file_txt.write(line)
                Therm_Prop_file_txt.close()
            except:
                print("Thermal_Properties file not found! Please check if the file is in the correct path")
            #Atomic Properties
            atomic_weight = 'to be determined'
            atomic_number = 'to be determined'
            ionic_radius = 'to be determined'
            atomic_radius = 'to be determined'

            new_atom_prop = Atomic_Properties(name, chem_name, type, comp_type, density, crystal_structure, 
                                        atomic_weight, atomic_number, ionic_radius, atomic_radius)
        
            try:
                Atom_Prop_file_txt = open("Atomic_Properties.txt", "a")
                line =(','.join([new_material.name, new_material.chem_name, new_material.type, new_material.comp_type, new_material.density, 
                        new_material.crystal_structure, new_atom_prop.atomic_weight, new_atom_prop.atomic_number,
                        new_atom_prop.ionic_radius, new_atom_prop.atomic_radius]) + "\n")
                Atom_Prop_file_txt.write(line)
                Atom_Prop_file_txt.close()
            except:
                print("Atomic_Properties file not found! Please check if the file is in the correct path")
            return False #to go back to main menu and choose again
        else:
            print("Invalid choice. Please enter 1 to continue or 2 to go back..")

    print("Select a category to insert properties: ")
    category_list = ["Mechanical Properties", "Electrical Properties", "Chemical Properties", "Optical Properties", "Thermal Properties", "Atomic Properties"]
    while len(category_list) != 0:
        for i in range(len(category_list)):
            print(i+1, ".", category_list[i])
        try:
            category_choice = int(input("Choose the category you want to insert properties in: "))
        except ValueError:
            print("Insert a number, not a character.")
            continue
        while category_choice > len(category_list) or category_choice < 1:
            print("Invalid choice. Try again.")
            try:
                category_choice = int(input("Choose the category you want to insert properties in: "))
            except ValueError:
                print("Insert a number not a character.")
        selected_category = category_list[category_choice - 1]
        if selected_category == "Mechanical Properties":
            print("~Mechanical Properties: ")
            young_modulus = input("Enter Young's modulus: ")
            poisson_ratio  = input("Enter Poisson's Ratio: ")
            yield_strength = input("Enter yield strength: ")
            tensile_strength = input("Enter tensile strength: ")

            new_mech_prop = Mechanical_Properties(name, chem_name, type, comp_type, density, crystal_structure, young_modulus, poisson_ratio,  yield_strength, 
                                            tensile_strength)
            try:
                Mech_prop_file_txt = open("Mechanical_Properties.txt", "a")
                line =(','.join([new_material.name, new_material.chem_name, new_material.type, new_material.comp_type, new_material.density, 
                            new_material.crystal_structure, new_mech_prop.young_modulus, new_mech_prop.poisson_ratio, new_mech_prop.yield_strength, 
                            new_mech_prop.tensile_strength]) + "\n")
                Mech_prop_file_txt.write(line)
                Mech_prop_file_txt.close()
                print("Mechanical Properties added successfully!")
            except FileNotFoundError:
                print("Mechanical_Properties file not found! Please check if the file is in the correct path")
        elif selected_category == "Electrical Properties":
            print("~Electrical Properties")
            el_conductivity = input("Enter electrical conductivity: ")
            permittivity = input("Enter permittivity: ")
            dielectric_const = input("Enter dielectric constant: ")
            electrical_resistivity = input("Enter electrical resistivity: ")

            new_el_prop = Electrical_Properties(name, chem_name, type, comp_type, density, crystal_structure, el_conductivity, 
                                        permittivity, dielectric_const, electrical_resistivity)
            try:
                El_Prop_file_txt = open("Electrical_Properties.txt", "a")
                line =(','.join([new_material.name, new_material.chem_name, new_material.type, new_material.comp_type, new_material.density, 
                        new_material.crystal_structure, new_el_prop.el_conductivity, new_el_prop.permittivity, 
                        new_el_prop.dielectric_const, new_el_prop.electrical_resistivity]) + "\n")
                El_Prop_file_txt.write(line)
                El_Prop_file_txt.close()
                print("Electrical Properties added successfully.")
            except:
                print("Electrical_Properties file not found! Please check if the file is in the correct path")
        elif selected_category == "Chemical Properties":
            print("~Chemical Properties")
            pH = input("Enter pH: ")

            new_chem_prop = Chemical_Properties(name, chem_name, type, comp_type, density, crystal_structure, pH)
            try:
                Chem_prop_file_txt = open("Chemical_Properties.txt", "a")
                line =(','.join([new_material.name, new_material.chem_name, new_material.type, new_material.comp_type, new_material.density, 
                        new_material.crystal_structure, new_chem_prop.pH]) + "\n")
                Chem_prop_file_txt.write(line)
                Chem_prop_file_txt.close()
                print("Chemical Properties added successfully.")
            except:
                print("Chemical_Properties file not found! Please check if the file is in the correct path")
        elif selected_category == "Optical Properties":
            print("~Optical Properties")
            color = input("Enter color (Use '-' if the values are between a range): ")

            new_opt_prop = Optical_Properties(name, chem_name, type, comp_type, density, crystal_structure, color)
            try:
                Opt_Prop_file_txt = open("Optical_Properties.txt", "a")
                line =(','.join([new_material.name, new_material.chem_name, new_material.type, new_material.comp_type, new_material.density, 
                        new_material.crystal_structure, new_opt_prop.color]) + "\n")
                Opt_Prop_file_txt.write(line)
                Opt_Prop_file_txt.close()
            except:
                print("Optical_Properties file not found! Please check if the file is in the correct path")
        elif selected_category == "Thermal Properties":
            print("~Thermal Properties")
            th_conductivity = input("Enter thermal conductivity: ")
            coefficient_expansion = input("Enter coefficient of expansion: ")
            specific_heat = input("Enter specific heat: ")

            new_therm_prop = Thermal_Properties(name, chem_name, type, comp_type, density, crystal_structure, 
                                        th_conductivity, coefficient_expansion, specific_heat)
            try:
                Therm_Prop_file_txt = open("Thermal_Properties.txt", "a")
                line =(','.join([new_material.name, new_material.chem_name, new_material.type, new_material.comp_type, new_material.density, 
                        new_material.crystal_structure, new_therm_prop.th_conductivity, new_therm_prop.coefficient_expansion, 
                        new_therm_prop.specific_heat]) + "\n")
                Therm_Prop_file_txt.write(line)
                Therm_Prop_file_txt.close()
            except:
                print("Thermal_Properties file not found! Please check if the file is in the correct path")
        elif selected_category == "Atomic Properties":
            print("~Atomic Properties")
            atomic_weight = input("Enter atomic weight: ")
            atomic_number = input("Enter atomic number: ")
            ionic_radius = input("Enter ionic radius: ")
            atomic_radius = input("Enter atomic radius: ")

            new_atom_prop = Atomic_Properties(name, chem_name, type, comp_type, density, crystal_structure, 
                                        atomic_weight, atomic_number, ionic_radius, atomic_radius)
        
            try:
                Atom_Prop_file_txt = open("Atomic_Properties.txt", "a")
                line =(','.join([new_material.name, new_material.chem_name, new_material.type, new_material.comp_type, new_material.density, 
                        new_material.crystal_structure, new_atom_prop.atomic_weight, new_atom_prop.atomic_number,
                        new_atom_prop.ionic_radius, new_atom_prop.atomic_radius]) + "\n")
                Atom_Prop_file_txt.write(line)
                Atom_Prop_file_txt.close()
            except:
                print("Atomic_Properties file not found! Please check if the file is in the correct path")

        
        category_list.pop(category_choice - 1)

#Function for reading pdf
def read_pdf_text():
    pdf = fitz.open(r"D:\Python\Project_Python_Kyzeridou\Material_Science_Callister.pdf")
    text = ""
    for page in pdf:
        text += page.get_text()
    pdf.close()
    return text

#Function for chatbot/ interface??
def chatbot():
    pdf_text = read_pdf_text()
    lines = pdf_text.split('\n')
    common_words = ["the", "a", "is", "and", "to", "of", "in", "that", "have", "I", "he", "she", "it", "us", "we", "you", "on", "at", "to", "by", "with"]
    while True:
        print("\nWelcome to the Materials Chat Bot!")
        print("What do you want to learn about?")
        print("Type 'exit' to quit.")
        question = input("Your question: ")
        if question.strip().lower() == "exit":
            print("You exited the chatbot.")
            break
        keywords = question.lower().split()
        found = False
        for line in lines:
            line_lower = line.lower()
            for word in keywords:
                if word in line_lower and word not in common_words:
                    print("Answer: ", line.strip())
                    found = True
                    break
            if found:
                validation = ""
                while "yes".lower() not in validation and "no".lower() not in validation:
                    validation = input("Are you satisfied with my answear?   ").strip().lower()
                    if "yes" in validation:
                        print("saved the answear for later") #i will save it later on somewhere
                    elif "no" in validation:
                        print("I'm sorry I couldn't help you..")
                    else:
                        print("I don't get the answear. Enter yes or no.")
                break
        if not found:
            print("Sorry I couldn't find anything relevant to your question :(")        

#Functions for plotting materials structure
#Plotting cubic
def simple_cubic():
    a = 1.0 #define lattice constant as 1

    atoms = np.array([
        [0, 0, 0], #0
        [1, 0, 0], #1
        [0, 0, 1], #2
        [1, 0, 1], #3
        [0, 1, 0], #4
        [0, 1, 1], #5
        [1, 1, 0], #6
        [1, 1, 1]  #7
    ]) * a

    bonds = [
        (0, 1), (0, 2), (0, 4),
        (1, 3), (1, 6),
        (2, 3), (2, 5),
        (4, 5), (4, 6),
        (7, 6), (7, 5), (7,3)
    ]

    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(atoms[:, 0], atoms[:, 1], atoms[:, 2], color='red', s=100)

    for bond in bonds:
        x = [atoms[bond[0], 0], atoms[bond[1], 0]]
        y = [atoms[bond[0], 1], atoms[bond[1], 1]]
        z = [atoms[bond[0], 2], atoms[bond[1], 2]]
        ax.plot(x, y, z, color='yellow')

    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    ax.set_title('Simple Cubic Unit Cell')

    ax.set_box_aspect([1, 1, 1])

    ax.set_xlim([0, a])
    ax.set_ylim([0, a])
    ax.set_zlim([0, a])

    plt.show()

#Plotting Body Centered Unit Cell
def bcc():
    a = 1.0

    atoms = np.array([
        [0, 0, 0], #0
        [1, 0, 0], #1
        [0, 0, 1], #2
        [1, 0, 1], #3
        [0, 1, 0], #4
        [0, 1, 1], #5
        [1, 1, 0], #6
        [1, 1, 1],  #7
        [0.5, 0.5, 0.5] #8
    ]) * a

    bonds1 = [
        (0, 1), (0, 2), (0, 4),
        (1, 3), (1, 6),
        (2, 3), (2, 5),
        (4, 5), (4, 6),
        (7, 6), (7, 5), (7,3)
    ]

    bonds2 = [
        (8, 0), (8, 1), (8, 2), (8, 3), (8, 6), (8, 4), (8, 7), (8, 5)
    ]

    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(atoms[:8, 0], atoms[:8, 1], atoms[:8, 2], color='yellow', s=100)
    ax.scatter(atoms[8, 0], atoms[8, 1], atoms[8, 2], color='hotpink', alpha = 1, s=100)

    for bond in bonds1:
        x = [atoms[bond[0], 0], atoms[bond[1], 0]]
        y = [atoms[bond[0], 1], atoms[bond[1], 1]]
        z = [atoms[bond[0], 2], atoms[bond[1], 2]]
        ax.plot(x, y, z, color='black')

    for bond in bonds2:
        x = [atoms[bond[0], 0], atoms[bond[1], 0]]
        y = [atoms[bond[0], 1], atoms[bond[1], 1]]
        z = [atoms[bond[0], 2], atoms[bond[1], 2]]
        ax.plot(x, y, z, '--', color='grey')

    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    ax.set_title('Body Centered Unit Cell')

    ax.set_box_aspect([1, 1, 1])

    ax.set_xlim([0, a])
    ax.set_ylim([0, a])
    ax.set_zlim([0, a])

    plt.show()

#Plotting Face Centered Unit Cell
def fcc():
    a = 1.0
    
    atoms = np.array([
        [0, 0, 0], #0
        [1, 0, 0], #1
        [0, 0, 1], #2
        [1, 0, 1], #3
        [0, 1, 0], #4
        [0, 1, 1], #5
        [1, 1, 0], #6
        [1, 1, 1],  #7
        [0.5, 0, 0.5], #8
        [0.5, 1, 0.5], #9
        [0, 0.5, 0.5], #10
        [1, 0.5, 0.5], #11
        [0.5, 0.5, 0], #12
        [0.5, 0.5, 1] #13
    ]) * a

    bonds1 = [
        (0, 1), (0, 2), (0, 4),
        (1, 3), (1, 6),
        (2, 3), (2, 5),
        (4, 5), (4, 6),
        (7, 6), (7, 5), (7,3)
    ]

    bonds2 = [
        (8, 0), (8, 1), (8, 2), (8, 3),
        (9, 4), (9, 6), (9, 5), (9, 7),
        (10, 0), (10, 2), (10, 4), (10, 5),
        (11, 1), (11, 3), (11, 6), (11, 7), 
        (12, 0), (12, 1), (12, 4), (12, 6), 
        (13, 2), (13, 3), (13, 5), (13, 7)
    ]

    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(atoms[:8, 0], atoms[:8, 1], atoms[:8, 2], color='yellow', s=100)
    for i in range(8,13+1):
        ax.scatter(atoms[i, 0], atoms[i, 1], atoms[i, 2], color='hotpink', alpha = 1, s=100)

    for bond in bonds1:
        x = [atoms[bond[0], 0], atoms[bond[1], 0]]
        y = [atoms[bond[0], 1], atoms[bond[1], 1]]
        z = [atoms[bond[0], 2], atoms[bond[1], 2]]
        ax.plot(x, y, z, color='black')

    for bond in bonds2:
        x = [atoms[bond[0], 0], atoms[bond[1], 0]]
        y = [atoms[bond[0], 1], atoms[bond[1], 1]]
        z = [atoms[bond[0], 2], atoms[bond[1], 2]]
        ax.plot(x, y, z, '--', color='grey')

    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    ax.set_title('Face Centered Unit Cell')

    ax.set_box_aspect([1, 1, 1])

    ax.set_xlim([0, a])
    ax.set_ylim([0, a])
    ax.set_zlim([0, a])

    plt.show()

#Plotting Hexagonal closed packed Unit Cell (Graphite)
def hcp():
    a = 2.46 
    c = 1.633 * a  # Distance between layers (angstroms)

    atoms = np.array([
    [0, 0, 0], #0
    [-a/2, -np.sqrt(3)*a/2, 0], #1
    [a, 0, 0], #2
    [a/2, np.sqrt(3)*a/2, 0], #3
    [-a, 0, 0], #4
    [a/2, -np.sqrt(3)*a/2, 0], #5
    [-a/2, np.sqrt(3)*a/2, 0], #6

    [0, 0, c/2], #7
    [a/2, np.sqrt(3)*a/2, c/2], #8
    [a/2, -np.sqrt(3)*a/2, c/2], #9

    [0, 0, c], #10
    [-a/2, -np.sqrt(3)*a/2, c], #11
    [a, 0, c], #12
    [a/2, np.sqrt(3)*a/2, c], #13
    [-a, 0, c], #14
    [a/2, -np.sqrt(3)*a/2, c], #15
    [-a/2, np.sqrt(3)*a/2, c] #16
    ])
    
    bonds1 = [
        (1, 5), (5, 2), (2, 3), (3, 6), (6, 4), (4, 1), 
        (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6),

        (7, 8), (7, 9),

        (11, 15), (15, 12), (12, 13), (13, 16), (16, 14), (14, 11),
        (10, 11), (10, 12), (10, 13), (10, 14), (10, 15), (10, 16)
    ]

    bonds2 = [
        (4, 14), (6, 16), (0, 10), (3, 13), (2, 12), (1, 11), (5, 15)
    ]

    bonds3 = [
        (0, 7), (7, 10), (5, 9), (9, 15), (3, 8), (8, 13)
    ]

    
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(atoms[:, 0], atoms[:, 1], atoms[:, 2], color='blue', s=100)
    
    for bond in bonds1:
        x = [atoms[bond[0], 0], atoms[bond[1], 0]]
        y = [atoms[bond[0], 1], atoms[bond[1], 1]]
        z = [atoms[bond[0], 2], atoms[bond[1], 2]]
        ax.plot(x, y, z, color='black')

    for bond in bonds2:
        x = [atoms[bond[0], 0], atoms[bond[1], 0]]
        y = [atoms[bond[0], 1], atoms[bond[1], 1]]
        z = [atoms[bond[0], 2], atoms[bond[1], 2]]
        ax.plot(x, y, z,'--', color='grey')
    
    for bond in bonds3:
        x = [atoms[bond[0], 0], atoms[bond[1], 0]]
        y = [atoms[bond[0], 1], atoms[bond[1], 1]]
        z = [atoms[bond[0], 2], atoms[bond[1], 2]]
        ax.plot(x, y, z, '--', color='lightblue')
    
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    ax.set_title('Closed packed Hexagonal Unit Cell')
    
    ax.set_box_aspect([1, 1, 1])  

    ax.set_xlim([-a, a])
    ax.set_ylim([-a, a])
    ax.set_zlim([0, c])

    plt.show()

#Plotting Simple Hexagonal Unit cell
def simple_hexagonal():
    a = 2.46 
    c = 1.633 * a  # Distance between layers (angstroms)

    atoms = np.array([
    [0, 0, 0], #0
    [-a/2, -np.sqrt(3)*a/2, 0], #1
    [a, 0, 0], #2
    [a/2, np.sqrt(3)*a/2, 0], #3
    [-a, 0, 0], #4
    [a/2, -np.sqrt(3)*a/2, 0], #5
    [-a/2, np.sqrt(3)*a/2, 0], #6

    [0, 0, c], #7
    [-a/2, -np.sqrt(3)*a/2, c], #8
    [a, 0, c], #9
    [a/2, np.sqrt(3)*a/2, c], #10
    [-a, 0, c], #11
    [a/2, -np.sqrt(3)*a/2, c], #12
    [-a/2, np.sqrt(3)*a/2, c] #13
    ])

    bonds = [
        (1, 2), (2, 3), (3, 4), (4, 5), (5, 6),
        (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6),

        (8, 9), (9 ,10), (10, 11), (11, 12), (12, 13),
        (7, 8), (7, 9), (7, 10), (7, 11), (7, 12), (7, 13),

        (0, 7), (1, 8), (2, 9), (3, 10), (4, 11), (5, 12), (6, 13)
    ]

    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(atoms[:, 0], atoms[:, 1], atoms[:, 2], color='blue', s=100)

    for bond in bonds:
        x = [atoms[bond[0], 0], atoms[bond[1], 0]]
        y = [atoms[bond[0], 1], atoms[bond[1], 1]]
        z = [atoms[bond[0], 2], atoms[bond[1], 2]]
        ax.plot(x, y, z, color='black')

    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    ax.set_title('Simple Hexagonal Unit Cell')
    
    ax.set_box_aspect([1, 1, 1])  

    ax.set_xlim([-a, a])
    ax.set_ylim([-a, a])
    ax.set_zlim([0, c])

    plt.show()

#Plotting diamond
def diamond_cubic():
    a = 1.0 #lattice constant
    atoms = np.array([
    [0, 0, 0],           # Corner
    [0.5, 0.5, 0],       # Face center
    [0.5, 0, 0.5],       # Face center
    [0, 0.5, 0.5],       # Face center
    [0.25, 0.25, 0.25],  # Tetrahedral position
    [0.75, 0.75, 0.25],  
    [0.75, 0.25, 0.75],  
    [0.25, 0.75, 0.75]   
    ]) * a

    bonds = [
        (0, 4), (1, 5), (2, 6), (3, 7),
        (4, 5), (4, 6), (4, 7),
        (5, 6), (5, 7),
        (6, 7)
    ]

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(atoms[:4, 0], atoms[:4, 1], atoms[:4, 2], color='blue', s=100, label='FCC atoms')
    ax.scatter(atoms[4:, 0], atoms[4:, 1], atoms[4:, 2], color='red', s=100, label='Tetrahedral atoms')

    for bond in bonds:
        x = [atoms[bond[0], 0], atoms[bond[1], 0]]
        y = [atoms[bond[0], 1], atoms[bond[1], 1]]
        z = [atoms[bond[0], 2], atoms[bond[1], 2]]
        ax.plot(x, y, z, color='blue', linewidth = 2)

    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    ax.set_title('Diamond Crystal Unit Cell')

    ax.set_box_aspect([1, 1, 1])

    ax.set_xlim([0, a])
    ax.set_ylim([0, a])
    ax.set_zlim([0, a])

    plt.show()

#function that creates data for materials in xrd 

#function for plotting energy bonds

#function for phase diagrams

#Starting menu of 2 choices
choice = 0
while choice not in [1, 2, 3, 4, 5]:
    main_menu()
    try:
        choice = int(input("Enter a choice: "))
    except ValueError:
        print("Invalid input. Try typing a number not a character.")
        continue
    if (choice == 1):
        if get_valid_choice():
            print("--Material search engine--")
    elif choice == 2:
        if get_valid_choice():
            chatbot()
    elif choice == 3:
        if get_valid_choice():
            new_material_register()
    elif choice == 4:
        if get_valid_choice():
            print("--View Plots--")
            option = 0
            menu_option = [1, 2, 3, 4, 5, 6]
            while (option not in menu_option):
                print("1. Sc\n2. BCC\n3. FCC\n4. HCP\n5. Simple Hexagonal\n6. Diamond")
                option = int(input("select the graph: "))
                if (option == 1):
                    simple_cubic()
                elif (option == 2):
                    bcc()
                elif option == 3:
                    fcc()
                elif option == 4:
                    hcp()
                elif option == 5:
                    simple_hexagonal()
                elif option == 6: 
                    diamond_cubic()
    elif choice == 5:
        print("--Exiting program--")
        break
    else:
        print("Please enter a valid option (1-3)")

     
#graphics
