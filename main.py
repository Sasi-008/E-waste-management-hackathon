import uuid

class EWasteMonitoringSystem:
    def __init__(self):
        self.reports = {}
        self.company_password = "ewaste"

    def report_e_waste(self, description, location):
        report_id = str(uuid.uuid4())
        self.reports[report_id] = {'description': description, 'location': location, 'status': 'reported'}
        print(f"Thank you for reporting. Your report ID is: {report_id}")

    def display_report_ids(self):
        if not self.reports:
            print("No e-waste reports available.")
        else:
            print("Available Report IDs:")
            for report_id in self.reports.keys():
                print(f"- {report_id}")

    def track_e_waste(self, password):
        if password != self.company_password:
            print("Access denied. Invalid password.")
            return
        
        self.display_report_ids()
        report_id = input("Enter report ID to track: ")
        
        report = self.reports.get(report_id)
        if report:
            print(f"ID: {report_id}")
            print(f"Description: {report['description']}")
            print(f"Location: {report['location']}")
            print(f"Status: {report['status']}")
        else:
            print("Report not found.")

    def recycle_e_waste(self, password):
        if password != self.company_password:
            print("Access denied. Invalid password.")
            return
        
        self.display_report_ids()
        report_id = input("Enter report ID to recycle: ")
        
        report = self.reports.get(report_id)
        if report:
            if report['status'] == 'reported':
                report['status'] = 'recycled'
                print(f"E-waste with ID {report_id} marked as recycled.")
            else:
                print("E-waste has already been recycled.")
        else:
            print("Report not found.")

def main():
    system = EWasteMonitoringSystem()

    while True:
        print("\nE-Waste Monitoring System")
        print("1. Report E-Waste (Customer)")
        print("2. Track E-Waste (Company)")
        print("3. Recycle E-Waste (Company)")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            description = input("Enter description of e-waste: ")
            location = input("Enter location of e-waste: ")
            system.report_e_waste(description, location)
        elif choice == '2':
            password = input("Enter company password: ")
            system.track_e_waste(password)
        elif choice == '3':
            password = input("Enter company password: ")
            system.recycle_e_waste(password)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
