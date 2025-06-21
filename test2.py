# import pandas as pd
# import pymysql

# # Step 1: Read Excel files
# property_df = pd.read_excel(r"D:\bhavan kumar\property.xlsx")
# lease_sale_df = pd.read_excel(r"D:\bhavan kumar\lease_sale.xlsx")

# # Step 1.1: Create mapping from lease_sale.xlsx
# # lease_code → lease_sale value
# lease_map = dict(zip(lease_sale_df['lease_code'], lease_sale_df['lease_sale']))

# # Step 1.2: Optional — Skip first 3 if already updated
# property_df = property_df.iloc[3:]  # So MySQL update starts from id = 7567

# # Step 2: MySQL Connection
# connection = pymysql.connect(
#     host='34.197.20.24', 
#     user='username123',
#     password='S@efir?wRlphan=H6=hl',
#     database='aryan_properties',
# )

# cursor = connection.cursor()

# if cursor:
#     print("✅ Connected successfully!")

# start_id = 7564
# updated_rows = 0

# # Step 3: Loop through property_df and update using lease_code match
# for index, row in property_df.iterrows():
#     current_id = start_id + index
#     lease_code = row['lease_code']
#     ll_outright_value = lease_map.get(lease_code)

#     if ll_outright_value is not None:
#         update_query = """
#         UPDATE property
#         SET ll_outright = %s
#         WHERE id = %s
#         """
#         cursor.execute(update_query, (ll_outright_value, current_id))
#         updated_rows += cursor.rowcount
#         print(f"✅ Updated ID {current_id} → lease_code: {lease_code}, ll_outright: {ll_outright_value}")
#     else:
#         print(f"❌ No match for lease_code: {lease_code} at ID {current_id}")

# connection.commit()
# connection.close()

# print(f"🎉 Total {updated_rows} rows updated successfully in ll_outright column!")




# import pandas as pd

# # Step 1: Read Excel files
# property_df = pd.read_excel(r"D:\bhavan kumar\PROPERTY.xlsx")
# lease_sale_df = pd.read_excel(r"D:\bhavan kumar\LEASESALE.xlsx")

# # Step 1.1: Create mapping from lease_sale.xlsx
# lease_map = dict(zip(lease_sale_df['LEASECODE'], lease_sale_df['LEASESALE']))

# # Step 1.2: Optional — Skip first 3 rows
# property_df = property_df.iloc[0:]

# start_id = 7564
# tested_rows = 0

# # Step 2: Loop and just compare, no DB update
# for index, row in property_df.iterrows():
#     current_id = start_id + index
#     lease_code = row['LEASECODE']
#     ll_outright_value = lease_map.get(lease_code)

#     if ll_outright_value is not None:
#         print(f"✅ ID {current_id} → Match: lease_code = {lease_code} → ll_outright = {ll_outright_value}")
#     else:
#         print(f"❌ ID {current_id} → No match for lease_code: {lease_code}")
    
#     tested_rows += 1
#     if tested_rows >= 10:
#         break  # Limit to first 10 rows for testing

# print("🔍 Test complete (first 10 rows).")





# import pandas as pd
# import pymysql

# # Step 1: Read Excel files
# property_df = pd.read_excel(r"D:\bhavan kumar\PROPERTY.xlsx")
# lease_sale_df = pd.read_excel(r"D:\bhavan kumar\LEASESALE.xlsx")

# # ✅ Step 1.1: Create mapping from lease_sale.xlsx using correct column names
# lease_map = dict(zip(lease_sale_df['LEASECODE'], lease_sale_df['LEASESALE']))

# # Step 2: MySQL Connection
# connection = pymysql.connect(
#     host='34.197.250.249',
#     user='username',
#     password='S@efir?wRlphan=H6=hl',
#     database='aryan_properties',
# )
# cursor = connection.cursor()
# if cursor:
#     print("✅ Connected successfully!")

# # Step 3: Loop and update with debug logs
# start_id = 7564
# updated_rows = 0
# for index, row in property_df.iterrows():
#     current_id = start_id + index
#     lease_code = row.get('LEASECODE')
#     ll_outright_value = lease_map.get(lease_code)


#     if pd.notna(lease_code) and ll_outright_value is not None:
#         update_query = """
#         UPDATE property
#         SET ll_outright = %s
#         WHERE id = %s
#         """
#         cursor.execute(update_query, (ll_outright_value, current_id))
#         updated_rows += cursor.rowcount
#         print(f"✅ DB Updated: ID {current_id} → ll_outright = {ll_outright_value}")
#     else:
#         print(f"❌ Skipped: No match found for LEASECODE {lease_code} at ID {current_id}")

#     print("-" * 60)

# # Step 4: Commit and Close
# connection.commit()
# connection.close()

# print(f"\n🎉 Total {updated_rows} rows updated successfully in ll_outright column!")





# import pandas as pd

# # Read Excel files
# df = pd.read_excel(r"D:\bhavan kumar\descriptionss.xlsx", sheet_name="Sheet6")
# lease_map_df = pd.read_excel(r"D:\bhavan kumar\LEASESALE.xlsx")

# # ✅ Create mapping without zfill
# lease_map = dict(zip(
#     lease_map_df['LEASECODE'].astype(str).str.strip(),
#     lease_map_df['LEASESALE']
# ))

# # ✅ Loop and print test output
# print("\n🔍 TESTING Update Preview:\n")
# for index, row in df.iterrows():
#     raw_property_code = row.get('property_code')
#     raw_lease_code = row.get('lease_code')

#     property_code = str(raw_property_code).strip() if pd.notna(raw_property_code) else None
#     lease_code = str(raw_lease_code).strip() if pd.notna(raw_lease_code) else None
#     lease_sale = lease_map.get(lease_code)

#     print(f"📄 Raw Values → PropertyCode: {property_code}, LeaseCode: {lease_code}")

#     if property_code and lease_sale:
#         print(f"✅ Would update → PropertyCode: {property_code}, ll_outright: {lease_sale}")
#     else:
#         print(f"⚠️ Skipped → PropertyCode: {property_code}, LeaseCode: {lease_code}, lease_sale: {lease_sale}")

#     print("-" * 60)



import pandas as pd
import pymysql

# Read Excel files
df = pd.read_excel(r"D:\bhavan kumar\descriptionss.xlsx", sheet_name="Sheet6")
lease_map_df = pd.read_excel(r"D:\bhavan kumar\LEASESALE.xlsx")

# Mapping dictionary: lease_code → lease_sale
lease_map = dict(zip(
    lease_map_df['LEASECODE'].astype(str).str.strip(),
    lease_map_df['LEASESALE']
))

# ✅ Connect to MySQL
connection = pymysql.connect(
    host='34.197.250.249',
    user='username',
    password='S@efir?wRlphan=H6=hl',
    database='aryan_properties',
)
cursor = connection.cursor()
print("✅ Connected to MySQL")

# ✅ Loop and update
updated_rows = 0
for index, row in df.iterrows():
    raw_property_code = row.get('property_code')
    raw_lease_code = row.get('lease_code')

    property_code = str(raw_property_code).strip() if pd.notna(raw_property_code) else None
    lease_code = str(raw_lease_code).strip() if pd.notna(raw_lease_code) else None
    lease_sale = lease_map.get(lease_code)

    if property_code and lease_sale:
        update_query = """
        UPDATE property
        SET ll_outright = %s
        WHERE property_code = %s
        """
        cursor.execute(update_query, (lease_sale, property_code))
        updated_rows += cursor.rowcount
        print(f"✅ Updated → PropertyCode: {property_code} → ll_outright = {lease_sale}")
    else:
        print(f"⚠️ Skipped → PropertyCode: {property_code}, LeaseCode: {lease_code}, lease_sale: {lease_sale}")

    print("-" * 60)

# ✅ Commit and close
connection.commit()
connection.close()

print(f"\n🎉 Total {updated_rows} rows updated in the `ll_outright` column!")
