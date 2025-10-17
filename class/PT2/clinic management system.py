import csv

class Patient:
    def __init__(self, id, name, age, weight, height, bp):
        self.id = id.strip()
        self.name = name.strip()
        self.age = int(age)
        self.weight = float(weight)
        self.height = float(height)
        self.bp = tuple(bp)

    def is_high_bp(self):
        systolic, diastolic = self.bp
        return systolic > 140 or diastolic > 90

    def calculate_BMI(self):
        if self.height <= 0 or self.weight <= 0:
            return None
        return round(self.weight / ((self.height / 100) ** 2))

    def __str__(self):
        bmi = self.calculate_BMI()
        bmi_str = "N/A" if bmi is None else str(bmi)
        return (
            f"Patient ID: {self.id}\n"
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Weight: {self.weight} kg\n"
            f"Height: {self.height} cm\n"
            f"BP (Systolic/Diastolic): {self.bp[0]}/{self.bp[1]}\n"
            f"High BP Status: {'YES' if self.is_high_bp() else 'NO'}\n"
            f"BMI: {bmi_str}"
        )


class Clinic:
    def __init__(self):
        self.patients = []

    def add_patient(self, patient: Patient):
        if any(p.id == patient.id for p in self.patients):
            print("Patient ID already exists. Not added.")
            return
        self.patients.append(patient)
        print("Added successfully")

    def find_patient_byid(self, patient_id):
        for patient in self.patients:
            if patient.id == patient_id:
                return patient
        return None

    def show_all_patient(self):
        if not self.patients:
            print("\nNo patient data.\n")
            return
        print("\n--- ALL PATIENT RECORDS ---")
        for i, patient in enumerate(self.patients, start=1):
            print(f"Record #{i}")
            print(patient)
            print("-" * 30)
        print(f"Total records: {len(self.patients)}")
        print("---------------------------\n")

    def show_high_bp_patient(self):
        found = False
        print("\n--- PATIENTS WITH HIGH BLOOD PRESSURE ---")
        for i, patient in enumerate(self.patients, start=1):
            if patient.is_high_bp():
                found = True
                print(f"Record #{i}")
                print(patient)
                print("-" * 30)
        if not found:
            print("No high blood pressure patients found.")
        print("---------------------------\n")

    def remove_patient_byid(self, patient_id):
        for i, patient in enumerate(self.patients):
            if patient.id == patient_id:
                del self.patients[i]
                print("Removed successfully")
                return
        print("Patient does not exist")

    def save_to_file(self, path="patients_data.csv"):
        with open(path, mode="w", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Age", "Weight(kg)", "Height(cm)", "BloodPressure(Systolic/Diastolic)"])
            for p in self.patients:
                writer.writerow([p.id, p.name, p.age, p.weight, p.height, f"{p.bp[0]}/{p.bp[1]}"])
        print("Save Done")

    def load_from_file(self, path="patients_data.csv"):
        try:
            with open(path, mode="r", encoding="utf-8") as file:
                reader = csv.reader(file)
                self.patients = []
                for row in reader:
                    if len(row) < 6:
                        continue  # bỏ dòng trống hoặc lỗi
                    id, name, age, weight, height, bp_str = row
                    try:
                        systolic, diastolic = map(int, bp_str.split("/"))
                    except:
                        continue
                    patient = Patient(
                        id=id,
                        name=name,
                        age=int(age),
                        weight=float(weight),
                        height=float(height),
                        bp=(systolic, diastolic)
                    )
                    self.patients.append(patient)
            print("Load Done")
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print("Error while loading:", e)

    def sort_patients_by_bmi(self):
        self.patients.sort(key=lambda p: (p.calculate_BMI() is None, p.calculate_BMI() or 0))
        print("Sort Done by BMI asscending")

    def sort_patients_by_age(self):
        self.patients.sort(key=lambda p: p.age)
        print("Sort Done by age asscending")




def display_menu():
    print("\n====== Clinic Management System ======")
    print("1. Add new patient")
    print("2. View all patients")
    print("3. Search patient by ID")
    print("4. Show patients with high blood pressure")
    print("5. Remove patient")
    print("6. Sort patients by BMI")
    print("7. Sort patients by Age")
    print("8. Save data to file")
    print("9. Load data from file")
    print("0. Exit")
    print("======================================")

if __name__ == "__main__":
    clinic = Clinic()

    while True:
        display_menu()
        choice = input("Choose operation: ").strip()

        if choice == "1":
            id_ = input("Enter patient's ID: ").strip()
            name = input("Patient's name: ").strip()
            while True:
                try:
                    age = int(input("Patient's age: ").strip())
                    weight = float(input("Patient's weight (kg): ").strip())
                    height = float(input("Patient's height (cm): ").strip())

                    bp_raw = input("Patient's blood pressure (Systolic,Diastolic or Systolic/Diastolic): ").strip().replace(" ", "")
                    sep = "," if "," in bp_raw else ("/" if "/" in bp_raw else None)
                    if not sep:
                        print("Use '120,80' or '120/80'. Try again.\n")
                        continue
                    systolic, diastolic = map(int, bp_raw.split(sep))
                    break  # tất cả hợp lệ -> thoát vòng lặp

                except ValueError:
                    print("Invalid input. Please enter numeric values correctly.\n")


            clinic.add_patient(Patient(id_, name, age, weight, height, (systolic, diastolic)))

        elif choice == "2":
            clinic.show_all_patient()

        elif choice == "3":
            find_id = input("Patient's ID: ").strip()
            p = clinic.find_patient_byid(find_id)
            if p:
                print("\n--- PATIENT FOUND ---")
                print(p)
                print("---------------------\n")
            else:
                print("Patient does not exist")

        elif choice == "4":
            clinic.show_high_bp_patient()

        elif choice == "5":
            remove_id = input("Patient's ID to remove: ").strip()
            clinic.remove_patient_byid(remove_id)

        elif choice == "6":
            clinic.sort_patients_by_bmi()

        elif choice == "7":
            clinic.sort_patients_by_age()

        elif choice == "8":
            clinic.save_to_file()

        elif choice == "9":
            try:
                clinic.load_from_file()
            except FileNotFoundError:
                print("File not found. Please save data first.")
            except Exception as e:
                print(f"Error while loading: {e}")

        elif choice == "0":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose again.")
