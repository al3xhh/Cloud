#!/bin/bash
python mapper_year.py < CleanedData.csv | sort | python reducer_year.py > avgByYears.csv
#sacamos el año maximo y minimo
#python mapper_max_min.py < avgByYears.csv |sort| python reducer_max_min.py > maxMinYears.csv
python filter_years.py avgByYears.csv < maxMinYears.csv > avgByYearsFiltered.csv

if [ -d "results" ]; then
		rm -r results
fi

mkdir results
echo "Sacramento
New York
Mexico" > configFile
python graphics.py avgByYearsFiltered.csv avgByYearsNA
echo "Caracas
La Serena" > configFile
python graphics.py avgByYearsFiltered.csv avgByYearsSA
echo "Madrid
Berlin
Moscow" > configFile
python graphics.py avgByYearsFiltered.csv avgByYearsEU
echo "Fez
Tripoli" > configFile
python graphics.py avgByYearsFiltered.csv avgByYearsAF
echo "Brisbane
Melbourne" > configFile
python graphics.py avgByYearsFiltered.csv avgByYearsOC
echo "Shanghai
Peking" > configFile
python graphics.py avgByYearsFiltered.csv avgByYearsAS

python mapper_seasons.py < CleanedData.csv | sort | python reducer_seasons.py > avgBySeasons.csv
python filter_years.py avgBySeasons.csv < maxMinYears.csv > avgBySeasonsFiltered.csv
max=4
for i in `seq 1 $max`
do
  echo "Sacramento
  New York
  Mexico" > configFile
  python graphicsSeasons.py avgBySeasonsFiltered.csv "$i" avgBySeasonsNA"$i"
  echo "Caracas
  La Serena" > configFile
  python graphicsSeasons.py avgBySeasonsFiltered.csv "$i" avgBySeasonsSA"$i"
  echo "Madrid
  Berlin
  Moscow" > configFile
  python graphicsSeasons.py avgBySeasonsFiltered.csv "$i" avgBySeasonsEU"$i"
  echo "Fez
  Tripoli" > configFile
  python graphicsSeasons.py avgBySeasonsFiltered.csv "$i" avgBySeasonsAF"$i"
  echo "Brisbane
  Melbourne" > configFile
  python graphicsSeasons.py avgBySeasonsFiltered.csv "$i" avgBySeasonsOC"$i"
  echo "Shanghai
  Peking" > configFile
  python graphicsSeasons.py avgBySeasonsFiltered.csv "$i" avgBySeasonsAS"$i"
done

python maper_years_group.py decade < CleanedData.csv | sort |python reducer_years_group.py decade > avgByDecade.csv
python filter_years.py avgByDecade.csv < maxMinYears.csv > avgByDecadeFiltered.csv

echo "Sacramento
New York
Mexico" > configFile
python graphicsYearsGroup.py avgByDecadeFiltered.csv avgByDecadeNA
echo "Caracas
La Serena" > configFile
python graphicsYearsGroup.py avgByDecadeFiltered.csv avgByDecadeSA
echo "Madrid
Berlin
Moscow" > configFile
python graphicsYearsGroup.py avgByDecadeFiltered.csv avgByDecadeEU
echo "Fez
Tripoli" > configFile
python graphicsYearsGroup.py avgByDecadeFiltered.csv avgByDecadeAF
echo "Brisbane
Melbourne" > configFile
python graphicsYearsGroup.py avgByDecadeFiltered.csv avgByDecadeOC
echo "Shanghai
Peking" > configFile
python graphicsYearsGroup.py avgByDecadeFiltered.csv avgByDecadeAS

python maper_years_group.py century < CleanedData.csv |sort|python reducer_years_group.py century > avgByCentury.csv
python filter_years.py avgByCentury.csv < maxMinYears.csv > avgByCenturyFiltered.csv
python graphicsByCentury.py avgByCenturyFiltered.csv avgByCentury

python mapper_max_min_years_group.py < avgByDecadeFiltered.csv | sort | python reducer_max_min_years_group.py > results/maxMinDecades.csv
