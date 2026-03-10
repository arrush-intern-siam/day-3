import pymongo
import json

# Connect to the database
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["school_db"]
collection = db["students"]

print("Connected to MongoDB 'school_db'!")
print("\n--- MongoDB CRUD Menu ---")
print("1. Create")
print("2. Read")
print("3. Update")
print("4. Delete")
print("5. Exit")
while True:
    
    choice = input("Select an operation (1-5): ")
    
    if choice == '5':
        print("Exiting program. Goodbye!")
        break
        
    if choice in ['1', '2', '3', '4']:
        scope = input("Do you want to apply this to 'one' or 'many' documents? ").strip().lower()
        
        try:
            # --- CREATE ---
            if choice == '1': 
                if scope == 'one':
                    data = input("Enter document as JSON (e.g., {\"name\": \"Alex\", \"grade\": \"A\"}): ")
                    doc = json.loads(data)
                    res = collection.insert_one(doc)
                    print(f"Success! Inserted ID: {res.inserted_id}")
                elif scope == 'many':
                    data = input("Enter list of documents as JSON (e.g., [{\"name\": \"Bob\"}, {\"name\": \"Charlie\"}]): ")
                    docs = json.loads(data)
                    res = collection.insert_many(docs)
                    print(f"Success! Inserted IDs: {res.inserted_ids}")
                    
            # --- READ ---
            elif choice == '2': 
                query_str = input("Enter filter query as JSON (type {} for all): ")
                query = json.loads(query_str)
                if scope == 'one':
                    print(collection.find_one(query))
                elif scope == 'many':
                    for doc in collection.find(query):
                        print(doc)
                        
            # --- UPDATE ---
            elif choice == '3': 
                query_str = input("Enter filter query as JSON (e.g., {\"name\": \"Alex\"}): ")
                update_str = input("Enter update operation as JSON (e.g., {\"$set\": {\"grade\": \"A+\"}}): ")
                query = json.loads(query_str)
                update = json.loads(update_str)
                
                if scope == 'one':
                    res = collection.update_one(query, update)
                    print(f"Modified {res.modified_count} document(s).")
                elif scope == 'many':
                    res = collection.update_many(query, update)
                    print(f"Modified {res.modified_count} document(s).")
                    
            # --- DELETE ---
            elif choice == '4': 
                query_str = input("Enter filter query as JSON (e.g., {\"name\": \"Alex\"}): ")
                query = json.loads(query_str)
                
                if scope == 'one':
                    res = collection.delete_one(query)
                    print(f"Deleted {res.deleted_count} document(s).")
                elif scope == 'many':
                    res = collection.delete_many(query)
                    print(f"Deleted {res.deleted_count} document(s).")
            else:
                print("⚠️ Please type exactly 'one' or 'many'.")
                
        except json.JSONDecodeError:
            print("Error: Invalid JSON format. Make sure to use double quotes (\") for keys and text values!")
        except Exception as e:
            print(f"An error occurred: {e}")