from database import Database

db = Database("smdb", False)
db.select('course', '*')

# CREATE THE INDEXES
print("--------------CREATE INDEX")
db.create_index('course', index_name='course_title', column_name='title', index_type="HashIndex")
print("HASH INDEX")
db.show_hashindex('course_title')
print("--------------SELECT WITH HASH INDEX")
db.select('course', '*', 'title==Robotics')
print("--------------DROP INDEX")
db.drop_index("course_title")
print("--------------HASH JOIN")
db.inner_join('course', 'teaches', 'course_id==course_id', hash_type='hash')
db.drop_index("course_title")
