## 2. Query Plan ##

import sqlite3
conn = sqlite3.connect("factbook.db")

query_plan_one = conn.execute("""
EXPLAIN QUERY PLAN
SELECT * 
FROM facts 
WHERE (population > 1000000) AND (population_growth<0.05)
""").fetchall()

conn.close()

print (query_plan_one)

## 3. Query plan for multi-column queries ##

conn = sqlite3.connect("factbook.db")
conn.execute("CREATE INDEX IF NOT EXISTS pop_idx ON facts(population)")
conn.execute("CREATE INDEX IF NOT EXISTS pop_growth_idx ON facts(population_growth)")
query_plan_two = conn.execute("EXPLAIN QUERY PLAN SELECT * FROM facts WHERE (population>1000000) AND (population_growth<0.05)").fetchall()
conn.close()

print(query_plan_two)

## 6. Creating a multi-column index ##

conn = sqlite3.connect("factbook.db")
conn.execute("create index if not exists pop_pop_growth_idx on facts(population, population_growth);")
query_plan_three = conn.execute("explain query plan select * from facts where (population > 1000000) and (population_growth < 0.05)").fetchall()
print(query_plan_three)

## 7. Covering index ##

conn = sqlite3.connect("factbook.db")
conn.execute("create index if not exists pop_pop_growth_idx on facts(population, population_growth);")
query_plan_four = conn.execute("EXPLAIN QUERY PLAN SELECT population, population_growth FROM facts WHERE (population>1000000) AND (population_growth<0.05)").fetchall()
conn.close()

print (query_plan_four)

## 8. Covering index for single column ##

conn = sqlite3.connect("factbook.db")
conn.execute("create index if not exists pop_pop_growth_idx on facts(population, population_growth);")
query_plan_five = conn.execute("EXPLAIN QUERY PLAN SELECT population FROM facts WHERE population>1000000").fetchall()
conn.close()

print (query_plan_five) 
