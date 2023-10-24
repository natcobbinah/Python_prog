import dbm
db = dbm.open('captions','c') # c means create the database if it doesn't exist

db['cleese.png'] = 'Photo of John Cleese'

print(db['cleese.png']) # the output is a byte object

# the database can be updated using an existing key
db['cleese.png'] = 'Photo of John Cleese doing a silly walk'
print(db['cleese.png'])

# dictionary methods like keys and items don't work with database objects
# but iteration with a for loop works
for key in db:
    print(key, db[key])

# as with other files, the database should be closed when done
db.close()