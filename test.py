import sys
from pyarrow import csv
import numpy as np
import pyarrow as pa
import pyarrow.feather as feather
import pandas as pd
import pyarrow.compute 


fn = 'metadata.csv'
table = csv.read_csv(fn)
# table = np.array(csv.read_csv(fn))
#feather.write_feather(df, file_path)
#switch_on = input("Turn off dictionary encoding for a column? (Y/N) : ")
#if switch_on == "Y" or switch_on == "yes" or switch_on == "Yes":
#    column = input("Enter a number: ")
#    table = np.delete(table,int(column),0)
chunks = []
encoded_chunks = []
name_list = []
for column in table:
	str_column = column.cast('string')
	encoded_chunks.append(str_column.dictionary_encode().combine_chunks())
	chunks.append(str_column.combine_chunks())
for chunk in encoded_chunks:
	name_list.append("");
encoded_table = pa.Table.from_arrays(encoded_chunks, name_list)
nonencoded_table = pa.Table.from_arrays(chunks, name_list)

print("encoded and uncompressed: " + str(sys.getsizeof(encoded_table)/1000))
print("nonencoded and uncompressed: " + str(sys.getsizeof(nonencoded_table)/1000))

encoded_buf = pyarrow.serialize(encoded_table).to_buffer()
non_encoded_buf = pyarrow.serialize(nonencoded_table).to_buffer()

encoded_compressed_bytes = pa.compress(encoded_buf, codec='lz4', asbytes=True)
non_encoded_compressed_bytes = pa.compress(non_encoded_buf, codec='lz4', asbytes=True)

print("encoded and compressed: " + str(sys.getsizeof(encoded_compressed_bytes)/1000))
print("nonencoded and compressed: " + str(sys.getsizeof(non_encoded_compressed_bytes)/1000))

#feather.write_feather(encoded_table, "./encoded_compressed", compression='zstd')
#feather.write_feather(nonencoded_table, "./nonencoded_compressed", compression='zstd')