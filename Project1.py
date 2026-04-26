from datetime import datetime, timedelta
import json

class LibraryManagementSystem:
    def __init__(self):
        self.books = {}  # {book_id: {"title": "", "author": "", "quantity": int, "available": int}}
        self.issued_books = {}  # {book_id: {"student_name": "", "issue_date": "", "return_date": "", "days_allowed": int}}
        self.load_data()
    
    def load_data(self):
        """Load initial sample data"""
        sample_books = {
            "B001": {"title": "Python Programming", "author": "John Smith", "quantity": 5, "available": 5},
            "B002": {"title": "Data Structures", "author": "Jane Doe", "quantity": 3, "available": 3},
            "B003": {"title": "Algorithms", "author": "Bob Wilson", "quantity": 4, "available": 4},
            "B004": {"title": "Database Systems", "author": "Alice Brown", "quantity": 2, "available": 2}
        }
        self.books.update(sample_books)
    
    def save_data(self):
        """Save data to JSON file (optional feature)"""
        data = {
            "books": self.books,
            "issued_books": self.issued_books
        }
        with open("library_data.json", "w") as f:
            json.dump(data, f, default=str)
    
    def display_header(self, title):
        print("\n" + "="*60)
        print(f"📚 LIBRARY MANAGEMENT SYSTEM 📚".center(60))
        print(f"{title}".center(60))
        print("="*60)
    
    def display_books(self):
        """Display all books with clear formatting"""
        self.display_header("📖 AVAILABLE BOOKS")
        print(f"{'ID':<6} {'TITLE':<25} {'AUTHOR':<20} {'TOTAL':<6} {'AVAILABLE':<10}")
        print("-" * 70)
        
        for book_id, details in self.books.items():
            print(f"{book_id:<6} {details['title']:<25} {details['author']:<20} "
                  f"{details['quantity']:<6} {details['available']:<10}")
        print("-" * 70)
    
    def add_book(self):
        """Add new book to library"""
        self.display_header("➕ ADD NEW BOOK")
        book_id = input("Enter Book ID (e.g., B005): ").strip().upper()
        
        if book_id in self.books:
            print("❌ Book ID already exists!")
            return
        
        title = input("Enter Book Title: ").strip()
        author = input("Enter Author Name: ").strip()
        quantity = int(input("Enter Total Quantity: "))
        
        self.books[book_id] = {
            "title": title,
            "author": author,
            "quantity": quantity,
            "available": quantity
        }
        print(f"✅ Book '{title}' added successfully!")
    
    def issue_book(self):
        """Issue book to student with details"""
        self.display_books()
        book_id = input("\nEnter Book ID to issue: ").strip().upper()
        
        if book_id not in self.books:
            print("❌ Book ID not found!")
            return
        
        book = self.books[book_id]
        if book["available"] == 0:
            print("❌ No copies available!")
            return
        
        student_name = input("Enter Student Name: ").strip()
        days_allowed = int(input("Enter days allowed (max 21): "))
        
        # Issue book
        book["available"] -= 1
        issue_date = datetime.now().strftime("%Y-%m-%d %H:%M")
        return_date = (datetime.now() + timedelta(days=days_allowed)).strftime("%Y-%m-%d")
        
        self.issued_books[book_id] = {
            "student_name": student_name,
            "issue_date": issue_date,
            "return_date": return_date,
            "days_allowed": days_allowed
        }
        
        print(f"\n✅ Book issued successfully!")
        print(f"📄 Issue Details:")
        print(f"   Book: {book['title']}")
        print(f"   Student: {student_name}")
        print(f"   Issue Date: {issue_date}")
        print(f"   Return By: {return_date}")
        print(f"\n⚠️  FINE STRUCTURE:")
        print(f"   1st Week: ₹10/day/book")
        print(f"   2nd Week: ₹20/day/book")
        print(f"   3rd Week: ₹60/day/book")
        print(f"   4th Week onwards: ₹120/day/book")
    
    def calculate_fine(self, days_overdue):
        """Calculate fine based on overdue days"""
        fine = 0
        if days_overdue <= 0:
            return 0
        
        weeks = [7, 7, 7, float('inf')]  # 1st, 2nd, 3rd week and beyond
        rates = [10, 20, 60, 120]
        
        remaining_days = days_overdue
        for i, week_days in enumerate(weeks):
            if remaining_days == 0:
                break
            days_in_week = min(remaining_days, week_days)
            fine += days_in_week * rates[i]
            remaining_days -= days_in_week
        
        return fine
    
    def return_book(self):
        """Return book and calculate fine if any"""
        self.display_header("🔙 RETURN BOOK")
        book_id = input("Enter Book ID to return: ").strip().upper()
        
        if book_id not in self.books or book_id not in self.issued_books:
            print("❌ Book not issued or ID not found!")
            return
        
        issued_info = self.issued_books[book_id]
        book = self.books[book_id]
        
        return_date = datetime.now()
        expected_date = datetime.strptime(issued_info["return_date"][:10], "%Y-%m-%d")
        days_overdue = (return_date - expected_date).days
        
        # Return book
        book["available"] += 1
        fine = self.calculate_fine(days_overdue)
        
        print(f"\n📄 RETURN SUMMARY:")
        print(f"   Book: {book['title']}")
        print(f"   Student: {issued_info['student_name']}")
        print(f"   Issued: {issued_info['issue_date']}")
        print(f"   Expected Return: {issued_info['return_date']}")
        print(f"   Actual Return: {return_date.strftime('%Y-%m-%d %H:%M')}")
        
        if days_overdue <= 0:
            print("✅ Book returned on time! No fine.")
        else:
            print(f"⚠️  Book returned {days_overdue} days late!")
            print(f"💰 Fine Amount: ₹{fine}")
        
        # Remove from issued books
        del self.issued_books[book_id]
    
    def display_issued_books(self):
        """Display all issued books"""
        self.display_header("📋 ISSUED BOOKS")
        if not self.issued_books:
            print("No books issued currently.")
            return
        
        print(f"{'ID':<6} {'TITLE':<25} {'STUDENT':<20} {'ISSUE DATE':<15} {'RETURN BY':<12} {'DAYS':<5}")
        print("-" * 90)
        
        for book_id, details in self.issued_books.items():
            book = self.books[book_id]
            print(f"{book_id:<6} {book['title']:<25} {details['student_name']:<20} "
                  f"{details['issue_date'][:16]:<15} {details['return_date']:<12} {details['days_allowed']:<5}")
        print("-" * 90)
    
    def menu(self):
        """Main menu"""
        while True:
            print("\n" + "🏛️  MAIN MENU 🏛️".center(60))
            print("1. 📖 View All Books")
            print("2. ➕ Add New Book")
            print("3. 📤 Issue Book")
            print("4. 🔙 Return Book")
            print("5. 📋 View Issued Books")
            print("6. ❌ Exit")
            
            choice = input("\nEnter your choice (1-6): ").strip()
            
            if choice == '1':
                self.display_books()
            elif choice == '2':
                self.add_book()
            elif choice == '3':
                self.issue_book()
            elif choice == '4':
                self.return_book()
            elif choice == '5':
                self.display_issued_books()
            elif choice == '6':
                self.save_data()
                print("👋 Thank you for using Library Management System!")
                break
            else:
                print("❌ Invalid choice! Please try again.")
            
            input("\nPress Enter to continue...")

# Run the Library Management System
if __name__ == "__main__":
    library = LibraryManagementSystem()
    library.menu()