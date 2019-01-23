## 1. Introduction ##

/home/dq$ ls -l

## 2. Moving Problematic Files to a Separate Folder ##

/home/dq$ mv legislators problematic

## 3. Fixing File Extensions ##

/home/dq/problematic$ mv forest_fires.cssv forest_fires.csv

## 4. Consolidating Files ##

/home/dq$ mv problematic csv_datasets

## 5. Restricting Permissions ##

/home/dq/csv_datasets$ chmod 0740 crime_rates.csv