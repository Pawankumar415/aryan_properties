# import os
# from dotenv import load_dotenv

# load_dotenv()


# data = os.getenv("SQLALCHEMY_DATABASE_URL")
# print(data)



# import pandas as pd
# import pymysql

# # Step 1: Read the Excel/CSV file
# df = pd.read_excel(r"D:\bhavan kumar\PROPERTY.xlsx")  # Replace with .read_excel() if using Excel

# print(df['PROJECT'].head(10))

# # # Optional: Filter only rows with building_name not null
# # df = df[df['building_name'].notnull()]

# # # Optional: Filter starting from id 7540
# # df = df[df['id'] >= 7540]

# # Step 2: MySQL Connection
# connection = pymysql.connect(
#     host='34.197.250.249',
#     user='username123',
#     password='S@efir?wRlphan=H6=hl',
#     database='aryan_properties',
#     # cursorclass=pymysql.cursors.DictCursor
# )

# cursor = connection.cursor()

# if cursor:
#     print("connected successfull!")

# # Step 3: Loop through the DataFrame and update building_name
# for index, row in df.iterrows():
#     update_query = """
#     UPDATE property
#     SET building_name = %s
#     WHERE id = %s
#     """
#     cursor.execute(update_query, (row['building_name'], row['id']))

# connection.commit()
# connection.close()

# print("✅ Building names updated successfully!")




# import pandas as pd
# import pymysql

# # Step 1: Read Excel file
# df = pd.read_excel(r"D:\bhavan kumar\PROPERTY.xlsx")

# # Step 2: MySQL Connection
# connection = pymysql.connect(
#     host='34.197.250.249',
#     user='username',
#     password='S@efir?wRlphan=H6=hl',
#     database='aryan_properties',
#     # cursorclass=pymysql.cursors.DictCursor
# )

# cursor = connection.cursor()

# if cursor:
#     print("✅ Connected successfully!")

# # Step 3: Loop using index + 7564
# start_id = 7564
# updated_rows = 0

# for index, row in df.iterrows():
#     current_id = start_id + index
#     building_name = row['PROJECT']

#     update_query = """
#     UPDATE property
#     SET building_name = %s
#     WHERE id = %s
#     """
#     cursor.execute(update_query, (building_name, current_id))
#     updated_rows += cursor.rowcount

#     print(f"inserting row id: {current_id} --> {building_name}")

# connection.commit()
# connection.close()

# print(f"✅ {updated_rows} building names updated from ID {start_id} onwards!")




# import pandas as pd
# import pymysql

# # படி 1: எக்செல் கோப்பை படிக்கவும்
# try:
#     df = pd.read_excel(r"D:\bhavan kumar\PROPERTY.xlsx")
# except FileNotFoundError:
#     print("பிழை: 'PROPERTY.xlsx' கோப்பு குறிப்பிட்ட இடத்தில் இல்லை.")
#     exit() # கோப்பு இல்லை என்றால் வெளியேறவும்

# # படி 2: MySQL இணைப்பு
# connection = None # இணைப்பை ஆரம்பத்தில் None ஆக அமைக்கவும்
# try:
#     connection = pymysql.connect(
#         host='34.197.250.249',
#         user='username',
#         password='S@efir?wRlphan=H6=hl',
#         database='aryan_properties',
#         # cursorclass=pymysql.cursors.DictCursor # இந்த செயல்பாட்டிற்கு தேவையில்லை
#     )
#     cursor = connection.cursor()

#     if cursor:
#         print("✅ connected success")

#     # படி 3: மொத்தமாக புதுப்பிக்க தரவுகளை தயார் செய்யவும்
#     start_id = 7564
#     update_data = []

#     for index, row in df.iterrows():
#         current_id = start_id + index
#         building_name = row['PROJECT']
#         update_data.append((building_name, current_id)) # புதுப்பிக்க வேண்டிய தரவுகளை பட்டியலாக சேர்க்கவும்

#     # படி 4: மொத்தமாக புதுப்பித்தலை இயக்கவும்
#     if update_data: # புதுப்பிக்க தரவு இருந்தால் மட்டுமே தொடரவும்
#         update_query = """
#         UPDATE property
#         SET building_name = %s
#         WHERE id = %s
#         """
#         # executemany பல புதுப்பித்தல்களுக்கு மிக வேகமாக இருக்கும்
#         cursor.executemany(update_query, update_data)
#         updated_rows = cursor.rowcount # மொத்தமாக பாதிக்கப்பட்ட வரிசைகளின் எண்ணிக்கையைப் பெறவும்
#         connection.commit() # மாற்றங்களை டேட்டாபேஸில் உறுதிப்படுத்தவும்
#         print(f"✅ {start_id}  {updated_rows} building name !")
#     else:
#         print("புதுப்பிக்க தரவு இல்லை.")

# except pymysql.Error as e:
#     print(f"error: {e}")
#     if connection:
#         connection.rollback() # பரிவர்த்தனையின் போது பிழை ஏற்பட்டால் மாற்றங்களை ரத்து செய்யவும்
# finally:
#     if connection:
#         connection.close() # இணைப்பு இருந்தால் அதை மூடவும்
#         print("closed.")







# import pandas as pd
# import pymysql

# # Step 1: Read Excel (Sheet6)
# try:
#     desc_df = pd.read_excel(r"D:\bhavan kumar\descriptionss.xlsx", sheet_name='Sheet6')
# except Exception as e:
#     print(f"❌ Error reading Excel: {e}")
#     exit()

# # Step 2: MySQL Connection
# connection = None
# try:
#     connection = pymysql.connect(
#         host='34.197.250.249',
#         user='username',
#         password='S@efir?wRlphan=H6=hl',
#         database='aryan_properties',
#     )
#     cursor = connection.cursor()
#     print("✅ MySQL connected successfully!")

#     # Step 3: Prepare update data
#     update_data = []
#     for index, row in desc_df.iterrows():
#         prop_code = row.get('PROPERTYCODE') or row.get('property_code')  # case-insensitive check
#         building_name = row.get('BUILDINGNAME') or row.get('building_name')

#         print(f"🔁 Preparing → property_code: {prop_code}, building_name: {building_name}")

#         if pd.notna(prop_code) and pd.notna(building_name):
#             update_data.append((building_name, prop_code))
#         else:
#             print(f"⚠️ Skipped: Missing data at row {index}")

#     # Step 4: Execute batch update
#     if update_data:
#         update_query = """
#         UPDATE property
#         SET building_name = %s
#         WHERE property_code = %s
#         """
#         cursor.executemany(update_query, update_data)
#         connection.commit()

#         print("\n🎯 Update Summary:")
#         for b_name, p_code in update_data:
#             print(f"✅ property_code {p_code} → building_name = {b_name}")
#         print(f"\n🎉 Total {cursor.rowcount} rows updated successfully!")
#     else:
#         print("❌ No data to update.")

# except pymysql.Error as e:
#     print(f"❌ MySQL Error: {e}")
#     if connection:
#         connection.rollback()

# finally:
#     if connection:
#         connection.close()
#         print("🔚 MySQL connection closed.")



#########################################################

# insert city code in property table 

# import pandas as pd
# import pymysql

# # Step 1: Read Excel file with property_code and citycode
# try:
#     df = pd.read_excel(r"D:\bhavan kumar\descriptionss.xlsx", sheet_name='Sheet6')  # Update file name & sheet if needed
# except Exception as e:
#     print(f"❌ Error reading Excel: {e}")
#     exit()

# # Step 2: MySQL Connection Setup
# connection = None
# try:
#     connection = pymysql.connect(
#         host='34.197.250.249',
#         user='username',
#         password='S@efir?wRlphan=H6=hl',
#         database='aryan_properties',
#     )
#     cursor = connection.cursor()
#     print("✅ MySQL connected successfully!")

#     # Step 3: Prepare update data
#     update_data = []
#     for index, row in df.iterrows():
#         prop_code = row.get('PROPERTYCODE') or row.get('property_code')  # Support different capitalizations
#         city_code = row.get('CITYCODE') or row.get('citycode')

#         print(f"🔁 Preparing → property_code: {prop_code}, citycode: {city_code}")

#         if pd.notna(prop_code) and pd.notna(city_code):
#             update_data.append((city_code, prop_code))
#         else:
#             print(f"⚠️ Skipped: Missing data at row {index}")

#     # Step 4: Batch Update Query
#     if update_data:
#         update_query = """
#         UPDATE property
#         SET citycode = %s
#         WHERE property_code = %s
#         """
#         cursor.executemany(update_query, update_data)
#         connection.commit()

#         print("\n🎯 Update Summary:")
#         for city_code, p_code in update_data:
#             print(f"✅ property_code {p_code} → citycode = {city_code}")
#         print(f"\n🎉 Total {cursor.rowcount} rows updated successfully!")
#     else:
#         print("❌ No data to update.")

# except pymysql.Error as e:
#     print(f"❌ MySQL Error: {e}")
#     if connection:
#         connection.rollback()

# finally:
#     if connection:
#         connection.close()
#         print("🔚 MySQL connection closed.")





###############################################################################



# import pandas as pd
# import pymysql

# # Step 1: Read Excel Sheet7
# try:
#     df = pd.read_excel(r"D:\bhavan kumar\descriptionss.xlsx", sheet_name='Sheet7')
# except Exception as e:
#     print(f"❌ Error reading Excel: {e}")
#     exit()

# # Step 2: Connect to MySQL
# try:
#     connection = pymysql.connect(
#         host='34.197.250.249',
#         user='username',
#         password='S@efir?wRlphan=H6=hl',
#         database='aryan_properties',
#     )
#     cursor = connection.cursor()
#     print("✅ MySQL connected successfully!")

#     update_count = 0

#     # Step 3: Loop through Excel rows and update 85 null rows one by one
#     for index, row in df.iterrows():
#         citycode = row.get('citycode') or row.get('CITYCODE')
#         city_name = row.get('city') or row.get('city_name') or row.get('CITY')

#         if pd.notna(citycode) and pd.notna(city_name):
#             # Update a single NULL row with this data
#             update_query = """
#             UPDATE filter_area
#             SET citycode = %s, city_name = %s
#             WHERE citycode IS NULL OR city_name IS NULL
#             LIMIT 1
#             """
#             cursor.execute(update_query, (citycode, city_name))
#             update_count += 1

#             if update_count >= 85:  # We only have 85 rows to update
#                 break

#     connection.commit()
#     print(f"\n🎉 Total {update_count} rows updated successfully!")

# except pymysql.Error as e:
#     print(f"❌ MySQL Error: {e}")
#     if connection:
#         connection.rollback()

# finally:
#     if connection:
#         connection.close()
#         print("🔚 MySQL connection closed.")




###########################################################################

# import pandas as pd
# import pymysql
# from datetime import datetime

# # Step 1: Read Excel
# try:
#     df = pd.read_excel(r"D:\bhavan kumar\descriptionss.xlsx", sheet_name='Sheet7')
# except Exception as e:
#     print(f"❌ Error reading Excel: {e}")
#     exit()

# # Step 2: MySQL Connection
# try:
#     connection = pymysql.connect(
#         host='34.197.250.249',
#         user='username',
#         password='S@efir?wRlphan=H6=hl',
#         database='aryan_properties',
#     )
#     cursor = connection.cursor()
#     print("✅ MySQL connected successfully!")

#     # Step 3: Slice remaining rows (from index 85 onwards)
#     remaining_df = df.iloc[85:]  # from row 86 (index 85) till end

#     insert_data = []
#     for index, row in remaining_df.iterrows():
#         citycode = row.get('citycode') or row.get('CITYCODE')
#         city_name = row.get('city') or row.get('city_name') or row.get('CITY')

#         if pd.notna(citycode) and pd.notna(city_name):
#             insert_data.append((
#                 "Default Area",              # area_name
#                 datetime.now(),                        # edit_date (or use datetime.now())
#                 citycode,
#                 city_name
#             ))
#         else:
#             print(f"⚠️ Skipped row {index}: missing citycode/city_name")

#     # Step 4: Insert Remaining Data
#     if insert_data:
#         insert_query = """
#         INSERT INTO filter_area (area_name, edit_date, citycode, city_name)
#         VALUES (%s, %s, %s, %s)
#         """
#         cursor.executemany(insert_query, insert_data)
#         connection.commit()

#         print(f"\n🎉 Total {cursor.rowcount} new rows inserted successfully!")

# except pymysql.Error as e:
#     print(f"❌ MySQL Error: {e}")
#     if connection:
#         connection.rollback()

# finally:
#     if connection:
#         connection.close()
#         print("🔚 MySQL connection closed.")



print(5.0*0.5)
